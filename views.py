from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Student
from .forms import StudentForm

class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'


class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'student_form.html'
    fields = ['first_name', 'last_name', 'age', 'grade']

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_confirm_delete.html'
    success_url = reverse_lazy('student_list')


class StudentCreateView(CreateView):
    model = Student
    template_name = 'student_form.html'
    fields = ['first_name', 'last_name', 'age', 'grade']
    success_url = reverse_lazy('student_list')  # Redirect to the student list page after successful form submission

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = reverse_lazy('student_list')  # Adjust the URL name as needed

