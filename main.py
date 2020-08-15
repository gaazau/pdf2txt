import os
import sys

from PySide2.QtWidgets import QApplication, QFileDialog, QDialog
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import Slot

from pdf2txt import Pdf2Txt

# 是否使用pyintaller构建
BUILED_BY_PYINTALLER = False


def resource_path(relative_path):
    """获取资源绝对路径

    ref: https://github.com/pyinstaller/pyinstaller/issues/4946#issuecomment-646904437
    """
    if not BUILED_BY_PYINTALLER:
        return relative_path
    bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
    return os.path.abspath(os.path.join(bundle_dir, relative_path))


class MainWindow():
    def __init__(self):
        self.ui = QUiLoader().load(resource_path('ui/pdf2txt.ui'))
        self.ui.openFileBtn.clicked.connect(self.open_file_dialog)
        self.ui.saveImageBtn.clicked.connect(self.save_image_dialog)

        self.pdf_worker = None

    @Slot()
    def open_file_dialog(self):
        dialog = QFileDialog()
        dialog.setNameFilters(["PDF file (*.pdf)"])
        dialog.selectNameFilter("PDF file (*.pdf)")
        if dialog.exec_() == QDialog.Accepted:
            filename_list = dialog.selectedFiles()
            self.pdf_worker = Pdf2Txt(filename_list[0])
            self.ui.outPutText.setText(self.pdf_worker.get_text())

    @Slot()
    def save_image_dialog(self):
        if not self.pdf_worker:
            return
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.DirectoryOnly)
        if dialog.exec_() == QDialog.Accepted:
            self.pdf_worker.output_dir = dialog.selectedFiles()[0]
            self.pdf_worker.output_image_to_file()


app = QApplication([])
window = MainWindow()
window.ui.show()
app.exec_()
