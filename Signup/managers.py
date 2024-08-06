from django.contrib.auth.base_user import BaseUserManager

class AppUserManager(BaseUserManager):

    def create_user(self, username, email, password, *args, **kwargs):
        if not email: 
            raise ValueError('An email is required.')
        if not password:
            raise ValueError('A password is required.')
        user = self.model(
            email = self.normalize_email(email=email),
            username=username,
            password=password
        )
        user.set_password(user.password)
        user.address = kwargs.get('address', '')
        user.user_type = kwargs.get('user_type', '')

        # user.address = kwargs['address']
        # user.user_type = kwargs['user_type']
        # TODO: Add other fields to be stored to the db here

        # if user_type == "customer":
        #     pass
        # elif user_type == "vendor":
        #     pass

        
        user.save()
        return user
         
    def create_superuser(self, username, email, password, *args, **kwargs):
            user = self.create_user( 
                email = self.normalize_email(email=email), 
                username=username, 
                password=password
                )
            #user.is_admin = True

            user.is_staff = True
            user.is_superuser = True
            
            if not user.is_staff:
                raise ValueError("Superuser must have is_staff = True")
            elif not user.is_superuser:
                raise ValueError("Superuser must have is_superuser = True")
            
            user.save()
            return user