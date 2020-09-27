from django.shortcuts import render
from information.models import Buildings, Interior, Agents
from django.db.models import Q

# Create your views here.
def showAgents(request, id):
  context = {
    'title' : id,
    'data' : Agents.objects.filter(owner=id),
  }
  return render(request, 'showAgents.html', context)

def showInterior(request, id):
  context = {
    'title' : id,
    'data' : Interior.objects.filter(owner=id),
  }
  return render(request, 'showInterior.html', context)

def fullData(request, id):
  context = {
    'title' : 'Full Data',
    'data' : Buildings.objects.filter(IDNO=id),
  }
  return render(request, 'fulldata.html', context)

def agents(request):
  email = request.COOKIES.get('realestate_cookies', 'NO')
  u = request.GET.dict()
  search = u.get('search')
  if search:
    if search == '':
      data = Agents.objects.filter(~Q(owner=email))
    else:
      data = Agents.objects.filter(~Q(owner=email), Q(name=search) | Q(city=search) | Q(state=search))
  else:
    data = Agents.objects.filter(~Q(owner=email))
  context = {
    'title' : 'Agents',
    'global_user' : email,
    'data' : data,
    'search' : search,
  }
  return render(request, 'agents.html', context)

def interior(request):
  email = request.COOKIES.get('realestate_cookies', 'NO')
  u = request.GET.dict()
  search = u.get('search')
  if search:
    if search == '':
      data = Interior.objects.filter(~Q(owner=email))
    else:
      data = Interior.objects.filter(~Q(owner=email), Q(name=search) | Q(city=search) | Q(state=search))
  else:
    data = Interior.objects.filter(~Q(owner=email))
  context = {
    'title' : 'Interior Designers',
    'global_user' : email,
    'data' : data,
    'search' : search,
  }
  return render(request, 'interior.html', context)

def farm(request):
  typ = 'farm'
  email = request.COOKIES.get('realestate_cookies', 'NO')
  u = request.GET.dict()
  action = u.get('action')
  search = u.get('search')
  if action:
    if action == 'both':
      if search == '':
        data = Buildings.objects.filter(~Q(owner=email), Q(typ=typ))
      else:
        data = Buildings.objects.filter(~Q(owner=email), Q(typ=typ), Q(localAdd=search) | Q(city=search) | Q(state=search) | Q(pin=search))
    else:
      if search == '':
        data = Buildings.objects.filter(~Q(owner=email), Q(typ=typ), action=action)
      else:
        data = Buildings.objects.filter(~Q(owner=email), Q(typ=typ), Q(action=action), Q(localAdd=search) | Q(city=search) | Q(state=search) | Q(pin=search))
  else:
    data = Buildings.objects.filter(~Q(owner=email), Q(typ=typ))
  context = {
    'title' : 'Farm',
    'global_user' : email,
    'action' : action,
    'search' : search,
    'data' : data,
  }
  return render(request, 'farm.html', context)

def commercial(request):
  typ = 'commercial'
  action = ''
  search = ''
  email = request.COOKIES.get('realestate_cookies', 'NO')
  u = request.GET.dict()
  action = u.get('action')
  search = u.get('search')
  if action:
    if action == 'both':
      if search == '':
        data = Buildings.objects.filter(~Q(owner=email), Q(typ=typ))
      else:
        data = Buildings.objects.filter(~Q(owner=email), Q(typ=typ), Q(localAdd=search) | Q(city=search) | Q(state=search) | Q(pin=search))
    else:
      if search == '':
        data = Buildings.objects.filter(~Q(owner=email), Q(typ=typ), action=action)
      else:
        data = Buildings.objects.filter(~Q(owner=email), Q(typ=typ), Q(action=action), Q(localAdd=search) | Q(city=search) | Q(state=search) | Q(pin=search))
  else:
    data = Buildings.objects.filter(~Q(owner=email), Q(typ=typ))
  context = {
    'title' : 'Commercial',
    'global_user' : email,
    'action' : action,
    'search' : search,
    'data' : data,
  }
  return render(request, 'commercial.html', context)

def plot(request):
  typ = 'plot'
  action = ''
  search = ''
  email = request.COOKIES.get('realestate_cookies', 'NO')
  u = request.GET.dict()
  action = u.get('action')
  search = u.get('search')
  if action:
    if action == 'both':
      if search == '':
        data = Buildings.objects.filter(~Q(owner=email), Q(typ=typ))
      else:
        data = Buildings.objects.filter(~Q(owner=email), Q(typ=typ), Q(localAdd=search) | Q(city=search) | Q(state=search) | Q(pin=search))
    else:
      if search == '':
        data = Buildings.objects.filter(~Q(owner=email), Q(typ=typ), action=action)
      else:
        data = Buildings.objects.filter(~Q(owner=email), Q(typ=typ), Q(action=action), Q(localAdd=search) | Q(city=search) | Q(state=search) | Q(pin=search))
  else:
    data = Buildings.objects.filter(~Q(owner=email), Q(typ=typ))
  context = {
    'title' : 'Plot',
    'global_user' : email,
    'action' : action,
    'search' : search,
    'data' : data,
  }
  return render(request, 'plot.html', context)

def villa(request):
  typ = 'villa'
  action = ''
  search = ''
  email = request.COOKIES.get('realestate_cookies', 'NO')
  u = request.GET.dict()
  action = u.get('action')
  search = u.get('search')
  if action:
    if action == 'both':
      if search == '':
        data = Buildings.objects.filter(~Q(owner=email), Q(typ=typ))
      else:
        data = Buildings.objects.filter(~Q(owner=email), Q(typ=typ), Q(localAdd=search) | Q(city=search) | Q(state=search) | Q(pin=search))
    else:
      if search == '':
        data = Buildings.objects.filter(~Q(owner=email), Q(typ=typ), action=action)
      else:
        data = Buildings.objects.filter(~Q(owner=email), Q(typ=typ), Q(action=action), Q(localAdd=search) | Q(city=search) | Q(state=search) | Q(pin=search))
  else:
    data = Buildings.objects.filter(~Q(owner=email), Q(typ=typ))
  context = {
    'title' : 'Villa',
    'global_user' : email,
    'action' : action,
    'search' : search,
    'data' : data,
  }
  return render(request, 'villa.html', context)

def flat(request):
  typ = 'flat'
  action = ''
  search = ''
  email = request.COOKIES.get('realestate_cookies', 'NO')
  u = request.GET.dict()
  action = u.get('action')
  search = u.get('search')
  if action:
    if action == 'both':
      if search == '':
        data = Buildings.objects.filter(~Q(owner=email), Q(typ=typ))
      else:
        data = Buildings.objects.filter(~Q(owner=email), Q(typ=typ), Q(localAdd=search) | Q(city=search) | Q(state=search) | Q(pin=search))
    else:
      if search == '':
        data = Buildings.objects.filter(~Q(owner=email), Q(typ=typ), action=action)
      else:
        data = Buildings.objects.filter(~Q(owner=email), Q(typ=typ), Q(action=action), Q(localAdd=search) | Q(city=search) | Q(state=search) | Q(pin=search))
  else:
    data = Buildings.objects.filter(~Q(owner=email), Q(typ=typ))
  context = {
    'title' : 'Flat',
    'global_user' : email,
    'action' : action,
    'search' : search,
    'data' : data,
  }
  return render(request, 'flat.html', context)

def getIndex(request):
  context = {
    'title' : 'Real Estate',
    'global_user' : request.COOKIES.get('realestate_cookies', 'NO'),
  }
  return render(request, 'index.html', context)