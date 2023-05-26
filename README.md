#  BRAINSPACE scripts. 

Python scripts used in the planning stages of the [BRAINSPACE Project] (https://github.com/Neural-Systems-at-UIO/BRAINSPACE). 

## Generate images.

The `overlay.py` script generates circles in a grid pattern on top of a base image, with the circle fill colour representing anchoring accuracy (green = 0 = correctly anchored; yellow = 2 = unknown; red = 1 = incorrectly anchored).  

The `addNumbers.py` script generates numbers in a grid pattern on top of a base image. The numbers are pulled from a csv file and correspond to the ID number of each grid point. 

The `gridCrosses.py` script generates a grid of crosses of a specified pixel distance apart that are randomly positioned in space. 

The `.cmd files` are used to run the above scripts.
