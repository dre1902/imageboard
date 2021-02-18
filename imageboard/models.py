from django.db import models

class Board(models.Model):
    name = models.CharField(max_length=32)
    short_name = models.CharField(max_length=4)

class Post(models.Model):
    name = models.CharField(max_length=32)
    subject = models.CharField(max_length=64, blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    image_name = models.CharField(max_length=64, blank=True, null=True)
    thumbnail = models.ImageField(upload_to='images', blank=True, null=True)
    text = models.CharField(max_length=2048)
    post_num = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_op = models.BooleanField()
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    thread = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    bump_order = models.IntegerField(blank=True, null=True)