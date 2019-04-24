import pymysql
import time
import requests


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
    
      #首次使用时修改该数据库参数
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
    
#数据爬取类，可通过函数爬取所需数据
class API:
        # 自定义头部
        headers = {}
        # 传递参数
        keyvalue = {}
        
        def get_pop(self):
            # 目标网址
            url = 'http://data.stats.gov.cn/easyquery.htm'

            # 头部的填充
            self.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' \
                                'AppleWebKit/537.36 (KHTML, like Gecko)'\
                                'Chrome/68.0.3440.75 Safari/537.36'

            # 下面是参数的填充
            self.keyvalue['m'] = 'QueryData'
            self.keyvalue['dbcode'] = 'hgnd'
            self.keyvalue['rowcode'] = 'zb'
            self.keyvalue['colcode'] = 'sj'
            self.keyvalue['wds'] = '[]'
            #通过浏览器查阅
    
            self.keyvalue['dfwds'] = '[{"wdcode":"sj","valuecode":"LAST20"},{"wdcode":"zb","valuecode":"A0301"}]'
            self.keyvalue['k1'] = str(gettime())        
            # 发出请求，使用post方法，这里使用自定义的头部和参数
            r = requests.post(url, headers=self.headers, params=self.keyvalue)
            return r

        def get_gdp(self):
            # 目标网址
            url = 'http://data.stats.gov.cn/easyquery.htm'

            # 头部的填充
            self.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' \
                                'AppleWebKit/537.36 (KHTML, like Gecko)'\
                                'Chrome/68.0.3440.75 Safari/537.36'

            # 下面是参数的填充
            self.keyvalue['m'] = 'QueryData'
            self.keyvalue['dbcode'] = 'hgnd'
            self.keyvalue['rowcode'] = 'zb'
            self.keyvalue['colcode'] = 'sj'
            self.keyvalue['wds'] = '[]'
            #通过浏览器查阅
    
            self.keyvalue['dfwds'] = '[{"wdcode":"sj","valuecode":"LAST20"},{"wdcode":"zb","valuecode":"A0201"}]'
            self.keyvalue['k1'] = str(gettime())        
            # 发出请求，使用post方法，这里使用自定义的头部和参数
            r = requests.post(url, headers=self.headers, params=self.keyvalue)
            return r    