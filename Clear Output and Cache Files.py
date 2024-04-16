import os
import glob

output_dir = "Output"
files = glob.glob(os.path.join(output_dir, "*"))

for f in files:
    os.remove(f)

for file in glob.glob("components/tmpFiles/tmp1/*png"):
    os.remove(file)

for file in glob.glob("components/tmpFiles/tmp1/*mp4"):
    os.remove(file)

for file in glob.glob("components/tmpFiles/tmp2/*mp4"):
    os.remove(file)

# Batch (.bat File)
# for %%t in ("Output\*") DO del %%t
