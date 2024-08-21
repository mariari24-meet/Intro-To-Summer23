def create_youtube_video (title,description):
	youtube = { "title": title, 
	"description" : description , 
	"likes" : 0 ,
	"dislikes" : 0 ,
	"comments" : {"username": None}
	}
	return youtube

def like (youtube):
	if "likes" in youtube:
		youtube["likes"]+=1
	return youtube

def dislike (youtube):
	if "dislikes" in youtube:
		youtube["dislikes"]+=1
	return youtube

def add_comment(youtube,username,comment_text):
	youtube ["comments"]["username"]= comment_text
	return youtube 

video = create_youtube_video("video1","this is video1")
video = like(video)
video = dislike(video)
video = add_comment("video", "maria","its beautiful")
print(video)