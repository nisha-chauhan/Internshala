from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import Users



# Create your views here.

def default_page(request):
    return HttpResponse("<h1> Thanks For The Opportunity <h1>")

def hello(request):
    return render(request,'app/hello.html',{})



def users(request):
    user=Users.objects.all()
    return render(request,'app/users.html',{"user":user})


def add_user(request):
    if request.method=="POST":
        # print("data is Added")
        # data fetch
        user_name=request.POST.get("user_name")
        user_id=request.POST.get("user_id")
        user_phone=request.POST.get("user_phone")
        user_role=request.POST.get("user_role")
        
        # create model object and set the data/
        u=Users()
        u.name=user_name
        u.user_id=user_id
        u.phone=user_phone
        u.role=user_role
     
            
        # save the data
        u.save()
        return redirect("/app/users/")
    return render(request,'app/add_user.html',{})




# def delete_user(request,user_id):
#     print(user_id)
#     user=Users.objects.get(pk=user_id)
#     user.delete()
#     return redirect('app/users.html')


# def update_user(request,user_id):
#     user=Users.objects.get(pk=user_id)
#     return render(request,"app/update_emp.html",{'user':user})



# def do_update_user(request,user_id):
#     if request.method=="POST":
#         user_name=request.POST.get("user_name")
#         user_id=request.POST.get("user_id")
#         user_phone=request.POST.get("user_phone")
#         user_role=request.POST.get("user_role")
        
#         u=Users.objects.get(pk=user_id)

#         u.name=user_name    
#         u.user_id=user_id
#         u.phone=user_phone
#         u.role=user_role
     
#         # save the data
#         u.save()
        
#     return redirect("/app/users/")




def each_user_detail(request, user_id):
    print(user_id)
    user = get_object_or_404(Users, pk=user_id)
    return render(request, 'app/user_details.html', {'user': user})