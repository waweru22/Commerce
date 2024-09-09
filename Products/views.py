from rest_framework import status
from .models import Category, Product
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer, ImageSerializer
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

@api_view(['GET'])
def getProducts(request):
    # Fetches every product in the database and returns in a JSON object
    queryset = Product.objects.all()
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class ProductAPI(APIView)
    permission_classes = ( IsAuthenticated, )
    authentication_classes = ( SessionAuthentication, TokenAuthentication, )

    def category(self, cat):
        # Fetches a category object based on the category
        category = Category.objects.get(name__exact=cat)
        if  category:
            return category
        raise KeyError("No Such Category")
    
    def image_store(self, image):
        # Store Provided Image and Return URL/Image Object ID
        import requests

        # Make reqest to image storage endpoint
        res = requests.post('http://127.0.0.1:8000/products/image/', data={
            'image': image
        })

        if res.status_code == 200:
            response = res.json
            data = response['data']
            
            # Return image id and url if successfully stored
            return data
        return None

    def post(self, request):
        data = request.data

        categories = data.pop('categories', '')

        feature_image = data.pop('feature_image', '')
        images = data.pop('images', '')

        # Store Feature Image and Return URL/Entity ID
        temp = self.image_store(feature_image)
        if temp:
            data['feature_image'] = temp
        
        # Store Array of Extra Images For A Product and Return URL/Entity ID
        image_array = {}
        count = 0
        for i in images:
            temp = self.image_store(i)
            if temp:
                image_array[f'img{count}'] = temp['image']
                count += 1
        data['images'] = image_array

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
                return Response({"Message": "Successfully Created Prod", "data": prodserializer.data}, status=status.HTTP_200_OK)
                
        except Exception as e:
            return Response({"Message": "Error Encountered", "Error": e}, status=status.HTTP_400_BAD_REQUEST)


class CategoryAPI(APIView):
    permission_classes = ( IsAuthenticated, )
    authentication_classes = ( SessionAuthentication, TokenAuthentication, )

    def get(self, request):
        categories = ["Clothes", "Jewellery", "Bags", "Shoes"]
        try:
            for i in categories:
                category = Category.objects.create(name=i)
                category.save()
            
            return Response({"message": "Categories Created Successfuly"}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"message": "Error Encountered On Creating Categories", "Error": e}, status=status.HTTP_400_BAD_REQUEST)


class ImageAPI(APIView):
    authentication_classes = ( SessionAuthentication, TokenAuthentication, )
    permission_classes = ( IsAuthenticated, )

    def post(self, request):
        data = request.data

        serializer = ImageSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response({"Message": "Image Saved Successfully", "Error": None, "data": serializer.data}, status=status.HTTP_200_OK)

        return Response({"Message": "Image Storage Unsuccessful"}, status=status.HTTP_400_BAD_REQUEST)


