import os
import pymysql

# 统计项目涉及包裹表
tables = set()
exists_tables = set()
host = "192.168.0.211"
user_name = "ops"
user_password = "123"
link_db = "information_schema"
# 统计的数据库
query_db_name = "main"
# 扫描的本地应用目录
dir_paths = ["/Users/zhuangjt/Documents/gitResource/logistics-api", "/Users/zhuangjt/Documents/gitResource/logistics-service", "/Users/zhuangjt/Documents/gitResource/logistics-web"]
table_to_apps = []
total_tables_set = set()

class TableToApp:
    def __init__(self,table_name,app_name):
        self.table_name = table_name
        self.app_name = app_name


# 加载数据库所有表名称 -- 过滤非业务表
def load_tables():
    db = pymysql.connect(host,user_name,user_password,link_db)
    cursor = db.cursor()
    cursor.execute("select TABLE_NAME from `tables` where `TABLE_SCHEMA` = '" + query_db_name + "'"
                   "and TABLE_NAME not like '%_rbak%' "
                   "and TABLE_NAME not like '%copy%'"
                   "and TABLE_NAME not like '%20%'")

    for table in cursor.fetchall():
        tables.add(table[0])

    return tables

# 递归扫描目录 -- 非目录文件进行调用parse_table进行表解析 -- 只针对.java/.xml文件
def scan(inner_path):
    if os.path.isdir(inner_path):
            for file_name in os.listdir(inner_path):
                # 递归扫描
                scan(inner_path + os.path.sep + file_name)
    else:
        if inner_path.endswith(".java") or inner_path.endswith(".xml"):
                parse_table(inner_path)

# 扫描文件每一行(文件名包含关键字dao/provider/) -- 匹mapper配line是否包含tables中的表名
def parse_table(file_path):
    file_name = file_path[file_path.rindex("/") + 1 : len(file_path)]

    if validate_mapper(file_name):
        with open(file_path, "r") as file:
            line = file.readline()
            while line:
                for main_table in tables:
                    if line.__contains__(main_table):
                        exists_tables.add(main_table)
                        total_tables_set.add(main_table)

                line = file.readline()

def validate_mapper(file_name):
    return not file_name.lower().__contains__("dto") \
           or not file_name.lower().__contains__("entity") \
           or not file_name.lower().__contains__("controller") \
           or not file_name.lower().__contains__("service") \
           or not file_name.lower().__contains__("vo")


def print_exists_tables():
    print(len(exists_tables))
    for exists_table in exists_tables:
        print(exists_table)

def main():
    global table_to_apps

    load_tables()
    for dir_path in dir_paths:
        scan(dir_path)

    #     app_name = dir_path[dir_path.rindex("/") + 1:]
    #     for exists_table in exists_tables:
    #         table_to_apps.append(TableToApp(exists_table, app_name))
    #     exists_tables.clear()
    #
    # inner_tables = set()
    #
    # for tableToApp in table_to_apps:
    #     inner_tables.add(tableToApp.table_name)
    #
    # for table in inner_tables:
    #     app_names = ""
    #     for tableToApp in table_to_apps:
    #         if tableToApp.table_name == table:
    #             app_names += (tableToApp.app_name + "/")
    #
    #     print(table + ":" + app_names)
    dir_path[dir_path.rindex("/") + 1:]
    return total_tables_set

main()