import os
import cv2

project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
files_dir = input("input pictures dir")
files = os.listdir(files_dir)

i = 0
cascade = cv2.CascadeClassifier(project_dir + '/haarcascades/lbpcascade_animeface.xml')

for file in files:
    file_dir = files_dir+"/"+file
    image = cv2.imread(file_dir)
    if image is None:
        print('Not open : ', file_dir)
        quit()

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    facerect = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1, minSize=(10, 10))

    if len(facerect) > 0:
        for rect in facerect:
            # 顔だけ切り出して保存
            x = rect[0]
            y = rect[1]
            width = rect[2]
            height = rect[3]
            dst = image[y:y + height, x:x + width]
            save_path = files_dir + '/face/' + 'image(' + str(i) + ')' + '.png'
            #認識結果の保存
            cv2.imwrite(save_path, dst)
            print("save!")
            i += 1
print("Finish")
