import pyktok as pyk
import requests
import moviepy

url="https://www.tiktok.com/@iam.asiadoll/video/7197460711801376006?lang=fr"

##Phase 1 : Download video
response = requests.get("https://tikwm.com/api/?url="+url+"&hd=1")


##Phase 2 : Reverse (mirror) video

# from moviepy.editor import VideoFileClip, vfx
# video = VideoFileClip('video.mp4')
# out = video.fx(vfx.mirror_x)
# out.write_videofile('out.mp4')

##Phase 3 : Removee all metadata

