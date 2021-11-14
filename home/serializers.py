from rest_framework import serializers
from .models import*
from django.contrib.auth.models import User

class userserializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password']
    def create(self, validated_data):
        user=User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user



class studentserializers(serializers.ModelSerializer):
    class Meta:
        model=student
       # field=['name','age']
        #exclude=['id',]
        fields='__all__'
    def validate(self, data):
        if data['age']<18:
            raise serializers.ValidationError({"error":"age can't be less than 18"})
        if data['name']:
            for n in data['name']:
                if n.isdigit():
                    raise serializers.ValidationError({"error":"name can't be numeric"})

        
        
        
        
        return data  
class catagoryserializer(serializers.ModelSerializer):
    class Meta:
        model=catagory
        fields='__all__'
class bookserializer(serializers.ModelSerializer):
    catagory=catagoryserializer()
    class Meta:
        model=book
        fields='__all__'
              