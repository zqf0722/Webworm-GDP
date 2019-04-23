from function import DB
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl


#设置字体，解决不支持中文的问题

mpl.rcParams['font.sans-serif']=['SimHei'] #指定默认字体 SimHei为黑体
mpl.rcParams['axes.unicode_minus']=False #用来正常显示负号



def draw_bar():
    db=DB()
    db.connect()
    # 获取年份
    sql="select year from pop_tbl where title = '男性人口（万人）' "
    cursor=db.execute(sql)
    #储存
    TIME = cursor.fetchall()
    db.close()
    db.connect()
    #获取人口
    sql="select number from pop_tbl where title = '年末总人口（万人）' "
    cursor=db.execute(sql)
    #储存
    NUM = cursor.fetchall()
    #类型转换
    time=np.array(TIME)
    num=np.array(NUM)
    #提取数据
    time=time[:,0]
    num=num[:,0]
    db.close()
    X=range(len(num))
    for i in X:
        i=i*2
    plt.figure(figsize=[16,8])
    plt.title("年末总人口")
    plt.ylabel("年末总人口（万人）")
    plt.xlabel("年份")
    plt.bar(X,num,width=0.5,color='red',tick_label=time)  
    for x,y in zip(X,num):
        plt.text(x,y+2000,'%d' %y, ha='center',va='bottom')
    plt.savefig('population_bar.jpg') 

def draw_line():
    