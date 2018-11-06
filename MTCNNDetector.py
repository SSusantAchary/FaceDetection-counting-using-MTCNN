'''
## MIT License
Copyright (c) 2016 David Sandberg

Process Flow:
1.Read the image
2.send to detect face
3.get the coordinates
4.draw bounding box on face
5.write the image
6.store the time in seperate text file ,image name, count of faces, dimension, time log for each image.

The below code is used for checking detecting faces and recording how fast does it detect, and can also be used in conjuntion with Face Tracker Algorithm to Track.

'''
#/usr/bin/python3


#import packages
import cv2
import tensorflow as tf
import detect_face
import argparse
import sys
import os
import time


def main(args):

    #list all the files from directory and sort them baseo in numerical order
    list = sorted(os.listdir(args['location']))
    list.sort(key=lambda f:int(''.join(filter(str.isdigit, f))))

    #Parameters for MTCNN
    sess = tf.Session()
    pnet, rnet, onet = detect_face.create_mtcnn(sess, None)
    minsize = 40  # minimum size of face
    threshold = [0.6, 0.7, 0.9]  # three steps's threshold
    factor = 0.709  # scale factor

    #create a file and write the metedata generated from precessing
    file = open(args['fileName'], "w")
    for each in range(0,len(list)):
        image = cv2.imread(args['location']+list[each])
        h,w = image.shape[:2]# get the shape row i.e h, column i.e w
        start = time.time()#start time
        bounding_boxes, points = detect_face.detect_face(image, minsize, pnet, rnet, onet, threshold, factor)# it return bounding box and point ie. the five facial features
        end = time.time()# here the time is to measure how much it takes to detect faces.
        count = 0
        for b in bounding_boxes:
            cv2.rectangle(image, (int(b[0]), int(b[1])), (int(b[2]), int(b[3])), (0, 255, 0), 1)# gives x-coordinate, y- coordinate, width(no of columns), height(no of rows)
            count += 1
        cv2.imwrite("/home/user/Frames/" + str(each) + ".jpg", image)
        file.write(str(list[each])+"  ," + "faces:" + str(count) + "  ," +"dimension:"+ str(h)+" x "+str(w)+"  ,"+ "timetaken:" + str((end - start)))
        file.write('\n')

    file.close()


#Driver Code
if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-l","--location", type=str, help="Location of the folder containing image")
    ap.add_argument("-f", "--fileName",type=str, help="file to write metadata of image")
    args = vars(ap.parse_args())

    if (args["location"] and args['fileName']) == None:
        print("Input image location/ file name is not provided")
        sys.exit()

    main(args)





