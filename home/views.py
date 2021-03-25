from django.shortcuts import render,HttpResponse,redirect
from home.models import Task
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')
class RegisterPage(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('login')

    def form_valid(self,form):
        user = form.save()
        if user is not None:
            login(self.request,user)
        return super(RegisterPage,self).form_valid(form)

    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage,self).get(*args,**kwargs)

@login_required
def home(request):
    context = {'success':False}
    if request.method=="POST":
        user=request.user
        title = request.POST['title']
        desc = request.POST['desc']
        print(title,desc)
        ins = Task(user=user,task_title=title,task_description=desc)
        ins.save()
        context = {'success':True}
    return render(request, 'index.html',context)

@login_required
def tasks(request,id):
    id = int(id)
    print(id)
    alltasks = Task.objects.all().filter(user=id)
    #results = alltasks.filter(user=id)
    #print(request.user)
    #print(results)
    #a=get_context_data(request.user)
    tcontext = {'tasks':alltasks}
    return render(request, 'about.html', tcontext)

def delete(request,id):
    id = int(id)
    context={'successTask':False}
    task = Task.objects.get(id=id)
    task.delete()
    context={'successTask':True}
    return render(request, 'index.html', context)

def edit(request,id):
    id = int(id)
    context={'successEdit':False}
    if request.method=="POST":
        task = Task.objects.get(id=id)
        task.task_title = request.POST.get('task_title')
        task.task_description = request.POST.get('task_desc')
        task.save()
        print(task.task_description)
        # ins = Task(task_title=title,task_description=description)
        # ins.save()
        context={'successEdit':True}
        return render(request, 'index.html', context)
    else:
        task = Task.objects.get(id=id)
        return render(request, 'edit.html',{'task':task})

