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
    """Search all products based on search product name or category"""

    if request.method == 'POST':
        srch = request.form
    else:
        srch = request.args

    search = srch.get('search')

    with conn:
        query = """
            select distinct on (p.id)
                p.id, p.name, p.price, c.category_name, i.img_binarydata
            from
                categories c
            join
                products p on c.id = p.category_id
            left join
                images i on p.id = i.prod_id
            where
                lower(p.name) like lower(%s) or lower(c.category_name) like lower(%s);
        """

        c = conn.cursor()
        c.execute(query, (f'%{search}%', f'%{search}%'))

        # fetch the results
        rows = c.fetchall()

        # convert the bytea data (4th element in each tuple in list) to base64
        for i, tup in enumerate(rows):
            conv_img = bytea_to_img(tup[4])
            rows[i] = (tup[0], tup[1], tup[2], tup[3], conv_img)

        # if no rows were returned, return a message
        if not rows:
            return f"404 No products found for {search}."

        return render_template('search.html', search=search, title='Search Results', rows=rows)


@app.route('/contact/')
def contact():
    return render_template('contact.html', title='Contact')


@app.route('/all_products/')
def all_prod():
    """Displays all items."""

    return render_template('all_products.html', alldata=prod_dict, title='All Products')


@app.route('/category/<category>')
def cat(category):
    """Renders a page for the chosen category"""

    # queries the database for all relevant information
    with conn:
        query = """
            select distinct on (p.id)
                p.id, p.name, p.price, c.category_name, i.img_binarydata
            from
                categories c
            join
                products p on c.id = p.category_id
            left join
                images i on p.id = i.prod_id
            where
                category_name = %s
            order by
                p.id, i.id;
        """

        # execute the query with the category parameter
        c = conn.cursor()
        c.execute(query, (category,))

        # fetch the results
        rows = c.fetchall()

        # convert the bytea data (4th element in each tuple in list) to base64
        for i, tup in enumerate(rows):
            conv_img = bytea_to_img(tup[4])
            rows[i] = (tup[0], tup[1], tup[2], tup[3], conv_img)

        # if no rows were returned, return a message
        if not rows:
            return f"No products found for category {category}"

    # render the template with the row and image list
    return render_template('category.html', rows=rows, title=rows[0][3].capitalize())


@app.route('/basket/')
def basket():
    """Displays the basket"""

    quant = int(request.args.get('quantity', 1))
    prod_id = request.args.get('prod_id')
    if prod_id:
        with conn:
            query = """
                select distinct on (p.id)
                    p.id, p.name, p.price, c.category_name, i.img_binarydata, p.stock
                from
                    categories c
                join
                    products p on c.id = p.category_id
                left join
                    images i on p.id = i.prod_id
                where
                    p.id = %s;
            """

            c = conn.cursor()
            c.execute(query, (prod_id,))

            # fetch the results
            rows = list(c.fetchone())
            rows[4] = bytea_to_img(rows[4])

        return render_template('basket.html', quant=quant, rows=rows, title="Your Basket")

    else:
        return render_template('empty_basket.html')


@app.route('/checkout/')
def check():
    """Displays the checkout screen"""

    return render_template('checkout.html', title="Confirm Payment")


@app.route('/complete/')
def complete():
    """Displays a Successful Transaction screen"""

    return render_template('complete.html', title="Secure Payment Portal")

@app.route('/easteregg/')
def easteregg():
    """This is a fun easter egg placed somewhere in the page."""

    return render_template('egg.html')


if __name__ == '__main__':
    app.run(debug=True)
