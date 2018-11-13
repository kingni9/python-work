# 解析入库冲红数据 #

insert_sql = "INSERT INTO tms_biz_place (id, biz_place_id, biz_place_name, biz_place_type, parent_id, active, create_time, update_time) VALUE "


def main(file_path):
    with open(file_path, "r") as file:
        line = file.readline()
        while line:
            global insert_sql
            print(insert_sql + parse_line(line))
            line = file.readline()


def parse_line(line):
    result = line.split("	")
    inner_sql = "( "
    for i in range(0, len(result)):
        if result[i].__contains__(":"):
            if i == len(result) - 1:
                inner_sql += "now()"
            else:
                inner_sql += "now(), "

            continue

        inner_sql += "\'" + result[i] + "\', "

    inner_sql += ");"
    return inner_sql


# parse_line(insert_sql)

main("/Users/zhuangjt/Documents/sql.txt")


