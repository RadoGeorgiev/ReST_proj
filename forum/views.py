from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Question
from .serializers import QuestionSerializer

# Create your views here.


"""
This is a paragraph comment
bla bla
bla bla
"""


class QuestionsList(APIView):

    def get(self, request):
        questions = Question.objects.all()
        print(questions)
        serializer = QuestionSerializer(questions, many=True)
        print(serializer)
        return Response(serializer.data)

    def post(self, request):
        seriliazer = QuestionSerializer(data=request.data)

        if seriliazer.is_valid():
            seriliazer.save()
            return Response(data=seriliazer.data, status=status.HTTP_201_CREATED)
        return Response(seriliazer.errors, status=status.HTTP_400_BAD_REQUEST)