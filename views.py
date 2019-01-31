from django.contrib.auth.models import User, Group 
from rest_framework import viewsets 
from mainApp.serializers import UserSerializer, GroupSerializer 

class CustomUserViewSet(viewsets.ModelViewSet):
	queryset = CustomUser.objects.all()
	serializer_class = CustomUserSerializer

class EvaluatorViewSet(viewsets.ModelViewSet):
	queryset = Evaluator.objects.all()
	serializer_class = EvaluatorSerializer

class QuestionViewSet(viewsets.ModelViewSet):
	queryset = Question.objects.all()
	serializer_class = QuestionSerializer

class QuizViewSet(viewsets.ModelViewSet):
	queryset = Quiz.objects.all()
	serializer_class = QuizSerializer

class AnswerViewSet(viewsets.ModelViewSet):
	queryset = Answer.objects.all()
	serializer_class = AnswerSerializer

class OptionViewSet(viewsets.ModelViewSet):
	queryset = Option.objects.all()
	serializer_class = OptionSerializer

class SubmissionViewSet(viewsets.ModelViewSet):
	queryset = Submission.objects.all()
	serializer_class = SubmissionSerializer

