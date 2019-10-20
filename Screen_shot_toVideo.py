# take multiple screenshots and convert them to video
import glob
import cv2
import pyautogui
import time


## taking number of screenshots
x = 1
while x < 800:
    pyautogui.screenshot('./ScreenShots/image'+str(x)+'.png')
    x += 1
    time.sleep(1)
# cv2.imread is used to read all images

img_array = []
#glob is used to fetch all images
for filename in glob.glob('./ScreenShots/*.png'):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)
    img_array.append(img)

# create image writer object
out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 25, size)

# save images into video
for i in range(len(img_array)):
    out.write(img_array[i])

# release the video
out.release()
cv2.destroyAllWindows()