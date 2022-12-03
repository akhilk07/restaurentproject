from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from productapi.models import Products
from rest_framework import status

# Create your views here.

from  productapi.serializers import ProductSerializer
class ProductView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Products.objects.all()
        serializer=ProductSerializer(qs,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    def post(self,request,*args,**kwargs):
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            Products.objects.create(**serializer.validated_data,status=status.HTTP_201_CREATED)
            # Products.objects.create(product_name=request.data.get("product_name"),
            #                         category=request.data.get("category"),
            #                         price=request.data.get("price"),
            #                         rating=request.data.get("rating"))
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class ProductDetailView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Products.objects.get(id=id)
        serializer=ProductSerializer(qs)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        instance=Products.objects.get(id=id)
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            # instance.product_name=serializer.validated_data("product_name")
            # instance.category=serializer.validated_data("category")
            # instance.price=serializer.validated_data("price")
            # instance.rating=serializer.validated_data("rating")
            #
            # instance.save()
            instance.update(**serializer.validated_data)
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        instance=Products.objects.get(id=id)
        serializer=ProductSerializer(instance)
        instance.delete()
        return Response({"msg:deleted"},status=status.HTTP_204_NO_CONTENT)