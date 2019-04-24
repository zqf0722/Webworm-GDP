from function import DB
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl


#设置字体，解决不支持中文的问题

mpl.rcParams['font.sans-serif']=['SimHei'] #指定默认字体 SimHei为黑体
mpl.rcParams['axes.unicode_minus']=False #用来正常显示负号



def draw_pop_bar():
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
    plt.figure(figsize=[16,8])
    plt.title("年末总人口")
    plt.ylabel("年末总人口（万人）")
    plt.xlabel("年份")
    plt.bar(X,num,width=0.5,color='red',tick_label=time)  
    for x,y in zip(X,num):
        plt.text(x,y+2000,'%d' %y, ha='center',va='bottom')
    plt.savefig('population_bar.jpg') 

def draw_pop_line():
    db=DB()
    db.connect()
    sql="select year from pop_tbl where title = '男性人口（万人）' "
    cursor=db.execute(sql)
    #储存
    TIME = cursor.fetchall()    
    #获取男性人口
    sql="select number from pop_tbl where title = '男性人口（万人）' "
    cursor=db.execute(sql)
    #储存
    NUM_M = cursor.fetchall()
    #获取女性人口
    sql="select number from pop_tbl where title = '女性人口（万人）' "
    
    cursor=db.execute(sql)
    #储存
    NUM_F = cursor.fetchall() 
    sql="select number from pop_tbl where title = '年末总人口（万人）' " 
    cursor=db.execute(sql)
    #储存
    NUM_ALL=cursor.fetchall()
    db.close()  
    #类型转换
    time=np.array(TIME)
    num_m=np.array(NUM_M)
    num_f=np.array(NUM_F)
    num_all=np.array(NUM_ALL)
    #提取
    time=time[:,0]
    num_m=num_m[:,0]
    num_f=num_f[:,0]
    num_all=num_all[:,0]
    #计算比率
    percent_m=np.true_divide(num_m,num_all)
    percent_f=np.true_divide(num_f,num_all)
    X=range(len(num_m))
    #绘图
    plt.figure(figsize=[14, 5])
    plt.plot(X,percent_m*100,color='red',marker='o',linewidth=2.5,label='男性人口占比')
    plt.plot(X,percent_f*100,color='blue',marker='o',linewidth=2.5,label='女性人口占比')
    plt.legend(loc='center')     
    plt.xticks(X,time)
    #标记
    plt.title('男女人口占比随时间变化图')
    plt.xlabel('年份')
    plt.ylabel('百分比')
    for x,y in zip(X,percent_m):
        plt.text(x,y*100-0.2,'%.2f' %(y*100) +'%', ha='center',va='bottom')   
    for x,y in zip(X,percent_f):
        plt.text(x,y*100+0.1,'%.2f' %(y*100) +'%', ha='center',va='bottom')          
    plt.savefig('population_ratio.jpg')  

def draw_gdp_bar():
    db=DB()
    db.connect()
    # 获取年份
    sql="select year from gdp_tbl where zb = '人均国内生产总值(元)' "
    cursor=db.execute(sql)
    #储存
    TIME = cursor.fetchall()
    db.close()
    db.connect()
    #获取数据
    sql="select number from gdp_tbl where zb = '人均国内生产总值(元)' "
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
    plt.figure(figsize=[16,8])
    plt.title("GDP")
    plt.ylabel("人均国内生产总值(元)")
    plt.xlabel("年份")
    plt.bar(X,num,width=0.5,color='red',tick_label=time)  
    for x,y in zip(X,num):
        plt.text(x,y+1500,'%.1f' %y, ha='center',va='bottom')
    plt.savefig('gdp_bar.jpg') 

def draw_gdp_pie():
    db=DB()
    db.connect()
    #获取数据
    sql="select number from gdp_tbl where zb = '国内生产总值（亿元）' AND year = '2018' "
    cursor=db.execute(sql)
    #储存
    money_all=cursor.fetchone()
    #获取数据
    sql="select number from gdp_tbl where zb = '第一产业增加值(亿元)' AND year = '2018' "
    cursor=db.execute(sql)
    #储存
    money_1=cursor.fetchone()         
    #获取数据
    sql="select number from gdp_tbl where zb = '第二产业增加值(亿元)' AND year = '2018' "
    cursor=db.execute(sql)
    #储存
    money_2=cursor.fetchone() 
    #获取数据
    sql="select number from gdp_tbl where zb = '第三产业增加值(亿元)' AND year = '2018' "
    cursor=db.execute(sql)
    #储存
    money_3=cursor.fetchone() 
    #类型转换
    money_all=np.array(money_all) 
    money_1=np.array(money_1)
    money_2=np.array(money_2)
    money_3=np.array(money_3)  
    sizes=np.append(money_1,money_2)
    sizes=np.append(sizes,money_3)
    colors=['gold','lightskyblue','lightcoral']
    explode = (0, 0, 0.1)
    labels='第一产业','第二产业','第三产业'
    # 饼状图
    plt.figure(figsize=[6, 6])
    plt.pie(sizes, 
            explode=explode,labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=100)
    
    plt.axis('equal')
    plt.savefig('gdp_pie.jpg')    
    
def draw_gdp_line():
    db=DB()
    db.connect()
    #获取数据
    sql="select year from gdp_tbl where zb = '国内生产总值（亿元）' "
    cursor=db.execute(sql)
    #储存
    time=cursor.fetchall()    
    #获取数据
    sql="select number from gdp_tbl where zb = '国内生产总值（亿元）' "
    cursor=db.execute(sql)
    #储存
    money_all=cursor.fetchall()
    #获取数据
    sql="select number from gdp_tbl where zb = '第一产业增加值(亿元)'  "
    cursor=db.execute(sql)
    #储存
    money_1=cursor.fetchall()         
    #获取数据
    sql="select number from gdp_tbl where zb = '第二产业增加值(亿元)' "
    cursor=db.execute(sql)
    #储存
    money_2=cursor.fetchall() 
    #获取数据
    sql="select number from gdp_tbl where zb = '第三产业增加值(亿元)' "
    cursor=db.execute(sql)
    #储存
    money_3=cursor.fetchall() 
    #类型转换
    time=np.array(time)
    money_all=np.array(money_all) 
    money_1=np.array(money_1)
    money_2=np.array(money_2)
    money_3=np.array(money_3) 
    time=time[:,0]
    money_all=money_all[:,0]   
    money_1=money_1[:,0] 
    money_2=money_2[:,0] 
    money_3=money_3[:,0]     
    #计算比率
    percent_1=np.true_divide(money_1,money_all)
    percent_2=np.true_divide(money_2,money_all)
    percent_3=np.true_divide(money_3,money_all)
    X=range(len(money_1))
    #绘图
    plt.figure(figsize=[14, 5])
    plt.plot(X,percent_1*100,color='red',marker='o',linewidth=2.5,label='第一产业占比')
    plt.plot(X,percent_2*100,color='blue',marker='o',linewidth=2.5,label='第二产业占比')
    plt.plot(X,percent_3*100,color='green',marker='o',linewidth=2.5,label='第三产业占比')
    plt.legend(loc='center')     
    plt.xticks(X,time)
    #标记
    plt.title('国民生产总值占比随时间变化图')
    plt.xlabel('年份')
    plt.ylabel('百分比')
    for x,y in zip(X,percent_1):
        plt.text(x,y*100+0.3,'%.2f' %(y*100) +'%', ha='center',va='bottom')   
    for x,y in zip(X,percent_2):
        plt.text(x,y*100+0.2,'%.2f' %(y*100) +'%', ha='center',va='bottom') 
    for x,y in zip(X,percent_3):
        plt.text(x,y*100+0.3,'%.2f' %(y*100) +'%', ha='center',va='bottom')         
    plt.savefig('gdp_ratio.jpg')  

    
    
    