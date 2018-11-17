# MTCNN-TensorFlow - Joint Face Detection and Alignment using Multi-task Cascaded Convolutional Networks based Counting
Face Detection is an important problem statement, the idea is to detect face in an image containing people.

original work can be reached at below link:

https://arxiv.org/pdf/1604.02878.pdf

#####################################

What essentially MTCNN algorithm does is :
-First Stage: produces candidate(possible features which refer to a face)windows quickly through a shallow CNN.
-Second Stage: refines the windows to reject a large number of non-faces windows through a more complex CNN.
-Third Stage: a more powerful CNN to refine the result and output facial landmarks positions.

#####################################

To execute the code download the files 
and run the command:

python MTCNNDetector.py -l "/location/of/the/images" -f "metadata file to write"

#####################################

Dependencies(Tested with):
1.Python 3.5 >=
2.OpenCV 3.4 and above(have tested with 3.4, one can even try with other opencv 3* versions)
3.Tensorflow 1.11.0

#####################################

Execution flow of the code:
1. Sets the parameters(can be changed based input size of image, stand evaluation for face is 120*120 px) for MTCNN algorthim
2. Reads the image, calculate the shape.
3. Sends the image to detect faces(ie. which internally runs through three NN(Proposal-Net, Residual-Net, Output-Net))
4. Returns the bounding box(x-coordinate, y-coordinate, width, height), and draw them on the face location.
5. Writes the metadata on to the file.

#####################################

Uses Cases:
1. People Counting
2. Face based Tracking
3. Face Recognition(Smart City, Law Enforcement)
4. Retail Stores
...more...

# MIT License
