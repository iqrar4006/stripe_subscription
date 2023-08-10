from django.shortcuts import render
from django.views import View
from .models import Customer,Purchased_plan,Cancelled_plan,Monthly_plan,Yearly_plan
from django.contrib import messages
from .forms import CustomerRegistrationForm,CustomerProfileForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from datetime import date,datetime,timedelta
import stripe

# Create your views here.
def home(request):
 return render(request, 'subscription/home.html')

class CustomerRegistrationView(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return render(request, 'subscription/customerregistration.html',{'form':form})
    def post(self,request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations!! Registered Successfully')
            form.save()
        return render(request, 'subscription/customerregistration.html',{'form':form})

@method_decorator(login_required,name='dispatch')
class ProfileView(View):
    def get(self,request):
        purchases=Purchased_plan.objects.filter(user=request.user).first()
        cancelled=Cancelled_plan.objects.filter(user=request.user).first()
        return render(request, 'subscription/profile.html',{'purchases':purchases,'cancelled':cancelled,'usr':request.user})

@login_required
def cancelplan(request):
    reg=Purchased_plan.objects.filter(user=request.user).first()
    if reg:
        canc=Cancelled_plan.objects.filter(user=request.user).first()
        if canc:
            canc.delete()
        canc=Cancelled_plan(user=request.user,plan_type=reg.plan_type,price=reg.price,allow_devices=reg.allow_devices,yr_mon=reg.yr_mon,cancelled_date=datetime.now())
        canc.save()
        reg.delete()
    return HttpResponseRedirect('/accounts/profile/')

@login_required
def showplan(request,saal,typ):
    if saal==0:
        cen=Monthly_plan.objects.all()
    elif saal==1:
        cen=Yearly_plan.objects.all()
    i=0
    ans=[['Monthly price'],['Video quality'],['Resolution'],['Allow device']]
    for el in cen:
        ans[i].append(el.price)
        i+=1
        ans[i].append(el.quality)
        i+=1
        ans[i].append(el.resolution)
        i+=1
        ans[i].append(el.allow_devices)
        i=0
    if typ==1:
        val={'mobile':1,'basic':0,'standard':0,'premium':0}
    elif typ==2:
        val={'mobile':0,'basic':1,'standard':0,'premium':0}
    elif typ==3:
        val={'mobile':0,'basic':0,'standard':1,'premium':0}
    else:
        val={'mobile':0,'basic':0,'standard':0,'premium':1}
    return render(request, 'subscription/showplan.html',{'saal':saal,'cen':ans,'typ':typ,'val':val})


@login_required
def subscribe(request,saal,typ):
    prc=[[0,100,200,500,700],[0,1000,2000,5000,7000]]
    tp=[0,'Mobile','Basic','Standard','Premium']
    allw_d={'Mobile':'Mob+Tab','Basic':'Mob+Tab+Comp+TV','Standard':'Mob+Tab+Comp+TV','Premium':'Mob+Tab+Comp+TV'}
    amount=prc[saal][typ]
    if request.method == "POST":
        stripe.api_key = 'sk_test_qu7ivgHp9WRHlHJjs2QHugIA00hKFbC5qc'

        customer = stripe.Customer.create(
             email = "iqrar4006@gmail.com",
			name=request.user,
            source=request.POST['stripeToken']
			)
            
        charge = stripe.Charge.create(
			customer=customer,
			amount=amount*100,
			currency='inr',
			description="Subscription",   
		)
        
        pln_typ=tp[typ]
        allow_dev=allw_d[pln_typ]
        cur_d=datetime.now()
        if saal==0:
            exp_d=cur_d+timedelta(30)
        else:
            exp_d=cur_d+timedelta(365)
        if amount>=1000:
            t='yr' 
        else:
            t='mon'

        canc=Purchased_plan.objects.filter(user=request.user).first()
        if canc:
            canc.delete()
        reg=Purchased_plan(user=request.user,plan_type=pln_typ,price=amount,allow_devices=allow_dev,yr_mon=t,start_date=cur_d,end_date=exp_d)
        reg.save()
        
        return HttpResponseRedirect('/accounts/profile/')
    if saal==0:
        context={'name':tp[typ],'cycle':'Monthly',"amount":amount}
    else:
        context={'name':tp[typ],'cycle':'Yearly',"amount":amount}
    return render(request, 'subscription/subscribe.html',{'saal':saal,'typ':typ,"context":context})

