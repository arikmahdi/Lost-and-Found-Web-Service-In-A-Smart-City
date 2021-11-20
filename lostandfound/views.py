from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import LostPet
from .models import FoundPet
from .models import LostObject 
from .models import FoundObject
from .models import LostPerson 
from .models import FoundPerson   
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone


def home(request):
    return render(request, 'lostandfound/home.html')

@login_required
def home2(request):
    return render(request, 'lostandfound/home2.html')


def about(request):
    return render(request, 'lostandfound/about.html') 

def team(request):
    return render(request, 'lostandfound/team.html') 

def signin(request):
    if(request.method == 'GET'):
        return render(request, 'lostandfound/signin.html')

    elif(request.method == 'POST'):
        u = request.POST.get('user', '') 
        p = request.POST.get('pass', '')
        user = authenticate(username=u, password=p)
        
        if user is None:
            messages.error(request, 'Invalid username or password')
            return render(request, 'lostandfound/signin.html')

        else:
            login(request, user)
            return redirect('home-page-2')    

def signup(request):

    if(request.method == 'GET'):
        return render(request, 'lostandfound/signup.html')

    elif(request.method == 'POST'):
    
        f = request.POST.get('first', '')
        l = request.POST.get('last', '')
        e = request.POST.get('email', '')
        u = request.POST.get('user', '') 
        p = request.POST.get('pass', '')
        u1 = User(username=u,password=p,email=e,first_name=f,last_name=l)
        u1.save() 
        return redirect('signin-page')


def signout(request):
    logout(request)
    return redirect('signin-page')

@login_required
def profile(request):
    return render(request, 'lostandfound/profile.html')  


@login_required
def report_lost_person(request):

    if(request.method == 'GET'):
        return render(request, 'lostandfound/report_lost_person.html')

    elif(request.method == 'POST'):
        b1 = request.user
        b2 = request.POST.get('per_name_lost', '')
        b3 = request.POST.get('per_gender_lost', '')
        b4 = request.POST.get('per_age_lost', '')
        b5 = request.POST.get('per_date_lost', '')
        b6 = request.POST.get('per_location_lost', '')
        b7 = request.POST.get('per_description_lost', '')
        b8 = request.FILES['per_picture_lost']
        b10 = request.POST.get('per_reward_lost', '')
        b9 = request.POST.get('per_number_lost', '')
        lper = LostPerson(uploader=b1,per_name_lost=b2,per_gender_lost=b3,per_age_lost=b4,per_date_lost=b5,per_location_lost=b6,per_description_lost=b7,per_picture_lost=b8,per_reward_lost=b10,per_number_lost=b9)
        lper.save() 
        return redirect('home-page-2')


@login_required
def report_found_person(request):

    if(request.method == 'GET'):
        return render(request, 'lostandfound/report_found_person.html')

    elif(request.method == 'POST'):
        c1 = request.user
        c2 = request.POST.get('per_name_found', '')
        c3 = request.POST.get('per_gender_found', '')
        c4 = request.POST.get('per_age_found', '')
        c5 = request.POST.get('per_date_found', '')
        c6 = request.POST.get('per_location_found', '')
        c7 = request.POST.get('per_description_found', '')
        c8 = request.FILES['per_picture_found']
        c9 = request.POST.get('per_number_found', '') 
        fper = FoundPerson(uploader=c1,per_name_found=c2,per_gender_found=c3,per_age_found=c4,per_date_found=c5,per_location_found=c6,per_description_found=c7,per_picture_found=c8,per_number_found=c9)
        fper.save() 
        return redirect('home-page-2')   

@login_required
def report_found_object(request):

    if(request.method == 'GET'):
        return render(request, 'lostandfound/report_found_object.html') 

    elif(request.method == 'POST'):
        a1 = request.user
        a2 = request.POST.get('obj_item_found', '')
        a3 = request.POST.get('obj_date_found', '')
        a4 = request.POST.get('obj_location_found', '')
        a5 = request.POST.get('obj_description_found', '')
        a6 = request.POST.get('obj_number_found', '')
        a7 = request.FILES['obj_picture_found']

        fo1 = FoundObject(uploader=a1,obj_item_found=a2, obj_date_found=a3,obj_location_found=a4,obj_description_found=a5,obj_number_found=a6,obj_picture_found=a7)
        fo1.save() 
        return redirect('home-page-2')          

@login_required
def report_lost_object(request):

    if(request.method == 'GET'):
        return render(request, 'lostandfound/report_lost_object.html')

    elif(request.method == 'POST'):
        z1 = request.user
        z2 = request.POST.get('obj_item_lost', '')
        z3 = request.POST.get('obj_date_lost', '')
        z4 = request.POST.get('obj_location_lost', '')
        z5 = request.POST.get('obj_description_lost', '')
        z6 = request.POST.get('obj_reward_lost', '')
        z7 = request.POST.get('obj_number_lost', '')
        z8 = request.FILES['obj_picture_lost']

        lo1 = LostObject(uploader=z1,obj_item_lost=z2, obj_date_lost=z3,obj_location_lost=z4,obj_description_lost=z5,obj_reward_lost=z6,obj_number_lost=z7,obj_picture_lost=z8)
        lo1.save() 
        return redirect('home-page-2')


@login_required
def report_lost_pet(request):

    if(request.method == 'GET'):
        return render(request, 'lostandfound/report_lost_pet.html')


    elif(request.method == 'POST'):
    
        x1 = request.user
        x2 = request.POST.get('animal_lost', '')
        x3 = request.FILES['picture_lost']
        x5 = request.POST.get('date_lost', '')
        x6 = request.POST.get('location_lost', '')
        x7 = request.POST.get('description_lost', '')
        x8 = request.POST.get('reward_pet_lost', '')
        x9 = request.POST.get('number_lost', '') 

        lp1 = LostPet(uploader=x1,animal_lost=x2,picture_lost=x3,date_lost=x5,location_lost=x6,description_lost=x7,reward_pet_lost=x8,number_lost=x9)
        lp1.save() 
        return redirect('home-page-2')   


@login_required
def report_found_pet(request):

    if(request.method == 'GET'):
        return render(request, 'lostandfound/report_found_pet.html')

    elif(request.method == 'POST'):
        y1 = request.user
        y2 = request.POST.get('animal_found', '')
        y3 = request.FILES['picture_found']
        y5 = request.POST.get('date_found', '')
        y6 = request.POST.get('location_found', '')
        y7 = request.POST.get('description_found', '')
        y8 = request.POST.get('number_found', '') 

        fp1 = FoundPet(uploader=y1,animal_found=y2,picture_found=y3,date_found=y5,location_found=y6,description_found=y7,number_found=y8)
        fp1.save() 
        return redirect('home-page-2')     




@login_required
def view_lost_person(request):
        context ={

            'reports' : LostPerson.objects.all()
            }
        return render(request, 'lostandfound/view_lost_person.html',context) 

@login_required
def view_lost_object(request):
        context ={

            'reports' : LostObject.objects.all()
            }
        return render(request, 'lostandfound/view_lost_object.html',context) 

@login_required
def view_found_person(request):
        context ={

            'reports' : FoundPerson.objects.all()
            }
        return render(request, 'lostandfound/view_found_person.html',context) 


@login_required
def view_found_object(request):
        context ={

            'reports' : FoundObject.objects.all()
            }
        return render(request, 'lostandfound/view_found_object.html',context) 


@login_required
def view_lost_pet(request):
        context ={

            'reports' : LostPet.objects.all()
            }
        return render(request, 'lostandfound/view_lost_pet.html',context) 


@login_required
def view_found_pet(request):
        context ={

            'reports' : FoundPet.objects.all()
            }
        return render(request, 'lostandfound/view_found_pet.html',context)                     

@login_required
def my_lost_object(request):
        context ={

            'reports' : LostObject.objects.all()
            }
        return render(request, 'lostandfound/my_lost_object.html',context) 


@login_required
def my_lost_person(request):
        context ={

            'reports' : LostPerson.objects.all()
            }
        return render(request, 'lostandfound/my_lost_person.html',context)         

@login_required
def my_lost_pet(request):
        context ={

            'reports' : LostPet.objects.all()
            }
        return render(request, 'lostandfound/my_lost_pet.html',context) 

@login_required
def my_found_person(request):
        context ={

            'reports' : FoundPerson.objects.all()
            }
        return render(request, 'lostandfound/my_found_person.html',context) 

@login_required
def my_found_object(request):
        context ={

            'reports' : FoundObject.objects.all()
            }
        return render(request, 'lostandfound/my_found_object.html',context) 


@login_required
def my_found_pet(request):
        context ={

            'reports' : FoundPet.objects.all()
            }
        return render(request, 'lostandfound/my_found_pet.html',context) 



@login_required
def delete_lost_pet(request, id):
     s1 = LostPet.objects.get(id=id)

     if(request.user != s1.uploader):
        return redirect('home-page')


     if(request.method == 'GET'):
        return render(request, 'lostandfound/delete_lost_pet.html', {'old_post' : s1})

     elif(request.method == 'POST'):
        s1.delete()
        return redirect('my-lost-pet-page')

@login_required
def delete_lost_person(request, id):
     s1 = LostPerson.objects.get(id=id)

     if(request.user != s1.uploader):
        return redirect('home-page')


     if(request.method == 'GET'):
        return render(request, 'lostandfound/delete_lost_person.html', {'old_post' : s1})

     elif(request.method == 'POST'):
        s1.delete()
        return redirect('my-lost-person-page')

@login_required
def delete_lost_object(request, id):
     s1 = LostObject.objects.get(id=id)

     if(request.user != s1.uploader):
        return redirect('home-page')


     if(request.method == 'GET'):
        return render(request, 'lostandfound/delete_lost_object.html', {'old_post' : s1})

     elif(request.method == 'POST'):
        s1.delete()
        return redirect('my-lost-object-page')

@login_required
def delete_found_pet(request, id):
     s1 = FoundPet.objects.get(id=id)

     if(request.user != s1.uploader):
        return redirect('home-page')


     if(request.method == 'GET'):
        return render(request, 'lostandfound/delete_found_pet.html', {'old_post' : s1})

     elif(request.method == 'POST'):
        s1.delete()
        return redirect('my-found-pet-page')

@login_required
def delete_found_person(request, id):
     s1 = FoundPerson.objects.get(id=id)

     if(request.user != s1.uploader):
        return redirect('home-page')


     if(request.method == 'GET'):
        return render(request, 'lostandfound/delete_found_person.html', {'old_post' : s1})

     elif(request.method == 'POST'):
        s1.delete()
        return redirect('my-found-person-page')

@login_required
def delete_found_object(request, id):
     s1 = FoundObject.objects.get(id=id)

     if(request.user != s1.uploader):
        return redirect('home-page')


     if(request.method == 'GET'):
        return render(request, 'lostandfound/delete_found_object.html', {'old_post' : s1})

     elif(request.method == 'POST'):
        s1.delete()
        return redirect('my-found-object-page')

@login_required
def edit_lost_pet(request, id):
    s1 = LostPet.objects.get(id=id)

    if(request.user != s1.uploader):
        return redirect('home-page')

    if(request.method == 'GET'):
        return render(request, 'lostandfound/edit_lost_pet.html', {'old_post' : s1})

    elif(request.method == 'POST'):

        s1.animal_lost = request.POST.get('animal_lost', '')
        s1.date_lost = request.POST.get('date_lost', '')
        s1.location_lost = request.POST.get('location_lost', '')
        s1.reward_pet_lost = request.POST.get('reward_pet_lost', '')
        s1.description_lost = request.POST.get('description_lost', '')
        s1.number_lost = request.POST.get('number_lost', '')
        s1.save()
        return redirect('my-lost-pet-page')


@login_required
def edit_found_pet(request, id):
    s1 = FoundPet.objects.get(id=id)

    if(request.user != s1.uploader):
        return redirect('home-page')

    if(request.method == 'GET'):
        return render(request, 'lostandfound/edit_found_pet.html', {'old_post' : s1})

    elif(request.method == 'POST'):

        s1.animal_found = request.POST.get('animal_found', '')
        s1.date_found = request.POST.get('date_found', '')
        s1.location_found = request.POST.get('location_found', '')
        s1.description_found = request.POST.get('description_found', '')
        s1.number_found = request.POST.get('number_found', '')
        s1.save()
        return redirect('my-found-pet-page')


@login_required
def edit_lost_object(request, id):
    s1 = LostObject.objects.get(id=id)

    if(request.user != s1.uploader):
        return redirect('home-page')

    if(request.method == 'GET'):
        return render(request, 'lostandfound/edit_lost_object.html', {'old_post' : s1})

    elif(request.method == 'POST'):

        s1.obj_item_lost = request.POST.get('obj_item_lost', '')
        s1.obj_date_lost = request.POST.get('obj_date_lost', '')
        s1.obj_location_lost = request.POST.get('obj_location_lost', '')
        s1.obj_description_lost = request.POST.get('obj_description_lost', '')
        s1.obj_number_lost = request.POST.get('obj_number_lost', '')
        s1.obj_reward_lost = request.POST.get('obj_reward_lost', '')
        s1.save()
        return redirect('my-lost-object-page') 


@login_required
def edit_found_object(request, id):
    s1 = FoundObject.objects.get(id=id)

    if(request.user != s1.uploader):
        return redirect('home-page')

    if(request.method == 'GET'):
        return render(request, 'lostandfound/edit_found_object.html', {'old_post' : s1})

    elif(request.method == 'POST'):

        s1.obj_item_found = request.POST.get('obj_item_found', '')
        s1.obj_date_found = request.POST.get('obj_date_found', '')
        s1.obj_location_found = request.POST.get('obj_location_found', '')
        s1.obj_description_found = request.POST.get('obj_description_found', '')
        s1.obj_number_found = request.POST.get('obj_number_found', '')
        s1.save()
        return redirect('my-found-object-page')


@login_required
def edit_lost_person(request, id):
    s1 = LostPerson.objects.get(id=id)

    if(request.user != s1.uploader):
        return redirect('home-page')

    if(request.method == 'GET'):
        return render(request, 'lostandfound/edit_lost_person.html', {'old_post' : s1})

    elif(request.method == 'POST'):

        s1.per_name_lost = request.POST.get('per_name_lost', '')
        s1.per_date_lost = request.POST.get('per_date_lost', '')
        s1.per_location_lost = request.POST.get('per_location_lost', '')
        s1.per_gender_lost = request.POST.get('per_gender_lost', '') 
        s1.per_number_lost = request.POST.get('per_number_lost', '')
        s1.per_reward_lost = request.POST.get('per_reward_lost', '') 
        s1.per_description_lost = request.POST.get('per_description_lost', '') 
        s1.per_age_lost = request.POST.get('per_age_lost', '')
        s1.save()
        return redirect('my-lost-person-page')         


@login_required
def edit_found_person(request, id):
    s1 = FoundPerson.objects.get(id=id)

    if(request.user != s1.uploader):
        return redirect('home-page')

    if(request.method == 'GET'):
        return render(request, 'lostandfound/edit_found_person.html', {'old_post' : s1})

    elif(request.method == 'POST'):

        s1.per_name_found = request.POST.get('per_name_found', '')
        s1.per_date_found = request.POST.get('per_date_found', '')
        s1.per_location_found = request.POST.get('per_location_found', '')
        s1.per_gender_found = request.POST.get('per_gender_found', '') 
        s1.per_number_found = request.POST.get('per_number_found', '')
        s1.per_description_found = request.POST.get('per_description_found', '') 
        s1.per_age_found = request.POST.get('per_age_found', '')
        s1.save()
        return redirect('my-found-person-page')          



@login_required
def search_lost_pet(request):
        

            if 'search_pet_name' in request.GET:
              
                search_pet_name = request.GET['search_pet_name']
                search_pet_location = request.GET['search_pet_location']
                context ={

                            'reports' : LostPet.objects.filter(animal_lost__contains=search_pet_name,location_lost__contains=search_pet_location)
                          }
                return render(request, 'lostandfound/search_lost_pet.html',context)

            else:
                context ={

                  'reports' : LostPet.objects.all()
                        }
                return render(request, 'lostandfound/search_lost_pet.html',context) 

                 
@login_required
def search_found_pet(request):
        

            if 'search_pet_name' in request.GET:
              
                search_pet_name = request.GET['search_pet_name']
                search_pet_location = request.GET['search_pet_location']
                context ={

                            'reports' : FoundPet.objects.filter(animal_found__contains=search_pet_name,location_found__contains=search_pet_location)
                          }
                return render(request, 'lostandfound/search_found_pet.html',context)

            else:
                context ={

                  'reports' : FoundPet.objects.all()
                        }
                return render(request, 'lostandfound/search_found_pet.html',context) 
     
 
@login_required
def search_lost_object(request):
        

            if 'search_item_name' in request.GET:
              
                search_item_name = request.GET['search_item_name']
                search_item_location = request.GET['search_item_location']
                context ={

                            'reports' : LostObject.objects.filter(obj_item_lost__contains=search_item_name,obj_location_lost__contains=search_item_location)
                          }
                return render(request, 'lostandfound/search_lost_object.html',context)

          
            else:
                context ={

                  'reports' : LostObject.objects.all()
                        }
                return render(request, 'lostandfound/search_lost_object.html',context) 



@login_required
def search_found_object(request):
        

            if 'search_item_name' in request.GET:
              
                search_item_name = request.GET['search_item_name']
                search_item_location = request.GET['search_item_location']
                context ={

                            'reports' : FoundObject.objects.filter(obj_item_found__contains=search_item_name,obj_location_found__contains=search_item_location)
                          }
                return render(request, 'lostandfound/search_found_object.html',context)

          
            else:
                context ={

                  'reports' : FoundObject.objects.all()
                        }
                return render(request, 'lostandfound/search_found_object.html',context) 




@login_required
def search_lost_person(request):
        

            if 'search_person_name' in request.GET:

                search_per_gender = request.GET['search_per_gender']            
                search_person_name = request.GET['search_person_name']
                search_person_location = request.GET['search_person_location']
                age_min = request.GET['age_min']
                age_max = request.GET['age_max']
        
                    
                

                
                context ={

                            'reports' : LostPerson.objects.filter(per_name_lost__contains=search_person_name,per_location_lost__contains=search_person_location,per_gender_lost__exact=search_per_gender,per_age_lost__lte=age_max,per_age_lost__gte=age_min)
                          }
                return render(request, 'lostandfound/search_lost_person.html',context)

          
            else:
                context ={

                  'reports' : LostPerson.objects.all()
                        }
                return render(request, 'lostandfound/search_lost_person.html',context)


@login_required
def search_found_person(request):

        

            if 'search_person_name' in request.GET:

                search_per_gender = request.GET['search_per_gender'] 
                search_person_name = request.GET['search_person_name']
                search_person_location = request.GET['search_person_location']
                age_min = request.GET['age_min']
                age_max = request.GET['age_max']
          
               
                
                context ={

                            'reports' : FoundPerson.objects.filter(per_name_found__contains=search_person_name,per_location_found__contains=search_person_location,per_gender_found__exact=search_per_gender,per_age_found__lte=age_max,per_age_found__gte=age_min)
                          }
                return render(request, 'lostandfound/search_found_person.html',context)

          
            else:
                context ={

                  'reports' : FoundPerson.objects.all()
                        }
                return render(request, 'lostandfound/search_found_person.html',context) 
