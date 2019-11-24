import cv2
import numpy as np
from os import listdir
from os.path import join

DEFAULT_WIDTH = 1000
PATH = "."
FLAG = "large"
IMAGE_EXT = ['jpg', 'jpeg', 'png']

for image_file in [f for f in listdir(PATH) if f.split('.')[-1] in IMAGE_EXT]:
    image_name = "".join(image_file.split('.')[0:-1])
    if image_name.endswith(FLAG):
        continue
    image_ext = image_file.split('.')[-1]
    image = cv2.imread(join(PATH, image_file), cv2.IMREAD_UNCHANGED)
    h, w, _ = image.shape
    scaling = DEFAULT_WIDTH / w
    image = cv2.resize(image, (0,0), fx=scaling, fy=scaling)
    new_image_file = f"{image_name}_{FLAG}.{image_ext}"
    cv2.imwrite(join(PATH, new_image_file), image)
