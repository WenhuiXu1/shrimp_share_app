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

def like_meme(user_id, meme_id):
    sql("INSERT INTO likes(user_id, meme_id) VALUES (%s, %s) RETURNING *", [user_id, meme_id])

def total_likes(id):
    total_likes = sql("SELECT COUNT(*) FROM likes WHERE meme_id = %s", [id])
    return total_likes[0]['count']

def comment_meme(user_id, id, content):
    sql("INSERT INTO comments(user_id, meme_id, content) VALUES(%s, %s, %s) RETURNING *", [user_id, id, content])

def get_comments():
    all_comments = sql("SELECT * FROM comments")
    return all_comments

def get_comments_by_id(id):
    comment_by_id = sql("SELECT * FROM comments WHERE meme_id=%s", [id])
    return comment_by_id

def delete_a_comment(id):
    sql("delete from comments where id = %s returning *", [id])
