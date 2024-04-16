import subprocess
import glob
import os

# Input Date
subprocess.call(["python", "components\\DateInput.py"])

# Get list of files in the directory
files = glob.glob("_input(image)/*.*")

for file in files:
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-to",
            "1.5",
            "-i",
            file,
            "-i",
            "components/Overlay.png",
            "-i",
            "components/blankVideo.mp4",
            "-filter_complex",
            "[0:v]scale=1280:720[vvid];[vvid][1:v]overlay=0:0[vvid2];[vvid2]drawtext=fontfile=components/Open_Sans.ttf:textfile=components/Date.txt:x=1032:y=150:fontsize=60:fontcolor=white[va];[2:v][va]overlay=0:0",
            "-preset",
            "ultrafast",
            "components/tmpFiles/tmp2/"
            + os.path.splitext(os.path.basename(file))[0]
            + ".mp4",
        ]
    )

files = glob.glob("components/tmpFiles/tmp2/*.*")

for file in files:
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-i",
            file,
            "-f",
            "image2",
            "-vf",
            "fps=1/1",
            "-preset",
            "ultrafast",
            "Output/"
            + os.path.splitext(os.path.basename(file))[0]
            + "_%3d_THUMBNAIL.png",
        ]
    )

# Delete files
for file in glob.glob("components/tmpFiles/tmp1/*"):
    os.remove(file)

for file in glob.glob("components/tmpFiles/tmp2/*mp4"):
    os.remove(file)
