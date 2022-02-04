from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse

from mainApp.models import *
from .forms import *
import datetime
import json
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError


def index(request):

    flyerList = Flyer.objects.filter(Event_date__gte = datetime.date.today()
                                    ).filter(Event_date__lte = datetime.date.today()+ datetime.timedelta(days=6))
    
    return render(request, 'mainApp/index.html', {'flyerList':flyerList})

def index2(request):
    
    flyerList = Flyer.objects.filter(Event_date__gte = datetime.date.today()
                                    ).filter(Event_date__lte = datetime.date.today()+ datetime.timedelta(days=6))
    
    return render(request, 'mainApp/index2.html', {'flyerList':flyerList})

# class FlyerCreateView(CreateView):
#     model = Flyer
#     form_class = FlyerForm



def watchList(request):

    if request.method == "GET":

        flyer_ids = []
        reminders = Reminder.objects.filter(User_email = request.GET.get('useremail', ''))

        for flyer in reminders:
            flyer_ids.append(flyer.Flyer.pk)

        return JsonResponse({"flyers": flyer_ids}, status=200)

    if request.method == "POST":

        postData = json.loads(request.body)
        email, id, func  = postData["email"], postData["id"], postData["func"]
        flyer = get_object_or_404(Flyer, pk = id)

        if postData["func"] == 'add':

            new_watched_flyer = Reminder(User_email = postData["email"], Flyer = flyer)
            new_watched_flyer.save()
            return HttpResponse('200')
        
        elif postData["func"] == 'del':

            watched_flyer = Reminder.objects.filter(User_email=email).filter(Flyer=flyer)
            watched_flyer.delete()
            return HttpResponse('200')
        
        else:
            return HttpResponse('ERROR')



def uploadImage(request):
    return render(request, 'mainApp/uploadImage.html')


def saveImage(request):
    
    # print (request.POST['imageInput'])
    form = Flyer_ImageForm(request.POST, request.FILES)
    # clearMessages(request)
    print(form.errors)
    if form.is_valid():
        print("okkkkkkkkk")
        newImg = form.save()
        print(newImg.pk)

        return redirect('newFlyerFormMobile', imgPk = newImg.pk)
    return HttpResponse(str(form.errors()))



def newFlyerFormMobile(request, imgPk):
    return render(request, 'mainApp/newFlyerFormMobile.html',{'imgPk':imgPk})

def saveFlyerMobile(request):

    form = FlyerForm(request.POST)
    if form.is_valid():
        print("okkkkkkkkk")
        form.save()
        return redirect('index')
    messages.add_message(request, messages.ERROR, 'There was an error, please try again.')
    return redirect('uploadImage')

def saveFlyerDesktop(request):
    # clearMessages()
    print(00)
    print(request.POST)
    imageForm = Flyer_ImageForm(request.POST, request.FILES)
    for field in imageForm:
        print(field)
        for error in field.errors:
             print(error)
    if imageForm.is_valid():
        newImg = imageForm.save()
        print(1)

        p = request.POST.dict()
        newFlyer = Flyer(Flyer_image=newImg, Boro=p["Boro"], Event_date=p['Event_date'], Event_type=p['Event_type'],
                            Contact_information=p['Contact_information'], Address=p['Address'])
        print(p)
        #REMEMBER TO CLEAM DATA!!!!!
        try:
            newFlyer.full_clean()
            print(2)
            newFlyer.save()
            return redirect('index')
        # except Exception as e:
        #     print (e)
        except:
        # except ValidationError as e:
        #     print(e.message_dict)
            messages.add_message(request, messages.ERROR, 'There was an error, please try again.')
            return redirect('uploadImage')
    messages.add_message(request, messages.ERROR, 'There was an error, please try again.')
    return redirect('uploadImage')

def test(request):
    form = FlyerForm()
    return render(request, 'mainApp/test.html',{'form':form})

# def clearMessages(request):
#     storage = messages.get_messages(request)
#     for _ in storage:
#         # This is important
#         # Without this loop `_loaded_messages` is empty
#         pass
#     for _ in list(storage._loaded_messages):
#         del storage._loaded_messages[0]