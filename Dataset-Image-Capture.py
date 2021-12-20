# Imports
import cv2
import argparse
import os

# Parse Arguments
parser = argparse.ArgumentParser()
parser.add_argument('--object', type=str, required=True)
args = parser.parse_args()

# make directory
cmnd = 'mkdir {}'.format(args.object)
os.system(cmnd)


# Intialize OpenCV image capture
cam = cv2.VideoCapture(0)
cv2.namedWindow("Dataset Image Capture")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("OpenCV couldn't capture the image, please try again!")
        break
    cv2.imshow("Dataset Image Capture", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        conf = input('Are you sure you wanna quit? Y - Yes, N - No : ')
        if conf == 'y' or 'Y':
            print("Closing Dataset Image Capture....")
            break
        else:
            pass
    elif k%256 == 32:
        # SPACE pressed
        img_name = "{}/{}_{}.png".format(args.object, args.object, img_counter)
        cv2.imwrite(img_name, frame)
        print("{} captured!".format(img_name))
        img_counter += 1

cam.release()
cv2.destroyAllWindows()