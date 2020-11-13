# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

STATUS_CHOICE = (
    ("send","send"),
    ('Accepted', 'Accepted'),

)
# Create your models here.

class UserDetails(models.Model):
    name = models.OneToOneField(User,on_delete=models.PROTECT)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='user_image', blank=True, null=True)
    friend_accepted = models.IntegerField(blank=True, null=True)
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.name.username


class UserPersonalInfo(models.Model):
    height = models.CharField(max_length = 100)
    hobbies = models.CharField(max_length = 100)
    color  = models.CharField(max_length= 100)
    user = models.OneToOneField(UserDetails,on_delete=models.PROTECT)
    def __str__(self):
        return self.hobbies


class UserPost(models.Model):
    user = models.ForeignKey(UserDetails,on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    discription = models.CharField(max_length=500,blank=True, null=True)
    post_image = models.ImageField(upload_to='user_post', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class UserPostComments(models.Model):
    comment_postid = models.ForeignKey(UserPost, on_delete=models.CASCADE, related_name='comment_postid')
    comment_postuserid = models.ForeignKey(UserDetails,on_delete=models.CASCADE, related_name='comment_postuserid')
    comments = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment_postuserid.name.username


class LikePost(models.Model):
    likepostid = models.ForeignKey(UserPost, max_length=50, on_delete=models.CASCADE, related_name='likepostid')
    likeuserid = models.ForeignKey(UserDetails,on_delete=models.CASCADE, related_name='likeuserid')
    like = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.likepostid.user.name.username

class FriendRelation(models.Model):

    sender_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE,related_name="sender_id")
    receiver_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE,related_name="receiver_id")
    status = models.CharField( choices=STATUS_CHOICE,max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.sender_id.name.username}-{self.receiver_id.name.username}-{self.status}"