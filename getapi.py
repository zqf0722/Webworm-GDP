from function import DB,API

#为了避免每次主程序冗长的运行时间，将获取API独立出来作为一个函数，不必要时不使用


#创建搜索需要的字典
DICT_pop = {'A030101':'年末总人口（万人）','A030102':'男性人口（万人）','A030103':'女性人口（万人）'}
DICT_gdp = {'A020101':'国民总收入（亿元）','A020102':'国内生产总值（亿元）','A020103':'第一产业增加值(亿元)','A020104':'第二产业增加值(亿元)','A020105':'第三产业增加值(亿元)','A020106':'人均国内生产总值(元)'}

def get_population():
#保存人口数据的部分    
    #连接数据库
    db = DB() 
    db.connect()
    #转换格式
    api=API()
    r=api.get_pop()
    #转换数据格式
    data=r.json()
    #数据提取并储存
    for i in range(0,60):
        NUM=data['returndata']['datanodes'][i]['data']['data']
        YEAR=data['returndata']['datanodes'][i]['wds'][1]['valuecode']
        KIND=data['returndata']['datanodes'][i]['wds'][0]['valuecode']
        KINDS=DICT_pop[KIND]
        #插入数据，重复数据不重复插入
        sql = "INSERT IGNORE INTO pop_tbl(title,year, number) VALUES ('%s','%s',%d)" %(KINDS,YEAR,NUM)
        db.execute(sql)
    db.close()    

def get_income():
    get_population()
#保存国民收入数据的部分
    #连接数据库
    db = DB() 
    db.connect()
    #转换格式
    api=API()
    r=api.get_gdp()
    #转换数据格式
    data=r.json()
    #数据提取并储存
    for i in range(20,120):
        NUM=data['returndata']['datanodes'][i]['data']['data']
        YEAR=data['returndata']['datanodes'][i]['wds'][1]['valuecode']
        KIND=data['returndata']['datanodes'][i]['wds'][0]['valuecode']
        KINDS=DICT_gdp[KIND]
        #插入数据，重复数据不重复插入
        sql = "INSERT IGNORE INTO gdp_tbl(zb,year, number) VALUES ('%s','%s',%f)" %(KINDS,YEAR,NUM)
        db.execute(sql)
    db.close()    

def get_all():
    get_population()
    get_income()
    
    
