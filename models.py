from django.db import models
from django.contrib.auth.models import User

class CommenInfo(models.Model):
	archived = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def delete(self):
		self.archived = True
		super().save()

	class Meta:
		abstract = True
class CustomUser(CommenInfo):
	pass

class Evaluator(CommenInfo):
	pass

class Question(CommenInfo):
	pass

class Quiz(CommenInfo):
	pass

class Answer(CommenInfo):
	pass

class Option(CommenInfo):
	pass

class Submission(CommenInfo):
	pass

