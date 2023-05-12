from db.db import sql

def all_memes():
    return sql('SELECT * FROM memes')

def get_meme(id):
  memes = sql("SELECT * FROM memes WHERE id = %s", [id])
  return memes[0]

def create_meme(name, image_url):
    sql('INSERT INTO memes(name, image_url) VALUES(%s, %s) RETURNING *', [name, image_url])

def update_meme(name, image_url, id):
    sql('UPDATE memes SET name=%s, image_url=%s WHERE id=%s RETURNING *', [name, image_url, id])

def delete_meme(id):
    sql('DELETE FROM memes WHERE id=%s RETURNING *', [id])