from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from myapp.models import Restorent
from myapp.serializers import RestorentSerializer


# Create your views here.

class RestorentList(APIView):
		def get(self,request,pk=None,format=None):
			if request.method == "GET":
				id=pk
				if id is not None:
					res = Restorent.objects.get(id=id)
					serializer = RestorentSerializer(res)
					return Response(serializer.data)
				res = Restorent.objects.all()
				serializer = RestorentSerializer(res,many=True)
				return Response(serializer.data)

		def post(self,request,format=None):
			if request.method == "POST":
				serializer = RestorentSerializer(data=request.data)
				if serializer.is_valid():
					serializer.save()
				return Response({"msg" : "Data Posted Successfully"})
			return Response(serializer.errors)

		def put(self,request,pk,format=None):
			id = pk
			res = Restorent.objects.get(pk=id)
			serializer = RestorentSerializer(res, data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response({"msg":"Data updated Successfully"})
			return Response(serializer.errors)

		def delete(self,request,pk):
			id = pk
			res = Restorent.objects.get(pk=id)
			res.delete()
			return Response({"msg":"Data Deleted"})

