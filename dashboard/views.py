from django.shortcuts import render , redirect
from dashboard.core.core import *

# Create your views here.

def main(request):
	return render(request,'input.html')

def results(request):
	if request.method == 'POST':
		ph_no = request.POST['ph-number']
		fetch_results = fetch_data(str('+91')+str(ph_no))
		return render(request,'details.html',fetch_results)
	else:
		return redirect("/")