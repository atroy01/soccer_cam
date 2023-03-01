# Soccer Cam project
# Combines two simultaneous videos into one video with a larger frame
# 2023-02-28


import cv2
#from tqdm.notebook import tqdm

# Open the two input videos
video1 = cv2.VideoCapture('assets/20230218_164554.mp4')
video2 = cv2.VideoCapture('assets/20230218_164554.mp4')

# Get the dimensions of the first video
width = int(video1.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video1.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the output video codec and framerate
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = 60

# Create the output video writer
out = cv2.VideoWriter('output.mp4', fourcc, fps, (width * 2, height))

# Loop through the frames of the videos and combine them
while True:
    # Read a frame from each video
    ret1, frame1 = video1.read()
    ret2, frame2 = video2.read()
    
    # If either video has reached the end, break out of the loop
    if not ret1 or not ret2:
        break
    
    # Resize the second video to match the height of the first video
    frame2_resized = cv2.resize(frame2, (int(height * (frame2.shape[1] / frame2.shape[0])), height))
    
    # Combine the two frames horizontally
    combined_frame = cv2.hconcat([frame1, frame2_resized])
    
    # Write the combined frame to the output video
    out.write(combined_frame)

# Release the video readers and writer
video1.release()
video2.release()
out.release()

# Close all OpenCV windows
cv2.destroyAllWindows()


