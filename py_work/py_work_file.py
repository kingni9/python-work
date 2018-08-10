import os

# 统计项目涉及包裹表总记录数
files = set()
tbl_keys = ["btropen"]

def scan(inner_path):
    if os.path.isdir(inner_path):
        for file_name in os.listdir(inner_path):
            scan(inner_path + os.path.sep + file_name)

    else:
        # if inner_path.endswith(".java") or inner_path.endswith(".xml"):
        if inner_path.endswith("pom.xml"):
            parse(inner_path, tbl_keys)

def parse(file_path, keys):
    with open(file_path, "r") as file:
        line = file.readline()
        while line:
            for key in keys:
                if line.__contains__(key):
                    # files.add(file_path[file_path.rfind(os.path.sep) + 1:])
                    files.add(file_path)

            line = file.readline()

def main():
    dir_path = "/Users/zhuangjt/Documents/gitResource"

    scan(dir_path)

    if len(files) > 0:
        for file in files:
            print(file)

main()