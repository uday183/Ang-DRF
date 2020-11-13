"""testproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from testapp.views import UserInfo, UserPersonalView, Login, Logout, SignUp, ForgotPassword, UserPost,\
                        UserPostComment, GetComments, UserLikes, FriendsList, FindFriends, FriendRequest,\
                        FriendAccept, UserInformation, MyAccountDetails, UserFollwers, UserFollwing,\
                        LikedUsersList, UserPostData
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', Login.as_view(), name = 'user_login_call'),
    url(r'^register/', SignUp.as_view(), name = 'user_register'),
    url(r'^logout/', Logout.as_view(), name = 'logout'),
    url(r'^forgot_password/', ForgotPassword.as_view(), name = 'forgot_password'),
    url(r'^user_info/', UserInfo.as_view(), name = 'user_info'),
    url(r'^user_prsnl_info/', UserPersonalView.as_view(), name = 'user_personal_info'),
    url(r'^user_post/', UserPost.as_view(), name = 'user_post'),
    url(r'^post_comment/', UserPostComment.as_view(), name = 'post_comment'),
    url(r'^get_comment/', GetComments.as_view(), name = 'get_comment'),
    url(r'^user_like/', UserLikes.as_view(), name = 'user_like'),
    url(r'^friends/', FriendsList.as_view(), name = 'user_friends'),
    url(r'^all_users/', FindFriends.as_view(), name = 'all_users'),
    url(r'^friend_req/', FriendRequest.as_view(), name = 'friend_req'),
    url(r'^friend_accept/', FriendAccept.as_view(), name = 'friend_accept'),
    url(r'^userinfo/', UserInformation.as_view(), name = 'userinfo'),
    url(r'^user_account/', MyAccountDetails.as_view(), name = 'user_account'),
    url(r'^user_fallowers/', UserFollwers.as_view(), name = 'user_fallowers'),
    url(r'^user_fallowing/', UserFollwing.as_view(), name = 'user_fallowing'),
    url(r'^liked_users/', LikedUsersList.as_view(), name = 'liked_users'),
    url(r'^user_post_data/', UserPostData.as_view(), name = 'user_post_data'),


]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_ROOT_URL, document_root=settings.MEDIA_ROOT)
