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
# text = ';'.join([str(i) for i in (1,2,3)])
#
# print(text)

import sqlite3

# dbname = "face_database.db"
# conn = sqlite3.connect(dbname)
# c = conn.cursor()
#
# IntList = list
# sqlite3.register_adapter(IntList, lambda l: ';'.join([str(i) for i in l]))
# sqlite3.register_converter("IntList", lambda s: [int(i) for i in s.split(';')])
#
# create_table = "create table images (name text, dir text, type text, box IntList)"
# c.execute(create_table)
#
# sql = 'insert into images (name, dir, type, box) values (?,?,?,?)'
# user = ("3b08b192.jpg", "D:/documents/PycharmProjects/check_character/data/test/front/3b08b192.jpg", "front", [1,2,3,4])
# c.execute(sql, user)
# conn.commit()
#
# select_sql = 'select * from images'
# for row in c.execute(select_sql):
#     print(row)
#
# conn.close()

dbname = "face_database.db"
conn = sqlite3.connect(dbname)
db = conn.cursor()

sql = "select name, type from images where type = 'front'"
db.execute(sql)
images = db.fetchall()
names = list(map(lambda image: image[0], images))

print(images)
