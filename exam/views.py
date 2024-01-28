from django.shortcuts import render
from rest_framework import  status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Exam, ExamTaker
from .serializers import userSerializer,ExamModelSerializer,authorsSerializer

@api_view(['GET'])
def allExamsView(request):
    if request.query_params:
        items = Exam.objects.filter(**request.query_params.dict())
    else:
        items = Exam.objects.all()
 
    # if there is something in items else raise error
    if items:
        serializer = ExamModelSerializer(items, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET'])
def allAthoursView(request):

    if request.query_params:
        items = ExamTaker.objects.filter(**request.query_params.dict())
    else:
        items = ExamTaker.objects.all()
 
    # if there is something in items else raise error
    if items:
        serializer = authorsSerializer(items, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

@api_view(['POST'])
def userRegistrationView(request):
    user = userSerializer(data=request.data)
    if user.is_valid():
        user.save()
        return Response(user.data, status=status.HTTP_201_CREATED)
    else:
        return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)
    



# def test(request):
#     return render(request,'main.html')

# def exam(request,exam_number):
#     return render(request,'main.html')