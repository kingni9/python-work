import os


def main():
    path1 = "/Users/zhuangjt/Documents/outer_app_tables.txt"

    with open(path1, "r") as file:
        line = file.readline()
        while line:
            var_list = line.split(":")
            if var_list[0]:
                print(var_list[0].strip())
            line = file.readline()

main()

