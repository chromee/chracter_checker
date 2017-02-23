import cv2
import sys
import os
from datetime import datetime
from xml.dom import minidom

project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))


def create_xml_text(img_dir):
    xml_text = """
<?xml version='1.0' encoding='ISO-8859-1'?>
<?xml-stylesheet type='text/xsl' href='image_metadata_stylesheet.xsl'?>
<dataset>
  <name>imglab dataset</name>
  <images>
"""

    files = os.listdir(img_dir)
    for file in files:
        img = cv2.imread(img_dir + file)
        y = 0
        x = 0
        w, h = img.shape[:2]
        xml_text += """
    <image file='{0}'>
      <box top='{1}' left='{2}' width='{3}' height='{4}'/>
    </image>
    """.format(img_dir + file, y, x, w, h).replace("\\", "/")

    xml_text += """
  </images>
</dataset>
"""

    return xml_text


def output_text(output_dir, text):
    file_name = output_dir + 'image_data_{0}.txt'.format(datetime.now().strftime('%Y%m%d%H%M'))
    f = open(file_name, 'w')
    f.write(text)
    f.close()


def replace_xml(dir, text):
    f = open(dir, 'w')
    f.write(text)
    f.close()

pic_dir = project_dir + "/data/test/side/"
text_dir = project_dir + "/face_detector/data_text/"
xml_dir = project_dir + "/face_detector/xml/"

training_xml_text = create_xml_text(pic_dir)
testing_xml_text = create_xml_text(pic_dir)

output_text(text_dir, training_xml_text)
output_text(text_dir, testing_xml_text)
print(xml_dir+"training.xml")
replace_xml(xml_dir+"training.xml", training_xml_text)
replace_xml(xml_dir+"testing.xml", testing_xml_text)