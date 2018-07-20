#!/usr/bin/env python
# -*- coding:utf-8 -*-
# mr wang

import pymysql


def main():
    # 创建连接
    conn = pymysql.connect(host='localhost', user='root', password='mysql',
                           port = 3306, database='jing_dong', charset ='utf8')
    # 创建游标,默认获取得元组游标,查询得结果是以元组得形式呈现的
    cs1 = conn.cursor()
    # 接收用户输入得查询关键字
    key_name = input("请输入要查询的商品：")
    # sql = "select * from goods where name = '%s'"%key_name  # 拼写字符串得形式
    sql = "select * from goods WHERE  name = %s" # 参数占位符
    # key_name = 'or 1 or'
    # key_name = 'or 1=1 or'
    # where name ='%s'

    # 执行查询
    params = [key_name]

    affect_rows = cs1.execute(sql, params)
    print("影响的行数：", affect_rows)
    # 获取结果，抓取结果集中所有得数据，默认是从第一条开始
    # 元组来封装每一条记录
    result = cs1.fetchall()
    for items in result:
        print(items[1], items[4])


if __name__ == '__main__':
        main()