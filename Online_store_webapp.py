from flask import Flask, render_template, request
import psycopg2

app = Flask('Online Videogame Store')

conn = psycopg2.connect(
    host="localhost",
    database="Store_database",
    user="postgres",
    password="hAv3eleFant77@%$"
)


@app.route('/')
@app.route('/home/')
def home_page():
    """Renders the home page"""

    return render_template('home.html')


@app.route('/product/<prod_id>')
def product():
    """Renders a page for the chosen product"""

    return render_template('product.html')


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
    return render_template('all_products.html')


@app.route('/basket/')
def basket():
    return render_template('basket.html')


@app.route('/easteregg/')
def easteregg():
    return render_template('egg.html')


if __name__ == '__main__':
    app.run(debug=True)
    
