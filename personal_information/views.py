from django.shortcuts import render
from gallery.models import Gallery


def home(request):
	gal = Gallery.objects
	return render(request,'home.html',{'gal1':gal})

