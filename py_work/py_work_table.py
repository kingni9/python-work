from py_work import py_work_table_finder
class TableStatus:

    def __init__(self, table_name, status_1, status_2, status_3):
        self.table_name = table_name
        self.status_1 = status_1
        self.status_2 = status_2
        self.status_3 = status_3

def main():
    tables = py_work_table_finder.main()
    tables_1 = set()

    path_1 = "/Users/zhuangjt/Documents/tablesToApp.txt"
    path_2 = "/Users/zhuangjt/Documents/table_tag.txt"
    path_3 = "/Users/zhuangjt/Documents/tables.txt"

    with open(path_1, "r") as file:
        line = file.readline()
        while line:
            tables_1.add(line[:line.index(':')].strip())
            # print(line[:line.index(':')].strip())
            # print(line[line.index(':') + 1:].strip())
            # var_list = line.split(":")
            # print(var_list[2])

            # tables.append(line[:line.index(':')].strip())

            # print(tables)

            line = file.readline()

    for table in tables:
        if not tables_1.__contains__(table):
            print(table)

    # table_status_list = []
    # with open(path_2, "r") as file:
    #     line = file.readline()
    #     while line:
    #         var_list = line.split(":")
    #         if len(var_list) > 0:
    #             table_name = ""
    #             status_1 = ""
    #             status_2 = ""
    #             status_3 = ""
    #
    #             for i in range(0, len(var_list)):
    #                 if i == 0:
    #                     table_name = var_list[i].strip()
    #                 if i == 1:
    #                     status_1 = var_list[1].strip()
    #                 if i == 2:
    #                     status_2 = var_list[2].strip()
    #                 if i == 3:
    #                     status_3 = var_list[3].strip()
    #
    #             table_status_list.append(TableStatus(table_name, status_1, status_2, status_3))
    #
    #         line = file.readline()
    #
    # for table in tables:
    #     for table_status in table_status_list:
    #         if table_status.table_name == table:
    #             print(table_status.table_name + ":" + table_status.status_1 + ':'+ table_status.status_2 + ':'+ table_status.status_3+ ':')
    # print(table_status_list)


main()


