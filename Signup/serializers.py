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

    def create(self, user_data): 

        user = AppUser.objects.create_user(**user_data)

        vendor = VendorSerializer(read_only=True)
        customer = CustomerSerializer(read_only=True)

        if user_data['user_type'] == "vendor":
            keys = ['email', 'username', 'address', 'business_name', 'contact_firstname', 'contact_lastname', 'bank_name', 'beneficiary_name', 'account_number', 'date_joined']
            vendor_info = { x:user_data[x] for x in keys }
            vendor = Vendor.objects.create( **vendor_info )
            
            vendor.save() 

        # elif user_data['user_type'] == "customer":
        #     customer = Customer.objects.create( **user_data )
        #     customer.save() 
        return user
    

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'