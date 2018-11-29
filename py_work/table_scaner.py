import os

tables = [
    'pt_address_config',
    'pt_logistics_check',
    'pt_logistics_receipt_record',
    'tms_transport_path',
    'qp_package_inbound',
    'qp_order_partner',
    'pt_logistics_check_detail',
    'tms_vehicle',
    'tms_carrier_delivery_detail',
    'pt_order_package_btl',
    'pt_dict_parts_city',
    'tms_batch_city',
    'fin_carrier_daily_detail',
    'tms_transline_cost_record',
    'qp_reentry_goods',
    'pt_order_package_detail_btl',
    'tms_supplier_warehouse_deliveryclass',
    'qp_receiving_point_cover_place',
    'tms_delivery_order_package_detail',
    'pt_offline_allocate_order',
    'tms_timeaddress_servicereceive',
    'h_pt_time_address',
    'tms_receivingpoint_partner',
    'tms_carrier_dailylist_manual_detail',
    'qp_freight_cal_record_detail',
    'tms_order_detail_track2',
    'tms_delivery_order_package',
    'pt_area_rule',
    'qp_fragile_tag',
    'pt_order_package_detail',
    'tms_biz_code_rule',
    'tms_delivery_collection_package',
    'tms_orderdetail_timecost',
    'tms_randominspection_record',
    'h_pt_warehouse',
    'qp_receiving_point_cover_org',
    'pt_offline_order_detail',
    'tms_batch_package',
    'tms_carrier_check',
    'qp_freight_cal_record',
    'pt_time_address_carrier',
    'pt_org_express',
    'pt_package_collection',
    'tms_carrier_delivery',
    'tms_left_word',
    'tms_crm_partner_mapping',
    'pt_service_receive',
    'tms_randominspection_config',
    'pt_agent_express',
    'pt_area_address',
    'h_pt_area_city',
    'pt_ferry_subscribe',
    'h_pt_area_rule',
    'tms_transline_package',
    'tms_feedback_before_check',
    'pt_principal_biz_role',
    'pt_carrier_cust',
    'qp_parts_freight_by_volume',
    'tms_message_reading_log',
    'tms_transport_path_map',
    'pt_offlineorder_expresspic',
    'tms_warehouse_wms_mapping',
    'tms_carrier_dailylist',
    'tms_carrier_account_config',
    'tms_bookcase_record',
    'pt_order_map',
    'pt_package_collection_detail',
    'pt_ship_express',
    'qp_deliveryorder_detail',
    'tms_transline_time_deliveryclass',
    'qp_logistics_check_depart',
    'tms_order_detail_track_log2',
    'tms_message_publish',
    'tms_area_freight',
    'pt_principal',
    'pt_logisticsqrcode',
    'tms_path_cost_record',
    'tms_supplier_not_support_deliveryclasses',
    'pt_order_package',
    'qp_deliveryorder',
    'pt_ferry_subscribe_detail',
    'tms_transline_package_map',
    'pt_service_area',
    'qp_receiving_point',
    'pt_offline_order',
    'pt_logistics_check_auto_confirm',
    'tms_randominspection_no_pass',
    'tms_transline_map',
    'qp_parts_freight_by_weight',
    'tms_batch',
    'tms_delivery_org_rel',
    'pt_bd_position_supplier',
    'pt_logisticsqrcodedetail',
    'pt_logisticscheck_pic',
    'tms_intercept_cancel_record',
    'tms_supplier_partscity',
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

scan("/Users/zhuangjt/Documents/gitResource/other")
