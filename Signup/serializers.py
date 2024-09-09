from rest_framework import serializers
from .models import AppUser
from django.core.exceptions import ValidationError


class AppUserSerializer(serializers.ModelSerializer):
    # user_type = serializers.CharField(required=False)
    email = serializers.EmailField(required=True)
    address = serializers.CharField(required=True)
    username = serializers.CharField(required=True)
    phone_no = serializers.CharField(required=True)
    firstname = serializers.CharField(required=True)
    lastname = serializers.CharField(required=True)
    state = serializers.CharField(required=True)

    # #VENDOR 
    # business_name = serializers.CharField(required=False)
    # contact_firstname = serializers.CharField(required=False)
    # contact_lastname = serializers.CharField(required=False)
    # bank_name = serializers.CharField(required=False)
    # beneficiary_name = serializers.CharField(required=False)
    # account_number = serializers.CharField(required=False)

    # #CUSTOMER
    # firstname = serializers.CharField(required=False)
    # lastname = serializers.CharField(required=False)
    
    class Meta:
        model = AppUser
        fields = '__all__'

    def validate_username(self, value):
        if AppUser.objects.filter(username=value).exists():
            raise ValidationError("This username already exists")
        return value
    
    def validate_email(self, value):
        if AppUser.objects.filter(email=value).exists():
            raise ValidationError("This email already exists")
        return value
    
    # def validate_phone_no(self, value):
    #     if AppUser.objects.filter(phone_no=value).exists():
    #         raise ValidationError("This phone number already exists")
    #     return value

    def create(self, user_data):
        user = AppUser.objects.create_user(**user_data)


        if user:
            # keys = ['firstname', 'lastname']
            # customer_info = { x:user_data[x] for x in keys }

            # if not customer_info:
            #     raise ValueError("Required Fields Not Passed")
            
            # customer = Customer.objects.create(user=user, **customer_info )
            # customer.save()
            # print('customer info: ', customer_info)
            # user.save()
            return user
        return None