from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm,UserUpdateForm,ProfileUpdateForm
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account has been created for {username}. Continue to Login')
            return redirect('user-login')
    else:
        form = CreateUserForm()
    context = {
        'form': form
    }
    return render(request, 'user/register.html', context)

# def login_view(request):
#     if request.method == "POST":
#         username  = request.POST.get("username")
#         password = request.POST.get("password")
#         user = authenticate(request, username= username,password=password)
#         if user is None:
#             contextlog = {"error":"Invalid username or password"}
#             return render(request,'user/login.html',contextlog)
#         login(request, user)
#         return redirect("inventory-index")
#     return render(request,"user/login.html")

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect("user-login")
    return render(request,'user/logout.html')

def profile(request):
    return render(request,'user/profile.html')

def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('user-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'user/profile_update.html', context)