from PIL import Image as imGg
import psycopg2
import io
import os
import base64


def filefinder(rootdir: str) -> list:
    # find all images in the directory and add their paths to a list

    path_list = []

    for root, dirs, files in os.walk(rootdir):
        for file in files:
            file_path = os.path.join(root, file).replace("\\", '/')
            path_list.append(file_path)
    return path_list


def img_to_bytea(conn, path_list: list):
    # convert images to bytea file for use in database

    c = conn.cursor()
    query1 = """
                select name from images
    """
    query2 = """
                insert into images 
                (name, img_binarydata) 
                values (%s, %s)
    """

    with conn:
        # creates a tuple of all values in 'name' column
        c.execute(query1)
        column = c.fetchall()

        # extracts all values in column tuple for ease of access
        names = [row[0] for row in column]

        for path in path_list:
            # gets filename from path
            filename = os.path.splitext(os.path.basename(path))[0]

            # if statement necessary to prevent duplicates in database
            if filename not in names:

                # opens the image file using open() method from Pillow (PIL)"""
                image = imGg.open(path)

                # converts image to bytes
                image_bytes = io.BytesIO()

                # save() saves image data as stream object in format specified below
                # - image format needs to be specified for each individual extension
                if '.webp' in path:
                    image.save(image_bytes, format='WebP')
                elif '.png' in path:
                    image.save(image_bytes, format='PNG')
                elif '.jpg' in path or '.jpeg' in path or '.jfif' in path:
                    # save() method specified as format 'JPEG' for JPEG encoded images
                    # regardless of file extension
                    image.save(image_bytes, format='JPEG')
                else:
                    continue

                # seek() moves the stream pointer to start of stream
                image_bytes.seek(0)

                # read() reads binary data from stream and stores in psycopg2.binary object
                bytea_data = psycopg2.Binary(image_bytes.read())
                couple = (filename, bytea_data)
                c.execute(query2, couple)
                conn.commit()


def bytea_to_img(conn, image_id: tuple):
    # retrieves and converts incoming bytea data from database to displayable base64-encoded image for use in html

    query = """
            select
                img_binarydata
            from 
                images
            where
                id=%s
    """

    # first connects to the database and retrieves the image based on the id
    c = conn.cursor()
    c.execute(query, image_id)
    image_data = c.fetchone()[0]

    # the retrieved binary data is converted to a base64 and stored in a local variable
    # called "base64_data" which can then be used in html
    base64_data = base64.b64encode(image_data).decode('utf-8')

    return base64_data


if __name__ == '__main__':

    source = 'C:/Users/Darren James/Documents/Coding/Python-Project/database/images'

    db = psycopg2.connect(
        host="localhost",
        database="mydb10",
        user="postgres",
        password="hAv3eleFant77@%$"
    )
    p = filefinder(source)
    img_to_bytea(db, p)
