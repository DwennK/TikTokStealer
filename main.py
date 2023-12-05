import pyktok as pyk
import requests
import browser_cookie3
import numpy
import pandas
import moviepy

##Phase 1 : Download video
# pyk.specify_browser('edge') 
# def saveVideo(url): 
#     pyk.save_tiktok(url,
#                 True,
#                     'video_data.csv')   

# url = "https://www.tiktok.com/@iam.asiadoll/video/7197460711801376006?lang=fr"

# saveVideo(url)


##Phase 2 : Reverse (mirror) video

from moviepy.editor import VideoFileClip, vfx
video = VideoFileClip('video.mp4')
out = video.fx(vfx.mirror_x)
out.write_videofile('out.mp4')

##Phase 3 : Removee all metadata

