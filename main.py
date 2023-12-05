import json
import requests
import os

url = "https://www.tiktok.com/@iam.asiadoll/video/7197460711801376006?lang=fr"

# Phase 1: Get video URL, without Watermark

response = requests.get("https://tikwm.com/api/?url=" + url + "&hd=1")
json_data = response.content
# Charger le JSON
data = json.loads(json_data)

# Extraire la valeur de "hdplay"
video_url = data["data"]["hdplay"]

# Create output directory if it doesn't exist
output_directory = "output/"
os.makedirs(output_directory, exist_ok=True)

# Specify the file path
save_path = os.path.join(output_directory, "video_out.mp4")

# Phase 2: Download video from URL

# Send a GET request to the URL
response = requests.get(video_url)

# Check if the request was successful
if response.status_code == 200:
    # Get the content of the response
    video_content = response.content

    # Save the video to a local file
    with open(save_path, "wb") as video_file:
        video_file.write(video_content)

    print("Video saved successfully.")
else:
    print(f"Failed to fetch the video. Status code: {response.status_code}")


#Phase 3 : Reverse (mirror) video

from moviepy.editor import VideoFileClip, vfx
video = VideoFileClip(save_path)
out = video.fx(vfx.mirror_x)
out.write_videofile(os.path.join(output_directory, "video_mirorred.mp4"))

#Phase 4 : Remove all metadata

