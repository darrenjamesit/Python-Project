from flask import Flask, render_template, request
import psycopg2

from image_converter import filefinder, img_to_bytea, bytea_to_img, dict_maker


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

prod_dict = dict_maker(conn)


@app.route('/')
@app.route('/home/')
def home_page():
    """Renders the home page"""

    return render_template('home.html')


@app.route('/product/<prod_id>')
def product(prod_id):
    """Renders a page for the chosen product"""

    # then queries the database for all relevant information.
    with conn:
        query = """
                        select
                            p.id, p.name, p.price, p.description, p.stock, c.category_name, i.img_binarydata, p.category_id
                        from
                            categories c
                        join
                            products p on c.id = p.category_id
                        left join
                            images i on p.id = i.prod_id
                        where
                            p.id = %s::integer
                        group by
                            p.id, p.name, p.price, c.category_name, i.img_binarydata;
                        """
        c = conn.cursor()
        c.execute(query, (prod_id,))

        # fetches row from the SQL query
        rows = c.fetchall()

        row = rows[0]

        image_list = []
        for element in rows:
            image_list.append(bytea_to_img(element[6]))

        return render_template('product.html', row=row, img=image_list, title=row[1])


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
    """Displays all items."""

    return render_template('all_products.html', alldata=prod_dict)


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
