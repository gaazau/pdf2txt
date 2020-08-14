import sys
if sys.version_info > (3, 0):
    from io import StringIO
else:
    from io import BytesIO as StringIO

from pdfminer.high_level import extract_text
from pdfminer.high_level import extract_text_to_fp


class Pdf2Txt():
    def __init__(self, path, output_dir=None):
        self.path = path
        self.output_dir = output_dir

    def get_text(self):
        return extract_text(self.path)

    def output_image_to_file(self):
        output_string = StringIO()
        with open(self.path, "rb") as fin:
            extract_text_to_fp(fin, output_string, output_dir=self.output_dir)
