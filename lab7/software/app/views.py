from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, UpdateView, DeleteView
from django.shortcuts import render
from .models import Software, Version

def index(request):

    num_versions = Version.objects.count()
    versions = Version.objects.all()

    context = {
        'num_versions': num_versions,
        'versions': versions
    }

    return render(request, 'index.html', context=context)

class SoftwareDetailView(DetailView):
    model = Software
    fields = '__all__'

class VersionDetailView(DetailView):
    model = Version
    fields = '__all__'

class VersionCreate(CreateView):
    model = Version
    fields = '__all__'
    success_url = "/"

class SoftwareCreate(CreateView):
    model = Software
    fields = '__all__'
    success_url = "/"

class VersionUpdate(UpdateView):
    model = Version
    fields = '__all__'
    success_url = "/"

class SoftwareUpdate(UpdateView):
    model = Software
    fields = '__all__'
    success_url = "/"

class VersionDelete(DeleteView):
    model = Version
    success_url = "/"

class SoftwareDelete(DeleteView):
    model = Software
    success_url = "/"