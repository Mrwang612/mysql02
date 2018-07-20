#!/usr/bin/env python
# -*- coding:utf-8 -*-
# mr wang



import pymysql


def main():
    conn = pymysql.connect(host="localhost", user="root",
                           password="mysql", database="jing_dong",
                           port=3306,charset="utf8")
    cs1 = conn.cursor()

    # sql = "insert into goods_cates(name) values('穿戴设备')"
    # affect_rows = cs1.execute(sql)
    # print("影响得行数：",affect_rows)

    # sql = "update goods_cates set NAME ='手环' WHERE id= 9"
    # affect_rows = cs1.execute(sql)
    # print("影响的行数：",affect_rows)

    sql = "delete from goods_cates where id =10"
    affect_rows = cs1.execute(sql)
    print("影响行数：",affect_rows)


    conn.commit()
    if affect_rows==1:
        print("修改成功")
    else:
        print("修改失败")

    cs1.close()
    conn.close()


if __name__ == '__main__':
    main()

