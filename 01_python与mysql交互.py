


import pymysql


def main1():
    """
     host=None,
     user=None,
     password="",
     database=None,
     port=0,
     charset=''
    """
    # 1.通过connection创建链接
    conn = pymysql.connect(host="localhost", user="root",
                           password="mysql", database="jing_dong",
                           port=3306,charset="utf8")
    # 2.通过connection 对象创建游标
    cs1 = conn.cursor()
    # 3.通过游标执行sql语句（命令）
    sql = "select * from goods"
    cs1.execute(sql)
    # 4.通过游标获取结果
    result = cs1.fetchall()
    # 5.依据业务处理结果数据
    for item in result:
        print(item)
    # 6.关闭游标
    cs1.close()
    # 7.关闭连接
    conn.close()

if __name__ == '__main__':
    main1()