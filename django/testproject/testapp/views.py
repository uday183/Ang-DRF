# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from django.db.models import Q
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from testapp.serializers import UserDetailsSerializer, UserPersonalInfoSerializer, UserPostSerializer                 
from testapp.models import UserDetails, UserPersonalInfo, UserPost as userpost, UserPostComments, LikePost,\
        FriendRelation
from django.http import JsonResponse
from django.contrib.auth import logout
# Create your views here.

class Login(APIView):
    def post(self,request):
        response = {"status":True,"msg":"login success","data":{},"url":''}
        try:
            usr_name = request.data.get('loginForm').get('username')
            password = request.data.get('loginForm').get('password')
            user = authenticate(
                username=usr_name,
                password=password)
            response['data'] = {"user_id":user.id}
            if not user:
                response['status'] = False
                response['msg'] ="wrong credentials"
        except Exception as e:
            response['status'] = False
            response['msg'] ="something went wrong"
        return Response(response)


class SignUp(APIView):
    def post(self,request):
        response_dict = {"status": True, "message": "", "data": {}}
        try:
            username = request.data.get('registerForm').get('username')
            email = request.data.get('registerForm').get('email')
            password = request.data.get('registerForm').get('password')
            user = User.objects.create_user(username,email,password)
            user.save()
        except Exception as e:
            pass
        return Response(response_dict)

class ForgotPassword(APIView):
    def post(self,request):
        response_dict = {}
        try:
            #import ipdb; ipdb.set_trace()
            user_name=request.data.get('forgotForm').get('username')
            email = request.data.get('forgotForm').get('email')
            user= User.objects.get(username=user_name,email=email)
            
            if user:
                pwd1=request.data.get('forgotForm').get('password1')
                pwd2=request.data.get('forgotForm').get('password2')
                if pwd1 == pwd2:
                    user.set_password(pwd1)
                    user.save()
                else:
                    response_dict['status'] = False
                    response_dict['message'] = 'Passwords are not matched'
            else:
                response_dict['status'] = False
                response_dict['message'] = 'Credentials worng'
            response_dict.update({'password':user_create.password})
            return Response(response_dict)
        except Exception as e:
            pass
        return Response(response_dict)


class Logout(APIView):
    def get(self,request):
        logout(request)
        return Response({"status":True,"message":"user logout"})
    
class UserInfo(APIView):
    def get(self,request):
        response = {"status":True,"msg":"success","data":{}}
        try:
            user_obj = UserDetails.objects.all()
            serializer = UserDetailsSerializer(user_obj,many=True,context={"request": request})
            response['data'] = serializer.data
        except Exception as e:
            response['status'] = False
            response['msg'] ="something went wrong"
        return Response(response)
    def post(self,request):
        response = {"status":True,"msg":"success","data":{}}
        try:
            if request.data.get('id'):
                user_obj = UserDetails.objects.filter(id = request.data.get('id'))
                if user_obj:
                    user_obj.update(name=request.data.get('username'),\
                                        city=request.data.get('city'),country=request.data.get('country'))
                else:
                    pass
                                            
            else:
                UserDetails.objects.create(name=request.data.get('username'),\
                                       city=request.data.get('city'),\
                                        country=request.data.get('country'))
        except Exception as e:
            response['status'] = False
            response['msg'] ="something went wrong"
        return Response(response)
    
    def delete(self,request):
        response = {"status":True,"msg":"success","data":{}}
        try:
            #import ipdb; ipdb.set_trace()
            UserDetails.objects.filter(id=request.GET.get('id')).delete()
        except Exception as e:
            response['status'] = False
            response['msg'] ="something went wrong"
        return Response(response)

class UserPersonalView(APIView):
    def get(self,request):
        response = {"status":True,"msg":"success","data":{}}
        try:
            user_obj = UserPersonalInfo.objects.all()
            serializer = UserPersonalInfoSerializer(user_obj,many=True)
            response['data'] = serializer.data
        except Exception as e:
            response['status'] = False
            response['msg'] ="something went wrong"
        return Response(response)

class UserPost(APIView):
    def get(self,request):
        response = {"status":True,"msg":"success","data":{}}
        try:
            userid = request.GET.get('user_id')
            http_protocol = 'http://'
            if request.is_secure():
                http_protocol = 'https://'
            host=http_protocol+request.META['HTTP_HOST']
            
            users = FriendRelation.objects.filter(Q(sender_id__name = userid) |
                                          Q(receiver_id__name = userid),status='Accepted')
            user_friends_list = []
            for each in users:
                if each.sender_id.name.id == int(userid):
                    user_friends_list.append(each.receiver_id.name.id)
                elif each.receiver_id.name.id == int(userid):
                    user_friends_list.append(each.sender_id.name.id)
                else:
                    pass
            user_obj = userpost.objects.filter(Q(user__name = userid) | Q(user__name__in = user_friends_list)).order_by('-updated_at')
            result = []
            for each in user_obj:
                d={}
                d['id'] = each.id
                d['user'] = each.user.name.username
                d['user_img'] =host+'/media'+each.user.profile_image.url
                d['name'] = each.name
                d['discription'] = each.discription
                d['post_image'] =  host+'/media'+each.post_image.url
                d['create_date'] = each.updated_at.strftime("%d-%m-%Y %H:%M %p")
                d['like_count'] = each.likepostid.filter(like=True).count()
                d['comment_count'] = each.comment_postid.all().count()
                try:
                    d['user_like'] = each.likepostid.values('like')[0].get('like')
                except:
                    d['user_like'] = False
                result.append(d)
            response['data'] = result
            response['usr_imge'] = host+'/media'+users[0].profile_image.url
        except Exception as e:
            response['status'] = False
            response['msg'] ="something went wrong"
        return Response(response)

class UserInformation(APIView):
    def get(self,request):
        response = {"status":True,"msg":"success","data":{}}
        try:
            http_protocol = 'http://'
            if request.is_secure():
                http_protocol = 'https://'
            host=http_protocol+request.META['HTTP_HOST']
            user_obj = UserDetails.objects.filter(name = request.GET.get('userid'))
            result = []
            for user in user_obj:
                d = {}
                d['username'] = user.name.username
                d['user_id'] = user.name.id
                d['profile_image'] = host+'/media'+user.profile_image.url
                d['city'] = user.city
                d['country'] = user.country
                result.append(d)
            response['data'] = result
        except Exception as e:
            response['status'] = False
            response['msg'] ="something went wrong"
        return Response(response)

class UserPostComment(APIView):
    def post(self,request):
        response = {"status":True,"msg":"success","data":{}}
        try:
            #import ipdb; ipdb.set_trace()
            post_id = request.data.get('postid')
            post_comment = request.data.get('postcomment')
            user_id = request.data.get('userid')
            userposts = userpost.objects.get(id =post_id )
            comment_user = UserDetails.objects.get(name = user_id)
            try:
                pk = post_comment.get('comment_id')
            except:
                pk = ''
            if pk:
                UserPostComments.objects.filter(comment_postid=userposts,comment_postuserid=comment_user,pk=pk).update(comments=post_comment.get('comments'))
            else:
                UserPostComments.objects.create(comment_postid=userposts,comment_postuserid=comment_user,comments=post_comment)
        except Exception as e:
            response['status'] = False
            response['msg'] ="something went wrong"
        return Response(response)


class GetComments(APIView):
    def get(self,request):
        response = {"status":True,"msg":"success","data":{}}
        try:
            user_obj = userpost.objects.filter(id =request.GET.get('post_id'))
            result = []
            http_protocol = 'http://'
            if request.is_secure():
                http_protocol = 'https://'
            host=http_protocol+request.META['HTTP_HOST']
            for each in user_obj:
                for com in each.comment_postid.all():
                    c={}
                    c['comment_id'] = com.id
                    c['comments'] = com.comments
                    c['coment_user_name'] = com.comment_postuserid.name.username
                    c['coment_user_img'] = host+'/media'+com.comment_postuserid.profile_image.url
                    result.append(c)
            response['data'] = result
        except Exception as e:
            response['status'] = False
            response['msg'] ="something went wrong"
        return Response(response)


class UserLikes(APIView):
    def post(self,request):
        response = {"status":True,"msg":"success","data":{}}
        try:
            post_id = request.data.get('postid')
            user_id = request.data.get('userid')
            userposts = userpost.objects.get(id =post_id )
            liked_user = UserDetails.objects.get(name = user_id)
            like_obj = LikePost.objects.filter(likepostid=userposts, likeuserid=liked_user, like=True)
            unlike = LikePost.objects.filter(likepostid=userposts, likeuserid=liked_user, like=False)
            if like_obj:
                like_obj.update(like=False)
            elif unlike:
                unlike.update(like=True)
            else:
                LikePost.objects.create(likepostid=userposts, likeuserid=liked_user, like=True)
            response['data'] = like_obj.count()
        except Exception as e:
            response['status'] = False
            response['msg'] ="something went wrong"
        return Response(response)

class FriendsList(APIView):
    def get(self,request):
        response = {"status":True,"msg":"success","data":{}}
        try:
            friendslist = FriendRelation.objects.filter(Q(sender_id__name =request.GET.get('userid')) |
                                            Q(receiver_id__name =request.GET.get('userid')),status='Accepted')
            result = []
            http_protocol = 'http://'
            if request.is_secure():
                http_protocol = 'https://'
            host=http_protocol+request.META['HTTP_HOST']
            for friend in friendslist:
                d={}
                if friend.receiver_id.name.id == int(request.GET.get('userid')):
                    d['username'] = friend.sender_id.name.username
                    d['userimage'] = host+'/media'+friend.sender_id.profile_image.url
                    d['city'] = friend.sender_id.city
                    d['country'] = friend.sender_id.country
                else:
                    d['username'] = friend.receiver_id.name.username
                    d['userimage'] = host+'/media'+friend.receiver_id.profile_image.url
                    d['city'] = friend.receiver_id.city
                    d['country'] = friend.receiver_id.country
                result.append(d)
            response['data'] = result
        except Exception as e:
            response['status'] = False
            response['msg'] ="something went wrong"
        return Response(response)

class FindFriends(APIView):
    def get(self,request):
        response = {"status":True,"msg":"success","data":{}}
        try:
            search_input = request.GET.get('searchinput')
            login_user = request.GET.get('userid')
            users = UserDetails.objects.filter(Q(name__username__startswith=search_input) | Q(city__startswith=search_input) |  Q(country__startswith=search_input)).exclude(name=login_user)
            result = []
            http_protocol = 'http://'
            if request.is_secure():
                http_protocol = 'https://'
            host=http_protocol+request.META['HTTP_HOST']
            for user in users:
                d={}
                obj = FriendRelation.objects.filter(Q(sender_id__name = user.name.id) |
                                          Q(receiver_id__name = user.name.id),status='Accepted')
                if not obj:
                    d['username'] = user.name.username
                    d['user_id'] = user.name.id
                    d['userimage'] = host+'/media'+user.profile_image.url
                    d['city'] = user.city
                    d['country'] = user.country
                    result.append(d)  
            response['data'] = result
        except Exception as e:
            response['status'] = False
            response['msg'] ="something went wrong"
        return Response(response)

class FriendRequest(APIView):
    def post(self,request):
        response = {"status":True,"msg":"success","data":{}}
        try:
            receiver_id = request.data.get('receiverid')
            sender_id = request.data.get('senderid')
            sender = UserDetails.objects.get(name = sender_id)
            receiver = UserDetails.objects.get(name = receiver_id)
            FriendRelation.objects.create(sender_id = sender,receiver_id = receiver, status = 'send')
        except Exception as e:
            response['status'] = False
            response['msg'] ="something went wrong"
        return Response(response)

class FriendAccept(APIView):
    def get(self,request):
        response = {"status":True,"msg":"success","data":{}}
        try:
            friendslist = FriendRelation.objects.filter(receiver_id__name =request.GET.get('userid'),status='send')
            result = []
            http_protocol = 'http://'
            if request.is_secure():
                http_protocol = 'https://'
            host=http_protocol+request.META['HTTP_HOST']
            count=0
            for friend in friendslist:
                d={}
                d['userid'] = friend.sender_id.name.id
                d['username'] = friend.sender_id.name.username
                d['userimage'] = host+'/media'+friend.sender_id.profile_image.url
                d['city'] = friend.sender_id.city
                d['country'] = friend.sender_id.country
                d['count'] = count+1
                result.append(d)
            response['data'] = result
        except Exception as e:
            response['status'] = False
            response['msg'] ="something went wrong"
        return Response(response)
    
    def post(self,request):
        response = {"status":True,"msg":"success","data":{}}
        try:
            #import ipdb; ipdb.set_trace()
            loginid = request.data.get('loginid')
            acceptedid = request.data.get('acceptid')
            sender = UserDetails.objects.get(name = acceptedid)
            receiver = UserDetails.objects.get(name = loginid)
            FriendRelation.objects.filter(sender_id = sender,receiver_id = receiver).update(status = 'Accepted')
            # UserDetails.objects.filter(name = loginid).update(friend_accepted=acceptedid,status=True)
            # UserDetails.objects.filter(name = acceptedid).update(friend_accepted=loginid,status=True)
        except Exception as e:
            response['status'] = False
            response['msg'] ="something went wrong"
        return Response(response)


class MyAccountDetails(APIView):
    def get(self,request):
        response = {"status":True,"msg":"success","data":{}}
        try:
            #import ipdb; ipdb.set_trace()
            user_id = request.GET.get('userid')
            result = []
            http_protocol = 'http://'
            if request.is_secure():
                http_protocol = 'https://'
            host=http_protocol+request.META['HTTP_HOST']
            posts = userpost.objects.filter(user__name = user_id)
            for post in posts:
                d={}
                d['post_image'] = host+'/media'+post.post_image.url
                d['post_id'] = post.pk
                d['name'] = post.name
                d['discription'] = post.discription
                d['like_count'] = post.likepostid.filter(like=True).count()
                try:
                    d['user_like'] = post.likepostid.values('like')[0].get('like')
                except:
                    d['user_like'] = False
                result.append(d)
            response['follwers_count'] = FriendRelation.objects.filter(receiver_id__name = user_id, status='Accepted').count()
            response['following_count'] = FriendRelation.objects.filter(sender_id__name = user_id, status='Accepted').count()
            response['post_count'] = posts.count()
            response['data'] = result
        except Exception as e:
            response['status'] = False
            response['msg'] ="something went wrong"
        return Response(response)

class UserFollwers(APIView):
    def get(self,request):
        response = {"status":True,"msg":"success","data":{}}
        try:
            #import ipdb; ipdb.set_trace()
            user_id = request.GET.get('userid')
            result = []
            http_protocol = 'http://'
            if request.is_secure():
                http_protocol = 'https://'
            host=http_protocol+request.META['HTTP_HOST']
            follwers = FriendRelation.objects.filter(receiver_id__name = user_id, status='Accepted')
            for follwer in follwers:
                d={}
                d['user_name'] = follwer.sender_id.name.username
                d['user_image'] = host+'/media'+follwer.sender_id.profile_image.url
                result.append(d)
            response['data'] = result
        except Exception as e:
            response['status'] = False
            response['msg'] ="something went wrong"
        return Response(response)

class UserFollwing(APIView):
    def get(self,request):
        response = {"status":True,"msg":"success","data":{}}
        try:
            #import ipdb; ipdb.set_trace()
            user_id = request.GET.get('userid')
            result = []
            http_protocol = 'http://'
            if request.is_secure():
                http_protocol = 'https://'
            host=http_protocol+request.META['HTTP_HOST']
            follwers = FriendRelation.objects.filter(sender_id__name =2,status='Accepted')
            for follwer in follwers:
                d={}
                d['user_name'] = follwer.receiver_id.name.username
                d['user_image'] = host+'/media'+follwer.receiver_id.profile_image.url
                result.append(d)
            response['data'] = result
        except Exception as e:
            response['status'] = False
            response['msg'] ="something went wrong"
        return Response(response)

class LikedUsersList(APIView):
    def get(self,request):
        response = {"status":True,"msg":"success","data":{}}
        try:
            #import ipdb; ipdb.set_trace()
            postid = request.GET.get('postid')
            result = []
            http_protocol = 'http://'
            if request.is_secure():
                http_protocol = 'https://'
            host=http_protocol+request.META['HTTP_HOST']
            follwers = LikePost.objects.filter(likepostid=postid, like=True)
            for follwer in follwers:
                d={}
                d['user_name'] = follwer.likeuserid.name.username
                d['user_image'] = host+'/media'+follwer.likeuserid.profile_image.url
                result.append(d)
            response['data'] = result
        except Exception as e:
            response['status'] = False
            response['msg'] ="something went wrong"
        return Response(response)

class UserPostData(APIView):
    def post(self,request):
        response = {"status":True,"msg":"success","data":{}}
        try:
            userid = request.data.get('userid')
            user = UserDetails.objects.get(name = userid)
            name = request.data.get('usertext')
            discription = request.data.get('usertext')
            post_image = request.FILES.getlist('file')
            for each in post_image:
                userpost.objects.create(user = user, name = discription, discription = discription, post_image = each)
        except Exception as e:
            response['status'] = False
            response['msg'] ="something went wrong"
        return Response(response)
