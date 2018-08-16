# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/DataVisualizer.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DataVisualizer(object):
    def setupUi(self, DataVisualizer):
        DataVisualizer.setObjectName(_fromUtf8("DataVisualizer"))
        DataVisualizer.resize(919, 617)
        
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DataVisualizer.sizePolicy().hasHeightForWidth())
        DataVisualizer.setSizePolicy(sizePolicy)
        
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.gridLayout = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))

        self.streamBtn = QtGui.QPushButton(self.dockWidgetContents)
        self.streamBtn.setCheckable(True)
        self.streamBtn.setObjectName(_fromUtf8("streamBtn"))
        self.gridLayout.addWidget(self.streamBtn, 2, 0, 1, 1)

        self.plot = GraphicsLayoutWidget(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot.sizePolicy().hasHeightForWidth())
        self.plot.setSizePolicy(sizePolicy)
        self.plot.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.plot.setObjectName(_fromUtf8("plot"))
        self.gridLayout.addWidget(self.plot, 1, 0, 1, 5)

        self.clearBtn = QtGui.QPushButton(self.dockWidgetContents)
        self.clearBtn.setObjectName(_fromUtf8("clearBtn"))
        self.gridLayout.addWidget(self.clearBtn, 2, 1, 1, 1)

        self.autorange = QtGui.QCheckBox(self.dockWidgetContents)
        self.autorange.setObjectName(_fromUtf8("autorange"))
        self.gridLayout.addWidget(self.autorange, 2, 2, 1, 1)

        self.label_5 = QtGui.QLabel(self.dockWidgetContents)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 2, 3, 1, 1)
        self.xRange = QtGui.QSpinBox(self.dockWidgetContents)
        self.xRange.setMinimum(1)
        self.xRange.setMaximum(50000)
        self.xRange.setSingleStep(1000)
        self.xRange.setProperty("value", 2000)
        self.xRange.setObjectName(_fromUtf8("xRange"))
        self.gridLayout.addWidget(self.xRange, 2, 4, 1, 1)

        self.dispStream = QtGui.QCheckBox(self.dockWidgetContents)
        self.dispStream.setObjectName(_fromUtf8("dispStream"))
        self.gridLayout.addWidget(self.dispStream, 3, 0, 1, 1)

        self.ch0 = QtGui.QSpinBox(self.dockWidgetContents)
        self.ch0.setMinimum(0)
        self.ch0.setMaximum(63)
        self.ch0.setSingleStep(1)
        self.ch0.setProperty("value", 0)
        self.ch0.setObjectName(_fromUtf8("ch0"))
        self.gridLayout.addWidget(self.ch0, 3, 1, 1, 1)

        self.ch1 = QtGui.QSpinBox(self.dockWidgetContents)
        self.ch1.setMinimum(0)
        self.ch1.setMaximum(63)
        self.ch1.setSingleStep(1)
        self.ch1.setProperty("value", 1)
        self.ch1.setObjectName(_fromUtf8("ch1"))
        self.gridLayout.addWidget(self.ch1, 3, 2, 1, 1)

        self.ch2 = QtGui.QSpinBox(self.dockWidgetContents)
        self.ch2.setMinimum(0)
        self.ch2.setMaximum(63)
        self.ch2.setSingleStep(1)
        self.ch2.setProperty("value", 2)
        self.ch2.setObjectName(_fromUtf8("ch2"))
        self.gridLayout.addWidget(self.ch2, 3, 3, 1, 1)

        self.ch3 = QtGui.QSpinBox(self.dockWidgetContents)
        self.ch3.setMinimum(0)
        self.ch3.setMaximum(63)
        self.ch3.setSingleStep(1)
        self.ch3.setProperty("value", 3)
        self.ch3.setObjectName(_fromUtf8("ch3"))
        self.gridLayout.addWidget(self.ch3, 3, 4, 1, 1)

        DataVisualizer.setWidget(self.dockWidgetContents)

        self.retranslateUi(DataVisualizer)
        QtCore.QMetaObject.connectSlotsByName(DataVisualizer)
        self.dispStream.setProperty("checked", True)

    def retranslateUi(self, DataVisualizer):
        DataVisualizer.setWindowTitle(_translate("DataVisualizer", "ADC Control", None))
        self.streamBtn.setText(_translate("DataVisualizer", "Stream Data", None))
        self.clearBtn.setText(_translate("DataVisualizer", "Clear plots", None))
        self.autorange.setText(_translate("DataVisualizer", "Autorange", None))
        self.label_5.setText(_translate("DataVisualizer", "X-axis range (ms):", None))
        self.dispStream.setText(_translate("DataVisualizer", "Display stream data from Ch:", None))


from pyqtgraph import GraphicsLayoutWidget
