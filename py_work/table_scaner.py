import os

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

# 递归扫描目录 -- 非目录文件进行调用parse_table进行表解析 -- 只针对.java/.xml文件
def scan(inner_path):
    # 忽略物流应用
    if inner_path.__contains__("logistics-service") \
            or inner_path.__contains__("logistics-api") \
            or inner_path.__contains__("logistics-web")\
            or inner_path.__contains__("tms-service"):
        return

    if os.path.isdir(inner_path):
        for file_name in os.listdir(inner_path):
            # 递归扫描
            scan(inner_path + os.path.sep + file_name)
    else:
        if inner_path.endswith(".java") or inner_path.endswith(".xml"):
            parse_table(inner_path)

# 扫描文件每一行(文件名包含关键字dao/provider/) -- 匹mapper配line是否包含tables中的表名
def parse_table(file_path):
    file_name = file_path[file_path.rindex("/") + 1 : len(file_path)]

    if validate_mapper(file_name):
        with open(file_path, "r") as file:
            line = file.readline()
            while line:
                for exists_table in tables:
                    if line.__contains__(exists_table):
                        print(file_path + ":" + exists_table)   #打印或输出到文件
                line = file.readline()

def validate_mapper(file_name):
    return not file_name.lower().__contains__("dto") \
           or not file_name.lower().__contains__("entity") \
           or not file_name.lower().__contains__("controller") \
           or not file_name.lower().__contains__("service") \
           or not file_name.lower().__contains__("vo")

scan("/Users/zhuangjt/Documents/gitResource/trade-service")
