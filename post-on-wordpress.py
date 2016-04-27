import datetime, xmlrpclib

wp_url = "http://192.168.3.10/xmlrpc.php"
wp_username = "admin"
wp_password = "admin123"
wp_blogid = ""

status_draft = 0
status_published = 1
status = "publish"

server = xmlrpclib.ServerProxy(wp_url)

with open('post-title.txt', 'r') as myfile:
        title=myfile.read().replace('\n', '')
with open('post.txt', 'r') as myfile:
	content=myfile.read().replace('\n', '')
post_date = xmlrpclib.DateTime(datetime.datetime.strptime("2016-04-24 22:08", "%Y-%m-%d %H:%M"))
categories = ["realestate"]
tags = ["hiranandani", "powai"]
post_data = {'title': title, 'description': content, 'dateCreated': post_date, 'categories': categories, 'mt_keywords': tags}

post_id = server.metaWeblog.newPost(wp_blogid, wp_username, wp_password, post_data, status)
