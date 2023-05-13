from flask import render_template, request, redirect
from models.memes import all_memes, get_meme, create_meme, update_meme, delete_meme
from services.session_info import current_user

def index():
    memes = all_memes()
    return render_template ('memes/index.html', memes = memes, current_user = current_user())

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

