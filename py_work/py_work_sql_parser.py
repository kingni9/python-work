# 解析入库冲红数据 #

insert_sql = "INSERT INTO pt_logistics_receipt_record (recordId, packageDetailId, supplierId, supplierName, supplierType, orderId, orderNo, orderDetailId, inbDetailId, poNo, supplierOrderDetailId, saleType, partsCode, partsName, brandName, securityCode, purchasePrice, num, inbNum, isSend, createBy, createTime, updateBy, updateTime, repeatTime, partsBrandName, warehouseId, warehousePositionId, directType) VALUES ";


def main(file_path):
    with open(file_path, "r") as file:
        line = file.readline()
        while line:
            global insert_sql
            print(insert_sql + parse_line(line))
            line = file.readline()


def parse_line(line):
    result = line.split("	")
    inner_sql = "(null, "
    for i in range(0, len(result)):
        if i == 0:
            continue

        if i == (len(result) - 1):
            inner_sql += "2"
            continue
            
        if i == 16:
            inner_sql += "\'-" + result[i] + "\', "
            continue

        if i == 19:
            inner_sql += "0, "
            continue

        if result[i].strip() == "" or result[i].strip() == "None":
            inner_sql += "null, "
            continue

        if result[i].__contains__(":"):
            inner_sql += "now(), "
            continue

        inner_sql += "\'" + result[i] + "\', "

    inner_sql += ");"
    return inner_sql


# parse_line(insert_sql)

main("/Users/zhuangjt/Documents/logistis_record.txt")


