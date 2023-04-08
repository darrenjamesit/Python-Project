def write_readme(filename: str):
    with open(filename, 'w') as file:
        file.write("""
        # Online Videogame Store

        This is a Flask-based web app intended to be used as an online store, in this case for a Video Games e-store.

        ## Installation

        1. Clone the GitHub repository.
        2. Create a virtual environment (Python 3.11 recommended) and activate it.
        3. Install the Flask Package.
        4. Install a PostgreSQL Database Administration Tool (DBeaver is recommended).
        5. a) Set up the database using the /database/init.sql script and run in your chosen Database Administration Tool.
        5. b) A visual table relationship diagram of the expected database structure is provided in /database/database_table_relationships.docx.
        
        ## Usage
        
        1. Run the app from Online_store_webapp.py.
        2. Navigate to http://localhost:5000 in your web browser to access the Front End Application.
        
        ## Contributing

        1. Any additional products can be added to the database by updating the table 'products' in your chosen Database Administration Tool
        (please consult the table 'categories' beforehand to determine which category_id to apply to the new product).
        2. a) Any additional product images can be added to /database/images, however their names must be indicative of
        their associated product for ease of assignment as their prod_id must be entered manually in table 'images' based on which item in
        table 'products' is associated with this image.
        2. b) Only images with '.webp', '.png', '.jpg', '.jpeg' and '.jfif' extensions may be used in the database.
        3. Style changes can be made to /static/css/styles.css.
        4. Background images can be added or replaced in /static/images.
        5. Additional routes may be added to Online_store_webapp.py, please note, their respective HTML files must be manually created.
        
        ## Credits
        
        I would like to thank Fast Track IT Cluj-Napoca for their incredible training and especially Ciprian Stoica for his excellent mentorship
        without which, this project would not have been possible.
        
        ## License
        
        A standard MIT OpenSource License has been used.
        
        """)


if __name__ == '__main__':
    write_readme('README.txt')