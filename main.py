import time
import requests
import pymysql
#创建搜索
CLASS =['A030101','AO30102','A030103']
DICT = {'A030101':'年末总人口（万人）','A030102':'男性人口（万人）','A030103':'女性人口（万人）'}
#获取时间
ntime = int(round(time.time() * 1000))
# 用来获取 时间戳
def gettime():
    return int(round(time.time() * 1000))

#数据库操作类
class DB:  
  conn = None  
  cursor = None  
  #连接
  def connect(self):  
    self.conn = pymysql.connect("localhost", "root", "123456", "POP", charset='utf8' )
  #执行操作
  def execute(self, sql):  
    try:  
      cursor = self.conn.cursor()  
      cursor.execute(sql)  
    #报错重连
    except (AttributeError, pymysql.OperationalError):  
      self.connect()  
      cursor = self.conn.cursor()  
      cursor.execute(sql)  
    return cursor  
  #关闭
  def close(self):  
    if(self.cursor):  
      self.cursor.close()  
    self.conn.commit()  
    self.conn.close()  





if __name__ == '__main__':  
        #连接数据库
        db = DB()
       
        # 使用cursor()方法获取操作游标 

        # 自定义头部
        headers = {}
        # 传递参数
        keyvalue = {}
        # 目标网址
        url = 'http://data.stats.gov.cn/easyquery.htm'

        # 头部的填充
        headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' \
                                'AppleWebKit/537.36 (KHTML, like Gecko)'\
                                'Chrome/68.0.3440.75 Safari/537.36'

        # 下面是参数的填充
        keyvalue['m'] = 'QueryData'
        keyvalue['dbcode'] = 'hgnd'
        keyvalue['rowcode'] = 'zb'
        keyvalue['colcode'] = 'sj'
        keyvalue['wds'] = '[]'
        #通过浏览器查阅
    
        keyvalue['dfwds'] = '[{"wdcode":"sj","valuecode":"LAST20"},{"wdcode":"zb","valuecode":"A0301"}]'
        keyvalue['k1'] = str(gettime())

        # 发出请求，使用post方法，这里使用自定义的头部和参数
        r = requests.post(url, headers=headers, params=keyvalue)
        #转换格式
        data=r.json()
        for i in range(0,60):
            NUM=data['returndata']['datanodes'][i]['data']['data']
            YEAR=data['returndata']['datanodes'][i]['wds'][1]['valuecode']
            KIND=data['returndata']['datanodes'][i]['wds'][0]['valuecode']
            KINDS=DICT[KIND]
            res=KINDS+" "+YEAR+" "+":"+" "+"%d" %NUM
            sql = "INSERT IGNORE INTO pop_tbl(title,year, number) VALUES ('%s','%s',%d)" %(KINDS,YEAR,NUM)
                    
                    
            cursor=db.execute(sql)
            if i==0:
                text=res
            else:
                text=text+'\n'+res
        db.close()
      