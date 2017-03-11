import sqlite3

project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
db_dir = project_dir + "/face_detector/db"

db_path = os.path.join(db_dir, "face_database.db")
conn = sqlite3.connect(db_path)
db = conn.cursor()

img_type = os.path.split(img_set_dir.rstrip("/"))[1]
sql = "select * from images where type = '%s'" % img_type
db.execute(sql)
images = db.fetchall()

print(images)
