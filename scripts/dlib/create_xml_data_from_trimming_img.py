import cv2
import os
from datetime import datetime

project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))


class CreateXmlDataFromTrimmingImg:

    @staticmethod
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

    @staticmethod
    def output_text(output_dir, text):
        file_name = output_dir + 'image_data_{0}.txt'.format(datetime.now().strftime('%Y%m%d%H%M'))
        f = open(file_name, 'w')
        f.write(text)
        f.close()

    @staticmethod
    def replace_xml(dir, text):
        f = open(dir, 'w')
        f.write(text)
        f.close()

train_img_dir = project_dir + "/data/test/front/finish/train/"
test_img_dir = project_dir + "/data/test/front/finish/test/"
text_dir = project_dir + "/face_detector/data_text/"
xml_dir = project_dir + "/face_detector/xml/"

training_xml_text = CreateXmlDataFromTrimmingImg.create_xml_text(train_img_dir)
testing_xml_text = CreateXmlDataFromTrimmingImg.create_xml_text(test_img_dir)

CreateXmlDataFromTrimmingImg.output_text(text_dir, training_xml_text)
CreateXmlDataFromTrimmingImg.output_text(text_dir, testing_xml_text)

CreateXmlDataFromTrimmingImg.replace_xml(xml_dir+"training.xml", training_xml_text)
CreateXmlDataFromTrimmingImg.replace_xml(xml_dir+"testing.xml", testing_xml_text)