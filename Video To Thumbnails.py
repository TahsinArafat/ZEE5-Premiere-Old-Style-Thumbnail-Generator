import os
import subprocess

# Input Date
subprocess.call(["python", "components/DateInput.py"])

input_dir = "_input(video)"
temp1_dir = "components/tmpFiles/tmp1"
temp2_dir = "components/tmpFiles/tmp2"
output_dir = "Output"

for file_name in os.listdir(input_dir):
    input_file = os.path.join(input_dir, file_name)
    base_name = os.path.splitext(file_name)[0]

    # First ffmpeg command
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-i",
            input_file,
            "-f",
            "image2",
            "-vf",
            "fps=1/10",
            "-preset",
            "ultrafast",
            f"{temp1_dir}/{base_name}_%3d.png",
        ]
    )

    # Second ffmpeg command
    subprocess.run(
        [
            "ffmpeg",
            "-r",
            "1",
            "-f",
            "image2",
            "-s",
            "1280x720",
            "-y",
            "-i",
            f"{temp1_dir}/{base_name}_%3d.png",
            "-i",
            "components\Overlay.png",
            "-filter_complex",
            "[0:v]scale=1280:720[vvid];[vvid][1:v]overlay=0:0[vvid2];[vvid2]drawtext=fontfile=components/Open_Sans.ttf:textfile=components/Date.txt:x=1032:y=150:fontsize=60:fontcolor=white",
            "-preset",
            "ultrafast",
            f"{temp2_dir}/{base_name}.mp4",
        ]
    )

    # Third ffmpeg command
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-i",
            f"{temp2_dir}/{base_name}.mp4",
            "-f",
            "image2",
            "-vf",
            "fps=1/1",
            "-preset",
            "ultrafast",
            f"{output_dir}/{base_name}_THUMBNAIL_%3d.png",
        ]
    )

# Delete temporary files
for file_name in os.listdir(temp1_dir):
    if file_name.endswith(".png"):
        os.remove(os.path.join(temp1_dir, file_name))

for file_name in os.listdir(temp2_dir):
    if file_name.endswith(".mp4"):
        os.remove(os.path.join(temp2_dir, file_name))
