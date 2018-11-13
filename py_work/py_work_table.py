
def main():
    tables = set()
    path_2 = "/Users/zhuangjt/Documents/not_confirm.txt"

    with open(path_2, "r") as file:
        line = file.readline()
        while line:
            tables.add(line.strip())
            line = file.readline()

    for table in tables:
        print(table)

main()


