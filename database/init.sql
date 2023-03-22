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
