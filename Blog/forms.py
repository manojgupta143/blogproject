from django import forms        
from django.forms import ModelForm
from django.forms.widgets import Textarea
from Blog.models import Comment
class EmailsendForm(forms.Form):
    name=forms.CharField(label='Enter Your Name', max_length=30, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Name'}), )
    email=forms.EmailField(label='Enter Your Email',widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Your Email'}))
    to=forms.EmailField(label='To',widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Share To'}))
    comment=forms.CharField(label='Write Something About Post', required=False,widget=Textarea(attrs={'class':'form-control','placeholder':'Write Comment Something About Post'}))
from django.forms import ModelForm
class CommentForm(ModelForm):
    class Meta:
        model=Comment
        fields=['name','email','body']
        labels={'name':"Enter Your Name",'email':'Enter Your Email Id','body':'Comment'}
        widgets={'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Name'}),
        'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Your Email'}),
        'body':forms.Textarea(attrs={'class':'form-control','placeholder':'Write Comment'})
        }
from django.contrib.auth.models import User
class SignupForm(ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password']
        labels={'username':' Enter User Name','password':' Enter Password','email':'Enter Email','first_name':'Enter First Name','last_name':'Enter Last Name'}
        widgets={'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your User Name'}),
        'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password'}),
        'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Your Email'}),
        'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}),
        'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'})
        }
        