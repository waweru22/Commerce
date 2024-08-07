from rest_framework import serializers
from Signup.models import AppUser
from django.contrib.auth import authenticate


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(label="Email Address")

    class Meta:
        model = AppUser
        fields = ["email" "password"]
        extra_kwargs = {"password": {"write_only": True}}
    
    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)

        emu = AppUser.objects.get(email__exact=email)
        if emu:
            if emu.check_password(password):
                print("Wprked up to here")
                user = authenticate(email=email, password=password)
                print("Worked so far")
                if user:
                    data["user"] = user
                else:
                    raise ValueError("Authentication Failed")
            else:
                raise ValueError("Incorrect Password")
        else:
            raise ValueError("User Does Not Exist")
        
        return data