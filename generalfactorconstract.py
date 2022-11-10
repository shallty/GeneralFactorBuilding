# -*- coding: utf-8 -*-

"""
Module implementing Action.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication, QMessageBox
import sys
import pandas as pd
from fc import (beta_extract, momentum_and_reverse_constract, extract_financial_real_data, extract_growthfactor,
daily_average_turnover, nonlinersize_constract, threefactor_constract, extract_threefactor_Rsqure)

from Ui_generalfactorconstract import Ui_MainWindow

sys.path.append("G:\\GeneralFactroConstract\\")


class Action(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Action, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_BetaInput_clicked(self):
        file_input_path, filetype = QFileDialog.getOpenFileName(self, '选取文件', "", "")
        try:
            self.dailyret = pd.read_excel(file_input_path)
            self.lineEdit_BetaPath.setText(str(file_input_path))
        except:
            pass
    
    @pyqtSlot()
    def on_pushButton_BetaCalculate_clicked(self):
        date = pd.to_datetime(self.lineEdit_Date.text())
        be = beta_extract(self.dailyret)
        try:
            self.Beta = be.extract_beta_df(date)
            self.pushButton_BetaOutput.setEnabled(True)
            self.checkBox_Beta.setEnabled(True)
            QMessageBox.about(self, '执行反馈', '执行成功！')
        except:
            QMessageBox.critical(self, '执行反馈', '执行失败！请确认后重试')
    
    @pyqtSlot()
    def on_pushButton_BetaOutput_clicked(self):
        file_output_path, filetype = QFileDialog.getSaveFileName(self, '选取文件夹', ".xlsx", "")
        file_output_path = file_output_path + '.xlsx'
        try:
            self.Beta.to_excel(file_output_path)
            QMessageBox.about(self, '执行反馈', '导出成功！')
        except:
            QMessageBox.critical(self, '执行反馈', '导出失败！请确认后重试')

    @pyqtSlot()
    def on_pushButton_MomentumCalculate_clicked(self):
        date = pd.to_datetime(self.lineEdit_Date.text())
        mom_rev = momentum_and_reverse_constract(self.dailyret)
        try:
            self.Momentum = mom_rev.get_mom_factor(date)
            self.pushButton_MomentumOutput.setEnabled(True)
            self.checkBox_Momentum.setEnabled(True)
            QMessageBox.about(self, '执行反馈', '执行成功！')
        except:
            QMessageBox.critical(self, '执行反馈', '执行失败！请确认后重试')

    @pyqtSlot()
    def on_pushButton_MomentumOutput_clicked(self):
        file_output_path, filetype = QFileDialog.getSaveFileName(self, '选取文件夹', ".xlsx", "")
        file_output_path = file_output_path + '.xlsx'
        try:
            self.Momentum.to_excel(file_output_path)
            QMessageBox.about(self, '执行反馈', '导出成功！')
        except:
            QMessageBox.critical(self, '执行反馈', '导出失败！请确认后重试')

    @pyqtSlot()
    def on_pushButton_ReverseCalculate_clicked(self):
        date = pd.to_datetime(self.lineEdit_Date.text())
        mom_rev = momentum_and_reverse_constract(self.dailyret)
        try:
            self.Reverse = mom_rev.get_reverse_factor(date)
            self.pushButton_ReverseOutput.setEnabled(True)
            self.checkBox_Reverse.setEnabled(True)
            QMessageBox.about(self, '执行反馈', '执行成功！')
        except:
            QMessageBox.critical(self, '执行反馈', '执行失败！请确认后重试')

    @pyqtSlot()
    def on_pushButton_ReverseOutput_clicked(self):
        file_output_path, filetype = QFileDialog.getSaveFileName(self, '选取文件夹', ".xlsx", "")
        file_output_path = file_output_path + '.xlsx'
        try:
            self.Reverse.to_excel(file_output_path)
            QMessageBox.about(self, '执行反馈', '导出成功！')
        except:
            QMessageBox.critical(self, '执行反馈', '导出失败！请确认后重试')
    
    @pyqtSlot()
    def on_pushButton_BookValueInput_clicked(self):
        file_input_path, filetype = QFileDialog.getOpenFileName(self, '选取文件', "", "")
        try:
            self.bookvalue = pd.read_excel(file_input_path)
            self.lineEdit_BookValuePath.setText(str(file_input_path))
        except:
            pass
    
    @pyqtSlot()
    def on_pushButton_RptDateInput_clicked(self):
        file_input_path, filetype = QFileDialog.getOpenFileName(self, '选取文件', "", "")
        try:
            self.rptdate = pd.read_excel(file_input_path)
            self.lineEdit_RptDatePath.setText(str(file_input_path))
        except:
            pass
    
    @pyqtSlot()
    def on_pushButton_MonthlySizeInput_clicked(self):
        file_input_path, filetype = QFileDialog.getOpenFileName(self, '选取文件', "", "")
        try:
            self.monthlysize = pd.read_excel(file_input_path)
            self.lineEdit_MonthlySizePath.setText(str(file_input_path))
        except:
            pass
    
    @pyqtSlot()
    def on_pushButton_BPCalculate_clicked(self):
        efc = extract_financial_real_data(self.bookvalue, self.rptdate)
        try:
            self.BP = efc.get_bp_value(self.monthlysize)
            self.pushButton_BPOutput.setEnabled(True)
            QMessageBox.about(self, '执行反馈', '执行成功！')
        except:
            QMessageBox.critical(self, '执行反馈', '执行失败！请确认后重试')
    
    @pyqtSlot()
    def on_pushButton_BPOutput_clicked(self):
        file_output_path, filetype = QFileDialog.getSaveFileName(self, '选取文件夹', ".xlsx", "")
        file_output_path = file_output_path + '.xlsx'
        try:
            self.BP.to_excel(file_output_path)
            QMessageBox.about(self, '执行反馈', '导出成功！')
        except:
            QMessageBox.critical(self, '执行反馈', '导出失败！请确认后重试')

    @pyqtSlot()
    def on_pushButton_AnnaulEarningInput_clicked(self):
        file_input_path, filetype = QFileDialog.getOpenFileName(self, '选取文件', "", "")
        try:
            self.annaulearning = pd.read_excel(file_input_path)
            self.lineEdit_AnnualEarningPath.setText(str(file_input_path))
        except:
            pass
    
    @pyqtSlot()
    def on_pushButton_AnnaulProfitInput_clicked(self):
        file_input_path, filetype = QFileDialog.getOpenFileName(self, '选取文件', "", "")
        try:
            self.annaulprofit = pd.read_excel(file_input_path)
            self.lineEdit_AnnaulProfitPath.setText(str(file_input_path))
        except:
            pass

    @pyqtSlot()
    def on_pushButton_AnnualRptDateInput_clicked(self):
        file_input_path, filetype = QFileDialog.getOpenFileName(self, '选取文件', "", "")
        try:
            self.annaulrptdate = pd.read_excel(file_input_path)
            self.lineEdit_AnnaulRptDatePath.setText(str(file_input_path))
        except:
            pass

    @pyqtSlot()
    def on_pushButton_SeasonProfitGrowthInput_clicked(self):
        file_input_path, filetype = QFileDialog.getOpenFileName(self, '选取文件', "", "")
        try:
            self.seasonprofitgrowth = pd.read_excel(file_input_path)
            self.lineEdit_SeasonProfitGrowthPath.setText(str(file_input_path))
        except:
            pass

    @pyqtSlot()
    def on_pushButton_SeasonRptDateInput_clicked(self):
        file_input_path, filetype = QFileDialog.getOpenFileName(self, '选取文件', "", "")
        try:
            self.seasonrptdate = pd.read_excel(file_input_path)
            self.lineEdit_SeasonRptDatePath.setText(str(file_input_path))
        except:
            pass

    @pyqtSlot()
    def on_pushButton_GrowthCalculate_clicked(self):
        date = pd.to_datetime(self.lineEdit_Date.text())
        eg = extract_growthfactor(self.annaulearning, self.annaulprofit, self.annaulrptdate,
                                  self.seasonprofitgrowth, self.seasonrptdate)
        try:
            self.Growth = eg.get_growthfactor(date)
            self.pushButton_GrowthOutput.setEnabled(True)
            self.checkBox_Growth.setEnabled(True)
            QMessageBox.about(self, '执行反馈', '执行成功！')
        except:
            QMessageBox.critical(self, '执行反馈', '执行失败！请确认后重试')

    @pyqtSlot()
    def on_pushButton_GrowthOutput_clicked(self):
        file_output_path, filetype = QFileDialog.getSaveFileName(self, '选取文件夹', ".xlsx", "")
        file_output_path = file_output_path + '.xlsx'
        try:
            self.Growth.to_excel(file_output_path)
            QMessageBox.about(self, '执行反馈', '导出成功！')
        except:
            QMessageBox.critical(self, '执行反馈', '导出失败！请确认后重试')
    
    @pyqtSlot()
    def on_pushButton_DailyTurnoverInput_clicked(self):
        file_input_path, filetype = QFileDialog.getOpenFileName(self, '选取文件', "", "")
        try:
            self.dailyturnover = pd.read_excel(file_input_path)
            self.lineEdit_DailyTurnoverPath.setText(str(file_input_path))
        except:
            pass
    
    @pyqtSlot()
    def on_pushButton_LiquidityCalculate_clicked(self):
        date = pd.to_datetime(self.lineEdit_Date.text())
        dat = daily_average_turnover(self.dailyturnover)
        try:
            self.Liquidity = dat.get_20average_tu(date)
            self.pushButton_LiquidityOutput.setEnabled(True)
            self.checkBox_Liquidity.setEnabled(True)
            QMessageBox.about(self, '执行反馈', '执行成功！')
        except:
            QMessageBox.critical(self, '执行反馈', '执行失败！请确认后重试')

    @pyqtSlot()
    def on_pushButton_LiquidityOutput_clicked(self):
        file_output_path, filetype = QFileDialog.getSaveFileName(self, '选取文件夹', ".xlsx", "")
        file_output_path = file_output_path + '.xlsx'
        try:
            self.Liquidity.to_excel(file_output_path)
            QMessageBox.about(self, '执行反馈', '导出成功！')
        except:
            QMessageBox.critical(self, '执行反馈', '导出失败！请确认后重试')

    @pyqtSlot()
    def on_pushButton_DailySizeInput_clicked(self):
        file_input_path, filetype = QFileDialog.getOpenFileName(self, '选取文件', "", "")
        try:
            self.dailysize = pd.read_excel(file_input_path)
            self.lineEdit_DailySizePath.setText(str(file_input_path))
        except:
            pass
    
    @pyqtSlot()
    def on_pushButton_SizeCalculate_clicked(self):
        date = pd.to_datetime(self.lineEdit_Date.text())
        try:
            nls = nonlinersize_constract(self.dailysize).get_nonlinersize_and_lnsize_factor(date)
            self.NonLinearSize = nls['nonlinearsize']
            self.Lnsize = nls['lnsize']
            self.pushButton_NonlinearSizeOutput.setEnabled(True)
            self.pushButton_LnSizeOutput.setEnabled(True)
            self.checkBox_NonLinearSize.setEnabled(True)
            self.checkBox_Lnsize.setEnabled(True)
            QMessageBox.about(self, '执行反馈', '执行成功！')
        except:
            QMessageBox.critical(self, '执行反馈', '执行失败！请确认后重试')
    
    @pyqtSlot()
    def on_pushButton_NonlinearSizeOutput_clicked(self):
        file_output_path, filetype = QFileDialog.getSaveFileName(self, '选取文件夹', ".xlsx", "")
        file_output_path = file_output_path + '.xlsx'
        try:
            self.NonLinearSize.to_excel(file_output_path)
            QMessageBox.about(self, '执行反馈', '导出成功！')
        except:
            QMessageBox.critical(self, '执行反馈', '导出失败！请确认后重试')
    
    @pyqtSlot()
    def on_pushButton_LnSizeOutput_clicked(self):
        file_output_path, filetype = QFileDialog.getSaveFileName(self, '选取文件夹', ".xlsx", "")
        file_output_path = file_output_path + '.xlsx'
        try:
            self.Lnsize.to_excel(file_output_path)
            QMessageBox.about(self, '执行反馈', '导出成功！')
        except:
            QMessageBox.critical(self, '执行反馈', '导出失败！请确认后重试')

    @pyqtSlot()
    def on_pushButton_BooktoMarketInput_clicked(self):
        file_input_path, filetype = QFileDialog.getOpenFileName(self, '选取文件', "", "")
        try:
            self.booktomarket = pd.read_excel(file_input_path)
            self.lineEdit_BooktoMarketPath.setText(str(file_input_path))
        except:
            pass
    
    @pyqtSlot()
    def on_pushButton_RiskFreeInput_clicked(self):
        file_input_path, filetype = QFileDialog.getOpenFileName(self, '选取文件', "", "")
        try:
            self.riskfree = pd.read_excel(file_input_path)
            self.lineEdit_RiskFreePath.setText(str(file_input_path))
        except:
            pass

    @pyqtSlot()
    def on_pushButton_MonthlyReturnInput_clicked(self):
        file_input_path, filetype = QFileDialog.getOpenFileName(self, '选取文件', "", "")
        try:
            self.monthlyReturn = pd.read_excel(file_input_path)
            self.lineEdit_MonthlyReturnPath.setText(str(file_input_path))
        except:
            pass

    @pyqtSlot()
    def on_pushButton_ThreeFactorCalculate_clicked(self):
        tc = threefactor_constract(self.booktomarket, self.riskfree, self.monthlyReturn)
        try:
            self.ThreeFactor = tc.extract_3factor()
            self.pushButton_ThreeFactorOutput.setEnabled(True)
            QMessageBox.about(self, '执行反馈', '执行成功！')
        except:
            QMessageBox.critical(self, '执行反馈', '执行失败！请确认后重试')
    
    @pyqtSlot()
    def on_pushButton_ThreeFactorOutput_clicked(self):
        file_output_path, filetype = QFileDialog.getSaveFileName(self, '选取文件夹', ".xlsx", "")
        file_output_path = file_output_path + '.xlsx'
        try:
            self.ThreeFactor.to_excel(file_output_path)
            QMessageBox.about(self, '执行反馈', '导出成功！')
        except:
            QMessageBox.critical(self, '执行反馈', '导出失败！请确认后重试')
    
    @pyqtSlot()
    def on_pushButton_ThreeFactorInput_clicked(self):
        file_input_path, filetype = QFileDialog.getOpenFileName(self, '选取文件', "", "")
        try:
            self.tfcalcul = pd.read_excel(file_input_path)
            self.lineEdit_ThreeFactorPath.setText(str(file_input_path))
        except:
            pass
    
    @pyqtSlot()
    def on_pushButton_MonthlyretInput_clicked(self):
        file_input_path, filetype = QFileDialog.getOpenFileName(self, '选取文件', "", "")
        try:
            self.m_ret = pd.read_excel(file_input_path)
            self.lineEdit_MonthlyretPath.setText(str(file_input_path))
        except:
            pass
    
    @pyqtSlot()
    def on_pushButton_RsqureCalculate_clicked(self):
        date = pd.to_datetime(self.lineEdit_Date.text())
        etr = extract_threefactor_Rsqure(self.tfcalcul, self.m_ret)
        try:
            self.Rsqure = etr.get_Rsqure(date)
            self.pushButton_RsqureOutput.setEnabled(True)
            self.checkBox_Rsqure.setEnabled(True)
            QMessageBox.about(self, '执行反馈', '执行成功！')
        except:
            QMessageBox.critical(self, '执行反馈', '执行失败！请确认后重试')
    
    @pyqtSlot()
    def on_pushButton_RsqureOutput_clicked(self):
        file_output_path, filetype = QFileDialog.getSaveFileName(self, '选取文件夹', ".xlsx", "")
        file_output_path = file_output_path + '.xlsx'
        try:
            self.Rsqure.to_excel(file_output_path)
            QMessageBox.about(self, '执行反馈', '导出成功！')
        except:
            QMessageBox.critical(self, '执行反馈', '导出失败！请确认后重试')
    
    @pyqtSlot()
    def on_pushButton_FactorMerger_clicked(self):
        n = 0
        premergerdict = {}
        # 对复选框进行判断
        if self.checkBox_Beta.isChecked():
            n = n + 1
            premergerdict[self.checkBox_Beta.text()] = self.Beta
        if self.checkBox_Momentum.isChecked():
            n = n + 1
            premergerdict[self.checkBox_Momentum.text()] = self.Momentum
        if self.checkBox_Reverse.isChecked():
            n = n + 1
            premergerdict[self.checkBox_Reverse.text()] = self.Reverse
        if self.checkBox_Growth.isChecked():
            n = n + 1
            premergerdict[self.checkBox_Growth.text()] = self.Growth
        if self.checkBox_Liquidity.isChecked():
            n = n + 1
            premergerdict[self.checkBox_Liquidity.text()] = self.Liquidity
        if self.checkBox_NonLinearSize.isChecked():
            n = n + 1
            premergerdict[self.checkBox_NonLinearSize.text()] = self.NonLinearSize
        if self.checkBox_Lnsize.isChecked():
            n = n + 1
            premergerdict[self.checkBox_Lnsize.text()] = self.Lnsize
        if self.checkBox_Rsqure.isChecked():
            n = n + 1
            premergerdict[self.checkBox_Rsqure.text()] = self.Rsqure

        if n < 2 :
            QMessageBox.critical(self, '执行反馈', '请选择两个及以上因子数据进行合并！')
            n = 0
        else:
            try:
                diclist = list(premergerdict.keys())
                init_df = pd.merge(premergerdict[diclist[0]], premergerdict[diclist[1]], on='code', how='outer')
                init_df.rename(columns={init_df.columns[1]: diclist[0], init_df.columns[2]: diclist[1]}, inplace=True)

                if n > 2:
                    for i in diclist[2:]:
                        init_df = pd.merge(init_df, premergerdict[i], on='code', how='outer')
                        init_df.rename(columns={init_df.columns[-1]: i}, inplace=True)

                self.pushButton_IntergredFactorOutput.setEnabled(True)
                self.IntergredDF = init_df
                QMessageBox.about(self, '执行反馈', '合并成功!')
            except:
                QMessageBox.critical(self, '执行反馈', '合并失败！请确认后重试')
    
    @pyqtSlot()
    def on_pushButton_IntergredFactorOutput_clicked(self):
        date = self.lineEdit_Date.text()
        file_output_path, filetype = QFileDialog.getSaveFileName(self, '选取文件夹', ".xlsx", "")
        file_output_path = file_output_path + '_' + date + '.xlsx'
        try:
            self.IntergredDF.to_excel(file_output_path)
            QMessageBox.about(self, '执行反馈', '导出成功！')
        except:
            QMessageBox.critical(self, '执行反馈', '导出失败！请确认后重试')

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '确认', '确认退出吗', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ft = Action()
    ft.show()
    sys.exit(app.exec_())