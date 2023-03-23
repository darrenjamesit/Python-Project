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


def bytea_to_img(image_data):
    """Converts image bytea data to html-displayable image"""

    # uses b64encode module to convert raw binary bytea data into base64 data
    base64_data = base64.b64encode(image_data).decode('utf-8')

    return base64_data


def dict_maker(conn):
    """Creates a dictionary of all product information, including images."""

    # first queries the database for all relevant information.
    query = """
                    select
                        p.id, p.name, p.price, i.img_binarydata
                    from
                        products p
                    inner join
                        images i on p.id = i.prod_id
            """
    c = conn.cursor()
    c.execute(query)

    # creates a list of all column names
    col_names = [desc[0] for desc in c.description]

    # fetches all rows from the SQL query
    all_data = c.fetchall()

    # creates a dictionary for ease of data manipulation
    prod_dict = {}

    for row in all_data:
        # a = bytea_to_img(row[4])
        prod_id = row[0]
        if prod_id not in prod_dict:
            prod_dict[prod_id] = {}
        for i in range(1, len(col_names)):
            column_name = col_names[i]
            if column_name == 'img_binarydata':
                column_value = bytea_to_img(row[i])
            else:
                column_value = row[i]
            prod_dict[prod_id][column_name] = column_value

    return prod_dict


if __name__ == '__main__':

    # proof of concept and dictionary reference

    conn = psycopg2.connect(
        host="localhost",
        database="store_database",
        user="postgres",
        password="hAv3eleFant77@%$"
    )

    prod_dict = dict_maker(conn)

    with open('dictionary.txt', 'w') as write:
        print(prod_dict, file=write)
