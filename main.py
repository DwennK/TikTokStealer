import json
import requests
import os
from moviepy.editor import VideoFileClip, vfx

def get_video_url(url):
    response = requests.get(f"https://tikwm.com/api/?url={url}&hd=1")
    json_data = response.content
    data = json.loads(json_data)
    return data["data"]["hdplay"]

def download_video(video_url, output_directory, output_filename):
    response = requests.get(video_url)
    if response.status_code == 200:
        video_content = response.content
        save_path = os.path.join(output_directory, output_filename)
        with open(save_path, "wb") as video_file:
            video_file.write(video_content)
        print("Video saved successfully.")
    else:
        print(f"Failed to fetch the video. Status code: {response.status_code}")

def reverse_video(input_path, output_directory, output_filename):
    video = VideoFileClip(input_path)
    mirrored_video = video.fx(vfx.mirror_x)
    save_path = os.path.join(output_directory, output_filename)
    mirrored_video.write_videofile(save_path)

if __name__ == "__main__":
    url = "https://www.tiktok.com/@iam.asiadoll/video/7197460711801376006?lang=fr"
    output_directory = "output/"
    os.makedirs(output_directory, exist_ok=True)

    # Phase 1: Get video URL, without Watermark
    video_url = get_video_url(url)

    # Phase 2: Download video from URL
    download_video(video_url, output_directory, "video.mp4")

    # Phase 3: Reverse (mirror) video
    reverse_video(os.path.join(output_directory, "video.mp4"), output_directory, "video_mirrored.mp4")

    # Phase 4: Remove all metadata

