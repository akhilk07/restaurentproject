from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from menus.models import menu_items

class DishesView(APIView):
    def get(self,request,*args,**kwargs):
        all_items=menu_items

        if "category" in request.query_params:
            category=request.query_params.get("category")
            items=[item for item in menu_items if item.get("category")==category]
        if "limit" in request.query_params:
            lim=int(request.query_params.get("limit"))
            all_items=all_items[:lim]

        return Response(data=all_items)
    def post(self,request,*args,**kwargs):
        dish=request.data
        menu_items.append(dish)
        return Response(data=dish)

class DishDetailView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("did")
        item=[item for item in menu_items if item.get("code")==id].pop()
        return Response(data=item)
    def put(self,request,*args,**kwargs):
        id= kwargs.get("did")
        instance=[item for item in menu_items if item.get("code")==id].pop()
        data=request.data
        instance.update(data)
        return Response(data=data)
    def delete(self,request,*args,**kwargs):
        id = kwargs.get("did")
        instance = [item for item in menu_items if item.get("code") == id].pop()
        menu_items.remove(instance)
        return Response(data=instance)

