#!/usr/bin/env python
# -*- coding:utf-8 -*-
# mr wang


import pymysql



def main():
    # 创建连接

    conn = pymysql.connect(host='localhost', user='root', password='mysql',
                           port = 3306, database='jing_dong', charset='utf8')
    # 创建游标，默默获取得元组游标,查询得结果是以元组得形式呈现的
    cs1 = conn.cursor()
    # 接受用户输入的查询关键字
    key_name = input("请输入要查询得商品名称：")
    # sql = "select * from goods where name rlike %s" # 使用正则
    sql = "select * from goods where name like %s"
    # 执行查询
    # params=[key_name]


    params = ['%%%s%%'%key_name]  # %笔记本% , 注意： % 需要转义,  _ 不需要转义
    affect_rows=cs1.execute(sql, params)
    print("影响得行数", affect_rows)

    # 获取结果，抓取结果集中所有数据,默认是从第一条开始
    # 元组来封装每一条记录
    result = cs1.fetchall()

    for item in result:
        print(item[1],item[4])


if __name__ == '__main__':
    main()