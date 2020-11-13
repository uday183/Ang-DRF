from rest_framework import serializers
from testapp.models import UserDetails, UserPersonalInfo, UserPost, UserPostComments

class UserDetailsSerializer(serializers.ModelSerializer):
    profile_image = serializers.SerializerMethodField('get_thumbnails',)
    def get_thumbnails(self,obj):
        
        request = self.context.get('request')

        http_protocol = 'http://'
        if request.is_secure():
            http_protocol = 'https://'
        host=http_protocol+request.META['HTTP_HOST']
        try:
            photos = obj.profile_image.url
            obj=host+'/media'+photos
        except:
            obj=''
            
        return obj

    class Meta:
        model = UserDetails
        fields = ('id','name','city','country','profile_image')



class UserPersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPersonalInfo
        fields = ('id', 'height','hobbies','color','user')


class UserPostSerializer(serializers.ModelSerializer):
    post_image = serializers.SerializerMethodField('get_thumbnails',)
    def get_thumbnails(self,obj):
        request = self.context.get('request')
        http_protocol = 'http://'
        if request.is_secure():
            http_protocol = 'https://'
        host=http_protocol+request.META['HTTP_HOST']
        try:
            photos = obj.post_image.url
            obj=host+'/media'+photos
        except:
            obj=''
        return obj
    class Meta:
        model = UserPost
        fields = ('id', 'user','name','discription','post_image')

