from django.shortcuts import render
from users.forms import UserForm, UserProfileInfoForm

#
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

# If you ever want a view to require a user to be logged in
from django.contrib.auth.decorators import login_required


# Create views here
def index(request):
    return render(request, 'first_board/index.html')


@login_required()
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            # Defines OneToOne Relationship
            profile.user = user

            if 'profile_pic' in request.FILES:
                """
                    Will use other very similar tactics when using other types of files.
                    Images, csv, resume, etc.
                    
                    You will use the key based on what you define in the models:
                        request.FILES['your_key']
                """
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'users/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered}
                  )


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')
        else:
            print('Login Failed')
            print('Username: {} and password {}'.format(username, password))
            return HttpResponse('invalid login details supplied.')

    else:
        return render(request, 'users/login.html', {})
