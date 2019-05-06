from django.shortcuts import render
from django.http import HttpResponse
from .models import Person, LoginCredential

# Create your views here.


def index(request):
    data_dict = {}
    data_dict['name'] = 'Danial'
    data_dict['render_name'] = False
    data_dict['names'] = ['Forrest', 'Kevin', 'Andy', 'Jerry', 'Vincent']
    outer_list = []
    outer_list.append(['Danial', '24', 'Senior', '90', '80', '70'])
    outer_list.append(['Tom', '21', 'Junior', '90', '45', '70'])
    outer_list.append(['John', '26', 'Senior', '80', '75', '87'])
    data_dict['outer_list'] = outer_list
    return render(request, 'firstApp/index.html', data_dict)
    # return HttpResponse('Here is my Response')


def about(request):
    return render(request, 'firstApp/about.html')


def contact(request):
    return render(request, 'firstApp/contact.html')


def cool_websites(request):
    data_dict = {}
    data_dict['data_passed'] = 'Data Passed'
    websites = []
    websites.append(['Google', 'https://www.google.com'])
    websites.append(['Amazon', 'https://www.amazon.com'])
    websites.append(['Microsoft', 'https://www.microsoft.com'])
    data_dict['websites'] = websites
    return render(request, 'firstApp/coolWebsites.html', data_dict)


def name_form(request):
    persons = Person.objects.all()
    data_dict = {}
    data_dict['persons'] = persons
    return render(request, 'firstApp/form.html', data_dict)


def greet(request):
    first_name = request.POST.get('fName')
    last_name = request.POST.get('lName')
    data_dict = {}
    data_dict['firstname'] = first_name
    data_dict['lastname'] = last_name
    return render(request, 'firstApp/greet.html', data_dict)


def login(request):
    return render(request, 'firstApp/login.html')


def loginPage(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    logged_in = False
    if username == 'admin' and password == 'admin':
        logged_in = True
    data_dict = {}
    data_dict['loggedIn'] = logged_in
    return render(request, 'firstApp/loginPage.html', data_dict)


def signUpPage(request):
    data_dict = {}
    return render(request, 'firstApp/signUpForm.html', data_dict)


def signUpResult(request):
    message = ''
    username = request.POST.get('uName')
    firstname = request.POST.get('fName')
    lastname = request.POST.get('lName')
    password = request.POST.get('pWord')
    password2 = request.POST.get('pWord2')
    if password != password2:
        message = "Your passwords did not match!"
    elif firstname == None or lastname == None:
        message = 'Firstname or Lastname cannot be empty'
    # implement other elifs
    else:
        q = LoginCredential(firstName=firstname, lastName=lastname,
                            userName=username, passWord=password)
        q.save()
        message = 'Signed Up Successfully!'
    data_dict = {}
    data_dict['message'] = message
    return render(request, 'firstApp/signUpResult.html', data_dict)
