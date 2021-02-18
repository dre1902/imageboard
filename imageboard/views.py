from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Board, Post
from .forms import OpPostForm, PostForm

import os
from PIL import Image

def board_view(request, board_name):
    board = Board.objects.get(short_name=board_name)
    all_boards = Board.objects.all()

    if request.method == 'POST':
        if OpPostForm(request.POST, request.FILES).is_valid():
            op_post = Post(
                name = request.POST.get('name'),
                subject = request.POST.get('subject'),
                image = request.FILES['image'],
                text = request.POST.get('text'),
                post_num = Post.objects.filter(board=board).count() + 1,
                is_op = True,
                board = board,
                thread = None,
                bump_order = 0
            )

            if op_post.name == '' or op_post.name is None:
                op_post.name = 'Anonymous'

            op_post.image_name = op_post.image.name
            thumb = Image.open(op_post.image)
            thumb.thumbnail((250, 250))
            thumb_path = os.path.splitext(op_post.image.path)[0] + 's.jpg'
            thumb.save(thumb_path, 'JPEG')
            op_post.thumbnail.name = thumb_path
            op_post.save()

            return render(request, 'thread.html', {
                'boards': all_boards,
                'board': board,
                'op_post': op_post,
                'posts': []
            })
        else:
            print(OpPostForm(request.POST).errors)

    else: # GET
        op_posts = list(Post.objects.filter(board=board, is_op=True).order_by('bump_order'))
        op_posts = op_posts[:10] # Get the last 10 bumped threads
        for i in op_posts:
            i.replies = list(Post.objects.filter(thread=i).order_by('post_num'))
            i.replies = i.replies[:5] # Get the latest 5 replies to those threads
        return render(request, 'board.html', {
            'boards': all_boards,
            'board': board,
            'op_posts': op_posts
        })

def thread_view(request, board_name, post_num):
    all_boards = Board.objects.all()
    board = Board.objects.get(short_name=board_name)
    op_post = Post.objects.get(board=board, post_num=post_num)

    if request.method == 'POST':
        if PostForm(request.POST, request.FILES).is_valid():
            post = Post(
                name = request.POST.get('name'),
                image = request.FILES['image'] if 'image' in request.FILES else None,
                text = request.POST.get('text'),
                post_num = Post.objects.filter(board=board).count() + 1,
                is_op = False,
                board = board,
                thread = op_post
            )

            if post.name == '' or post.name is None:
                post.name = 'Anonymous'

            if post.image:
                post.image_name = post.image.name
                thumb = Image.open(post.image)
                thumb.thumbnail((250, 250))
                thumb_path = os.path.splitext(post.image.path)[0] + 's.jpg'
                thumb.save(thumb_path, 'JPEG')
                post.thumbnail.name = thumb_path

            post.save()
        else:
            print(PostForm(request.POST, request.FILES).errors)


    #else:
    posts = list(Post.objects.filter(thread=op_post).order_by('post_num'))
    return render(request, 'thread.html', {
        'boards': all_boards,
        'board': board,
        'op_post': op_post,
        'posts': posts
    })