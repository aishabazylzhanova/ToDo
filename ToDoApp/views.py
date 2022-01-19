
from django.shortcuts import redirect
from django.http import HttpResponse, HttpRequest

from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from ToDoApp.models import Tasks
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class TasksView(ListView):
    model = Tasks
    template_name = 'ToDoApp/tasks_list.html'
    context_object_name = 'tasks'

class Login(LoginView):
    template_name = 'ToDoApp/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')


class Register(FormView):
    template_name = 'ToDoApp/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Register, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(Register, self).get(*args, **kwargs)



def create(request: HttpRequest):
    todo = Tasks(content=request.POST['content'],user_id = request.user.id)
    todo.save()
    return redirect('/')
def delete(request, task_id):
    delete = Tasks.objects.get(id=task_id)
    delete.delete()
    return redirect('/')