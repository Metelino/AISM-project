from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
#from django.contrib import auth
from .forms import UserCreateForm, LearningTypeForm, QuestionnairyForm
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
#from .models import UserInCourse
from courses.models import Course, LessonFile

class SignUp(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('accounts:login')
    template_name='accounts/signup.html'

def user_profile(request):
    courses = None
    if request.user.is_staff:
        courses = request.user.author_courses.all()
    else:
        courses = request.user.profile.courses.all()
    return render(request, 'accounts/profile.html', {'courses':courses})

def course_singup(request, course_slug):
    try:
        course = Course.objects.get(slug=course_slug)
        request.user.profile.courses.add(course)
        # UserInCourse.objects.create(user=request.user.profile, course=course)
        return HttpResponse('OK')
    except:
        return HttpResponse('ERROR')

def change_learning(request):
    if request.method == 'POST':   
        form = LearningTypeForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            print(form)
            form.save()
            print(request.user.profile.learning_type)
            http = HttpResponse()
            http['OK'] = True
            return http
        else:
            http = HttpResponse()
            http['OK'] = False
            return http

@login_required
def questionnairy_view(request):
    if request.method == 'POST':
        form = QuestionnairyForm(request.POST)
        if form.is_valid():
            request.user.profile.learning_type = form.count_points()
            request.user.profile.save()
            return redirect('accounts:profile')          
    context = {}
    context['form'] = QuestionnairyForm()
    return render(request, 'accounts/questionnairy.html', context)
    



