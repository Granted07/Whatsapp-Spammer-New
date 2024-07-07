msg=''
import os,sys
from whatsapp import returnDictData, send_message
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect, QStringListModel,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QMainWindow, QFileDialog, QDialogButtonBox, QRadioButton,
    QLabel, QMenuBar, QStatusBar, QPushButton, QSizePolicy, QWidget, QAbstractButton, QTextBrowser, QTextEdit)
from PySide6 import QtWidgets

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(400,400,425,332)
        self.initUI()

    def initUI(self):
        
        font = QFont()
        font.setFamilies([u"Montserrat"])
        font.setPointSize(10)
        font.setBold(True)

        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(10, 230, 111, 17))
        self.radioButton.setFont(font)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(self)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 425, 21))
        self.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName(u"statusbar")
        self.setStatusBar(self.statusbar)

        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(70, 290, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.rejected.connect(self.reject)
        self.buttonBox.accepted.connect(self.accept)
        self.b1 = QPushButton(self)
        self.b1.setObjectName(u"b1")
        self.b1.setGeometry(QRect(10, 50, 75, 23))
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 211, 21))
        self.label.setFont(font)
        self.b2 = QPushButton(self)
        self.b2.setObjectName(u"b2")
        self.b2.setGeometry(QRect(10, 160, 75, 23))
        self.b1.clicked.connect(self.profileselect)
        self.b2.clicked.connect(self.openform)
        self.label_2 = QLabel(self)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 130, 211, 21))
        self.label_2.setFont(font)
        self.label_3 = QLabel(self)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(150, 130, 211, 21))
        self.label_3.setFont(font)
        self.setWindowTitle(QCoreApplication.translate("Dialog", u"Whatsapp Spammer", None))
        self.b1.setText(QCoreApplication.translate("Dialog", u"Choose File", None))
        self.b2.setText(QCoreApplication.translate("Dialog", u"Open", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Current selected file:\n ", None))
        self.label.adjustSize()
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Edit Form.csv:", None))
        self.label_2.adjustSize()
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Enter Message (use {name} for name)", None))
        self.label_3.adjustSize()
        self.textEdit = QTextEdit(self)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(150, 160, 251, 121))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Use Ctrl+V", None))

    def profileselect(self):
        global folderName
        
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        options |= QFileDialog.DontUseCustomDirectoryIcons
        dialog = QFileDialog()
        dialog.setOptions(options)
        if os.name == 'nt':
            x=os.getenv('APPDATA')
            x+='\\\\'
            dialog.setDirectory(x+'Mozilla\\Firefox\\Profiles')
        else:
            x=os.getenv('HOME')
            dialog.setDirectory(x+'/.mozilla/firefox/')
        folderName = str(dialog.getExistingDirectory(self, "Select Directory"))
        self.label.setText(QCoreApplication.translate("Dialog", u"Current selected file:\n"+folderName , None))
        self.label.adjustSize()

    def reject(self):
        sys.exit(1)

    def openform(self):
        os.startfile("form.csv")

    def accept(self):
        global msg
        print('Toggled: ', self.radioButton.isChecked())
        csvlist = returnDictData("form.csv","Name", "Number")
        active_list = csvlist # or test_list
        msg = self.textEdit.toPlainText()
        print('Message:',msg)
        if self.radioButton.isChecked():
            send_message(active_list, msg, False, folderName, f=1)
        else:
            send_message(active_list, msg, False, folderName, f=0)
        # filtered = []

        # for user in active_list:
        #      print(user[2])
        #      if user[2]==8:
        #          filtered.append(user)


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec())

window()

