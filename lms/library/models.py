from django.db import models

# Create your models here.
class Author(models.Model):
	authorid=models.IntegerField(primary_key=True)
	authorname=models.CharField(max_length=100)

class Book(models.Model):
	bookid=models.IntegerField(primary_key=True)
	title=models.CharField(max_length=300)
	isbn=models.CharField(max_length=20)
	year=models.DateField(null=True)
	size=models.IntegerField()
	authorid=models.ForeignKey(Author,on_delete=models.CASCADE)

class Receiver(models.Model):
	sid=models.IntegerField(primary_key=True)
	firstname=models.CharField(max_length=50)
	lastname=models.CharField(max_length=50)
	email=models.CharField(max_length=300)
	phonenumber=models.CharField(max_length=15)

"""class Transaction(models.Model):
	transactionid=models.IntegerField(primary_key=True)
	bookid=models.ForeignKey(Book,on_delete=models.CASCADE)
	sid=models.ForeignKey(Receiver,on_delete=models.CASCADE)
	receiveddate=models.DateField(null=True)
	submissiondate=models.DateField(null=True)"""

class Transactionn(models.Model):
	transactionid=models.IntegerField(primary_key=True)
	bookid=models.ForeignKey(Book,on_delete=models.CASCADE)
	sid=models.ForeignKey(Receiver,on_delete=models.CASCADE)
	receiveddate=models.DateField(null=True)
	submissiondate=models.DateField(null=True)



