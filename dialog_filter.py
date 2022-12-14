# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_filter.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_filter(object):

    def __init__(self, Mainwindow):
        self.Mainwindow = Mainwindow

    def click_on_ok(self, dialog):

        #print(self.lineEdit_2.text()) #название
        #print(self.comboBox.currentText()) #Акватория
        #print(self.lineEdit.text()) # Страна
        #print(self.comboBox_2.currentText()) # Тип

        type_table = self.comboBox_tipe_table.currentText()

        type_table_num = 0
        if type_table == "Метки":
            type_table_num = 1
        elif type_table == "Суда":
            type_table_num = 2
        elif type_table == "Satais":
            type_table_num = 3

        name = self.lineEdit_2.text()
        name = name.replace(' ', '')
        #akva = self.comboBox.currentText()
        count = self.lineEdit.text()
        count = count.replace(' ', '').upper()
        types = self.comboBox_2.currentText()

        num = 0

        where = ""
        if len(name) > 0:
            names = name.split(',')
            num += 1
            for i in range(0, len(names)):
                where += "t2.name = '" + str(names[i]) + "'"
                if i + 1 != len(names):
                    where += " OR "
        if len(count) > 0:
            if num > 0:
                where += " AND "
            num += 1
            counts = count.split(',')
            for i in range(0, len(counts)):
                where += "t2.flag = '" + str(counts[i]) + "'"
                if i + 1 != len(counts):
                    where += " OR "
        if len(types) > 0:
            if num > 0:
                where += " AND "
            num += 1
            where += "t2.type = '" + str(types) + "'"
        result = ""
        if num > 0:
            result = "AND " + where
        #print(result)
        #self.Mainwindow.where = result
        self.Mainwindow.remake_table(result, type_table_num)

        dialog.reject()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(481, 371)
        Dialog.setMinimumSize(QtCore.QSize(481, 371))
        Dialog.setMaximumSize(QtCore.QSize(481, 371))
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(30, 20, 421, 331))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(33)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.comboBox_tipe_table = QtWidgets.QComboBox(self.widget)
        self.comboBox_tipe_table.setMinimumSize(QtCore.QSize(150, 0))
        self.comboBox_tipe_table.setMaximumSize(QtCore.QSize(150, 16777215))
        self.comboBox_tipe_table.setObjectName("comboBox_tipe_table")
        self.comboBox_tipe_table.addItem("")
        self.comboBox_tipe_table.addItem("")
        self.comboBox_tipe_table.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox_tipe_table)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(64, 0))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setMinimumSize(QtCore.QSize(64, 0))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setMinimumSize(QtCore.QSize(150, 0))
        self.comboBox.setMaximumSize(QtCore.QSize(150, 16777215))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setMinimumSize(QtCore.QSize(64, 0))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEdit.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setMinimumSize(QtCore.QSize(64, 0))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_2.setMinimumSize(QtCore.QSize(150, 0))
        self.comboBox_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")

        self.horizontalLayout_4.addWidget(self.comboBox_2)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem8)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.widget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(lambda: self.click_on_ok(Dialog)) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_5.setText(_translate("Dialog", "Фильтрация данных"))
        self.label.setText(_translate("Dialog", "Название: "))
        self.label_2.setText(_translate("Dialog", "Акватория:"))
        self.comboBox.setItemText(0, _translate("Dialog", ""))
        self.comboBox.setItemText(1, _translate("Dialog", "Владивосток"))
        self.comboBox.setItemText(2, _translate("Dialog", "Акватория 1"))
        self.comboBox.setItemText(3, _translate("Dialog", "Акватория 2"))
        self.label_6.setText(_translate("Dialog", "Тип таблицы:"))
        self.comboBox_tipe_table.setItemText(0, _translate("Dialog", "Метки"))
        self.comboBox_tipe_table.setItemText(1, _translate("Dialog", "Суда"))
        self.comboBox_tipe_table.setItemText(2, _translate("Dialog", "Satais"))
        self.label_3.setText(_translate("Dialog", "Страна:"))
        self.label_4.setText(_translate("Dialog", "Тип:"))
        self.comboBox_2.setItemText(0, _translate("Dialog", ""))
        self.comboBox_2.setItemText(1, _translate("Dialog", "fishing"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "tag"))
        self.comboBox_2.setItemText(3, _translate("Dialog", "pleasure craft"))
        self.comboBox_2.setItemText(4, _translate("Dialog", "cargo"))
        self.comboBox_2.setItemText(5, _translate("Dialog", "tanker"))
        self.comboBox_2.setItemText(6, _translate("Dialog", "passenger"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
