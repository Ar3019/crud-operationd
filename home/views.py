from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Details
from .forms import DetailsForm

#Create your views here.

def details_list(request):
    if request.user.is_authenticated:
        print(request.user)
        print("Is authenticated:", request.user.is_authenticated)
        print("User is authenticated:", request.user)
        user = request.user
        if user.is_superuser:
            context = {'records_list': Details.objects.all()}
            return render(request,"home/records_list.html", context )

        else:
            user_details = Details.objects.get(email=request.user)
            print(user_details)
            return render(request, "home/details_list.html", {'user_details':user_details})
    else:
        return HttpResponseForbidden("User details not found")





def details_form(request, id=0):
        if request.method == "GET":
            if id == 0:
                form = DetailsForm()
                return render(request, "home/details_form.html", {'form': form})
            else:
                user_details = Details.objects.get(pk=id)
                form = DetailsForm(instance = user_details)

                return render(request, "home/details_update.html", {'form': form})
        else:
            print(request.POST)
            email = request.POST.get("email")
            password = request.POST.get("password")
            confirm_password = request.POST.get("confirm_password")
            if id == 0 :
                form = DetailsForm(request.POST)
                if password != confirm_password:
                    messages.add_message(request, messages.INFO, 'Password missmatch!')
                    return redirect('/details')


                    print(form.is_valid())
                else:
                    if form.is_valid():
                        form.save()
                        user = User.objects.create_user(username=email, password=password)
                        user.is_staff = True
                        user.save()
                    messages.success(request, "Registered Successfully ! Login to continue")
                # print(password)
                    # login(request, user)
                    return redirect('/details/login')
            else:
                user_details = Details.objects.get(pk=id)
                form = DetailsForm(request.POST, instance =user_details)
                
                if form.is_valid():
                        form.save()
                        return render(request, "home/details_update.html", {'form': form})
                        
                return redirect('/details/list')
                


def loginView(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            # user = Details.objects.get(email= email,password =  password)
            # user = User.objects.get(username=email, password=password)
            user = authenticate(request, username= email, password= password)
            print(user)
            login(request, user)

            # if user is not None:
            print("User is authenticated:", request.user)  # Debugging
            # login(request, user)
            return redirect('/details/list')

        except Details.DoesNotExist:
            messages.error(request, "invalid email or password")
            return render(request, "home/login.html", {})


    return render(request, "home/login.html")  

def details_delete(request, id):
    print("Deleting user details with ID:", id)
    
    user = request.user
    if user.is_superuser:
        user_details = Details.objects.get(pk=id)
        user_details.delete()
        return redirect('/details/list')
    else:
        user_details = Details.objects.get(pk=id)
        user_details.delete()
        return redirect('/details')