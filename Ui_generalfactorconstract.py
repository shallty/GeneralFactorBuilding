# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\GeneralFactroConstract\generalfactorconstract.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1167, 846)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.lineEdit_Date = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_Date.setGeometry(QtCore.QRect(20, 50, 261, 31))
        self.lineEdit_Date.setAutoFillBackground(False)
        self.lineEdit_Date.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_Date.setText("")
        self.lineEdit_Date.setClearButtonEnabled(False)
        self.lineEdit_Date.setObjectName("lineEdit_Date")
        self.pushButton_BetaInput = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_BetaInput.setGeometry(QtCore.QRect(20, 120, 101, 111))
        self.pushButton_BetaInput.setWhatsThis("")
        self.pushButton_BetaInput.setObjectName("pushButton_BetaInput")
        self.lineEdit_BetaPath = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_BetaPath.setGeometry(QtCore.QRect(130, 120, 251, 111))
        self.lineEdit_BetaPath.setObjectName("lineEdit_BetaPath")
        self.pushButton_BetaCalculate = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_BetaCalculate.setGeometry(QtCore.QRect(390, 120, 71, 31))
        self.pushButton_BetaCalculate.setObjectName("pushButton_BetaCalculate")
        self.pushButton_BetaOutput = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_BetaOutput.setEnabled(False)
        self.pushButton_BetaOutput.setGeometry(QtCore.QRect(470, 120, 71, 31))
        self.pushButton_BetaOutput.setObjectName("pushButton_BetaOutput")
        self.pushButton_BookValueInput = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_BookValueInput.setGeometry(QtCore.QRect(20, 270, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_BookValueInput.setFont(font)
        self.pushButton_BookValueInput.setObjectName("pushButton_BookValueInput")
        self.pushButton_RptDateInput = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_RptDateInput.setGeometry(QtCore.QRect(20, 310, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_RptDateInput.setFont(font)
        self.pushButton_RptDateInput.setObjectName("pushButton_RptDateInput")
        self.pushButton_MonthlySizeInput = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_MonthlySizeInput.setGeometry(QtCore.QRect(20, 350, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_MonthlySizeInput.setFont(font)
        self.pushButton_MonthlySizeInput.setObjectName("pushButton_MonthlySizeInput")
        self.lineEdit_BookValuePath = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_BookValuePath.setGeometry(QtCore.QRect(130, 270, 251, 31))
        self.lineEdit_BookValuePath.setObjectName("lineEdit_BookValuePath")
        self.lineEdit_RptDatePath = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_RptDatePath.setGeometry(QtCore.QRect(130, 310, 251, 31))
        self.lineEdit_RptDatePath.setObjectName("lineEdit_RptDatePath")
        self.lineEdit_MonthlySizePath = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_MonthlySizePath.setGeometry(QtCore.QRect(130, 350, 251, 31))
        self.lineEdit_MonthlySizePath.setObjectName("lineEdit_MonthlySizePath")
        self.pushButton_BPCalculate = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_BPCalculate.setGeometry(QtCore.QRect(390, 270, 71, 111))
        self.pushButton_BPCalculate.setObjectName("pushButton_BPCalculate")
        self.pushButton_BPOutput = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_BPOutput.setEnabled(False)
        self.pushButton_BPOutput.setGeometry(QtCore.QRect(470, 270, 71, 111))
        self.pushButton_BPOutput.setObjectName("pushButton_BPOutput")
        self.pushButton_AnnaulProfitInput = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_AnnaulProfitInput.setGeometry(QtCore.QRect(20, 460, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_AnnaulProfitInput.setFont(font)
        self.pushButton_AnnaulProfitInput.setObjectName("pushButton_AnnaulProfitInput")
        self.lineEdit_AnnaulProfitPath = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_AnnaulProfitPath.setGeometry(QtCore.QRect(130, 460, 251, 31))
        self.lineEdit_AnnaulProfitPath.setObjectName("lineEdit_AnnaulProfitPath")
        self.pushButton_GrowthOutput = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_GrowthOutput.setEnabled(False)
        self.pushButton_GrowthOutput.setGeometry(QtCore.QRect(470, 420, 71, 191))
        self.pushButton_GrowthOutput.setObjectName("pushButton_GrowthOutput")
        self.lineEdit_AnnualEarningPath = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_AnnualEarningPath.setGeometry(QtCore.QRect(130, 420, 251, 31))
        self.lineEdit_AnnualEarningPath.setObjectName("lineEdit_AnnualEarningPath")
        self.pushButton_GrowthCalculate = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_GrowthCalculate.setGeometry(QtCore.QRect(390, 420, 71, 191))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_GrowthCalculate.sizePolicy().hasHeightForWidth())
        self.pushButton_GrowthCalculate.setSizePolicy(sizePolicy)
        self.pushButton_GrowthCalculate.setObjectName("pushButton_GrowthCalculate")
        self.lineEdit_AnnaulRptDatePath = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_AnnaulRptDatePath.setGeometry(QtCore.QRect(130, 500, 251, 31))
        self.lineEdit_AnnaulRptDatePath.setObjectName("lineEdit_AnnaulRptDatePath")
        self.pushButton_AnnualRptDateInput = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_AnnualRptDateInput.setGeometry(QtCore.QRect(20, 500, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_AnnualRptDateInput.setFont(font)
        self.pushButton_AnnualRptDateInput.setObjectName("pushButton_AnnualRptDateInput")
        self.pushButton_AnnaulEarningInput = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_AnnaulEarningInput.setGeometry(QtCore.QRect(20, 420, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_AnnaulEarningInput.setFont(font)
        self.pushButton_AnnaulEarningInput.setObjectName("pushButton_AnnaulEarningInput")
        self.lineEdit_SeasonProfitGrowthPath = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_SeasonProfitGrowthPath.setGeometry(QtCore.QRect(130, 540, 251, 31))
        self.lineEdit_SeasonProfitGrowthPath.setObjectName("lineEdit_SeasonProfitGrowthPath")
        self.lineEdit_SeasonRptDatePath = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_SeasonRptDatePath.setGeometry(QtCore.QRect(130, 580, 251, 31))
        self.lineEdit_SeasonRptDatePath.setObjectName("lineEdit_SeasonRptDatePath")
        self.pushButton_SeasonRptDateInput = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_SeasonRptDateInput.setGeometry(QtCore.QRect(20, 580, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_SeasonRptDateInput.setFont(font)
        self.pushButton_SeasonRptDateInput.setObjectName("pushButton_SeasonRptDateInput")
        self.pushButton_SeasonProfitGrowthInput = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_SeasonProfitGrowthInput.setGeometry(QtCore.QRect(20, 540, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_SeasonProfitGrowthInput.setFont(font)
        self.pushButton_SeasonProfitGrowthInput.setObjectName("pushButton_SeasonProfitGrowthInput")
        self.lineEdit_DailyTurnoverPath = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_DailyTurnoverPath.setGeometry(QtCore.QRect(130, 650, 251, 31))
        self.lineEdit_DailyTurnoverPath.setObjectName("lineEdit_DailyTurnoverPath")
        self.pushButton_DailyTurnoverInput = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_DailyTurnoverInput.setGeometry(QtCore.QRect(20, 650, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_DailyTurnoverInput.setFont(font)
        self.pushButton_DailyTurnoverInput.setObjectName("pushButton_DailyTurnoverInput")
        self.pushButton_LiquidityCalculate = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_LiquidityCalculate.setGeometry(QtCore.QRect(390, 650, 71, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_LiquidityCalculate.sizePolicy().hasHeightForWidth())
        self.pushButton_LiquidityCalculate.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_LiquidityCalculate.setFont(font)
        self.pushButton_LiquidityCalculate.setObjectName("pushButton_LiquidityCalculate")
        self.pushButton_LiquidityOutput = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_LiquidityOutput.setEnabled(False)
        self.pushButton_LiquidityOutput.setGeometry(QtCore.QRect(470, 650, 71, 31))
        self.pushButton_LiquidityOutput.setObjectName("pushButton_LiquidityOutput")
        self.pushButton_MomentumCalculate = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_MomentumCalculate.setGeometry(QtCore.QRect(390, 160, 71, 31))
        self.pushButton_MomentumCalculate.setObjectName("pushButton_MomentumCalculate")
        self.pushButton_MomentumOutput = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_MomentumOutput.setEnabled(False)
        self.pushButton_MomentumOutput.setGeometry(QtCore.QRect(470, 160, 71, 31))
        self.pushButton_MomentumOutput.setObjectName("pushButton_MomentumOutput")
        self.pushButton_ReverseCalculate = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_ReverseCalculate.setGeometry(QtCore.QRect(390, 200, 71, 31))
        self.pushButton_ReverseCalculate.setObjectName("pushButton_ReverseCalculate")
        self.pushButton_ReverseOutput = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_ReverseOutput.setEnabled(False)
        self.pushButton_ReverseOutput.setGeometry(QtCore.QRect(470, 200, 71, 31))
        self.pushButton_ReverseOutput.setObjectName("pushButton_ReverseOutput")
        self.lineEdit_DailySizePath = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_DailySizePath.setGeometry(QtCore.QRect(130, 720, 251, 71))
        self.lineEdit_DailySizePath.setObjectName("lineEdit_DailySizePath")
        self.pushButton_DailySizeInput = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_DailySizeInput.setGeometry(QtCore.QRect(20, 720, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_DailySizeInput.setFont(font)
        self.pushButton_DailySizeInput.setObjectName("pushButton_DailySizeInput")
        self.pushButton_SizeCalculate = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_SizeCalculate.setGeometry(QtCore.QRect(390, 720, 71, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_SizeCalculate.sizePolicy().hasHeightForWidth())
        self.pushButton_SizeCalculate.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_SizeCalculate.setFont(font)
        self.pushButton_SizeCalculate.setObjectName("pushButton_SizeCalculate")
        self.pushButton_NonlinearSizeOutput = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_NonlinearSizeOutput.setEnabled(False)
        self.pushButton_NonlinearSizeOutput.setGeometry(QtCore.QRect(470, 720, 71, 31))
        self.pushButton_NonlinearSizeOutput.setObjectName("pushButton_NonlinearSizeOutput")
        self.pushButton_LnSizeOutput = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_LnSizeOutput.setEnabled(False)
        self.pushButton_LnSizeOutput.setGeometry(QtCore.QRect(470, 760, 71, 31))
        self.pushButton_LnSizeOutput.setObjectName("pushButton_LnSizeOutput")
        self.line = QtWidgets.QFrame(self.centralWidget)
        self.line.setGeometry(QtCore.QRect(570, 10, 20, 801))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralWidget)
        self.line_2.setGeometry(QtCore.QRect(20, 100, 118, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralWidget)
        self.line_3.setGeometry(QtCore.QRect(20, 250, 118, 3))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralWidget)
        self.line_4.setGeometry(QtCore.QRect(20, 400, 118, 3))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralWidget)
        self.line_5.setGeometry(QtCore.QRect(20, 630, 118, 3))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralWidget)
        self.line_6.setGeometry(QtCore.QRect(20, 700, 118, 3))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(250, 10, 101, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(750, 10, 231, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_RiskFreeInput = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_RiskFreeInput.setGeometry(QtCore.QRect(600, 160, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_RiskFreeInput.setFont(font)
        self.pushButton_RiskFreeInput.setObjectName("pushButton_RiskFreeInput")
        self.lineEdit_RiskFreePath = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_RiskFreePath.setGeometry(QtCore.QRect(710, 160, 251, 31))
        self.lineEdit_RiskFreePath.setObjectName("lineEdit_RiskFreePath")
        self.pushButton_ThreeFactorOutput = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_ThreeFactorOutput.setEnabled(False)
        self.pushButton_ThreeFactorOutput.setGeometry(QtCore.QRect(1050, 120, 71, 111))
        self.pushButton_ThreeFactorOutput.setObjectName("pushButton_ThreeFactorOutput")
        self.lineEdit_BooktoMarketPath = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_BooktoMarketPath.setGeometry(QtCore.QRect(710, 120, 251, 31))
        self.lineEdit_BooktoMarketPath.setObjectName("lineEdit_BooktoMarketPath")
        self.pushButton_ThreeFactorCalculate = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_ThreeFactorCalculate.setGeometry(QtCore.QRect(970, 120, 71, 111))
        self.pushButton_ThreeFactorCalculate.setObjectName("pushButton_ThreeFactorCalculate")
        self.lineEdit_MonthlyReturnPath = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_MonthlyReturnPath.setGeometry(QtCore.QRect(710, 200, 251, 31))
        self.lineEdit_MonthlyReturnPath.setObjectName("lineEdit_MonthlyReturnPath")
        self.pushButton_MonthlyReturnInput = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_MonthlyReturnInput.setGeometry(QtCore.QRect(600, 200, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_MonthlyReturnInput.setFont(font)
        self.pushButton_MonthlyReturnInput.setObjectName("pushButton_MonthlyReturnInput")
        self.pushButton_BooktoMarketInput = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_BooktoMarketInput.setGeometry(QtCore.QRect(600, 120, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_BooktoMarketInput.setFont(font)
        self.pushButton_BooktoMarketInput.setObjectName("pushButton_BooktoMarketInput")
        self.pushButton_ThreeFactorInput = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_ThreeFactorInput.setGeometry(QtCore.QRect(600, 270, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_ThreeFactorInput.setFont(font)
        self.pushButton_ThreeFactorInput.setObjectName("pushButton_ThreeFactorInput")
        self.pushButton_MonthlyretInput = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_MonthlyretInput.setGeometry(QtCore.QRect(600, 310, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_MonthlyretInput.setFont(font)
        self.pushButton_MonthlyretInput.setObjectName("pushButton_MonthlyretInput")
        self.lineEdit_MonthlyretPath = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_MonthlyretPath.setGeometry(QtCore.QRect(710, 310, 251, 31))
        self.lineEdit_MonthlyretPath.setObjectName("lineEdit_MonthlyretPath")
        self.lineEdit_ThreeFactorPath = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_ThreeFactorPath.setGeometry(QtCore.QRect(710, 270, 251, 31))
        self.lineEdit_ThreeFactorPath.setObjectName("lineEdit_ThreeFactorPath")
        self.pushButton_RsqureCalculate = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_RsqureCalculate.setGeometry(QtCore.QRect(970, 270, 71, 71))
        self.pushButton_RsqureCalculate.setObjectName("pushButton_RsqureCalculate")
        self.pushButton_RsqureOutput = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_RsqureOutput.setEnabled(False)
        self.pushButton_RsqureOutput.setGeometry(QtCore.QRect(1050, 270, 71, 71))
        self.pushButton_RsqureOutput.setObjectName("pushButton_RsqureOutput")
        self.line_7 = QtWidgets.QFrame(self.centralWidget)
        self.line_7.setGeometry(QtCore.QRect(600, 380, 118, 3))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.pushButton_FactorMerger = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_FactorMerger.setGeometry(QtCore.QRect(800, 440, 91, 161))
        self.pushButton_FactorMerger.setObjectName("pushButton_FactorMerger")
        self.pushButton_IntergredFactorOutput = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_IntergredFactorOutput.setEnabled(False)
        self.pushButton_IntergredFactorOutput.setGeometry(QtCore.QRect(900, 440, 101, 161))
        self.pushButton_IntergredFactorOutput.setObjectName("pushButton_IntergredFactorOutput")
        self.line_8 = QtWidgets.QFrame(self.centralWidget)
        self.line_8.setGeometry(QtCore.QRect(20, 810, 118, 3))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(650, 420, 141, 211))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_Beta = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_Beta.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_Beta.setFont(font)
        self.checkBox_Beta.setObjectName("checkBox_Beta")
        self.verticalLayout.addWidget(self.checkBox_Beta)
        self.checkBox_Momentum = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_Momentum.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_Momentum.setFont(font)
        self.checkBox_Momentum.setObjectName("checkBox_Momentum")
        self.verticalLayout.addWidget(self.checkBox_Momentum)
        self.checkBox_Reverse = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_Reverse.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_Reverse.setFont(font)
        self.checkBox_Reverse.setObjectName("checkBox_Reverse")
        self.verticalLayout.addWidget(self.checkBox_Reverse)
        self.checkBox_Growth = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_Growth.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_Growth.setFont(font)
        self.checkBox_Growth.setObjectName("checkBox_Growth")
        self.verticalLayout.addWidget(self.checkBox_Growth)
        self.checkBox_Liquidity = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_Liquidity.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_Liquidity.setFont(font)
        self.checkBox_Liquidity.setObjectName("checkBox_Liquidity")
        self.verticalLayout.addWidget(self.checkBox_Liquidity)
        self.checkBox_NonLinearSize = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_NonLinearSize.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_NonLinearSize.setFont(font)
        self.checkBox_NonLinearSize.setObjectName("checkBox_NonLinearSize")
        self.verticalLayout.addWidget(self.checkBox_NonLinearSize)
        self.checkBox_Lnsize = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_Lnsize.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_Lnsize.setFont(font)
        self.checkBox_Lnsize.setObjectName("checkBox_Lnsize")
        self.verticalLayout.addWidget(self.checkBox_Lnsize)
        self.checkBox_Rsqure = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_Rsqure.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_Rsqure.setFont(font)
        self.checkBox_Rsqure.setObjectName("checkBox_Rsqure")
        self.verticalLayout.addWidget(self.checkBox_Rsqure)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit_Date.setPlaceholderText(_translate("MainWindow", "请在此输入需要计算的日期（例如：20220531）"))
        self.pushButton_BetaInput.setToolTip(_translate("MainWindow", "<html><head/><body><p>收益率为日度收益率模式，市场收益率采用中证全指，无风险利率采用GC007年化收益率对应的日度数据，格式采用第一列为日期列，格式为日期格式(‘date’)，第二列为日度无风险收益率-原始数据名称为gc007（‘riskfreeret’——GC007取wind时间序列中的收盘行情-均价），第三列为中证全指收益率(\'000985.CSI‘），往后是各公司日度收益率！！！!注意！！！计算所得公司个数直接与df中传入公司个数相等</p></body></html>"))
        self.pushButton_BetaInput.setText(_translate("MainWindow", "日度收益率"))
        self.lineEdit_BetaPath.setPlaceholderText(_translate("MainWindow", "文件路径"))
        self.pushButton_BetaCalculate.setToolTip(_translate("MainWindow", "需在日期栏输入日期以获得精确结果"))
        self.pushButton_BetaCalculate.setText(_translate("MainWindow", "Beta计算"))
        self.pushButton_BetaOutput.setText(_translate("MainWindow", "导出"))
        self.pushButton_BookValueInput.setToolTip(_translate("MainWindow", "<html><head/><body><p>公司定期报告披露的数据，即是各年报、季报、中报的标准数据（注意！！！在获取最新数据时，建议向前选取四个季度，例如，若要获取2022年Q2数据，则建议向前选取2021年Q2-2022年Q2）</p></body></html>"))
        self.pushButton_BookValueInput.setText(_translate("MainWindow", "定期报告总资产"))
        self.pushButton_RptDateInput.setToolTip(_translate("MainWindow", "<html><head/><body><p>wind下载的公司定期报告披露日数据，用以对比意图获取的真实数据日期</p></body></html>"))
        self.pushButton_RptDateInput.setText(_translate("MainWindow", "定期报告披露日"))
        self.pushButton_MonthlySizeInput.setToolTip(_translate("MainWindow", "<html><head/><body><p>传入数据格式为wind的excel插件中获取的总市值2(单一A股市值)的月度时间序列数据，最后得到的公司对应数据也以此df为基准，第一列为日期数据</p></body></html>"))
        self.pushButton_MonthlySizeInput.setText(_translate("MainWindow", "月度总市值"))
        self.lineEdit_BookValuePath.setPlaceholderText(_translate("MainWindow", "文件路径"))
        self.lineEdit_RptDatePath.setPlaceholderText(_translate("MainWindow", "文件路径"))
        self.lineEdit_MonthlySizePath.setPlaceholderText(_translate("MainWindow", "文件路径"))
        self.pushButton_BPCalculate.setText(_translate("MainWindow", "BP计算"))
        self.pushButton_BPOutput.setText(_translate("MainWindow", "导出"))
        self.pushButton_AnnaulProfitInput.setToolTip(_translate("MainWindow", "<html><head/><body><p>wind下载的年报净利润数据，格式为第一列日期，第二列开始是公司代码注意，传入数据必须大于或等于3年</p></body></html>"))
        self.pushButton_AnnaulProfitInput.setText(_translate("MainWindow", "定期报告净利润"))
        self.lineEdit_AnnaulProfitPath.setPlaceholderText(_translate("MainWindow", "文件路径"))
        self.pushButton_GrowthOutput.setText(_translate("MainWindow", "导出"))
        self.lineEdit_AnnualEarningPath.setPlaceholderText(_translate("MainWindow", "文件路径"))
        self.pushButton_GrowthCalculate.setToolTip(_translate("MainWindow", "需在日期栏输入日期以获得精确结果"))
        self.pushButton_GrowthCalculate.setText(_translate("MainWindow", "Growth计算"))
        self.lineEdit_AnnaulRptDatePath.setPlaceholderText(_translate("MainWindow", "文件路径"))
        self.pushButton_AnnualRptDateInput.setToolTip(_translate("MainWindow", "<html><head/><body><p>wind下载的年报实际披露日期数据，格式为第一列为公司代码\'code\'，第二列开始为相应年份年报披露日，年份格式为“2005Q4，2006Q4”如此类推</p></body></html>"))
        self.pushButton_AnnualRptDateInput.setText(_translate("MainWindow", "年度报告披露日"))
        self.pushButton_AnnaulEarningInput.setToolTip(_translate("MainWindow", "<html><head/><body><p>wind下载的年报营业收入数据，格式为第一列日期，第二列开始是公司代码注意，传入数据必须大于或等于3年</p></body></html>"))
        self.pushButton_AnnaulEarningInput.setText(_translate("MainWindow", "定期报告总营收"))
        self.lineEdit_SeasonProfitGrowthPath.setPlaceholderText(_translate("MainWindow", "文件路径"))
        self.lineEdit_SeasonRptDatePath.setPlaceholderText(_translate("MainWindow", "文件路径"))
        self.pushButton_SeasonRptDateInput.setToolTip(_translate("MainWindow", "<html><head/><body><p>wind下载的季度报表实际披露日期数据，季度格式长短要与季度净利润增速保持一致</p></body></html>"))
        self.pushButton_SeasonRptDateInput.setText(_translate("MainWindow", "季度报告披露日"))
        self.pushButton_SeasonProfitGrowthInput.setToolTip(_translate("MainWindow", "<html><head/><body><p>季度净利润同比增速，wind下载，格式为第一列为公司代码\'code\'，第二列开始为相应季度净利润增速数据</p></body></html>"))
        self.pushButton_SeasonProfitGrowthInput.setText(_translate("MainWindow", "季度净利润同比"))
        self.lineEdit_DailyTurnoverPath.setPlaceholderText(_translate("MainWindow", "文件路径"))
        self.pushButton_DailyTurnoverInput.setToolTip(_translate("MainWindow", "<html><head/><body><p>从wind获取的日度交易日换手率数据，第一列为日期，第二列开始为公司代码</p></body></html>"))
        self.pushButton_DailyTurnoverInput.setText(_translate("MainWindow", "日度换手率"))
        self.pushButton_LiquidityCalculate.setToolTip(_translate("MainWindow", "需在日期栏输入日期以获得精确结果"))
        self.pushButton_LiquidityCalculate.setText(_translate("MainWindow", "Liquidity"))
        self.pushButton_LiquidityOutput.setText(_translate("MainWindow", "导出"))
        self.pushButton_MomentumCalculate.setToolTip(_translate("MainWindow", "需在日期栏输入日期以获得精确结果"))
        self.pushButton_MomentumCalculate.setText(_translate("MainWindow", "Momentum"))
        self.pushButton_MomentumOutput.setText(_translate("MainWindow", "导出"))
        self.pushButton_ReverseCalculate.setToolTip(_translate("MainWindow", "需在日期栏输入日期以获得精确结果"))
        self.pushButton_ReverseCalculate.setText(_translate("MainWindow", "Reverse"))
        self.pushButton_ReverseOutput.setText(_translate("MainWindow", "导出"))
        self.lineEdit_DailySizePath.setPlaceholderText(_translate("MainWindow", "文件路径"))
        self.pushButton_DailySizeInput.setToolTip(_translate("MainWindow", "<html><head/><body><p>取wind中总市值2（单一A股市值）为标准，第一列为date（日度），第二列开始为公司代码</p></body></html>"))
        self.pushButton_DailySizeInput.setText(_translate("MainWindow", "日度总市值"))
        self.pushButton_SizeCalculate.setToolTip(_translate("MainWindow", "需在日期栏输入日期以获得精确结果"))
        self.pushButton_SizeCalculate.setText(_translate("MainWindow", "执行计算"))
        self.pushButton_NonlinearSizeOutput.setText(_translate("MainWindow", "非线性Size"))
        self.pushButton_LnSizeOutput.setText(_translate("MainWindow", "lnsize导出"))
        self.label.setText(_translate("MainWindow", "普通因子计算"))
        self.label_2.setText(_translate("MainWindow", "Fama-Franch三因子相关计算"))
        self.pushButton_RiskFreeInput.setToolTip(_translate("MainWindow", "<html><head/><body><p>GC028的年化数据（例如，5月无风险收益率需要选择4月第一个交易日的GC028）</p></body></html>"))
        self.pushButton_RiskFreeInput.setText(_translate("MainWindow", "无风险收益率"))
        self.lineEdit_RiskFreePath.setPlaceholderText(_translate("MainWindow", "文件路径"))
        self.pushButton_ThreeFactorOutput.setText(_translate("MainWindow", "导出"))
        self.lineEdit_BooktoMarketPath.setPlaceholderText(_translate("MainWindow", "文件路径"))
        self.pushButton_ThreeFactorCalculate.setText(_translate("MainWindow", "三因子计算"))
        self.lineEdit_MonthlyReturnPath.setPlaceholderText(_translate("MainWindow", "文件路径"))
        self.pushButton_MonthlyReturnInput.setToolTip(_translate("MainWindow", "<html><head/><body><p> 个股月度收益率数据，第一列为date，第二列开始为公司数据</p></body></html>"))
        self.pushButton_MonthlyReturnInput.setText(_translate("MainWindow", "个股月度收益率"))
        self.pushButton_BooktoMarketInput.setToolTip(_translate("MainWindow", "<html><head/><body><p>全市场个股市值及股票账面总资产数据，第一列为code，第二列为市值size（wind-总市值2数据），第三列为账面总资产数据；注意！因为三因子的计算要求，若要求第T年5月-T+1年4月三因子数据，则需要取T年5月1日（非交易日顺延）总市值数据，及T-1年年报披露总资产数据</p></body></html>"))
        self.pushButton_BooktoMarketInput.setText(_translate("MainWindow", "Book-to-Market"))
        self.pushButton_ThreeFactorInput.setToolTip(_translate("MainWindow", "<html><head/><body><p>12个月以上的三因子数据，具体格式为，第一列为date，第二列为riskfree，第三列为marketret，第四列为hml，第五列为smb</p></body></html>"))
        self.pushButton_ThreeFactorInput.setText(_translate("MainWindow", "一年以上三因子"))
        self.pushButton_MonthlyretInput.setToolTip(_translate("MainWindow", "<html><head/><body><p>个股月度收益率，第一列为date，第二列开始为公司代码为标记的月度收益率</p></body></html>"))
        self.pushButton_MonthlyretInput.setText(_translate("MainWindow", "个股月度收益率"))
        self.lineEdit_MonthlyretPath.setPlaceholderText(_translate("MainWindow", "文件路径"))
        self.lineEdit_ThreeFactorPath.setPlaceholderText(_translate("MainWindow", "文件路径"))
        self.pushButton_RsqureCalculate.setToolTip(_translate("MainWindow", "需在日期栏输入日期以获得精确结果"))
        self.pushButton_RsqureCalculate.setText(_translate("MainWindow", "Rsqure"))
        self.pushButton_RsqureOutput.setText(_translate("MainWindow", "导出"))
        self.pushButton_FactorMerger.setText(_translate("MainWindow", "因子结果合并"))
        self.pushButton_IntergredFactorOutput.setText(_translate("MainWindow", "导出"))
        self.groupBox.setTitle(_translate("MainWindow", "可合并因子"))
        self.checkBox_Beta.setText(_translate("MainWindow", "Beta"))
        self.checkBox_Momentum.setText(_translate("MainWindow", "Momentum"))
        self.checkBox_Reverse.setText(_translate("MainWindow", "Reverse"))
        self.checkBox_Growth.setText(_translate("MainWindow", "Growth"))
        self.checkBox_Liquidity.setText(_translate("MainWindow", "Liquidity"))
        self.checkBox_NonLinearSize.setText(_translate("MainWindow", "NonLinearSize"))
        self.checkBox_Lnsize.setText(_translate("MainWindow", "Lnsize"))
        self.checkBox_Rsqure.setText(_translate("MainWindow", "Rsqure"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
