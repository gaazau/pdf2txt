from PySide2.QtWidgets import QApplication, QFileDialog, QDialog
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import Slot

from pdf2txt import Pdf2Txt


class MainWindow():
    def __init__(self):
        self.ui = QUiLoader().load('ui/pdf2txt.ui')
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


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.ui.show()
    app.exec_()
