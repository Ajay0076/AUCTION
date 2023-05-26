from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from django.contrib.auth.decorators import login_required

def index(request):    
    return render(request, "auctions/home.html",{
        "a": Player.objects.all(),
            })


def login_view(request):
    if request.method == "POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        player=Player.objects.filter(email=email,password=password)
        club= Club.objects.filter(email=email,password=password)
        if player.filter(email=email,password=password).exists():
            for i in player:
                id=i.id
                email=i.email
                request.session['id']=id
                request.session['email']=email
            return redirect('/player_home')
        elif club.filter(email=email,password=password).exists():
            for i in club:
                id=i.id
                email=i.email
                request.session['id']=id
                request.session['email']=email
            return redirect('/club_home')


        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid email and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

from django.shortcuts import render, redirect
from .models import Player

def register_player(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        mobilenumber = request.POST.get('mobilenumber')
        currentclub = request.POST.get('currentclub')
        age = request.POST.get('age')
        position = request.POST.get('position')
        conf = request.POST.get('conf')
        password = request.POST.get('password')
        image_url = request.FILES.get('image_url')
        if password != conf:
            msg='Passwords Did not Match'
            return render(request, 'auctions/p_register.html',{'msg':msg})
        elif password == conf :
            player = Player(username=username, email=email,mobilenumber=mobilenumber, position=position, currentclub=currentclub, Age=age, password=password, image_url=image_url)
            player.save()
            return redirect('/login')  # Redirect to a success page



    return render(request, 'auctions/p_register.html')

def register_club(request):
    if request.method=='POST':
        clubname=request.POST.get('clubname')
        manager=request.POST.get('manager')
        email=request.POST.get('email')
        contactNo=request.POST.get('contactNo')
        place=request.POST.get('place')
        logo=request.FILES.get('logo')
        conf = request.POST.get('conf')
        password=request.POST.get('password')
        if password != conf:
            msg='Passwords Did not Match'
            return render(request, 'auctions/c_register.html',{'msg':msg})
        elif password == conf :
            club = Club(clubname=clubname, email=email, contactNo=contactNo,logo=logo, place=place,manager=manager,
                        password=password, )
            club.save()

            return redirect('/login')  # Redirect to a success page
    return render(request, 'auctions/c_register.html')

def player_home(request):
    a=auction.objects.filter(status='No')
    return render(request,'auctions/player_home.html',{'a':a})

def participate(request,id):
    userid=request.session['id']
    player=Player.objects.get(id=userid)
    a=auction.objects.get(id=id)
    if auctionreg.objects.filter(playername=player,auction=a).exists():
        msg='Already Registred'
        a=auction.objects.filter(status='No')
        all={'a':a,'msg':msg}
        return render(request,'auctions/player_home.html',all)
    else:    
        auctionreg.objects.create(playername=player,auction=a,status='Player')
    return redirect('/my')

def club_home(request):
    a=auction.objects.filter(status='No')
    return render(request,'auctions/club_home.html',{'a':a})

def participatec(request,id):
    userid=request.session['id']
    club=Club.objects.get(id=userid)
    a=auction.objects.get(id=id)
    if auctionreg.objects.filter(clubname=club,auction=a).exists():
        msg='Already Registred'
        a=auction.objects.filter(status='No')
        all={'a':a,'msg':msg}
        return render(request,'auctions/club_home.html',all)
    else:    
        auctionreg.objects.create(clubname=club,auction=a,status='Club')
    return redirect('/myc')

def my(request):
    player=request.session['id']
    a=auctionreg.objects.filter(playername=player)
    return render(request,'auctions/my.html',{'a':a})

def myc(request):
    club=request.session['id']
    a=auctionreg.objects.filter(clubname=club)
    return render(request,'auctions/myc.html',{'a':a})

def registred(request,auction):
    # auction=auctionreg.objects.get(id=auction)
    a=auctionreg.objects.filter(auction=auction,status='Player')
    b=bidplayer.objects.filter(auction=auction)
    return render(request,'auctions/registered.html',{'a':a,'b':b})


from django.shortcuts import render, redirect
from .models import bidplayer
from django.contrib import messages

def add_bid(request, id, pid):
    userid = request.session.get('id')
    
    if not userid:
        return HttpResponse('User ID not found in session.')

    if request.method == 'POST':
        request.session['id'] = userid
        try:
            auction_obj = auction.objects.get(id=int(id))
            club = Club.objects.get(id=userid)
            player = Player.objects.get(id=pid)
            amount = int(request.POST.get('amount'))

            # Check if the bid amount is greater than the base price
            if amount <= 1000:
                msg = 'Bid amount should be greater than the base price.'
                a = auctionreg.objects.filter(auction=id, status='Player')
                b=bidplayer.objects.filter(auction=id)
                context = {'a': a,'b':b, 'msg': msg}
                return render(request, 'auctions/registered.html', context)

            existing_bid = bidplayer.objects.filter(auction=auction_obj, playername=player).first()

            if existing_bid:
                current_amount = existing_bid.amount

                # Check if the bid amount is greater than the current amount
                if amount <= current_amount:
                    msg = 'Bid amount should be greater than the current amount.'
                    a = auctionreg.objects.filter(auction=id, status='Player')
                    b=bidplayer.objects.filter(auction=id)
                    context = {'a': a,'b':b, 'msg': msg}
                    return render(request, 'auctions/registered.html', context)

            # Create a new bid
            bid = bidplayer.objects.create(auction=auction_obj, clubname=club, playername=player, amount=amount)

            msg = 'Bid added successfully.'
            a = auctionreg.objects.filter(auction=id, status='Player')
            b=bidplayer.objects.filter(auction=id)
            context = {'a': a,'b':b, 'msg': msg}
            return render(request, 'auctions/registered.html', context)

        except auction.DoesNotExist:
            return HttpResponse('Auction does not exist.')

        except (Club.DoesNotExist, Player.DoesNotExist):
            return HttpResponse('Club or Player does not exist.')
    else:
        return render(request, 'auctions/addbid.html')
def viewbid(request):
    id=request.session['id']
    a=bidplayer.objects.filter(playername=id)
    return render(request,'auctions/viewbid.html',{'a':a})
def acceptoffer(request,cid):
    id=request.session['id']
    player=Player.objects.get(id=id)
    club=Club.objects.get(id=cid)
    Acceptdeal.objects.create(clubname=club,playername=player,status='Completed')
    return redirect('/myclub')

def myclub(request):
    id=request.session['id']
    a =Acceptdeal.objects.filter(playername=id)
    return render(request,'auctions/myclub.html',{'a':a})

def editplayer(request):
    if request.method == 'POST':
        id = request.session['id']
        user = Player.objects.filter(id=id)
        up = Player.objects.get(id=id)
        username = request.POST.get('username')
        currentclub = request.POST.get('currentclub')
        mobilenumber = request.POST.get('mobilenumber')
        email = request.POST.get('email')

        if 'image_url' in request.FILES:
            image_url = request.FILES['image_url']
            up.image_url = image_url

        up.username = username
        up.currentclub = currentclub
        up.mobilenumber = mobilenumber
        up.email = email

        up.save()
        ud = Player.objects.filter(email=request.session['email'])
        context = {'details': ud,
                   'user': user,
                   'msg': 'Profile Details Updated'}

        return redirect('/my')
    else:
        id = request.session['id']
        up = Player.objects.filter(id=id)
        user =Player.objects.filter(id=id)
        all_data = {
            'user': user,
            'details': up,
        }
        return render(request, 'auctions/editprofile-player.html', all_data)
    


def editculb(request):
    if request.method == 'POST':
        id = request.session['id']
        user = Club.objects.filter(id=id)
        up = Club.objects.get(id=id)
        clubname = request.POST.get('clubname')
        manager = request.POST.get('manager')
        contactNo = request.POST.get('contactNo')
        email = request.POST.get('email')

        if 'logo' in request.FILES:
            logo = request.FILES['logo']
            up.logo = logo

        up.clubname = clubname
        up.manager = manager
        up.conactNo = contactNo
        up.email = email

        up.save()
        ud = Club.objects.filter(email=request.session['email'])
        context = {'details': ud,
                   'user': user,
                   'msg': 'Profile Details Updated'}

        return redirect('/myc')
    else:
        id = request.session['id']
        up = Club.objects.filter(id=id)
        user =Club.objects.filter(id=id)
        all_data = {
            'user': user,
            'details': up,
        }
        return render(request, 'auctions/editprofile-club.html', all_data)
    

def myplayers(request):
    id=request.session['id']
    a =Acceptdeal.objects.filter(clubname=id)
    return render(request,'auctions/myplayers.html',{'a':a})

def changepassword_player(request):
    id = request.session['id']
    print(id)
    user = Player.objects.filter(id=id)
    all = {
        'user': user,
    }
    if request.method == 'POST':
        email = request.session['email']
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        print('Email Is:' + email)
        print("Current_password" + str(current_password))
        try:

            ul = Player.objects.get(email=email, password=current_password)

            if ul is not None:
                ul.password = new_password  # change field
                ul.save()
                msg =  'Password Changed Successfully'
                all = {
                    'user': user,
                    'msg': msg
                }
                return render(request, 'auctions/change_password_player.html',all)
            else:
                context =  'Your Old Password is Wrong'
                all = {
                    'user': user,
                    'msg': context
                }
                return render(request, 'auctions/change_password_player.html',all)

        except Player.DoesNotExist:
            context =  'Your Old Password is Wrong'
            all = {
                'user': user,
                'msg': context
            }
            return render(request, 'auctions/change_password_player.html',all)
    else:
        return render(request, 'auctions/change_password_player.html',all)
    
def changepassword_club(request):
    id = request.session['id']
    print(id)
    user = Club.objects.filter(id=id)
    all = {
        'user': user,
    }
    if request.method == 'POST':
        email = request.session['email']
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        print('Email Is:' + email)
        print("Current_password" + str(current_password))
        try:

            ul = Club.objects.get(email=email, password=current_password)

            if ul is not None:
                ul.password = new_password  # change field
                ul.save()
                msg =  'Password Changed Successfully'
                all = {
                    'user': user,
                    'msg': msg
                }
                return render(request, 'auctions/change_password_club.html',all)
            else:
                context =  'Your Old Password is Wrong'
                all = {
                    'user': user,
                    'msg': context
                }
                return render(request, 'auctions/change_password_club.html',all)

        except Club.DoesNotExist:
            context =  'Your Old Password is Wrong'
            all = {
                'user': user,
                'msg': context
            }
            return render(request, 'auctions/change_password_club.html',all)
    else:
        return render(request, 'auctions/change_password_club.html',all)
def view_catagories(request):
    Forwards=Player.objects.filter(position='Forwards')
    Midfielders=Player.objects.filter(position='Midfielders')
    Defenders=Player.objects.filter(position='Defenders')
    Goalkeepers=Player.objects.filter(position='Goalkeepers')
    all={'a':Forwards,'b':Midfielders,'c':Defenders,'d':Goalkeepers}
    return render(request,'auctions/results.html',all)