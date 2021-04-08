import cv2

vidcap = cv2.VideoCapture('sample_video.mp4')
success, image = vidcap.read()
# image is an array of array of [R,G,B] values

count = 0;
while success:
    success, image = vidcap.read()
    cv2.imwrite("frame%d.jpg" % count, image)  # save frame as JPEG file
    if cv2.waitKey(10) == 27:  # exit if Escape is hit
        break
    count += 1
