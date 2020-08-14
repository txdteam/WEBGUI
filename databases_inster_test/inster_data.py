
import pymysql
# #

import psycopg2
import pandas as pd
import sys
import time
import multiprocessing
from io import StringIO
from functools import wraps


def func_timer(function):
    '''
    用装饰器实现函数计时
    :param function: 需要计时的函数
    :return: None
    '''

    @wraps(function)
    def function_timer(*args, **kwargs):
        print('[Function: {name} start...]'.format(name=function.__name__))
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print('[Function: {name} finished, spent time: {time:.2f}s]'.format(name=function.__name__, time=t1 - t0))
        return result

    return function_timer



def add_filed(num):
    fied1 = []
    for i in range(num):
        fied1.append(0)
    return fied1


def create_databases():
    sql = ""
    n = 200
    code_name = []
    for i in range(n):
        if i != n - 1:
            sql += "`f%s` float(255, 0)," % (i)
        else:
            sql += "`f%s` float(255, 0)" % (i)
        code_name.append("f%s" % i)
    #print(sql)
    create_sql = "CREATE TABLE `float_test3`(%s) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Compact;SET FOREIGN_KEY_CHECKS = 1;" % sql

    return code_name, create_sql


def create_data_fuction(num):
    code_name_list, create_sql = create_databases()
    fied1 = add_filed(num)
    data = {}
    for name in code_name_list:
        data[name] = fied1
    return data


# dataframe类型转换为IO缓冲区中的str类型

# @func_timer
def test(data):
    data1 = pd.DataFrame(data)
    output = StringIO()
    data1.to_csv(output, sep='\t', index=False, header=False)
    output1 = output.getvalue()
    conn = pymysql.connect('192.168.4.101', 'root', '111111', 'test')
    cur = conn.cursor()
    # conn = psycopg2.connect(host=host, port=port, dbname=dbname, user=user, password=password)
    # cur = conn.cursor()
    cur.copy_from(StringIO(output1), "float_test3")
    conn.commit()
    cur.close()
    conn.close()
    print('done')


@func_timer
def main(num):
    data = create_data_fuction(num)
    p1 = multiprocessing.Process(target=test, args=(data,))
    # p2 = multiprocessing.Process(target=test, args=(data,))
    # p3 = multiprocessing.Process(target=test, args=(data,))
    p1.start()
    # p2.start()
    # p3.start()
    # p3.join()
    p1.join()
    # p2.join()


if __name__ == '__main__':
    if sys.argv[1]:
        # print('目前线程数为1，单个进程插入数据等于%s,共插入数据%s'%(sys.argv[1],int(sys.argv[1])*3)
        print('插入:', int(sys.argv[1]) * 3)
        # add_filed(int(sys.argv[1]))
        main(int(sys.argv[1]))
    else:
        # add_filed(10000)
        main(10000)

