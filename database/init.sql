create database Store_databse;

create table if not exists categories(
    id serial primary key,
    category_name text
)

insert into categories (category_name)
    values
    ('consoles'),
    ('games'),
    ('merchandise'),
    ('accessories');

create table if not exists products(
    id serial primary key,
    name text not null,
    price real null,
    description text null,
    stock smallint null,
    category_id int,
    foreign key (category_id)
        references categories(id)
);

create table if not exists images(
    id serial primary key,
    name text,
    img_binarydata bytea,
    prod_id int,
    foreign key (prod_id)
        references products(id)
);

insert into products (name, price, stock, category_id)
    values
    ('Aux to Analogue Cable 1.5m', '29.99', '53', '4'),
    ('3.5mm Aux Cord 3m', '14.99', '44', '4'),
    ('10m High-Speed Ethernet Cable', '19.99', '29', '4'),
    ('4K Gold-Plated HDMI Cable 5m', '49.99', '10', '4'),
    ('3.5mm Aux Splitter 0,5m', '17.99', '32', '4'),
    ('USB-A to Type-C Cable (Fast Charge) 3m', '59.99', '88', '4'),
    ('VGA-to-VGA Cable 1,5m', '14.99', '7', '4');
