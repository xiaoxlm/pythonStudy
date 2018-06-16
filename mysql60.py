import pymysql

connect = pymysql.connect(
    host = '127.0.0.1',
    user = 'root',
    password = 'root',
    db = 'lmtest',
    charset = 'utf8mb4',
)

cursor = connect.cursor()

# sql = 'create table book (id varchar(20) primary key, name varchar(20))'
#
# cursor.execute(sql)

# cursor.execute('insert into book (id, name) values (%s, %s)', ['1', 'jpm'])
#
# print(cursor.rowcount)
# #
# connect.commit() # 提交事务
# cursor.close()


# cursor.execute('select * from user')
# values = cursor.fetchall()
#
# for k, v in values:
#     print(k, v)
#
# # 关闭Cursor和Connection:
# cursor.close()
#
# connect.close()



# 执行INSERT等操作后要调用commit()提交事务；
#
# MySQL的SQL占位符是%s。