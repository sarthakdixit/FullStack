from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Users
from django.contrib.auth.hashers import make_password, check_password
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.
def back(request):
  response = redirect(request.COOKIES.get('realestate_gotoback', 'index'))
  response.delete_cookie('realestate_gotoback')
  return response

def logoutUser(request):
  email = request.COOKIES.get('realestate_cookies', 'NO')
  u = Users.objects.get(email=email)
  u.online = 'F'
  u.save()
  goto_prev_page = request.GET.get('next', '/')
  goto_prev_page = goto_prev_page.replace('/','')
  if goto_prev_page == 'information':
    response = redirect('index')
  else:
   response = redirect(goto_prev_page)
  response.delete_cookie('realestate_cookies')
  return response

def SetCookie(response, email):
  response.set_cookie('realestate_cookies', email)

def loginUser(request):
  if request.method == 'POST':
    user = request.POST.dict()
    email = user.get('email')
    if checkIfUserExist(email):
      u = Users.objects.get(email=email)
      if check_password(user.get('password'), u.password):
        u.online = 'T'
        u.save()
        response = redirect(request.COOKIES.get('realestate_gotoback', 'index'))
        SetCookie(response, email)
        response.delete_cookie('realestate_gotoback')
        return response
      else:
        messages.error(request, 'Wrong password.')
    else:
      messages.error(request, 'Email does not exists')
    return redirect('user_login')

def checkIfUserExist(email):
  try:
    user = Users.objects.get(email=email)
    return True
  except Users.DoesNotExist:
    return False

def saveUser(user):
  u = Users()
  u.email = user.get('email')
  u.password = make_password(user.get('password'))
  u.save()

def sendEmailLink(email): 
  subject = 'Subject'
  html_message = render_to_string('mail_template.html', {'context': 'values'})
  plain_message = strip_tags(html_message)
  from_email = 'sarthak.dixit_cs17@gla.ac.in'
  to = email
  mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)

def registerUser(request):
  if request.method == 'POST':
    user = request.POST.dict()
    if checkIfUserExist(user.get('email')):
      messages.error(request, 'Email Already Exists.')
      return redirect('user_register')
    else:
      saveUser(user)
      # sendEmailLink(user.get('email'))
      messages.success(request, 'User Created, Please Verify your account')
      return redirect('user_login')

def login(request):
  goto_prev_page = request.GET.get('next', '/')
  goto_prev_page = goto_prev_page.replace('/','')
  if goto_prev_page == '':
    goto_prev_page = 'index'
  context = {
    'title' : 'Login Form',
    'h1' : 'Login',
    'action' : 'loginUser',
    'login' : True,
    'register' : False,
  }
  response = render(request, 'login.html', context)
  response.set_cookie('realestate_gotoback', goto_prev_page)
  return response

def register(request):
  context = {
    'title' : 'Registeration Form',
    'h1' : 'Register',
    'action' : 'registerUser',
    'login' : False,
    'register' : True,
  }
  return render(request, 'login.html', context)