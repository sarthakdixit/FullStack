from django.shortcuts import render, redirect
from .models import Buildings, Agents, Interior
from time import gmtime, strftime
import string 
import random
from datetime import date 

# Create your views here.
def deleteInterior(request, poll_id):
  Interior.objects.get(owner=poll_id).delete()
  return redirect('info_interior')

def saveInterior(request):
  if request.method == 'POST':
    email = request.COOKIES.get('realestate_cookies', 'NO')
    user = request.POST.dict()
    agnt = Interior()
    agnt.owner = email
    agnt.name = user.get('name')
    agnt.email = user.get('email')
    agnt.number = user.get('number')
    agnt.add = user.get('address')
    agnt.city = user.get('city')
    agnt.state = user.get('state')
    agnt.about = user.get('about')
    agnt.licence = user.get('licence')
    agnt.photo = request.FILES['photo']
    agnt.date = str(date.today())
    agnt.video = request.FILES['video']
    agnt.save()
    return redirect('info_interior')
    
def saveAgents(request):
  if request.method == 'POST':
    email = request.COOKIES.get('realestate_cookies', 'NO')
    user = request.POST.dict()
    agnt = Agents()
    agnt.owner = email
    agnt.name = user.get('name')
    agnt.email = user.get('email')
    agnt.number = user.get('number')
    agnt.add = user.get('address')
    agnt.city = user.get('city')
    agnt.state = user.get('state')
    agnt.about = user.get('about')
    agnt.licence = user.get('licence')
    agnt.photo = request.FILES['photo']
    agnt.date = str(date.today())
    agnt.save()
    return redirect('info_agent')

def deleteToDB(request, poll_id):
  Buildings.objects.get(IDNO=poll_id).delete()
  return redirect('info')

def deleteAgent(request, poll_id):
  Agents.objects.get(owner=poll_id).delete()
  return redirect('info_agent')

def generateKey():
  showtime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
  showtime = showtime.replace(' ', '')
  showtime = showtime.replace('-', '')
  showtime = showtime.replace(':', '')
  res = str(''.join(random.choices(string.ascii_uppercase+string.digits, k = 10)))
  return showtime+res

def searchKey(key):
  try:
    user = Buildings.objects.get(IDNO=key)
    return True
  except Buildings.DoesNotExist:
    return False

def saveToDB(request):
  if request.method == 'POST':
    user = request.POST.dict()
    build = Buildings()
    key = generateKey()
    while searchKey(key):
      key = generateKey()
    build.IDNO = key
    build.typ = user.get('type')
    build.action = user.get('action')
    build.localAdd = user.get('address')
    build.city = user.get('city')
    build.state = user.get('state')
    build.pin = user.get('pin')
    build.phone = user.get('number')
    build.desc = user.get('desc')
    build.neigh = user.get('nedesc')
    build.area = user.get('area')
    build.price = user.get('price')
    build.owner = user.get('email')
    build.date = str(date.today())
    build.photo1 = request.FILES['photo1']
    build.photo2 = request.FILES['photo2']
    build.photo3 = request.FILES['photo3']
    build.photo4 = request.FILES['photo4']
    build.video = request.FILES['video']
    build.save()
    return redirect('info')

def getAgent(email):
  try:
    user = Agents.objects.get(owner=email)
    return True
  except Agents.DoesNotExist:
    return False

def infoAgent(request):
  email = request.COOKIES.get('realestate_cookies', 'NO')
  if getAgent(email):
    infoData = Agents.objects.filter(owner=email).values()
  else:
    infoData = 'NO'
  context = {
    'title' : 'Be An Agent',
    'user_email' : request.COOKIES.get('realestate_cookies', 'NO'),
    'Data' : infoData,
  }
  return render(request, 'beAnAgent.html', context)

def getInterior(email):
  try:
    user = Interior.objects.get(owner=email)
    return True
  except Interior.DoesNotExist:
    return False

def infoInterior(request):
  email = request.COOKIES.get('realestate_cookies', 'NO')
  if getInterior(email):
    infoData = Interior.objects.filter(owner=email).values()
  else:
    infoData = 'NO'
  context = {
    'title' : 'Be A Designer',
    'user_email' : request.COOKIES.get('realestate_cookies', 'NO'),
    'Data' : infoData,
  }
  return render(request, 'beADesigner.html', context)
  
def getData(email):
  try:
    user = Buildings.objects.filter(owner=email)
    return True
  except Buildings.DoesNotExist:
    return False

def info(request):
  if request.COOKIES.get('realestate_cookies', 'NO') == 'NO':
    return redirect('index')
  email = request.COOKIES.get('realestate_cookies', 'NO')
  if getData(email):
    infoData = Buildings.objects.filter(owner=email).values()
  else:
    infoData = 'NO'
  context = {
    'title' : 'Profile',
    'user_email' : request.COOKIES.get('realestate_cookies', 'NO'),
    'info' : infoData,
  }
  return render(request, 'profile.html', context)