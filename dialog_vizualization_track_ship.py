# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_animation.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate

class Ui_Dialog_vizualization_track_ship(object):

    def __init__(self, Mainwindow):
        self.Mainwindow = Mainwindow

    def visualization(self, dialog):
        name = self.lineEdit_name.text()
        name = name.replace(' ', '')
        num = 0

        where = ""
        result = ""
        if len(name) > 0:
            names = name.split(',')
            num += 1
            for i in range(0, len(names)):
                where += "t2.name = '" + str(names[i]) + "'"
                if i + 1 != len(names):
                    where += " OR "
        if num > 0:
            result = "AND " + where
        self.Mainwindow.track_ship(result)
        dialog.reject()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(414, 300)
        Dialog.setMinimumSize(QtCore.QSize(414, 300))
        Dialog.setMaximumSize(QtCore.QSize(414, 300))
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(20, 20, 371, 251))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(18)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.horizontalLayout_new = QtWidgets.QHBoxLayout()
        self.horizontalLayout_new.setObjectName("horizontalLayout")
        self.label_new = QtWidgets.QLabel(self.widget)
        self.label_new.setObjectName("label")
        self.horizontalLayout_new.addWidget(self.label_new)
        self.lineEdit_name = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_name.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEdit_name.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.horizontalLayout_new.addWidget(self.lineEdit_name)
        #self.horizontalLayout_new.addWidget(spacerItem_new)
        self.label_new_2 = QtWidgets.QLabel(self.widget)
        self.label_new_2.setObjectName("label_2")
        self.label_new_2.setMinimumSize(QtCore.QSize(150, 0))
        self.label_new_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.horizontalLayout_new.addWidget(self.label_new_2)
        self.verticalLayout.addLayout(self.horizontalLayout_new)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.dateEdit = QtWidgets.QDateEdit(self.widget)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout.addWidget(self.dateEdit)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.widget)
        self.dateEdit_2.setObjectName("dateEdit_2")

        d = QDate(2030, 1, 1)

        # setting date to the date edit
        self.dateEdit_2.setDate(d)

        self.horizontalLayout.addWidget(self.dateEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        #self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        #self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        #
        #self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.widget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(lambda: self.visualization(Dialog)) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_6.setText(_translate("Dialog", "Следы судов"))
        self.label.setText(_translate("Dialog", "Дата"))
        self.label_2.setText(_translate("Dialog", "От:"))
        self.label_3.setText(_translate("Dialog", "До:"))
        self.label_new.setText(_translate("Dialog", "Названия: "))
        self.label_new_2.setText(_translate("Dialog", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
