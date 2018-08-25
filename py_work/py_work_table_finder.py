import os
import pymysql

# 统计项目涉及包裹表总记录数
tables = set()
exists_tables = set()


def load_tables():
    db = pymysql.connect("192.168.0.211","ops","123","information_schema")
    cursor = db.cursor()
    cursor.execute("select TABLE_NAME from `tables` where `TABLE_SCHEMA` = 'main' "
                   "and TABLE_NAME not like '%_rbak%' "
                   "and TABLE_NAME not like '%copy%'"
                   "and TABLE_NAME not like '%20%'")

    results = cursor.fetchall()

    for table in results:
        tables.add(table[0])

    main_tables_file_path = "/Users/zhuangjt/Documents/main_online_tables.txt"
    with open(main_tables_file_path, "r") as file:
        line = file.readline()
        while line:
            tables.add(line.strip())
            line = file.readline()

def scan(inner_path):
    if os.path.isdir(inner_path):
        for file_name in os.listdir(inner_path):
            # 递归扫描
            scan(inner_path + os.path.sep + file_name)
    else:
        if inner_path.endswith(".java") or inner_path.endswith(".xml"):
            parse_table(inner_path)

def parse_table(file_path):
    with open(file_path, "r") as file:
        line = file.readline()
        while line:
            for main_table in tables:
                if line.__contains__(main_table):
                    file_name = file_path[file_path.rindex("/") + 1 : len(file_path)]
                    if file_name.lower().__contains__("dao") or file_name.lower().__contains__("provider") or file_name.lower().__contains__("mapper"):
                        exists_tables.add(main_table)
                        # print(main_table + " --> " + file_name)

            line = file.readline()

def main():
    load_tables()
    dir_path = "/Users/zhuangjt/Documents/gitResource/logistics-api"
    scan(dir_path)

    for exists_table in exists_tables:
        print(exists_table)

main()