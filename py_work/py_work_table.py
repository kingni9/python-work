
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

class AppToTable:
    def __init__(self, app_path, table_name):
        self.app_path = app_path
        self.table_name = table_name

def main():
    path_1 = "/Users/zhuangjt/Documents/logistics_tables.txt"
    path_2 = "/Users/zhuangjt/Documents/result.txt"

    logistics_tables = []
    app_to_tables = []

    with open(path_1, "r") as file:
        line = file.readline()
        while line:
            logistics_tables.append(line.strip())
            line = file.readline()

    with open(path_2, "r") as file:
        line = file.readline()
        while line:
            var_list = line.split(":")
            app_to_tables.append(AppToTable(var_list[0].strip(), var_list[1].strip()))

            line = file.readline()

    for table in tables:
        app_names = set()

        for app_to_table in app_to_tables:
            if table == app_to_table.table_name:
                app_names.add(parse_app_name(app_to_table.app_path))

        print_info(app_names, table)

def parse_app_name(app_path):
    return app_path.split("/")[3]

def print_info(app_names, table):
    app_names_str = ""
    if len(app_names) >= 0:
        for app_name in app_names:
            app_names_str += app_name + "/"

    app_names_str += ":" + table

    print(app_names_str)

def parser_line(path):
    with open(path, "r") as file:
        line = file.readline()

        while line:
            var_list = line.split(":")
            print(var_list[0].strip())

            line = file.readline()

# main()

parser_line("/Users/zhuangjt/Documents/outer_app_tables.txt")

