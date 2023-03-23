from flask import Flask, render_template, request
import psycopg2

from image_converter import filefinder, img_to_bytea, bytea_to_img


app = Flask('Online Videogame Store')

conn = psycopg2.connect(
    host="localhost",
    database="store_database",
    user="postgres",
    password="hAv3eleFant77@%$"
)

source = 'C:/Users/Darren James/Documents/Coding/Python-Project/database/images'

path_list = filefinder(source)

img_to_bytea(conn, path_list)


@app.route('/')
@app.route('/home/')
def home_page():
    """Renders the home page"""

    return render_template('home.html')


@app.route('/product/<prod_id>')
def product(prod_id):

    """Renders a page for the chosen product"""
#
# # first queries database
# query = """
#         select
#             img_binarydata
#         from
#             images
#         where
#             id = %s
# """
# c = conn.cursor()
# c.execute(query, (image_id,))
# image = bytea_to_img(conn, tuple(c.fetchone()))
# c.close()
#
# if image is None:
#     return 'Image not found', 404
# return render_template('product.html')


@app.route('/search/', methods=['GET', 'POST'])
def search():
    print(request.form)
    print(dict(request.form))
    print(request.form.get(''))
    return render_template('search.html', search=request.form, )


@app.route('/contact/')
def contact():
    return render_template('contact.html')


@app.route('/all_products/')
def all_prod():

    query = """
                select
                    img_binarydata
                from
                    images
                where
                    id = %s
        """
    c = conn.cursor()
    c.execute(query, '9')
    image_data1 = c.fetchone()[0]

    image1 = bytea_to_img(image_data1)

    c.execute(query, ('50',))
    image_data2 = c.fetchone()[0]
    image2 = bytea_to_img(image_data2)

    # not to self use fetchall() then create a list of dictionaries here to display all products
    # eg [{id: image_id, name: image_name, price: prod_price, description: description,
    # img_binarydata: bytea (?or convert bytea before then store in dictionary?) }]
    # then render the list of dictionaries rather than each individual image...

    return render_template('all_products.html', image1=image1, image2=image2)


@app.route('/category/<category>')
def cat():

    return render_template('category.html')

@app.route('/basket/')
def basket():
    return render_template('basket.html')


@app.route('/easteregg/')
def easteregg():
    return render_template('egg.html')


if __name__ == '__main__':
    app.run(debug=True)
    
