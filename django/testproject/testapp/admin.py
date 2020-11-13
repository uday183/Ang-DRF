# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from testapp.models import UserDetails, UserPersonalInfo, UserPost, UserPostComments, LikePost, FriendRelation
# Register your models here.

class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','city','country')
    # list_editable = ('name','description','qp_json')
    list_per_page = 50
    search_fields = ('name','city')
admin.site.register(UserDetails,UserDetailsAdmin)

class UserPersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'height','hobbies','color','user')
    # list_editable = ('name','description','qp_json')
    list_per_page = 50
    search_fields = ('hobbies','color')

admin.site.register(UserPersonalInfo,UserPersonalInfoAdmin)


class UserPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','discription','post_image')
admin.site.register(UserPost,UserPostAdmin)


class UserPostCommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment_postid','comments','status','created_at','updated_at')
admin.site.register(UserPostComments,UserPostCommentsAdmin)

class LikePostAdmin(admin.ModelAdmin):
    list_display = ('id', 'likepostid','likeuserid','like','created_at','updated_at')
admin.site.register(LikePost,LikePostAdmin)


class FriendRelationAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender_id','receiver_id','status','created_at','updated_at')
admin.site.register(FriendRelation,FriendRelationAdmin)