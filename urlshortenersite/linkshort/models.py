from django.db import models
# from django import forms

class Link(models.Model):
	url = models.CharField(max_length=100, unique=True)
	shortened = models.Char(max_length=10, primary_key=True)

	def __str__(self):
		return self.url +'-'+ self.shortened

