from .models import Author,Book,Receiver,Transactionn
from django import forms
class Aform(forms.ModelForm):
	class Meta:
		model=Author
		fields=["authorid","authorname"]
		widgets={
		"authorid":forms.NumberInput(
			attrs={"class":"form-control my-2","placeholder":"Author ID",
			}),
		"authorname":forms.TextInput(
			attrs={"class":"form-control my-2","placeholder":"Author Name"
			})
		}

class Bform(forms.ModelForm):
	class Meta:
		model=Book
		fields=["bookid","title","isbn","year","size","authorid"]
		widgets={
		"bookid":forms.NumberInput(
			attrs={"class":"form-control my-2","placeholder":"Book Id"
			}),
		"title":forms.TextInput(
			attrs={"class":"form-control my-2","placeholder":"Title"
			}),
		"isbn":forms.TextInput(
			attrs={"class":"form-control my-2","placeholder":"ISBN"
			}),
		"year":forms.DateInput(
			attrs={"class":"form-control my-2","type":"Date","placeholder":"Published Year"
			}),
		"size":forms.NumberInput(
			attrs={"class":"form-control my-2","placeholder":"Size of Book"
			}),
		"authorid":forms.Select(
			attrs={"class":"form-control my-2","placeholder":"Author Id"
			})
		}

class Cform(forms.ModelForm):
	class Meta:
		model=Receiver
		fields=["sid","firstname","lastname","email","phonenumber"]
		widgets={
		"sid":forms.NumberInput(
			attrs={"class":"form-control my-2","placeholder":"Student Id"
			}),
		"firstname":forms.TextInput(
			attrs={"class":"form-control my-2","placeholder":"First Name"
			}),
		"lastname":forms.TextInput(
			attrs={"class":"form-control my-2","placeholder":"Last Name"
			}),
		"email":forms.TextInput(
			attrs={"class":"form-control my-2","placeholder":"Email"
			}),
		"phonenumber":forms.TextInput(
			attrs={"class":"form-control my-2","placeholder":"Phone Number"
			})
		}

class Dform(forms.ModelForm):
	class Meta:
		model=Transactionn
		fields=["transactionid","bookid","sid","receiveddate","submissiondate"]
		widgets={
		"transactionid":forms.NumberInput(
			attrs={"class":"form-control my-2","placeholder":"ID"
			}),
		"bookid":forms.Select(
			attrs={"class":"form-control my-2","placeholder":"Bookid"
			}),
		"sid":forms.Select(
			attrs={"class":"form-control my-2","placeholder":"Student id"
			}),
		"receiveddate":forms.DateInput(
			attrs={"class":"form-control my-2","type":"Date","placeholder":"Received Date"
			}),
		"submissiondate":forms.DateInput(
			attrs={"class":"form-control my-2","type":"Date","placeholder":"Submmission date"
			})
		}