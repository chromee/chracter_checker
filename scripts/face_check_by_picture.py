import os
import shutil
import cv2
import numpy as np

project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

face_cascade = cv2.CascadeClassifier(project_dir + '/haarcascades/lbpcascade_animeface.xml')
files_dir = project_dir+'/data/gj-bu/GJ-bu 02.mp4/'
files = os.listdir(files_dir)

MASK_SIZE = 10


def check_face(img):
    size = img.shape[:2]
    face_img = np.zeros((size[0], size[1], 3), np.uint8)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    is_face_present = False

    faces = face_cascade.detectMultiScale(gray)
    for (x, y, w, h) in faces:
        lx = x - 10 if x > 10 else 0
        ly = y - 20 if y > 20 else 0
        lw = w + 20
        lh = h + 20

        roi_color = img[ly:ly + lh, lx:lx + lw]
        face_img[ly:ly + lh, lx:lx + lw] = roi_color
        is_face_present = True

        cv2.rectangle(img, (lx, ly), (lx + lw, ly + lh), (255, 0, 0), 2)

    cv2.imshow("original", img)
    return face_img if is_face_present else img


def check_character(check_img, character_name, color_name, hsv_min_array, hsv_max_array):
    check_img = cv2.resize(check_img, (orig_size[1] // MASK_SIZE, orig_size[0] // MASK_SIZE))
    hsv = cv2.cvtColor(check_img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, hsv_min_array, hsv_max_array)
    m = cv2.countNonZero(mask)
    print(color_name + "のブロック数", m)

    show = cv2.bitwise_and(check_img, check_img, mask=mask)
    show = cv2.resize(show, view_size, interpolation=cv2.INTER_NEAREST)
    cv2.imshow(character_name, show)

    return [m, character_name]


for file in files:
    img = cv2.imread(files_dir + file)
    orig_size = img.shape[:2]
    view_size = (500, 500 * orig_size[0] // orig_size[1])
    img = cv2.resize(img, view_size)
    # cv2.imshow("original", img)

    character_and_color_counts = []

    face_img = check_face(img)

    character_and_color_counts.append(
        check_character(face_img, 'mao', 'orange', np.array([10, 120, 140]), np.array([20, 255, 255])))
    character_and_color_counts.append(
        check_character(face_img, 'sion', 'violet', np.array([120, 80, 50]), np.array([150, 255, 255])))
    character_and_color_counts.append(
        check_character(face_img, 'megumi', 'pink', np.array([155, 80, 50]), np.array([170, 255, 255])))
    character_and_color_counts.append(
        check_character(face_img, 'kirara', 'yellow', np.array([20, 10, 10]), np.array([34, 255, 255])))

    character = max(character_and_color_counts)[1]
    print(character + "が映っています")
    # shutil.move('./data/' + file, "./data/%s/%s" % (character, file))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
