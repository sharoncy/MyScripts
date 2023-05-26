
#Example: print out all paths to files that have jpg or png extension in C:\Users\admin directory

import os

directory = r'C:\Users\sharoncy\Desktop\Programming\QC_mock_up_python'
for entry in os.scandir(directory):
    if (entry.path.endswith(".jpg")
            or entry.path.endswith(".png")) and entry.is_file():
        print(entry.path)

      