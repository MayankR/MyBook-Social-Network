from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import website.util as wu

# Create your views here.

def index(request):
	uname = request.session.get('uname', False)
	if uname == False:
		response = HttpResponseRedirect('/login')
		return response

	return render(request, 'home.html', {'uname': uname})

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

def user_profile(request, username):
	uname = request.session.get('uname', False)
	res = {'uname': uname, 'ouname': username}
	res["odetail"] = wu.user_info(username)
	if uname != False:
		res["following"] = wu.is_following(uname, username)
	else:
		res["following"] = False
	return render(request, 'user_profile.html', res)


def add_video(request):
	response = HttpResponseRedirect('/')
	return response

def add_image(request):
	response = HttpResponseRedirect('/')
	return response

def add_message(request):
	uname = request.session.get('uname', False)
	if uname == False:
		response = HttpResponseRedirect('/login')
		return response

	if request.method == "POST":
		title = request.POST.get("title", False)
		content = request.POST.get("content", False)
		print(title)
		print(content)
		if title==False or content==False or title=="" or content=="":
			return render(request, 'new_message.html', {'uname': uname, 'error': "Enter all details"})

		wu.save_message(uname, title, content)
		return render(request, 'new_message.html', {'uname': uname})


	

	return render(request, 'new_message.html', {'uname': uname})



