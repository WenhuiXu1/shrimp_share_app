CREATE DATABASE memes_app;
\c memes_app

CREATE TABLE memes (
    id SERIAL PRIMARY KEY,
    name TEXT,
    image_url TEXT
);

INSERT INTO memes(name, image_url)
VALUES
    ('Cute Shrimps', 'https://media.tenor.com/1Y_dkOOTBwAAAAAd/meh-idc.gif');

UPDATE memes 
SET name = 'Meh'
WHERE id = '1';

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    password_digest TEXT
);