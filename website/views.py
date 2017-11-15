from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import website.util_copy as wu

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

def signup(request):
	uname = request.session.get('uname', False)
	if uname != False:
		response = HttpResponseRedirect('/')
		return response

	if request.method == "POST":
		uname = request.POST.get('uname', False)
		pswd = request.POST.get('pswd', False)
		name = request.POST.get('name', False)
		age = request.POST.get('age', False)

		if uname==False or pswd==False or name==False or age==False:
			return render(request, 'signup.html', {'error': 'Enter all details'})

		if(wu.does_user_exist(uname)):
			return render(request, 'signup.html', {'error': 'Username already exists'})

		wu.add_new_user(uname, pswd, name, age)

		request.session['uname'] = uname
		request.session.set_expiry(622080000)			#20 years expiry
		response = HttpResponseRedirect('/')
		return response

	return render(request, 'signup.html')

def logout(request):
	del request.session['uname']
	request.session.modified = True
	response = HttpResponseRedirect('/')
	return response

def user_profile(request, username):
	uname = request.session.get('uname', False)

	if request.method == "POST":
		info_dict = {}
		info_dict["name"] = request.POST.get("name", False)
		info_dict["age"] = request.POST.get("age", False)
		wu.update_user_info(uname, info_dict)

		response = HttpResponseRedirect('/user/' + uname)
		return response
	
	res = {'uname': uname, 'ouname': username}
	res["odetail"] = wu.user_info(username)
	if uname != False:
		res["following"] = wu.is_following(uname, username)
	else:
		res["following"] = False
	return render(request, 'user_profile.html', res)

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

def follow_user(request, username):
	uname = request.session.get('uname', False)
	if uname == False:
		response = HttpResponseRedirect('/login')
		return response

	wu.follow_user(uname, username)

	response = HttpResponseRedirect('/user/' + username)
	return response

def unfollow_user(request, username):
	uname = request.session.get('uname', False)
	if uname == False:
		response = HttpResponseRedirect('/login')
		return response

	wu.unfollow_user(uname, username)

	response = HttpResponseRedirect('/user/' + username)
	return response

def add_image(request):
	uname = request.session.get('uname', False)
	if uname == False:
		response = HttpResponseRedirect('/login')
		return response

	if request.method == "POST":
		print(request.FILES)
		title = request.POST.get("title", False)
		content = request.POST.get("pic", False)
		print(title)
		print(content)
		if title==False or content==False or title=="" or content=="":
			return render(request, 'new_image.html', {'uname': uname, 'error': "Enter all data"})

		wu.save_image(uname, title, request.FILES['pic'])
		return render(request, 'new_image.html', {'uname': uname})

	return render(request, 'new_image.html', {'uname': uname})

def add_video(request):
	uname = request.session.get('uname', False)
	if uname == False:
		response = HttpResponseRedirect('/login')
		return response

	if request.method == "POST":
		print(request.FILES)
		title = request.POST.get("title", False)
		content = request.POST.get("vid", False)
		print(title)
		print(content)
		if title==False or content==False or title=="" or content=="":
			return render(request, 'new_video.html', {'uname': uname, 'error': "Enter all data"})

		wu.save_video(uname, title, request.FILES['vid'])
		return render(request, 'new_video.html', {'uname': uname})

	return render(request, 'new_video.html', {'uname': uname})

