def check_user(uname, pswd):
	#Check user with these credentials is there on azure db
	return True

def user_info(uname):
	#Get these details from azure
	return {"name": "Super Man", "uname": uname, "age": 23, "following": ["batman", "wonderwoman"]}

def is_following(uname, ouname):
	#check if uname follows oname
	return False

def save_message(uname, post_title, post_content):
	#Save this post to azure DB
	return True

def following(uname):
	#Return uname of all users followed by this uname
	return {}