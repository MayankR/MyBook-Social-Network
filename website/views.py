from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import website.util as wu

# Create your views here.

def index(request):
	uname = request.session.get('uname', False)
	if uname == False:
		response = HttpResponseRedirect('/login')
		return response

	return render(request, 'home.html')

def login(request):
	uname = request.session.get('uname', False)
	if uname != False:
		response = HttpResponseRedirect('/')
		return response

	uname = request.GET.get('uname', False)
	pswd = request.GET.get('pswd', False)

	if uname==False or pswd==False:
		return render(request, 'login.html')

	if(wu.check_user(uname, pswd)):
		request.session['uname'] = uname
		request.session.set_expiry(622080000)			#20 years expiry
		response = HttpResponseRedirect('/')
		return response

	return render(request, 'login.html')

def logout(request):
	del request.session['uname']
	request.session.modified = True
	response = HttpResponseRedirect('/')
	return response