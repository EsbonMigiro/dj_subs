from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm

from django.views.generic.edit import FormView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
# Create your views here.
from django.views import View
import json
from .models import person_collection
from django.http import HttpResponse

def user_login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            # print('email', request.POST)
            post_data = dict(request.POST)

            """
            print(username, password)
            print(post_data)
            
            request_info = {
                'method': request.method,
                'headers': dict(request.headers),
                'POST Data': post_data,
                'GET Data': dict(request.GET),
                'COOKIES': dict(request.COOKIES),
                'META': dict(request.META),
                'body': request.body.decode('utf-8') if request.body else None,
                'path': request.path,
                'full_path': request.get_full_path(),
                'content_type': request.content_type,
                # 'content_length': request.content_length,
                'scheme': request.scheme,
                'host': request.get_host(),
                'remote_addr': request.META.get('REMOTE_ADDR'),
                'user_agent': request.META.get('HTTP_USER_AGENT'),
                'protocol': request.META.get('SERVER_PROTOCOL'),
                'referer': request.META.get('HTTP_REFERER'),
                'encoding': request.encoding,
                'is_secure': request.is_secure(),
                # 'is_ajax': request.is_ajax() 
            }

            # json_data = json.dumps(dict(request_info), indent=4)
            print('json_data', request_info)
             """

            user = authenticate(request, username =username, password=password)
            if user is not None:
                login(request, user)
                return redirect("login")
            else:
                return render(request, 'login.html', {'form': form, 'error_message': 'Invalid user'})
            
        else:
            form = LoginForm()
            return render(request, 'login.html', {'form': form})    
        
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})          




class SignUpView(FormView):
    template_name = 'signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')  # Redirect to login page after successful signup
    
    def form_valid(self, form):
        # Create the user if the form is valid
        username = form.cleaned_data['username']
        first_name = form.cleaned_data['first_name']
        second_name = form.cleaned_data['second_name']
        password = form.cleaned_data['password']
        
        # Create the user (assuming User is from django.contrib.auth.models)
        User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=second_name,
            password=password
        )
        return super().form_valid(form)


def app_running(request):
    return HttpResponse("<h1>App is running ...</h1>")

def add_person(request):
    records = {
        "first_name": "Michael",
        "age": 25
    }
    person_collection.insert_one(records)
    return HttpResponse("<h4>this person added</h4>")

def get_all_persons(request):
    persons = person_collection.find()
    print('persons', persons[0]["first_name"])
    return HttpResponse(persons)


class SignUpView(FormView):
    template_name = 'signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')  # Redirect to login page after successful signup
    
    def form_valid(self, form):
        # Create the user if the form is valid
        username = form.cleaned_data['username']
        first_name = form.cleaned_data['first_name']
        second_name = form.cleaned_data['second_name']
        password = form.cleaned_data['password']
        
        # Create the user (assuming User is from django.contrib.auth.models)
        User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=second_name,
            password=password
        )
        return super().form_valid(form)



class DeleteUsernameView(View):

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        users_array =[user.username for user in users]
        return render(request, 'delete.html', {"users": users_array})
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        if username:
            try:
                user = User.objects.get(username=username)
                user.delete()
                return HttpResponse(f'user {username} successfully deleted')
            except Exception as e:
                return HttpResponse(f'user does not exist: {username}')
        else:
            return HttpResponse(f'No username')    
 
        
def landing_view(request):
    return render(request, 'landingpage.html')
