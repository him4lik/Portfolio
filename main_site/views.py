from django.shortcuts import render, redirect
from .models import info, project



def home(request):
	template_name='main_site/landing-page.html'
	applicant=info.objects.all()[0]
	projects=project.objects.all()
	context={'applicant': applicant, 'projects': projects}
	return render(request, template_name, context)

