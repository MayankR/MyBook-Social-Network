def check_user(uname, pswd):
	#Check user with these credentials is there on azure db
	return True

def user_info(uname):
	#Get these details from azure
	return {"name": "Super Man", "uname": uname, "age": 23, "following": ["batman", "wonderwoman"]}

def update_user_info(uname, info_dict):
	#info_dict will be of form {name: "", age: <int>}
	return True

def is_following(uname, ouname):
	#check if uname follows oname
	return False

def follow_user(uname, ouname):
	#make uname follow oname
	return False

def unfollow_user(uname, ouname):
	#make uname unfollow oname
	return False

def save_message(uname, post_title, post_content):
	#Save this post to azure DB
	return True

def following(uname):
	#Return uname of all users followed by this uname
	return {}

def save_video(uname, video_title, video_file):
	#Wriet it to azure object store


	# with open('some/file/name.txt', 'wb+') as destination:
	# 	for chunk in video_file.chunks():
	# 	destination.write(chunk)
	return True

def save_image(uname, image_title, image_file):
	#Wriet it to azure object store


	# with open('some/file/name.txt', 'wb+') as destination:
	# 	for chunk in image_file.chunks():
	# 	destination.write(chunk)
	return True




def does_user_exist(uname):
	#check if user with this username already exists?
	return False

def add_new_user(uname, pswd, name, age):
	#Save this new user to azure db
	return True