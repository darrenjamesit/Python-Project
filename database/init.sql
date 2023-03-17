CREATE TABLE if not exists images(
  id serial PRIMARY KEY,
  name text,
  img_binarydata bytea
);