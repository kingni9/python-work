import os


def main():
    path1 = "/Users/zhuangjt/Documents/outer_app_tables.txt"
    tables = set()
    with open(path1, "r") as file:
        line = file.readline()
        while line:
            var_list = line.split(":")
            if var_list[0]:
                tables.add(var_list[1].strip())
                # print(var_list[0] + ":" + var_list[1].strip())

            line = file.readline()

main()

