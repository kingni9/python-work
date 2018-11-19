import os
from py_work import py_work_cat_fetch, py_work_table_finder

mapper_set = set()
tables_set = set()
exists_tables_set = set()
app_path = "/Users/zhuangjt/Documents/gitResource/logistics-service"

def init():
    global mapper_set, tables_set
    mapper_set = py_work_cat_fetch.fetch_data("logistics-service", "20181101", "20181201")
    tables_set = py_work_table_finder.load_tables()

# 递归扫描目录 -- 非目录文件进行调用parse_table进行表解析 -- 只针对.java/.xml文件
def scan(inner_path):
    if os.path.isdir(inner_path):
        for file_name in os.listdir(inner_path):
            # 递归扫描
            scan(inner_path + os.path.sep + file_name)
    else:
        if inner_path.endswith(".java") or inner_path.endswith(".xml"):
            parse_table(inner_path)

def parse_table(file_path):
    global exists_tables_set
    file_name = file_path[file_path.rindex("/") + 1 : len(file_path)]
    class_name = file_name[0:file_name.index(".")]
    for mapper in mapper_set:
        if not ("Test" in class_name) and (mapper in class_name):
            with open(file_path, "r") as file:
                line = file.readline()

                while line:
                    for main_table in tables_set:
                        if line.__contains__(main_table):
                            exists_tables_set.add(main_table)

                    line = file.readline()

def main():
    init()
    scan(app_path)
    print(len(exists_tables_set))
    print(exists_tables_set)

main()
