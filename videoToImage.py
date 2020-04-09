# Importing all necessary libraries
import cv2
import os, argparse


parser = argparse.ArgumentParser (description='Creates a images from input videos')
    # add arguments
parser.add_argument('--input-video', dest='input_video', required=True)
parser.add_argument('--output-folder', dest='output_folder', required=True)
args = parser.parse_args()

# Read the video from specified path
cam = cv2.VideoCapture(args.input_video)

try:
    # creating a folder named data
    if not os.path.exists(args.output_folder):
        os.makedirs(args.output_folder)
        os.chdir(args.output_folder)
    # if not created then raise error
except OSError:
    print('Error: Creating directory ' + args.output_folder)

# frame
currentframe = 0

while (currentframe < 2500):

    # reading from frame
    ret, frame = cam.read()

    if ret:
        # if video is still left continue creating images
        name = 'frame_' + str(currentframe) + '.jpg'
        print('Creating...' + name)

        # writing the extracted images
        cv2.imwrite(name, frame)

        # increasing counter so that it will
        # show how many frames are created
        currentframe += 1
    else:
        break

# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()
