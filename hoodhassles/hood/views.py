from django.shortcuts import render
# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout

from django.http import JsonResponse
from .models import *
from math import sin, cos, sqrt, atan2, radians
import datetime
from django.http import JsonResponse


def distance(lat1, lon1, lat2, lon2):

    # approximate radius of earth in km
    R = 6373.01
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance


def home(request):
    if request.method == 'POST':
        # add the lati and longi in the session
        request.session['lati'] = request.POST['lati']
        request.session['longi'] = request.POST['longi']
        return HttpResponseRedirect(reverse('forum',kwargs={'loc': 'city'}))
    else:
        return render(request, 'home.html')


class cc:
    def __init__(self, c, dist):
        self.complaint = c
        self.dist = dist

def forum(request, loc):
    if request.session.has_key('lati') and request.session.has_key('longi'):
        site = 'city.html'
        litt = []

        if loc == 'mycomplaints':
            complaints = Complain.objects.filter(user = request.user).order_by('date').reverse()
            for c in complaints: 
                litt.append(cc(c, 0))
        else: 
            # get all items in range
            complaints = Complain.objects.filter(ran=loc).order_by('date').reverse()
            # calculate distace if they are near the user then add them to the dictionary
            for c in complaints:
                dist = distance(float(request.session['lati']), float(request.session['longi']), c.lati, c.longi)
                flag = 0
                if loc == 'city':
                    if dist < 25:
                        flag = 1
                elif loc == 'locality':
                    if dist < 4:
                
                        flag = 1
                elif loc == 'neighborhood':
                    if dist < 1.5:
            
                        flag = 1
                elif loc == 'society':
                    if dist < 0.5:
                
                        flag = 1
                if flag == 1:
                    litt.append(cc(c, dist))
                # print(dist, c.title)

        context = {
            'complaints': litt,
            'lati': request.session["lati"],
            'longi':request.session['longi'],
            'loc':loc,
            'noc': len(litt)
        }

        return render(request, site, context)
    else:
        return HttpResponseRedirect(reverse('home'))



def mylogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            return render(request, "error.html", {
                "message":"Invalid credentials."
            })



def mylogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def myregister(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]

        if User.objects.filter(username=username).exists():
            print("you messed up")
            context = {
                "message": "username already taken",
            }
            return render(request, "error.html", context)
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            login(request, user)
            return HttpResponseRedirect(reverse("forum", kwargs={'loc':"city"}))


def newcomplaint(request):
    if request.method == "POST":
        newcomplaint = Complain.objects.create(
            user=request.user,
            title=request.POST['title'],
            content = request.POST['content'],
            ran = request.POST['range'],
            lati = request.POST['lati'],
            longi = request.POST['longi'],
            date = datetime.datetime.now()
            )
        
        print(datetime.datetime.now())

        if len(request.FILES) == 0:
            print('no files')
        else: 
            _, file = request.FILES.popitem()
            file = file[0]
            newcomplaint.image = file
            newcomplaint.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def upvote(request, cid, uid):

    
    check = Complain.objects.filter(voters = request.user, id=cid)
    
    state = True
    print(len(check), check)
    if len(check) == 0:
        state = False
        c = Complain.objects.get(id=cid)
        c.voters.add(request.user)
        c.votes += 1
        c.save()
        print('here')   

    return JsonResponse({
        "state": state
    })
    
def solve(request, cid):
    try:
        check = Complain.objects.get(user = request.user, id = cid, solved = False)
        check.solved = True
        check.save()
        return JsonResponse({
            "state": True
        })
    except:
        check = None
        if check == None:
            # not allowed
            return JsonResponse({
                "state": False
            })


def delete(request, cid):
    try:
        check = Complain.objects.get(user = request.user, id = cid)
        check.delete()
        return JsonResponse({
            "state": True
        })
    except:
        check = None
        if check == None:
            # not allowed
            return JsonResponse({
                "state": False
            })