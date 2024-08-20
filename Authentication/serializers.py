from rest_framework import serializers
from Signup.models import AppUser
from django.contrib.auth import authenticate


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()

    class Meta:
        model = AppUser
        fields = ["username", "password"]
        extra_kwargs = {"password": {"write_only": True}}
    
    def validate(self, data):
        username = data.get("username", None)
        password = data.get("password", None)

        # Username-Matched User
        umu = AppUser.objects.get(username__exact=username)
        if umu:
            if umu.check_password(password):
                # print("Wprked up to here")
                user = authenticate(username=username, password=password)
                # print("Worked so far")
                if user:
                    data["user"] = user
                else:
                    raise ValueError("Authentication Failed")
            else:
                raise ValueError("Incorrect Password")
        else:
            raise ValueError("User Does Not Exist")
        
        return data