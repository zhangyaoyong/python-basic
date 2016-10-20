#encoding=utf-8
import  MySQLdb

def mysqlQuery(sql, database="hotel_revenue"):
    '执行mysql查询操作'
    db=MySQLdb.connect(charset="utf8",host="localhost",user="root",passwd="root",db=database)
    cursor=db.cursor()
    cursor.execute(sql)
    rs=cursor.fetchall()
    return rs

def save2File(fileName, rs):
    '将结果集保存到文件'
    file=open(fileName,"w+")
    for r in rs:
        row=""
        for c in r:
            row=row+c+" "
        file.write(row + "\n")
    file.close()
def readFile(fileName):
    '从文件中读出内容'
    file=open(fileName, "r")
    return file.read()
rs=mysqlQuery("show tables")
file="/tmp/rs.txt"
save2File(file, rs)
print readFile(file)




