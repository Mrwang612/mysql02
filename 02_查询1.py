
import pymysql
def main():
    # 创建链接
    conn = pymysql.connect(host="localhost", user="root",
                           password="mysql", database="jing_dong",
                           port=3306,charset="utf8")
    # 创建游标，默默获取的元组游标，查询的结果是以元组得形式呈现的
    cs1 = conn.cursor()

    sql = "select * from goods"
    # 执行查询
    affect_rows = cs1.execute(sql)
    print("影响的行数：", affect_rows)
    # 获取结果,抓取结果集中得一条数据，默认是从第一条开始得
    # 一条记录封装在元组中
    item = cs1.fetchone()
    print("fetchone",item[1], item[4])
    # 获取结果，抓取结果集中所有得数据，默认是从第一条开始的
    # 元组来封装每一条记录
    result =cs1.fetchall()
    for item in result:
        print(item[1], item[4])



if __name__ == '__main__':
    main()
