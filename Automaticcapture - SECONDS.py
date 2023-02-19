
import cv2                                  #computer vision library for image and video processing
import time                                 #working with times and dates
import os

# Open the camera
camera = cv2.VideoCapture(0)

# Set the time for 60 seconds
end_time = time.time() + 60                 #returns the current time in seconds

# Create a folder to save the images
folder_name = "images"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)

while True:                                 # a loop that runs indefinitely until a break statement is encountered or until a specific condition is met.
    # Capture frame-by-frame
    ret, frame = camera.read()

    # Save the current frame as an image
    image_name = "image_{}.jpg".format(time.strftime("%Y%m%d-%H%M%S"))
    image_path = os.path.join(folder_name, image_name)
    cv2.imwrite(image_path, frame)            #save an image to a specified path
    print("Image saved to", image_path)
    
    # wait for 10 Seconds
    time.sleep(10)                            #stops execution of the program for the specified number of seconds.
    
    # check if 60 Seconds is over
    if time.time() > end_time:
        break

# Release the camera and close the window
camera.release()
print("All images saved!")
#cv2.destroyAllWindows()

while True:
    try:
        user_input = input("Press 'q' to quit: ")
        if user_input.lower() == 'q':
            break
    except:
        break

