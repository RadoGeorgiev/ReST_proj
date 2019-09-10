from django.shortcuts import render
from django.http import Http404
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
        serialiazer = QuestionSerializer(data=request.data)

        if serialiazer.is_valid():
            serialiazer.save()
            return Response(data=serialiazer.data, status=status.HTTP_201_CREATED)
        return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDetails(APIView):

    def get_object(self, pk):
        try:
            question = Question.objects.get(pk=pk)
            return question
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, question_id):
        question = self.get_object(pk=question_id)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    def put(self, request, question_id):         ### function PUT finds and REPLACAES the obj// function Patch - Edits part of it
        question = self.get_object(pk=question_id)
        serializer = QuestionSerializer(question, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, question_id):
        question = self.get_object(pk=question_id)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
