import pymongo
from datetime import datetime, timedelta
from azure.storage.blob import BlockBlobService , ContentSettings , ContainerPermissions
from .private import *

block_blob_service = BlockBlobService(account_name=AZURE_BLOB_ACCOUNT, account_key=AZURE_BLOB_KEY)

#uri = "mongodb://dabba:GxDQLaOeUFH66CxoBlMXEefVMnNYbfaeKHNRguj3PpQMe8u69FU7RlJkvNWTQhCk2zZkfuzds2D63Nr5sNg7ug==@dabba.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
client = pymongo.MongoClient(MONGO_DB_URI)
my_db = client.mybook
users = my_db.user
posts = my_db.Posts

def check_user(uname, pswd):
	#Check user with these credentials is there on azure db	
	item = users.find_one({'username':uname,'passwd':pswd})
	if not item:
		return False
	else:
		return True

def user_info(uname):
	#Get these details from azure
	item = users.find_one({'username':uname})
	return item
	
def update_user_info(uname, info_dict):
	#info_dict will be of form {name: "", age: <int>}
	item = users.update_one({'username':uname},{'$set':info_dict})
	if not item:
		return False
	else:
		return True

def is_following(uname, ouname):
	#check if uname follows oname
	item = users.find_one({'username':uname,'following':{"$all":[ouname]}})
	if not item:
		return False
	else:
		return True
	return False

def follow_user(uname, ouname):
	#make uname follow oname
	item = users.update_one({'username':uname},{"$addToSet":{'following':ouname}})
	if not item:
		return False
	else:
		return True
	 

def unfollow_user(uname, ouname):
	#make uname unfollow oname
	item = users.update_one({'username':uname},{"$pull":{'following':ouname}})
	if not item:
		return False
	else:
		return True

def save_message(uname, post_title, post_content):
	#Save this post to azure DB
	posts.insert_one({'username':uname,'type':0,'title':post_title,'content':post_content})
	return True

def following(uname):
	#Return uname of all users followed by this uname
	items  = users.find({"following":{"$all":[uname]}})
	return items
	
def save_video(uname, video_title,video_file):
	#Wriet it to azure object store
	video_path = 'uploads/'+uname+'/'+video_title+'.mp4'
	block_blob_service.create_blob_from_stream(
    AZURE_BLOB_CONTAINER,
    video_path,
    video_file,
    content_settings=ContentSettings(content_type='video/mp4')
            )
	posts.insert_one({'username':uname,'type':2,'title':video_title,'content':video_path})
	# with open('some/file/name.txt', 'wb+') as destination:
	# 	for chunk in video_file.chunks():
	# 	destination.write(chunk)
	return True

def save_image(uname, image_title,image_file):
	#Wriet it to azure object store
	image_path  = 'uploads/'+uname+'/'+image_title+'.png'
	block_blob_service.create_blob_from_stream(
    AZURE_BLOB_CONTAINER,
    image_path,
    image_file,
    content_settings=ContentSettings(content_type='image/png')
            )
	posts.insert_one({'username':uname,'type':1,'title':image_title,'content':image_path})
	
	# with open('some/file/name.txt', 'wb+') as destination:
	# 	for chunk in image_file.chunks():
	# 	destination.write(chunk)
	return True
	
def does_user_exist(uname):
	#check if user with this username already exists?
	item = users.find_one({'username':uname})
	if not item:
		return False
	else:
		return True
	return False

def add_new_user(uname, pswd, name, age):
	#Save this new user to azure db
	users.insert_one({'username':uname,'passwd':pswd,'name':name,'age':age,'following':[]})
	return True

def get_posts(uname):
	# get the messages, images and videos by this user
	items = posts.find({'username':uname})
	return items
	
def get_feed(uname):
	# get the messages, images and videos by the people followed by this user
	usernames = users.find_one({'username':uname})['following']
	iterable_cursor = posts.find({'username':{'$in':usernames}})
	items = []
	for item in iterable_cursor:
		items.append(item)
	return items
	

def get_post_url(uname, own_relative_url):
	#u know what to do here :p
	sas_url = block_blob_service.generate_container_shared_access_signature(
            AZURE_BLOB_CONTAINER,
            ContainerPermissions.READ,
            datetime.utcnow() + timedelta(minutes=5),
        )
	url = block_blob_service.make_blob_url(AZURE_BLOB_CONTAINER, own_relative_url,sas_token=sas_url)
	return url
	

	
