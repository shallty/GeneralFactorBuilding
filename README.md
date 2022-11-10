# GeneralFactorBuilding
利用python构建了一个小程序，以用于权益市场中根据MSCI-BARRA-USE4相关算法快速计算得出相应股票市场因子
现小程序为第一个成熟版本，其中还有部分UI设计存在明显缺陷，已知的问题是在分辨率设置较低情况下程序按钮名称显示不完全
此外，由于本程序主要针对wind数据格式进行设计，故导入数据也需根据此格式进行导入才能最终得出结果，具体数据格式请参考《业绩归因因子构建所需数据模版格式》
主要参考文献：
1. The Barra US Equity Model (USE4)
2. 20180410天风证券-金融工程：多因子模型的业绩归因评价体系
