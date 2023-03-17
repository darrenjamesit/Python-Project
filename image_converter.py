from PIL import Image as imGg
import psycopg2
import io
import os


def filefinder(rootdir: str) -> list:
    # find all images in the directory and add their paths to a list

    path_list = []

    for root, dirs, files in os.walk(rootdir):
        for file in files:
            file_path = os.path.join(root, file).replace("\\", '/')
            path_list.append(file_path)
    return path_list


def img_to_bytea_converter(conn, path_list: list):
    # convert images to bytea file for use in database

    c = conn.cursor()
    query = """
                insert into images 
                (name, data) 
                values (%s, %s)
    """
    with conn:
        for path in path_list:
            # opens the image file using open() method from
            # Image (imgg) from Pillow (PIL)"""
            image = imGg.open(path)

            # get filename from path
            filename = os.path.splitext(os.path.basename(path))[0]

            # convert image to bytes
            image_bytes = io.BytesIO()

            # save() saves image data as stream object in format specified below
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

            # read() reads binary data from stream
            bytea_data = psycopg2.Binary(image_bytes.read())
            couple = (filename, bytea_data)
            c.execute(query, couple)
            conn.commit()


# def bytea_to_img_converter():
#     convert incoming image from database to be displayed in html


if __name__ == '__main__':

    source = 'C:/Users/Darren James/Documents/Coding/Python-Project/database/images'

    db = psycopg2.connect(
        host="localhost",
        database="mydb10",
        user="postgres",
        password="hAv3eleFant77@%$"
    )
    p = filefinder(source)
    img_to_bytea_converter(db, p)
