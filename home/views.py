from pickletools import read_uint1
from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests
from . import phaseNo
from home.models import Feedback

# Create your views here.
def enter(request):
    if request.method == 'POST':
        numOfPersons = request.POST['persons']
        if(numOfPersons=='1'):
             return redirect('index')
        if numOfPersons=='2':
            return redirect('index2')
    return render(request,'enter.html')

def upcoming(request):
    return render(request,'upcoming.html')
def feedback(request):
    context = {
            'submit' : False
        }
    if request.method=='POST':
        name = request.POST['name']
        feedback = request.POST['feedback']
        person = Feedback(name= name, feedback = feedback)
        person.save()
        return render(request,'feedback.html',{'submit' : True})
    return render(request,'feedback.html',{'submit':False})
    
def index2(request):
    context = {
        'source' : '',
        'source2' : ''
        }
    if(request.method=="POST"):
        day1 = request.POST['day']
        month1 = request.POST['month']
        year1 = request.POST['year']
        day2 = request.POST['day2']
        month2 = request.POST['month2']
        year2 = request.POST['year2']
        timestampreq1 = requests.get("https://showcase.api.linx.twenty57.net/UnixTime/tounix?date="+year1+"/"+month1+"/"+day1+" 17:00:00")
        timestampreq2 = requests.get("https://showcase.api.linx.twenty57.net/UnixTime/tounix?date="+year2+"/"+month2+"/"+day2+" 17:00:00")
        unxtimestamp1 = timestampreq1.json()
        unxtimestamp2 = timestampreq2.json()
        print(unxtimestamp1)
        print(unxtimestamp2)
        req1 = requests.get("https://api.farmsense.net/v1/moonphases/?d="+unxtimestamp1)
        req2 = requests.get("https://api.farmsense.net/v1/moonphases/?d="+unxtimestamp2)
        phase = req1.json()[0]["Phase"]
        phase2 = req2.json()[0]["Phase"]
        illumination1 = req1.json()[0]['Illumination'] * 100
        illumination2 = req2.json()[0]['Illumination'] * 100
        moon_name1 = req1.json()[0]['Moon']
        moon_name2 = req2.json()[0]['Moon']
        print(phase, illumination1,day1,month1,year1)
        print(phase2, illumination2,day2,month2,year2)
        print(year1, month1)
        print(year2, month2)
        num_of_days1 = phaseNo.numberOfDays(y = year1,m = month1)
        num_of_days2 = phaseNo.numberOfDays(y = year2,m = month2)
        phase_no1 = phaseNo.getPhaseno(phase= phase, illumination = illumination1,num_of_days =num_of_days1)
        phase_no2 = phaseNo.getPhaseno(phase= phase2, illumination = illumination2,num_of_days =num_of_days2)
        print(num_of_days1, phase_no1)
        print(num_of_days2, phase_no2)
        context['source'] =  "static/home/l-phase-"+str(phase_no1)+".png"
        context['source2'] =  "static/home/l-phase-"+str(phase_no2)+".png"
        context['phaseNo1'] = phase_no1
        context['phaseNo2'] = phase_no2
        context['day1'] = day1
        context['month1'] = month1
        context['year1'] = year1
        context['illumination1'] = illumination1
        context['moon_name1'] = moon_name1
        context['age1'] =  req1.json()[0]['Age']
        context['distance1'] =  req1.json()[0]['Distance']
        context['distanceToSun1'] =  req1.json()[0]['DistanceToSun']
        context['phase'] = phase
        context['phase2'] = phase2
        context['day2'] = day2
        context['month2'] = month2
        context['year2'] = year2
        context['illumination2'] = illumination2
        context['moon_name2'] = moon_name2
        context['age2'] =  req2.json()[0]['Age']
        context['distance2'] =  req2.json()[0]['Distance']
        context['distanceToSun2'] =  req2.json()[0]['DistanceToSun']
        context['afterSubmitDay1'] = int(day1)
        context['afterSubmitMonth1'] = int(month1)
        context['afterSubmitYear1'] = int(year1)
        context['afterSubmitDay2'] = int(day2)
        context['afterSubmitMonth2'] = int(month2)
        context['afterSubmitYear2'] = int(year2)
        
        return render(request,'index2.html', context)
    return render(request,'index2.html',context)


def index(request):
    context = {
        'source' : ''
        }
    if(request.method=="POST"):
        day = request.POST['day']
        month = request.POST['month']
        year = request.POST['year']
        timestampreq = requests.get("https://showcase.api.linx.twenty57.net/UnixTime/tounix?date="+year+"/"+month+"/"+day+" 17:00:00")
        unxtimestamp = timestampreq.json()
        print(unxtimestamp)
        req = requests.get("https://api.farmsense.net/v1/moonphases/?d="+unxtimestamp)
        phase = req.json()[0]["Phase"]
        illumination = req.json()[0]['Illumination'] * 100
        moon_name = req.json()[0]['Moon']
        print(phase, illumination,day,month,year)
        print(year, month)
        num_of_days = phaseNo.numberOfDays(y = year,m = month)
        phase_no = phaseNo.getPhaseno(phase= phase, illumination = illumination,num_of_days =num_of_days)
        print(num_of_days, phase_no)
        context['source'] = "static/home/l-phase-"+str(phase_no)+".png"
        context['phaseNo'] = phase_no
        context['phase'] = phase
        context['day'] = day
        context['month'] = month
        context['year'] = year
        context['illumination'] = illumination
        context['moon_name'] = moon_name
        context['age'] =  req.json()[0]['Age']
        context['distance'] =  req.json()[0]['Distance']
        context['distanceToSun'] =  req.json()[0]['DistanceToSun']
        context['afterSubmitDay'] = int(day)
        context['afterSubmitMonth'] = int(month)
        context['afterSubmitYear'] = int(year)
        print(context)
        return render(request,'index.html', context)
    return render(request,'index.html',context)


