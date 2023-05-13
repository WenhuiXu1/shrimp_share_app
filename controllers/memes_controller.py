from flask import render_template, request, redirect, session
from models.memes import all_memes, get_meme, create_meme, update_meme, delete_meme, like_meme, total_likes, comment_meme, get_comments, get_comments_by_id, delete_a_comment
from models.user import find_user_by_id
from services.session_info import current_user
from db.db import sql

def index():
    memes = all_memes()
    likes = {}
    for meme in memes:
        likes[meme['id']] = total_likes(meme['id'])
    return render_template ('memes/index.html', memes = memes, current_user = current_user(), likes = likes)

def new():
    return render_template('memes/new.html')

def create():
    name = request.form.get('name')
    image_url = request.form.get('image_url')

    create_meme(name, image_url)
    return redirect('/')

def edit(id):
    meme = get_meme(id)
    return render_template('memes/edit.html', meme = meme)

def update(id):
    name = request.form.get('name')
    image_url = request.form.get('image_url')

    update_meme(name, image_url, id)
    return redirect('/')

def delete(id):
  delete_meme(id)
  return redirect('/')

def like(id):
    like_meme(session['user_id'], id)
    return redirect('/')

def comment_new(id):
    meme = get_meme(id)
    comments = get_comments()
    comment_by_id = get_comments_by_id(id)
    user_id = session['user_id']
    user = find_user_by_id(user_id)
    return render_template('comments/new.html', current_user=current_user(), meme = meme, comments = comments, comment_by_id = comment_by_id, user=user)

def create_comment(id):
    content = request.form.get('content')
    # user_id = request.form.get('user_id')
    comment_meme(session['user_id'], id, content)
    comments = get_comments()
    comment_by_id = get_comments_by_id(id)
    return render_template('comments/display.html', comments = comments, comment_by_id = comment_by_id)

def delete_comment(id):
    delete_a_comment(id)
    return redirect('/')