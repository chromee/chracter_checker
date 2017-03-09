# a = [1, 2, 3, 10, 20, 30, 100, 1000]
b = []

import cv2
import os
import sys
import codecs
import numpy as np
import unicodedata
from scripts.movie_to_picture_converter import MovieToPictureConverter
from scripts.delete_similar_picture import SimilarPictureDeleter


project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
pic_dir = project_dir + "/data/test/ore_twi.jpg"
movie_dir = project_dir + "/data/movie/のんのんびより りぴーと op.mp4"
cap_dir = project_dir + "/data/cap/のんのんびより りぴーと op/"
file_name = os.path.splitext(os.path.split(movie_dir)[1])[0]

# MovieToPictureConverter.convert(movie_dir, cap_dir)
# os.rename(project_dir + "/data/cap/あああ op/", cap_dir)
# text=os.path.split(cap_dir.rstrip("/"))[0] + "/%s/" % "aaa"
# print("_{0:06d}.jpg".format(3))
# SimilarPictureDeleter.delete("D:\documents\PycharmProjects\check_character/data/cap/メカクシティアクターズ/", 0)
# path = "D:\documents\PycharmProjects\check_character/data/cap/新妹魔王の契約者 OP_001/"
# text = os.path.normcase(path)
# files=os.listdir()
# print(text)
# path="D:\documents\PycharmProjects\check_character\data\cap\アスタリスク1期 OP/アスタリスク1期 OP_000001.jpg"
# img=cv2.imread(path)
# cv2.imshow("image", img)
# cv2.waitKey(0)

import sqlite3

dbname = "face_database.db"
conn = sqlite3.connect(dbname)
c = conn.cursor()

create_table = "create table images (name text, dir text, type text)"
c.execute(create_table)

conn.commit()

select_sql = 'select * from images'
for row in c.execute(select_sql):
    print(row)

conn.close()
