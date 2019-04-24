import drawmap

#需要时重新获取api
import getapi

#最大的保证主函数的简洁
#功能均在其他文件中实现

#如果为第一次使用此程序，请在function中自行修改数据库连接参数
#并使用下方注释掉的getall函数











if __name__ == '__main__':  
    #首次使用时请运行一次这条语句来获取数据
    #getapi.get_all()
    drawmap.draw_pop_bar()
    drawmap.draw_pop_line()
    drawmap.draw_gdp_bar()
    drawmap.draw_gdp_pie()
    drawmap.draw_gdp_line()
      