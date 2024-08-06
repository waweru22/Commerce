from rest_framework import serializers
from .models import AppUser, Vendor, Customer
from django.core.exceptions import ValidationError


class AppUserSerializer(serializers.ModelSerializer):
    user_type = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    date_joined = serializers.DateTimeField(write_only=True)
    address = serializers.CharField(write_only=True)
    username = serializers.CharField(write_only=True)

    #VENDOR 
    business_name = serializers.CharField(write_only=True)
    contact_firstname = serializers.CharField(write_only=True)
    contact_lastname = serializers.CharField(write_only=True)
    bank_name = serializers.CharField(write_only=True)
    beneficiary_name = serializers.CharField(write_only=True)
    account_number = serializers.CharField(write_only=True)

    #CUSTOMER
    firstname = serializers.CharField(write_only=True)
    lastname = serializers.CharField(write_only=True)
    
    class Meta:
        model = AppUser
        fields = '__all__'

    def validate_username(self, value):
        if AppUser.objects.filter(username=value).exists():
            raise ValidationError("Username already exists")
        return value

    def create(self, validated_data):
        print('From serializer: ')
        print('validated_data: ', type(validated_data), validated_data)
        email = validated_data.pop('email', '')
        password = validated_data.pop('password', '')
        # user_id = validated_data.pop('id', '')
        username = validated_data.pop('username', '')
        user_type = validated_data.pop('user_type', '')
        date_joined = validated_data.pop('date_joined', '')
        address = validated_data.pop('address', '')
        business_name = validated_data.pop('business_name','')
        contact_firstname = validated_data.pop('contact_firstname', '')
        contact_lastname = validated_data.pop('contact_firstname', '')
        bank_name = validated_data.pop('bank_name', '')
        beneficiary_name = validated_data.pop('beneficiary_name', '')
        account_number = validated_data.pop('account_number', '')
        firstname = validated_data.pop('firstname', '')
        lastname = validated_data.pop('lastname', '')

        user = AppUser.objects.create_user(username, email, password, **validated_data)

        vendor = VendorSerializer(read_only=True)
        customer = CustomerSerializer(read_only=True)

        if user_type == "vendor":
            vendor = Vendor.objects.create(
                email=email,
                user=user, 
                # user_id=user_id, 
                username=username, 
                address=address, 
                business_name=business_name,
                contact_firstname=contact_firstname,
                contact_lastname=contact_lastname,
                bank_name=bank_name,
                beneficiary_name=beneficiary_name,
                account_number=account_number,  
                date_joined=date_joined
                )
            vendor.save()

        elif user_type == "customer":
            customer = Customer.objects.create(
                user=user, 
                # user_id=user_id, 
                username=username, 
                firstname=firstname, 
                lastname=lastname, 
                address=address, 
                date_joined=date_joined
                )
            customer.save()
        return user
    

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'