from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse

# Create your views here.


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")


def index(request):

    # Check if there already exists a "tasks" key in our session
    if "tasks" not in request.session:

        #If not, create a new list
        request.session["tasks"] = []

    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

def add_task(request):
    
    # check if method is POST
    if request.method == "POST":

        # Take in the date the user submitted and save it as form
        form = NewTaskForm(request.POST)
    
        # Check if form  data is valid (server-side)
        if form.is_valid():
            
            #Isolate the data from the 'cleaned' version of form data
            task = form.cleaned_data["task"]

            #Add the new task to our list of tasks
            request.session['tasks'] += [task]

            # Redirect user to list of tasks
            return HttpResponseRedirect(reverse("tasks:index"))
        else:

            # If the form is invalid, re-render the page with existing information
            return render(request, "tasks/add_task.html", {
                "form": form
            })

    return render(request, "tasks/add_task.html", {
        "form": NewTaskForm()
    })