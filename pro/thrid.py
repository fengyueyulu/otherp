import random
import pymysql

db = pymysql.connect(  # 赋值给 conn连接对象
            host='43.143.224.120',  # 本地回环地址
            port=3306,  # 默认端口
            user='orangepi',  # 用户名
            password='orangepi',  # 密码
            database='data',  # 连接数据库名称
            charset='utf8'  # 编码 不能写utf-8
        )
cur=db.cursor()
def gen(x):
    if x <= 0.4:
        return random.choice(
            ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'L', 'K', 'J', 'H', 'G', 'F', 'D', 'S', 'A', 'Z', 'X',
             'C', 'V', 'B', 'N', 'M'])
    elif x <= 0.8:
        return random.choice(
            ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'l', 'k', 'j', 'h', 'g', 'f', 'd', 's', 'a', 'z', 'x',
             'c', 'v', 'b', 'n', 'm'])
    else:
        return random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])
def con():
    a=['']*19
    for i in  range(19):
        x=random.random()
        if((i+1)%5!=0):
            a[i]=gen(x)
        else:
            a[i]='-'

    cur.execute("SELECT * FROM active")
    sql = "INSERT INTO active(num) VALUES(%s)"
    a=''.join(a)
    cur.execute(sql, a)
    db.commit()
    return a


if __name__=='__main__':
    for i in range(200):
        print("".join(con()))
    cur.close()
    db.close()