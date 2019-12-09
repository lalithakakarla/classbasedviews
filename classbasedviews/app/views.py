from django.shortcuts import render

from django.views.generic import View, CreateView, UpdateView, DeleteView, ListView,DetailView
from .models import Employee
from django.contrib.messages.views import SuccessMessageMixin


class CreateNewEmp(SuccessMessageMixin, CreateView):
    model = Employee
    fields = "__all__"
    template_name = "registration.html"
    success_url = "/create/"
    success_message = "Employee saved"


class Viewallemployees(ListView):
    model = Employee
    template_name = "view.html"


class Viewoneemployee(DetailView):
    model = Employee
    template_name = "viewone.html"


class Updateemp(SuccessMessageMixin,UpdateView):
    model = Employee
    fields = ['name','salary']
    template_name = "update.html"
    success_url = '/view/'
    success_message = "Updated successfully"


class Deleteemp(SuccessMessageMixin,DeleteView):
    model=Employee
    fields="__all__"
    template_name="delete.html"
    success_url="/view/"
    success_message = "Deleted successfully"
