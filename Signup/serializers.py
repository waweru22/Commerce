from rest_framework import serializers
from .models import AppUser, Vendor, Customer
from django.core.exceptions import ValidationError


class AppUserSerializer(serializers.ModelSerializer):
    user_type = serializers.CharField(required=False)
    email = serializers.EmailField(write_only=True, required=False)
    date_joined = serializers.DateTimeField(write_only=True, required=False)
    address = serializers.CharField(write_only=True, required=False)
    username = serializers.CharField(write_only=True, required=False)
    phone_no = serializers.CharField(write_only=True, required=False)

    #VENDOR 
    business_name = serializers.CharField(write_only=True, required=False)
    contact_firstname = serializers.CharField(write_only=True, required=False)
    contact_lastname = serializers.CharField(write_only=True, required=False)
    bank_name = serializers.CharField(write_only=True, required=False)
    beneficiary_name = serializers.CharField(write_only=True, required=False)
    account_number = serializers.CharField(write_only=True, required=False)

    #CUSTOMER
    firstname = serializers.CharField(write_only=True, required=False)
    lastname = serializers.CharField(write_only=True, required=False)
    
    class Meta:
        model = AppUser
        fields = '__all__'

    def validate_username(self, value):
        if AppUser.objects.filter(username=value).exists():
            raise ValidationError("Username already exists")
        return value

    def create(self, user_data): 
        vendor = VendorSerializer(read_only=True)
        customer = CustomerSerializer(read_only=True)

        user = AppUser.objects.create_user(**user_data)


        if user:
            if user_data['user_type'] == "vendor":
                keys = ['business_name', 'contact_firstname', 'contact_lastname', 'bank_name', 'beneficiary_name', 'account_number']
                vendor_info = { x:user_data[x] for x in keys }
                vendor = Vendor.objects.create(user=user, **vendor_info )
                vendor.save() 
                print('vendor info: ', vendor_info)
                # new_user = vendor_info.update(user)
                # print(new_user)
                print(type(vendor_info))
                print(type(user))

            elif user_data['user_type'] == "customer":
                keys = ['firstname', 'lastname']
                customer_info = { x:user_data[x] for x in keys }
                customer = Customer.objects.create(user=user, **customer_info )
                customer.save()
                print('customer info: ', customer_info)
            else:
                raise ValidationError("User must either be a 'customer' or 'vendor' ")
            # print(user)
            return user
    

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'