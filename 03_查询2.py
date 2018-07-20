
import pymysql
def main():
    # 创建链接
    conn = pymysql.connect(host="localhost", user="root",
                           password="mysql", database="jing_dong",
                           port=3306,charset="utf8")
    # 创建游标,cursor=pymysql.cursors.DictCursor:取得字典游标,取得的结果以字典的形式呈现的
    cs1 = conn.cursor(cursor=pymysql.cursors.DictCursor)


    sql = "select * from goods"
    # 执行查询
    affect_rows = cs1.execute(sql)
    print("影响的行数：", affect_rows)
    # 获取结果,抓取结果集中得一条数据，默认是从第一条开始得
    # 一条记录封装在元组中
    item = cs1.fetchone()
    print(item)
    print("fetchone",item["name"], item["price"])
    # 获取结果，抓取结果集中所有得数据，默认是从第一条开始的
    # 元组来封装每一条记录
    result =cs1.fetchall()
    for item in result:
        print(item["name"], item["price"])



if __name__ == '__main__':
    main()
