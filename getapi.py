from function import DB,API

#为了避免每次主程序冗长的运行时间，将获取API独立出来作为一个函数，不必要时不使用


#创建搜索需要的字典
CLASS =['A030101','AO30102','A030103']
DICT = {'A030101':'年末总人口（万人）','A030102':'男性人口（万人）','A030103':'女性人口（万人）'}

def get_all():
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
        KINDS=DICT[KIND]
        #插入数据，重复数据不重复插入
        sql = "INSERT IGNORE INTO pop_tbl(title,year, number) VALUES ('%s','%s',%d)" %(KINDS,YEAR,NUM)
        db.execute(sql)
    db.close()