from rest_framework import status
from .models import Category, Product
from Signup.models import Vendor
from rest_framework.views import APIView
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

@api_view(['GET'])
def getProducts(request):
    queryset = Product.objects.all()
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

class ProductAPI(APIView):
    permission_classes = ( IsAuthenticated, )
    authentication_classes = ( SessionAuthentication, TokenAuthentication, )

    # def get(self, request, format=None):
    #     return Response({"message": "Iniital Test Successful"}, status=status.HTTP_200_OK)

    def category(self, cat):
        category = Category.objects.get(name__exact=cat)
        if  category:
            return category
        raise KeyError("No Such Category")

    def post(self, request):
        data = request.data

        categories = data.pop('categories', '')

        data['vendor'] = Vendor.objects.get(id__exact=data['vendor'])

        try:
            try:
                product = Product.objects.create(**data)
            except Exception as e:
                return Response({"Message": "Error Encountered", "Error": "Product Creation Failed", "Exception": e}, status=status.HTTP_400_BAD_REQUEST)

            if product:
                product.save()
                for i in categories:
                    category = self.category(i)
                    print(category)
                    product.categories.add(category)
                    product.save()
                
                prodserializer = ProductSerializer(product)
                return Response({"message": "Successfully Created Prod", "product": prodserializer.data}, status=status.HTTP_200_OK)
                
        except Exception as e:
            return Response({"Message": "Error Encountered", "Error": e}, status=status.HTTP_400_BAD_REQUEST)

class CategoryAPI(APIView):
    permission_classes = ( IsAuthenticated, )
    authentication_classes = ( SessionAuthentication, TokenAuthentication, )

    def get(self, request):
        categories = ["Clothes", "Jewellery", "Bags", "Shoes"]
        try:
            for i in categories:
                category =Category.objects.create(name=i)
                category.save()
            
            return Response({"message": "Categories Created Successfuly"}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"message": "Error Encountered On Creating Categories", "Error": e}, status=status.HTTP_400_BAD_REQUEST)

class ImageTest(APIView):
    authentication_classes = ( SessionAuthentication, TokenAuthentication, )
    permission_classes = ( IsAuthenticated, )

    def get(self, request):
        import cloudinary

        cloudinary.config(
            cloud_name = "dwaomuo1l",
            secure = True
        )

        image_tag = cloudinary.CloudinaryImage("gcbqmwr1hbvprfohlabz").url
        print(f"This is the image: {image_tag}")
        return Response(image_tag, status=status.HTTP_200_OK)
