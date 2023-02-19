import cv2
import time
import os

# Open the camera
camera = cv2.VideoCapture(0)

# Set the time for 15 min
end_time = time.time() + 15*60

# Create a folder to save the images
folder_name = "images"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)

while True:
    # Capture frame-by-frame
    ret, frame = camera.read()

    # Save the current frame as an image
    image_name = "image_{}.jpg".format(time.strftime("%Y%m%d-%H%M%S"))
    image_path = os.path.join(folder_name, image_name)
    cv2.imwrite(image_path, frame)
    print("Image saved to", image_path)
    
    # wait for 5 minutes
    time.sleep(5*60)
    
    # check if 15 min is over
    if time.time() > end_time:
        break

# Release the camera and close the window
camera.release()
cv2.destroyAllWindows()
