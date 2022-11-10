# -*- codeing = utf-8 -*-
# @Time : 2022/8/29 23:52
# @Author : H.T
# @File : fc.py
# @software : PyCharm


import pandas as pd
import numpy as np
import statsmodels.api as sm
import copy
import datetime

class beta_extract(object):
    def __init__(self, df):
        '''
        收益率为日度收益率模式，市场收益率采用中证全指，无风险利率采用GC007年化收益率对应的日度数据

        :param df: 格式采用第一列为日期列，格式为日期格式(‘date’)，第二列为日度无风险收益率-原始数据名称为gc007（‘riskfreeret’——GC007取wind时间序列中的收盘行情-均价），第三列为中证全指收益率('000985.CSI‘），往后是各公司日度收益率！！！!注意！！！计算所得公司个数直接与df中传入公司个数相等
        '''

        self.df = copy.deepcopy(df)
        self.df.insert(1, 'riskfreeret', self.df[self.df.columns[1]] / 365)
        self.df.drop([self.df.columns[2]], axis=1, inplace=True)

    def extract_beta_df(self, date):
        '''

        :param date: pd.to_datetime()格式的日期数据，输入日期，返回相应的beta值数组
        :return: 返回beta值，返回数据具体格式为code为第一列，第二列是以日期为列名的数据
        '''
        '''首先构造指数收益率权重'''
        w_0 = 0.5 ** (1 / 63)
        e = np.arange(0, 252)
        e = -e
        e.sort()
        e = -e
        weight = w_0 ** e

        beta_df = pd.DataFrame({'code': self.df.columns[3:]})
        beta_df[date] = 0.0 # 初始化数据容器

        for i in self.df.columns[3:]:
            cpslice = self.df.loc[:][['date', 'riskfreeret', '000985.CSI', i]]
            cpslice.replace(0.0, np.nan, inplace=True)
            cpslice.dropna(inplace=True)
            cpslice.reset_index(inplace=True)
            cpslice.drop(['index'], axis=1, inplace=True)
            cpslice['000985.CSI'] = cpslice['000985.CSI'] - cpslice['riskfreeret']
            cpslice[cpslice.columns[-1]] = cpslice[cpslice.columns[-1]] - cpslice['riskfreeret']
            datelens = len(cpslice.date)

            if datelens > 251:
                target_date = date
                dumy = 0
                main_index_list = cpslice[cpslice.date == target_date].index.to_list()
                while len(main_index_list) == 0 and dumy <= 30:
                    target_date = target_date - datetime.timedelta(1)
                    main_index_list = cpslice[cpslice.date == target_date].index.to_list()
                    dumy += 1
                if dumy > 30:
                    beta = np.nan
                else:
                    main_index = main_index_list[0]
                    prebeta = cpslice.loc[main_index-251 : main_index][['date', '000985.CSI', cpslice.columns[-1]]]
                    if len(prebeta) > 120:
                        s_weight = weight[252 - len(prebeta): ]
                        prebeta.loc[:]['000985.CSI'] = prebeta['000985.CSI'] * s_weight
                        prebeta.loc[:][prebeta.columns[-1]] = prebeta[prebeta.columns[-1]] * s_weight
                        x = prebeta['000985.CSI']
                        y = prebeta[prebeta.columns[-1]]
                        x = sm.add_constant(x)
                        est = sm.OLS(y, x, missing='drop')
                        model = est.fit()
                        beta = model.params['000985.CSI']
                    else:
                        beta = np.nan
                beta_df.loc[beta_df.code == i, date] = beta

        return beta_df

class extract_financial_real_data(object):
    def __init__(self, financialrptdata, rptdate):
        '''

        :param financialrptdata: 公司定期报告披露的数据，即是各年报、季报、中报的标准数据
        :param rptdate: wind下载的公司定期报告披露日数据，用以对比意图获取的真实数据日期

        注意财务报表报告期必须与定期报告实际披露日报告期相等同,而且尽量做到财务数据公司个数和报告日数据公司个数等同。
        此外，由于本次算法逻辑上只对比到rptdate中最远季度，若输入日期还是在最远季度财报公布日期之前，那算法即选择rptdate中的最远季度最为数据记录，
        所以本公式只适用于更新最新季度数据之用途，若需更新历史数据，则公式中的算法缘故，可能导致数据失真
        '''
        self.finrptdata = copy.deepcopy(financialrptdata)
        rptdate.replace(pd.NaT, pd.to_datetime('21221231'), inplace=True) #将空值替换成较大日期，以方面后期进行日期对比
        self.rptdate = copy.deepcopy(rptdate)

    def get_real_data(self, date):
        '''

        :param date: pd.to_datetime()格式下的日期格式，此输入值代表真实需要获得的相应数据的日期
        :return: 返回真实日期所对应的在真实世界该日期下能获取到的最新财务数据（例如，若该日期为2022年4月30日，若该日期下该公司已经公布一季报数据则取一季报数据，若未公布，则取年报数据）
        '''
        acu_fin_df = pd.DataFrame({'code': self.finrptdata.code})
        acu_fin_df[date] = 0.0 # 构建相应的数据容器
        for i in self.finrptdata.code:
            index_list = self.rptdate[self.rptdate.code == i].index.to_list()
            if len(index_list) != 0:
                index = self.rptdate[self.rptdate.code == i].index.to_list()[0]
                col_ind = len(self.rptdate.columns) - 1
                bench_date = self.rptdate.loc[index][self.rptdate.columns[col_ind]]
                while date < bench_date and col_ind > 1: # 按照由近及远的方式逐日对比需求日期和报告期实际披露日，直至数据中最远季度
                    col_ind -= 1
                    bench_date = self.rptdate.loc[index][self.rptdate.columns[col_ind]]
                else:
                    bench_season = self.rptdate.columns[col_ind]
                    accurate_fin_data = self.finrptdata[self.finrptdata.code == i][bench_season].to_list()[0]
            else:
                accurate_fin_data = np.nan
            acu_fin_df.loc[acu_fin_df.code == i, date] = accurate_fin_data

        return acu_fin_df

    def get_bp_value(self, sizedf):
        '''

        :param sizedf: 传入数据格式为wind的excel插件中获取的总市值2(单一A股市值)的时间序列数据，最后得到的公司对应数据也以此df为基准，第一列为日期数据
        :return: 返回实际日期BP值

        注意，由于get_real_data中可以放入任意财务数据，所以，在BP值函数中务必确认初始化的是总资产数据，以及总市值数据
        '''
        bpdf = pd.DataFrame({'code': sizedf.columns[1:]}) #构造容器
        for i in sizedf.date:
            bookvalue = self.get_real_data(i)
            singel_size = sizedf[sizedf.date == i]
            singel_size = singel_size.T
            singel_size.drop('date', inplace=True)
            singel_size.insert(0, 'code', singel_size.index)
            pre_bp = pd.merge(bookvalue, singel_size, on='code', how='outer')
            pre_bp['bp'] = pre_bp[pre_bp.columns[1]] / pre_bp[pre_bp.columns[2]]
            bp_slice = pre_bp[['code', 'bp']]
            bpdf = bpdf.merge(bp_slice, on='code', how='outer')
            bpdf.rename(columns={'bp': i}, inplace=True)

        return bpdf

class extract_growthfactor(object):
    def __init__(self, annual_earning, annual_profit, annual_rpt_date, season_profit_grw, season_rpt_date):
        '''
        注意，所有传入的数据，财务数据的传入要求为所要获取的最近年份年报数据前推5年，例如，若现在要获取的增长率数据为2021年数据，那么至少要传入2017-2021年这5年的数据，而年报实际披露日期数据则只需要最近3年，既是2019-2021年

        :param annual_earning: wind下载的年报营业收入数据，格式为第一列日期，第二列开始是公司代码注意，传入数据必须大于或等于3年
        :param annual_profit: wind下载的年报净利润数据，格式为第一列日期，第二列开始是公司代码注意，传入数据必须大于或等于3年
        :param annual_rpt_date: wind下载的年报实际披露日期数据，格式为第一列为公司代码'code'，第二列开始为相应年份年报披露日，年份格式为“2005Q4，2006Q4”如此类推
        :param season_profit_grw: 季度净利润同比增速，wind下载，格式为第一列为公司代码'code'，第二列开始为相应季度净利润增速数据
        :param season_rpt_date: wind下载的季度报表实际披露日期数据，季度格式长短要与季度净利润增速保持一致
        '''
        self.earning = copy.deepcopy(annual_earning)
        self.profit = copy.deepcopy(annual_profit)
        self.annual_rpt_date = copy.deepcopy(annual_rpt_date)
        self.s_prt_grw = copy.deepcopy(season_profit_grw)
        self.s_rpt = copy.deepcopy(season_rpt_date)

    def __get_annual_gorwth__(self, raw_annual_df):
        '''
        函数目的，输入未经处理的，自wind下载的年报营业收入和净利润总额数据，注意初始化对象时传入数据必须大于或等于3年

        :param raw_annual_df: wind下载的年报收入和净利润总额数据，格式为第一列日期，第二列开始是公司代码，注意传入数据必须大于或等于3年
        :return: 返回经过3年回归后的平滑净利润或营业收入增长率数据
        '''
        fufill_df = pd.DataFrame({'date': raw_annual_df.date})  # 首先构建填充容器
        for i in raw_annual_df.columns[1:]:
            fufill_df[i] = 0.0
            slice = raw_annual_df.loc[:][['date', i]]
            slice.replace(np.nan, 0.0, inplace=True)
            for n in range(3, len(slice.date) + 1):
                y = slice[slice.columns[-1]][n - 3: n]
                if 0.0 not in list(y):
                    x = [1.0, 2.0, 3.0]
                    x = sm.add_constant(x)
                    est = sm.OLS(y, x, missing='drop')
                    model = est.fit()
                    coef = model.params['x1']
                    ann_gro = coef / y.mean()
                    date = slice.date[n - 1]
                    main_index = fufill_df[fufill_df.date == date].index.to_list()[0]
                    fufill_df.loc[main_index, i] = ann_gro
                else:
                    pass
        return fufill_df

    def get_accurate_growth(self, date):
        '''

        :param date: pd.to_datetime()格式的日期格式，输入日期，获得相应月份的真实回归平滑后的增长率数据
        :return: 获得相应月份的真实回归平滑后的增长率数据，字典格式
        '''
        ag_earning_gwt = self.__get_annual_gorwth__(self.earning)
        ag_profit_gwt = self.__get_annual_gorwth__(self.profit)

        ag_earning_gwt = ag_earning_gwt.T
        col_list = []
        for i in ag_earning_gwt.loc['date']:
            col_list.append(str(i.year) + 'Q4')
        ag_earning_gwt.columns = col_list
        ag_earning_gwt.insert(0, 'code', ag_earning_gwt.index)
        ag_earning_gwt.drop('date', inplace=True)
        ag_earning_gwt.reset_index(inplace=True)
        ag_earning_gwt.drop([ag_earning_gwt.columns[0], ag_earning_gwt.columns[2],
                             ag_earning_gwt.columns[3]], axis=1, inplace=True)

        ag_profit_gwt = ag_profit_gwt.T
        col_list = []
        for i in ag_profit_gwt.loc['date']:
            col_list.append(str(i.year) + 'Q4')
        ag_profit_gwt.columns = col_list
        ag_profit_gwt.insert(0, 'code', ag_profit_gwt.index)
        ag_profit_gwt.drop('date', inplace=True)
        ag_profit_gwt.reset_index(inplace=True)
        ag_profit_gwt.drop([ag_profit_gwt.columns[0], ag_profit_gwt.columns[2],
                            ag_profit_gwt.columns[3]], axis=1, inplace=True)

        # 以上两步对earning和profit的操作为整理相应回归后数据，以便后面匹配真实日期获得数据之用

        efr_earning = extract_financial_real_data(ag_earning_gwt, self.annual_rpt_date)
        accurate_ean_data = efr_earning.get_real_data(date)
        efr_profit = extract_financial_real_data(ag_profit_gwt, self.annual_rpt_date)
        accurate_prf_data = efr_profit.get_real_data(date)

        return {'an_earning_growth': accurate_ean_data, 'an_profit_growth': accurate_prf_data}

    def get_growthfactor(self, date):
        '''

        :param date: pd.to_datetime()格式的日期格式
        :return: 返回相应月份下【季度净利润同比0.7权重+3年回归净利润增速0.3权重+3年回归营收增速0.1权重】计算而得的Growth因子数据
        '''

        s_efr = extract_financial_real_data(self.s_prt_grw, self.s_rpt)
        real_prt = s_efr.get_real_data(date)
        accurate_gwt = self.get_accurate_growth(date)
        annual_earning = accurate_gwt['an_earning_growth']
        annual_profit = accurate_gwt['an_profit_growth']
        mm_pd = pd.merge(real_prt, annual_profit, on='code', how='outer')
        mm_pd = pd.merge(mm_pd, annual_earning, on='code', how='outer')
        mm_pd.replace(np.nan, 0.0, inplace=True)
        mm_pd['growth'] = (mm_pd[mm_pd.columns[1]] / 100) * 0.7 + mm_pd[mm_pd.columns[2]] * 0.2 + mm_pd[mm_pd.columns[3]] * 0.1
        mm_pd.drop([mm_pd.columns[1], mm_pd.columns[2], mm_pd.columns[3]], axis=1, inplace=True)
        mm_pd.rename(columns={'growth': date}, inplace=True)

        return mm_pd

class daily_average_turnover(object):
    def __init__(self, dailyturnover):
        '''

        :param dailyturnover: 从wind获取的日度交易日换手率数据，第一列为日期，第二列开始为公司代码
        '''
        self.dailyturnover = copy.deepcopy(dailyturnover)

    def get_20average_tu(self, date):
        '''

        :param date: pd.to_datetime()格式的日期，输入相应日期，即可返回相应前20日换手率
        :return: 返回对应日期的前20日换手率数据DataFrame，返回数据具体格式为code为第一列，第二列是以日期为列名的数据
        '''
        averagetu_df = pd.DataFrame({'code': self.dailyturnover.columns[1:]})
        averagetu_df[date] = 0.0 # 构建数据容器
        for i in self.dailyturnover.columns[1:]:
            target_date = date
            slice = self.dailyturnover.loc[:][['date', i]]
            slice.replace(0.0, np.nan, inplace=True)
            slice.dropna(inplace=True)
            if len(slice) >= 20:
                slice.reset_index(inplace=True)
                main_index_list = slice[slice.date == target_date].index.to_list()
                dumy = 0
                while len(main_index_list) == 0 and dumy <= 60:
                    target_date = target_date - datetime.timedelta(1)
                    main_index_list = slice[slice.date == date].index.to_list()
                    dumy += 1
                if dumy > 60:
                    avtu = np.nan
                else:
                    main_index = main_index_list[0]
                    temp = slice.loc[main_index - 19: main_index]
                    avtu = temp[i].mean()
                averagetu_df.loc[averagetu_df.code == i, date] = avtu

        return averagetu_df

class momentum_and_reverse_constract(object):
    def __init__(self, dailyret):
        '''

        :param dailyret: 沿用Beta值构建中所用到的日度股票涨跌幅数据表格，从第四列开始是公司代码，注意，这个数据表格中的日度涨跌幅数据是百分比数据，实际使用时需要除以100
        '''
        self.dailyret = copy.deepcopy(dailyret)

    def get_mom_factor(self, date):
        '''

        :param date: pd.to_datetime()格式日期，输入格式，返回相应momentum因子的值
        :return: 返回相应momentum因子的值，返回数据具体格式为code为第一列，第二列是以日期为列名的数据
        '''
        mom_df = pd.DataFrame({'code': self.dailyret.columns[3:]})
        mom_df[date] = 0.0 # 构建数据容器

        w_0 = 0.5 ** (1 / 126)
        e = np.arange(19, 260)
        e = -e
        e.sort()
        e = -e
        weight = w_0 ** e  # 构建指数半衰期权重序列

        for i in self.dailyret.columns[3: ]:
            target_date = date
            slice = self.dailyret.loc[:][['date', i]]
            slice.replace(0.0, np.nan, inplace=True)
            slice.dropna(inplace=True)
            if len(slice) > 281:
                slice.reset_index(inplace=True)
                main_index_list = slice[slice.date == target_date].index.to_list()
                dumy = 0
                while len(main_index_list) == 0 and dumy <= 60:
                    target_date = target_date - datetime.timedelta(1)
                    main_index_list = slice[slice.date == target_date].index.to_list()
                    dumy += 1
                if dumy > 60 :
                    momvalue = np.nan
                else:
                    main_index = main_index_list[0]
                    temp = slice.loc[main_index - 259: main_index - 19][['date', i]]
                    temp.loc[:][temp.columns[-1]] = temp[[temp.columns[-1]]] / 100
                    temp.loc[:][temp.columns[-1]] = temp[[temp.columns[-1]]] + 1
                    temp.loc[:][temp.columns[-1]] = np.log(temp[[temp.columns[-1]]])
                    temp.loc[:][temp.columns[-1]] = temp[temp.columns[-1]] * weight[241-len(temp):]
                    momvalue = temp[temp.columns[-1]].sum()
                mom_df.loc[mom_df.code == i, date] = momvalue

        return mom_df

    def get_reverse_factor(self, date):
        '''

        :param date: pd.to_datetime()格式日期，输入格式，返回相应因子的值
        :return: 返回数据具体格式为code为第一列，第二列是以日期为列名的数据
        '''
        reverse_20_df = pd.DataFrame({'code': self.dailyret.columns[3:]})
        reverse_20_df[date] = 0.0 # 构建容器

        for i in self.dailyret.columns[3:]:
            target_date = date
            slice = self.dailyret.loc[:][['date', i]]
            slice.replace(0.0, np.nan, inplace=True)
            slice.dropna(inplace=True)
            if len(slice) > 21:
                slice.reset_index(inplace=True)
                main_index_list = slice[slice.date == target_date].index.to_list()
                dumy = 0
                while len(main_index_list) == 0 and dumy <= 60:
                    target_date = target_date - datetime.timedelta(1)
                    main_index_list = slice[slice.date == target_date].index.to_list()
                    dumy += 1
                if dumy > 60:
                    tw_rev = np.nan
                else:
                    main_index = main_index_list[0]
                    temp = slice.loc[main_index - 19: main_index][['date', i]]
                    temp.loc[:][temp.columns[-1]] = temp[[temp.columns[-1]]] / 100
                    temp.loc[:][temp.columns[-1]] = temp[[temp.columns[-1]]] + 1
                    pre_tw_rev = np.product(temp[[temp.columns[-1]]]) - 1
                    tw_rev = pre_tw_rev[0]
                reverse_20_df.loc[reverse_20_df.code == i, date] = tw_rev

        return reverse_20_df

class nonlinersize_constract(object):
    def __init__(self, sizedf):
        '''

        :param sizedf: 取wind中总市值2（单一A股市值）为标准，第一列为date（日度），第二列开始为公司代码
        '''
        self.sizedf = copy.deepcopy(sizedf)

    def get_nonlinersize_and_lnsize_factor(self, date):
        '''

        :param date: pd.to_datetime()格式的日期数据，输入数据，返回相应因子值
        :return: 返回数据为一个字典容器，里面包含非线性总市值（nonlinersize）和对数总市值（lnsize）两个因子数组，每个数组的具体格式为code为第一列，第二列是以日期为列名的数据
        '''
        nlsdf = pd.DataFrame({'code': self.sizedf.columns[1:]})
        nlsdf[date] = 0.0 # 首先构建容器_非线性市值

        lnsizedf = pd.DataFrame({'code': self.sizedf.columns[1:]})
        lnsizedf[date] = 0.0 # 构建容器_市值对数

        for i in self.sizedf.columns[1:]:
            target_date = date
            slice = self.sizedf.loc[:][['date', i]]
            slice.replace(0.0, np.nan, inplace=True)
            slice.dropna(inplace=True)
            if len(slice) > 252:
                slice.reset_index(inplace=True)
                main_index_list = slice[slice.date==target_date].index.to_list()
                dumy = 0
                while len(main_index_list) == 0 and dumy <= 60:
                    target_date = target_date - datetime.timedelta(1)
                    main_index_list = slice[slice.date == target_date].index.to_list()
                    dumy += 1
                if dumy > 60:
                    nlsvalue = np.nan
                    lnszvalue = np.nan
                else:
                    main_index = main_index_list[0]
                    temp = slice.loc[main_index - 251: main_index][['date', i]]
                    col_name = temp.columns[-1]
                    temp['s_log_size'] = temp[col_name] * np.log(temp[col_name])
                    temp['s_log_size_cube'] = temp[col_name] * (np.log(temp[col_name])) ** 3
                    x = temp['s_log_size_cube']
                    y = temp['s_log_size']
                    est = sm.OLS(y, x, missing='drop')
                    model = est.fit()
                    nlsvalue = np.mean(model.resid)
                    lnszvalue = np.log(list(temp[col_name])[-1])
                nlsdf.loc[nlsdf.code == i, date] = nlsvalue
                lnsizedf.loc[lnsizedf.code == i, date] = lnszvalue

        return {'nonlinearsize': nlsdf, 'lnsize': lnsizedf}

class threefactor_constract(object):
    def __init__(self, book_market_value_df, riskfree_ret, monthlyret):
        '''
        注意，所有与收益率有关的数据只能传入需要计算的T年5月-T+1年4月收益率数据

        :param book_market_value_df: 全市场个股市值及股票账面总资产数据，第一列为code，第二列为市值size（wind-总市值2数据），第三列为账面总资产数据；注意！因为三因子的计算要求，若要求第T年5月-T+1年4月三因子数据，则需要取T年5月1日（非交易日顺延）总市值数据，及T-1年年报披露总资产数据
        :param riskfree_ret: GC028的年化数据（例如，5月无风险收益率需要选择4月第一个交易日的GC028）
        :param monthlyret: 个股月度收益率数据，第一列为date，第二列开始为公司数据
        '''
        self.bmv = copy.deepcopy(book_market_value_df)
        self.riskfree = copy.deepcopy(riskfree_ret)
        self.monthlyret = copy.deepcopy(monthlyret)

    def __get_bm_size_rank__(self):
        '''

        :return: 返回个股带size和booktomarket分组标签的数组，同时保存市值数据以便后续使用
        '''
        c_bmv = copy.deepcopy(self.bmv)
        c_bmv.replace(0.0, np.nan, inplace=True)
        c_bmv.dropna(inplace=True)
        c_bmv['booktomarket'] = c_bmv[c_bmv.columns[-1]] / c_bmv[c_bmv.columns[1]]
        c_bmv['bm_rank'] = 'low'
        c_bmv['bm_rank'].mask(c_bmv['booktomarket'] > c_bmv['booktomarket'].quantile(0.3), 'medium', inplace=True)
        c_bmv['bm_rank'].mask(c_bmv['booktomarket'] > c_bmv['booktomarket'].quantile(0.7), 'high', inplace=True)
        c_bmv['size_rank'] = 'small'
        c_bmv['size_rank'].mask(c_bmv[c_bmv.columns[1]] > c_bmv[c_bmv.columns[1]].quantile(0.5), 'big', inplace=True)
        c_bmv.drop([c_bmv.columns[2], 'booktomarket'], axis=1, inplace=True)

        return c_bmv

    def extract_3factor(self):
        '''

        :return: 返回月度三因子marketret，smb，hml数据，注意，返回值是除以一百以后的数据，也就是需要乘以100%
        '''
        rank = self.__get_bm_size_rank__()
        tf_df = pd.DataFrame({'date': self.monthlyret.date})
        tf_df['riskfree'] = 0.0
        tf_df['marketret'] = 0.0
        tf_df['hml'] = 0.0
        tf_df['smb'] = 0.0 # 构建三因子容器
        for i in self.monthlyret.date:
            singel_ret = self.monthlyret.loc[self.monthlyret.date==i, :]
            singel_ret = singel_ret.T
            singel_ret.rename(columns={singel_ret.columns[0]: i}, inplace=True)
            singel_ret.insert(0, 'code', singel_ret.index)
            ret_merge = rank.merge(singel_ret, on='code', how='left')
            ret_merge['market_weight'] = ret_merge[ret_merge.columns[1]] / ret_merge[ret_merge.columns[1]].sum()
            market_ret = np.sum(ret_merge[i] * ret_merge['market_weight']) / 100  # 首先计算出市场收益率

            group = ret_merge.groupby(by=['bm_rank', 'size_rank'])
            group_sum = group[ret_merge.columns[1]].sum()
            g_df = pd.DataFrame(group_sum)
            g_df['ret'] = 0.0

            for n in group:
                g_name = n[0]
                g_data = n[1]
                g_data['group_weight'] = g_data[ret_merge.columns[1]] / group_sum[g_name]
                g_df.loc[g_name]['ret'] = np.sum(g_data['group_weight'] * g_data[i]) / 100

            hml = g_df.loc['high']['ret'].mean() - g_df.loc['low']['ret'].mean()
            small_mean = (g_df.loc['high', 'small']['ret'] + g_df.loc['medium', 'small']['ret'] +
                          g_df.loc['low', 'small']['ret']) / 3
            big_mean = (g_df.loc['high', 'big']['ret'] + g_df.loc['medium', 'big']['ret'] + g_df.loc['low', 'big'][
                'ret']) / 3
            smb = small_mean - big_mean

            riskfree = self.riskfree.loc[self.riskfree.date==i, self.riskfree.columns[1]] / 1200
            riskfree = list(riskfree)[0]

            tf_df.loc[tf_df.date == i, 'riskfree'] = riskfree
            tf_df.loc[tf_df.date == i, 'marketret'] = market_ret
            tf_df.loc[tf_df.date == i, 'hml'] = hml
            tf_df.loc[tf_df.date == i, 'smb'] = smb

        return tf_df

class extract_threefactor_Rsqure(object):
    def __init__(self, threefactordf, monthlyret):
        '''

        :param threefactordf: 传入已经计算好的三因子数据组，具体格式以上一个对象threefactor_constract中返回的为准，注意，在传入因子时间区间上，以所需计算月份的24个月以上数据为准，因为计算R方我们采用24期月度收益率进行回归
        :param monthlyret: 个股的月度收益率数据组，第一列为日期date，第二列开始为公司月度收益率
        '''
        self.tfdf = copy.deepcopy(threefactordf)
        self.monthlyret = copy.deepcopy(monthlyret)
        # 对个股月度收益率进行初始化，以使其与三因子单位相等
        self.monthlyret.loc[:, self.monthlyret.columns[1:]] = self.monthlyret.loc[:, self.monthlyret.columns[1:]] / 100

    def get_Rsqure(self, date):
        '''

        :param date: pd.to_datetime()格式的日期数据，输入数据，返回R方
        :return: 返回R方值，格式为第一列为code，第二列为以日期命名的R方值
        '''
        big_df = pd.merge(self.monthlyret, self.tfdf, on='date', how='right')
        rsdf = pd.DataFrame({'code': big_df.columns[1: -4]})
        rsdf[date] = 0.0
        for i in big_df.columns[1: -4]:
            colname = ['date', i]
            for n in self.tfdf.columns[1:]:
                colname.append(n)
            pregdf = big_df.loc[:][colname]
            pregdf.replace(0.0, np.nan, inplace=True)
            pregdf.dropna(inplace=True)
            pregdf.reset_index(inplace=True)
            pregdf.drop(['index'], axis=1, inplace=True)
            target_index_list = pregdf[pregdf.date == date].index.to_list()
            prlen = len(pregdf)
            if prlen >= 12 and len(target_index_list) > 0:
                target_index = pregdf[pregdf.date == date].index.to_list()[0]
                pgslice = pregdf.loc[target_index - 11: target_index][:]
                pgslice.insert(1, 'ex_companyret', pgslice[i] - pgslice[pgslice.columns[2]])
                pgslice.insert(4, 'ex_mktret', pgslice[pgslice.columns[4]] - pgslice[pgslice.columns[3]])
                y = pgslice[['ex_companyret']]
                x = pgslice[[pgslice.columns[4], pgslice.columns[6], pgslice.columns[7]]]
                x = sm.add_constant(x)
                est = sm.OLS(y, x, missing='drop')
                model = est.fit()
                rsquared = model.rsquared
            else:
                rsquared = np.nan
            rsdf.loc[rsdf.code == i, date] = rsquared

        return rsdf

def get_icvalue(monthlyret, factordf):
    '''
    注意，因为ic值采用皮尔森相关系数进行计算，所以当要计算T月的因子ic值时，需要传入T+1月的月收益率数据

    :param monthlyret: 具体格式为第一列为公司代码code，第二列为相应收益率的数据组（注意，数据组推荐用纯数字格式，不要百分比格式）
    :param factordf: 具体格式为第一列为公司代码code，第二列为相应因子取值（未进行任何标准化处理的纯原生数据）
    :return: 返回ic值——浮点数形式
    '''
    pre_ic = pd.merge(factordf, monthlyret, on='code', how='outer')
    pre_ic.replace(0.0, np.nan, inplace=True)
    pre_ic.dropna(inplace=True)
    covdf = pre_ic[pre_ic.columns[1:]].astype('float64').corr()
    icvalue = covdf.loc[pre_ic.columns[1], pre_ic.columns[2]]
    return icvalue

