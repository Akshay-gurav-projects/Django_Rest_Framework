from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def student_api(request):
    if request.method == "GET":
        json_data = request.body #take all from body
        stream = io.BytesIO(json_data) #convert into bytes form
        pythondata = JSONParser().parse(stream) #convert into pythondata from (Dictionary)
        #this is for single data
        id = pythondata.get('id',None) #get id from python data
        if id is not None: #check if id is not none
            stu = Student.objects.get(id=id) #get id data from database table
            serializer = StudentSerializer(stu) #check with serializer
            # json_data = JSONRenderer().render(serializer.data) #convert into json
            # return HttpResponse(json_data,content_type='application/json') #sent back to frontent
            return JsonResponse(serializer.data, safe=False)
        #this is for multiple data
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        # json_data = JSONRenderer().render(serializer.data)
        # return HttpResponse(json_data,content_type='application/json')
        return JsonResponse(serializer.data, safe=False)

    if request.method == "POST":
        json_data = request.body #take all from body
        stream = io.BytesIO(json_data) #convert into bytes form
        pythondata = JSONParser().parse(stream) #convert into pythondata from (Dictionary)
        serializer = StudentSerializer(data = pythondata) #convert into complex data with help of serializer
        if serializer.is_valid(): #check the data is valid
            serializer.save() #save data in database
            res = {"msg":"data inserted"}
            # json_data = JSONRenderer().render(res)
            # return HttpResponse(json_data,content_type='application/json')
            return JsonResponse(res, safe=False)
        else:
            res = serializer.errors
            # json_data = JSONRenderer().render(res)
            # return HttpResponse(json_data,content_type='application/json')
            return JsonResponse(res, safe=False)
        

    if request.method == "PUT":
        json_data = request.body #take all from body
        stream = io.BytesIO(json_data) #convert into bytes form
        pythondata = JSONParser().parse(stream) #convert into pythondata from (Dictionary)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        #this is for partially update means if one data is missing or old still this update the data
        serializer = StudentSerializer(stu, data=pythondata, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {"msg":"data updated !!"}
            # json_data = JSONRenderer().render(res)
            # return HttpResponse(json_data,content_type='application/json')
            return JsonResponse(res, safe=False)
        else:
            res = serializer.errors
            # json_data = JSONRenderer().render(res)
            # return HttpResponse(json_data,content_type='application/json')
            return JsonResponse(res, safe=False)

    if request.method == "DELETE":
        json_data = request.body #take all from body
        stream = io.BytesIO(json_data) #convert into bytes form
        pythondata = JSONParser().parse(stream) #convert into pythondata from (Dictionary)
        id = pythondata.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()
        res = {"msg":"data deleted !!"}
        # json_data = JSONRenderer().render(res)
        # return HttpResponse(json_data,content_type='application/json')
        return JsonResponse(res, safe=False) #it is not dictionary thats why we use sefe=False