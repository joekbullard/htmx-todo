from django.http.response import HttpResponse, HttpResponsePermanentRedirect
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from todo.models import TodoList
from django.views.generic.list import ListView
from django.views.generic import FormView, TemplateView
from django.contrib.auth import get_user_model
from todo.forms import RegisterForm

# Create your views here.
class IndexView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    template_name = 'index.html'
    
class Login(LoginView):
    template_name = 'registration/login.html'

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()  # save the user
        return super().form_valid(form)

class TodoListView(ListView):
    template_name = 'lists.html'
    model = TodoList
    context_object_name = 'lists'

    def get_queryset(self):
        user = self.request.user
        return user.lists.all()

def check_username(request):
    username = request.POST.get('username')
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse("<div id='username-error' style='color: red;' class='error'>This username already exists</div>")
    else:
        return HttpResponse("<div id='username-error' style='color: green;' class='success'>This username is available</div>")

def add_list(request):
    name = request.POST.get('listname')

    # get or create film with name
    list = TodoList.objects.create(name=name)

    # add film to users list
    request.user.lists.add(list)

    # return template with all of the users films
    lists = request.user.lists.all()
    return render(request, 'partials/todo-list.html', {'lists': lists})

def delete_list(request, pk):
    # remove film from users list
    list = TodoList.objects.get(pk=pk)
    request.user.lists.remove(list)

    # return template file
    lists = request.user.lists.all()
    return render(request, 'partials/todo-list.html', {'lists': lists})