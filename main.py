from PySide2.QtWidgets import QApplication, QMessageBox, QFileDialog
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import Signal, Slot

from pdf2txt import Pdf2Txt


class MainWindow():
    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('ui/pdf2txt.ui')

        self.ui.openFileBtn.clicked.connect(self.open_file_dialog)

    @Slot()
    def open_file_dialog(self):
        # 生成文件对话框对象
        dialog = QFileDialog()
        # 设置文件过滤器，这里是任何文件，包括目录噢
        dialog.setFileMode(QFileDialog.AnyFile)
        # 设置显示文件的模式，这里是详细模式
        dialog.setViewMode(QFileDialog.Detail)
        if dialog.exec_():
            filename_list = dialog.selectedFiles()
            converter = Pdf2Txt(filename_list[0])
            self.ui.outPutText.setText(converter.get_text())


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.ui.show()
    app.exec_()
