import psycopg2
import os
import time

pg_config = {"dbname": 'flying',
             "user": "postgres",
             "paswrd": "******",
             "host": "888.888.888.888",
             "post": 5432,
             "tbname": "Databases_monitoring"}


class PostgresExp(object):
    def __init__(self):
        self.connect()

    def connect(self):
        self.conn = psycopg2.connect(
            database=pg_config['dbname'],
            user=pg_config['user'],
            password=pg_config["paswrd"],
            host=pg_config["host"],
            port=pg_config["post"])
        self.cur = self.conn.cursor()

    # 获取全部数据
    def get_all(self, sql, args):
        self.cur.execute(sql, args)
        res = self.cur.fetchall()
        return res

    def get_all_noargs(self, sql):
        self.cur.execute(sql)
        res = self.cur.fetchall()
        return res

    # 添加  就是添加一次提交多次
    def add_mode(self, sql, args):
        self.cur.execute(sql, args)
        self.conn.commit()

    # 更新数据
    def upd_mode(self, sql, args):
        self.cur.execute(sql, args)
        self.conn.commit()

    # 关闭游标，释放资源
    def get_close(self):
        self.cur.close()
        self.conn.close()


class Monitoring(PostgresExp):
    def __init__(self):
        super().__init__()

    def select_sql(self, sql):
        """ 获取sql返回的信息 """
        res = self.get_all(sql=sql, args=[])
        # print(type(reportTime))
        self.get_close()
        return res

    def inster_ctrl_reportTime(self, select_sql, inster_sql):
        # pg_ctrl = PostgresExp()
        # pg_ctrl.connect()
        res = self.get_all(sql=select_sql, args=[])
        self.add_mode(sql=inster_sql, args=[res[0][0]])
        self.get_close()

    def inster_ctrl_dBList_and_dBName(self, select_sql, inster_sql):
        # pg_ctrl = PostgresExp()
        # pg_ctrl.connect()
        res = self.get_all(sql=select_sql, args=[])
        self.add_mode(sql=inster_sql, args=[res, res])
        self.get_close()

    def inster_ctrl_dBName(self, select_sql, inster_sql):
        # pg_ctrl = PostgresExp()
        # pg_ctrl.connect()
        res = self.get_all(sql=select_sql, args=[])
        self.add_mode(sql=inster_sql, args=[res])
        self.get_close()

    def inster_ctrl_dBMSName_dBVer(self, select_sql, inster_sql):
        # pg_ctrl = PostgresExp()
        # pg_ctrl.connect()
        res = self.get_all(sql=select_sql, args=[])
        self.add_mode(sql=inster_sql, args=[res, res, res[0]])
        self.get_close()

    def inster_ctrl_dBCreateTime(self, select_sql, inster_sql):
        # pg_ctrl = PostgresExp()
        # pg_ctrl.connect()
        res = self.get_all_noargs(sql=select_sql)  # 由于sql里带了占位符，所以取消了带参数的命令
        self.add_mode(sql=inster_sql, args=[res])
        self.get_close()

    def inster_ctrl_dBMacName(self, select_sql, inster_sql):
        # pg_ctrl = PostgresExp()
        # pg_ctrl.connect()
        res = self.get_all(sql=select_sql, args=[])
        self.add_mode(sql=inster_sql, args=[res[0]])
        self.get_close()

    def inster_ctrl_dBStartTime(self, select_sql, inster_sql):
        # pg_ctrl = PostgresExp()
        # pg_ctrl.connect()
        res = self.get_all(sql=select_sql, args=[])
        self.add_mode(sql=inster_sql, args=[res[0][0]])
        self.get_close()

    def inster_ctrl_dBAllUser(self, select_sql, inster_sql):
        # pg_ctrl = PostgresExp()
        # pg_ctrl.connect()
        res = self.get_all(sql=select_sql, args=[])
        self.add_mode(sql=inster_sql, args=[res])
        self.get_close()

    def inster_ctrl_userExpirdTime(self, select_sql, inster_sql):
        # pg_ctrl = PostgresExp()
        # pg_ctrl.connect()
        res = self.get_all(sql=select_sql, args=[])
        self.add_mode(sql=inster_sql, args=[res])
        self.get_close()

    def inster_ctrl_sysID(self, select_sql, inster_sql):
        # pg_ctrl = PostgresExp()
        # pg_ctrl.connect()
        res = self.get_all(sql=select_sql, args=[])
        self.add_mode(sql=inster_sql, args=[res[0]])
        self.get_close()

    def inster_ctrl_curUserConnects(self, select_sql, inster_sql):
        # pg_ctrl = PostgresExp()
        # pg_ctrl.connect()
        res = self.get_all(sql=select_sql, args=[])
        self.add_mode(sql=inster_sql, args=[res[0]])
        self.get_close()

    def inster_ctrl_permitMaxConnects_parConnects(self, select_sql, inster_sql):
        # pg_ctrl = PostgresExp()
        # pg_ctrl.connect()
        res = self.get_all(sql=select_sql, args=[])
        self.add_mode(sql=inster_sql, args=[res[0], res[0]])
        self.get_close()

    def inster_ctrl_totalConnects(self, select_sql, inster_sql):
        # pg_ctrl = PostgresExp()
        # pg_ctrl.connect()
        res = self.get_all(sql=select_sql, args=[])
        self.add_mode(sql=inster_sql, args=[res[0]])
        self.get_close()

    def inster_ctrl_activeConnects(self, select_sql, inster_sql):
        # pg_ctrl = PostgresExp()
        # pg_ctrl.connect()
        res = self.get_all(sql=select_sql, args=[])
        self.add_mode(sql=inster_sql, args=[res[0]])
        self.get_close()

    def inster_ctrl_dBSpace(self, select_sql, inster_sql):
        # pg_ctrl = PostgresExp()
        # pg_ctrl.connect()
        res = self.get_all(sql=select_sql, args=[])
        self.add_mode(sql=inster_sql, args=[res[0]])
        self.get_close()

    def inster_ctrl_cpu_cmd(self, select_cmd, mem_cmd, update_sql):
        r = os.popen(select_cmd)
        f = r.read().split("\n")
        pid_use_dict = {}
        cpu_use_list = []
        for i in f:
            if i:
                res = i.split(" ")
                cpu_use_list.append(res[1])
                pid_use_dict[res[1]] = res[0]  # 拼接使用率为key，pid为values的字典
        cpu_use_list.sort(reverse=True)  # 排序以降序
        cpu_max_use = cpu_use_list[0]  # CPU最大使用率
        max_pid = pid_use_dict[cpu_max_use]  # 最大的cpu使用率的pid
        cpu_use_num_list = []  # 列表中是字符串
        for num in cpu_use_list:
            cpu_use_num_list.append(float(num))
        cpu_s = sum(cpu_use_num_list)  # 间隔
        cpu_avg_use = sum(cpu_use_num_list) / len(cpu_use_list)  # cpu的平均使用率
        mem_r = os.popen(mem_cmd)
        mem_f = mem_r.read().split("\n")
        mem_use_list = []
        for mem_i in mem_f:
            if mem_i:
                res = mem_i.split(" ")
                mem_use_list.append(float(res[1]))
        mem_sun = sum(mem_use_list)  # 数据库内存使用之和
        # pg_ctrl = PostgresExp()
        # pg_ctrl.connect()
        self.add_mode(sql=update_sql, args=[max_pid, "node", cpu_s, cpu_avg_use, mem_sun])  # 这个位置的node是写死的
        self.get_close()

    def inster_ctrl_sysID_sysName_dBObj_userCreateTime(self, update_sql):
        # pg_ctrl = PostgresExp()
        # pg_ctrl.connect()
        self.add_mode(sql=update_sql, args=["-", "-", "-"])
        self.get_close()


def update_main(update_time):  # 更新20秒一次
    while True:
        try:
            Monitoring().inster_ctrl_cpu_cmd(select_cmd="pidstat | grep postgres | awk '{print $3,$7}'",
                                             mem_cmd="ps aux | grep postgres | awk '{print $2,$4}'",
                                             update_sql='UPDATE "public"."Database_monitoring" set "cpuMaxExe" = %s,"cpuMaxMacName"=%s,"cpuRatePerT"=%s,"cpuRate"=%s,"dBLoadMem"=%s WHERE id = 1;')
            Monitoring().inster_ctrl_curUserConnects(
                select_sql="select count(1) from pg_stat_activity where usename='postgres';",
                inster_sql='UPDATE "public"."Database_monitoring" set "curUserConnects" = %s WHERE id = 1;')  # 当前用户的连接数
        except Exception as e:
            print("错误信息：%s" % e)
        time.sleep(int(update_time))


def main(update_time):  # 更新60秒一次不太常变化的数据
    while True:
        try:
            Monitoring().inster_ctrl_reportTime(select_sql="select now();",
                                                inster_sql='UPDATE "public"."Database_monitoring" set "reportTime" = %s WHERE id = 1;')  # 更新数据上传时间
            Monitoring().inster_ctrl_dBList_and_dBName(select_sql="select oid,datname from pg_database;",
                                                       inster_sql='UPDATE "public"."Database_monitoring" set "dBList" = %s,"dBName" = %s WHERE id = 1;')  # 更新数据库列表和名称
            Monitoring().inster_ctrl_dBName(select_sql="select oid,datname from pg_database;",
                                            inster_sql='UPDATE "public"."Database_monitoring" set "dBName" = %s WHERE id = 1;')  # 更新数据库名字
            Monitoring().inster_ctrl_dBMSName_dBVer(select_sql="select version();",
                                                    inster_sql='UPDATE "public"."Database_monitoring" set "dBMSName" = %s,"dBVer"= %s,"sysName"=%s WHERE id = 1;')  # 数据库版本及产品名称
            Monitoring().inster_ctrl_dBCreateTime(
                select_sql="select datname,(pg_stat_file(format('%s/%s/PG_VERSION',case when spcname='pg_default' then 'base' else 'pg_tblspc/'||t2.oid||'/PG_11_201804061/' end,t1.oid))).*from pg_database t1,pg_tablespace t2 where t1.dattablespace=t2.oid;",
                inster_sql='UPDATE "public"."Database_monitoring" set "dBCreateTime" = %s WHERE id = 1;')  # 数据库创建时间
            Monitoring().inster_ctrl_dBMacName(select_sql="select inet_server_addr();",
                                               inster_sql='UPDATE "public"."Database_monitoring" set "dBMacName" = %s WHERE id = 1;')  # 数据库所在机器IP地址
            Monitoring().inster_ctrl_dBStartTime(select_sql="select pg_postmaster_start_time();",
                                                 inster_sql='UPDATE "public"."Database_monitoring" set "dBStartTime" = %s WHERE id = 1;')  # 数据库启动时间
            Monitoring().inster_ctrl_dBAllUser(select_sql="select rolname from pg_roles where rolname !~ '^pg_';",
                                               inster_sql='UPDATE "public"."Database_monitoring" set "dBAllUser" = %s WHERE id = 1;')  # 数据库所有用户
            Monitoring().inster_ctrl_userExpirdTime(
                select_sql="select rolname,rolvaliduntil from pg_roles where rolname !~ '^pg_';",
                inster_sql='UPDATE "public"."Database_monitoring" set "userExpirdTime" = %s WHERE id = 1;')  # 数据库用户过期时间

            Monitoring().inster_ctrl_permitMaxConnects_parConnects(select_sql="show max_connections;",
                                                                   inster_sql='UPDATE "public"."Database_monitoring" set "permitMaxConnects" = %s,"parConnects"=%s WHERE id = 1;')  # 数据库最大连接数
            Monitoring().inster_ctrl_totalConnects(select_sql="select count(1) from pg_stat_activity;",
                                                   inster_sql='UPDATE "public"."Database_monitoring" set "totalConnects" = %s WHERE id = 1;')  # 数据库最大连接数
            Monitoring().inster_ctrl_activeConnects(
                select_sql="select count(*) from pg_stat_activity where state='active';",
                inster_sql='UPDATE "public"."Database_monitoring" set "activeConnects" = %s WHERE id = 1;')  # 活动连接数
            Monitoring().inster_ctrl_dBSpace(select_sql="select pg_size_pretty(pg_database_size('postgres'));",
                                             inster_sql='UPDATE "public"."Database_monitoring" set "dBSpace" = %s WHERE id = 1;')  # 活动连接数

            Monitoring().inster_ctrl_sysID_sysName_dBObj_userCreateTime(
                update_sql='UPDATE "public"."Database_monitoring" set "userCreateTime"=%s,"dBObj"=%s,"dBConn"=%s WHERE id = 1;')
            Monitoring().inster_ctrl_sysID(select_sql="select uuid_generate_v1();",
                                           inster_sql='UPDATE "public"."Database_monitoring" set "sysID" = %s WHERE id = 1;')  # 查询uuid
        except Exception as e:
            print("错误信息：%s" % e)
        time.sleep(int(update_time))


if __name__ == '__main__':
    main(200)  # 不常更新数据
    update_main(20)  # 常更新数据
