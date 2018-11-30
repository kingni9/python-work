
tables = [
    'qp_freight_cal_record',
    'tms_transline_package_map',
    'tms_supplier_not_support_deliveryclasses',
    'pt_logistics_check',
    'tms_area_freight',
    'pt_ship_express',
    'pt_offline_order',
    'tms_carrier_delivery_detail',
    'qp_receiving_point',
    'h_pt_warehouse',
    'qp_deliveryorder',
    'tms_delivery_org_rel',
    'h_pt_time_address',
    'pt_offline_order_detail',
    'tms_randominspection_record',
    'pt_order_package_detail',
    'qp_parts_freight_by_weight',
    'tms_feedback_before_check',
    'qp_freight_cal_record_detail',
    'pt_offline_allocate_order',
    'pt_logistics_check_detail_backup',
    'qp_package_inbound',
    'pt_order_package',
    'tms_left_word',
    'pt_area_rule',
    'pt_time_address_carrier',
    'pt_address_config',
    'pt_dict_parts_city',
    'tms_warehouse_wms_mapping',
    'tms_randominspection_no_pass',
    'tms_carrier_delivery',
    'tms_batch',
    'tms_crm_partner_mapping',
    'tms_carrier_account_config',
    'pt_logistics_receipt_record',
    'tms_delivery_collection_package',
    'pt_order_package_detail_btl',
    'pt_principal',
    'tms_batch_package',
    'tms_intercept_cancel_record',
    'tms_orderdetail_timecost',
    'pt_ferry_subscribe',
    'tms_message_publish',
    'tms_receivingpoint_partner',
    'tms_biz_code_rule',
    'pt_carrier_cust',
    'pt_order_package_btl',
    'tms_carrier_dailylist_manual_detail',
    'pt_logistics_check_detail',
    'tms_transport_path',
    'pt_service_receive',
    'tms_supplier_partscity',
    'tms_timeaddress_servicereceive',
    'pt_order_map',
    'tms_delivery_order_package_detail',
    'h_pt_area_city',
    'pt_bd_position_supplier',
    'tms_transline_package',
    'pt_service_area',
    'pt_principal_biz_role',
    'pt_agent_express',
    'tms_carrier_check',
    'pt_offlineorder_expresspic',
    'pt_logisticsqrcode',
    'pt_ferry_subscribe_detail',
    'tms_transline_map',
    'pt_org_express',
    'pt_logisticscheck_pic',
    'tms_randominspection_config',
    'tms_carrier_dailylist',
    'pt_package_collection',
    'tms_order_detail_track2',
    'tms_transline_cost_record',
    'h_pt_area_rule',
    'qp_logistics_check_depart',
    'qp_parts_freight_by_volume',
    'pt_package_collection_detail',
    'tms_path_cost_record',
    'tms_message_reading_log',
    'tms_delivery_order_package',
    'tms_bookcase_record',
    'qp_order_partner',
    'qp_deliveryorder_detail',
    'tms_transport_path_map',
    'tms_batch_city',
    'qp_receiving_point_cover_place',
    'fin_carrier_daily_detail',
    'qp_fragile_tag',
    'qp_receiving_point_cover_org',
    'tms_order_detail_track_log2',
    'tms_vehicle',
    'tms_transline_time_deliveryclass',
    'pt_area_address',
    'pt_logistics_check_auto_confirm',
    'pt_logisticsqrcodedetail',
    'tms_supplier_warehouse_deliveryclass',
    'qp_reentry_goods'
]

class TableStatus:

    def __init__(self, table_name, status_1, status_2, status_3):
        self.table_name = table_name
        self.status_1 = status_1
        self.status_2 = status_2
        self.status_3 = status_3

def main():
    path_1 = "/Users/zhuangjt/Documents/tablesToApp.txt"
    path_2 = "/Users/zhuangjt/Documents/table_tag.txt"
    path_3 = "/Users/zhuangjt/Documents/tables.txt"

    with open(path_3, "r") as file:
        line = file.readline()
        while line:
            print(line[line.index(":")+1:].strip())
            # print(line[:line.index(':')].strip())
            # print(line[line.index(':') + 1:].strip())
            # var_list = line.split(":")
            # print(var_list[2])
            # tables.append(line[:line.index(':')].strip())
            # for table in tables:
            #     if line.__contains__(table):
            #         var_set.add(line.strip())
            #         break

            # print(tables)

            line = file.readline()


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


