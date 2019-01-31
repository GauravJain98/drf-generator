from django.contrib.auth.models import *
from rest_framework import serializers
from .models import *

class CustomUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields = '__all__'

class EvaluatorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Evaluator
		fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Question
		fields = '__all__'

class QuizSerializer(serializers.ModelSerializer):
	class Meta:
		model = Quiz
		fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Answer
		fields = '__all__'

class OptionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Option
		fields = '__all__'

class SubmissionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Submission
		fields = '__all__'

