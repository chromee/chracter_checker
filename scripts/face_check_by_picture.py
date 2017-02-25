import os
import cv2
import numpy as np
import dlib

project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

face_cascade = cv2.CascadeClassifier(project_dir + '/haarcascades/lbpcascade_animeface.xml')
my_detector = dlib.simple_object_detector(project_dir + "/face_detector/detector.svm")
files_dir = project_dir+'/data/test/front/'
files = os.listdir(files_dir)

MASK_SIZE = 10

for file in files:
    img = cv2.imread(files_dir+file)
    size = img.shape[:2]
    face_img = np.zeros((size[0], size[1], 3), np.uint8)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    is_face_present = False

    faces = face_cascade.detectMultiScale(gray)
    dets = my_detector(img)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    for d in dets:
        cv2.rectangle(img, (d.left(), d.top()), (d.right(), d.bottom()), (0, 0, 255), 2)

    cv2.imshow("original", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
