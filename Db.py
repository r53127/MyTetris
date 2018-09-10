import os
import pickle
import shelve
import sqlite3

from Player import GamePlayer


class Data():
    def loadData(self):
        pass

    def saveData(self):
        pass


class Database(Data):
    def __init__(self):
        self.initDB()

    def initDB(self):
        db_path = 'data/user_point.db'
        # 连接到SQLite数据库
        # 数据库文件是use_point.db
        # 如果文件不存在，会自动在当前目录创建:
        self.conn = sqlite3.connect(db_path)
        # 创建一个Cursor:
        self.cursor = self.conn.cursor()
        # 执行一条SQL语句，创建user表:AUTOINCREMENT类型必须是主键
        self.cursor.execute(
            r'CREATE TABLE IF NOT EXISTS user (userid INTEGER  primary key AUTOINCREMENT ,name varchar(10),score int,game_type int)')

    def insertDB(self, name, score, game_type):
        # 继续执行一条SQL语句，插入一条记录:
        insert_statement = r'insert into user (name,score,game_type) values (?,?,?)'
        self.conn.execute(insert_statement, (name, score, game_type))
        self.conn.commit()  # 修改类操作必须commit

    def queryDB_ByName(self, name=None):
        # 查询
        query_statement = r'select * from user where name=?'
        self.cursor.execute(query_statement, (name,))  ##注意加括号，表示这是一个元组
        return self.cursor.fetchall()

    def queryDB_ByField(self, field='name', fieldvalue=None):
        # 查询
        query_statement = r'select * from user where ' + str(field) + "='" + str(fieldvalue) + "'"
        self.cursor.execute(query_statement)

        return self.cursor.fetchall()

    def queryDB_ByFieldList(self, field='score', listNum=1):
        # 查询
        query_statement = r'select * from user order by ' + str(field) + ' DESC limit ' + str(listNum)
        self.cursor.execute(query_statement)  ##注意加括号，表示这是一个元组
        return self.cursor.fetchall()

    def closeDB(self):
        # 关闭Cursor:
        self.cursor.close()


class DataDisk(Data):
    def __init__(self):
        self.data_path='data\player.dat'

    #shelve是用key来访问的，使用起来和字典类似
    #可用shelf.get()默认返回None来检测空字典
    #shelve可以像字典一样同时操作多个名称的对象，但pickle只能同时操作一个对象
    def saveShelveData(self,player):
        with shelve.open(self.data_path) as sh:
            sh.writeback=True
            try:
                tmp=sh['datadisk']
            except BaseException as e:
                tmp=[]
                tmp.append(player)
                sh['datadisk']=tmp
            else:
                sh['datadisk'].append(player)

    def loadShelveData(self):
        with shelve.open(self.data_path) as sh:
            try:
                players=sh['datadisk']
            except:
                # QMessageBox.information(None, '提示', '请选择打印模板！')
                print('本地数据不存在！')
            else:
                return players

    # 必须以2进制打开文件，否则pickle无法将对象序列化只文件
    def savePickleData(self,player):
        if self.isFileExist(self.data_path)==1:
            with open(self.data_path, 'rb+') as f:
                fi = pickle.load(f)
                fi.append(player)
                f.seek(0)#把文件指针指到开头
                pickle.dump(fi, f)  # serialize and save object
        else:
            with open(self.data_path, 'wb') as f:
                pickle.dump([player], f)

    def loadPickleData(self):
        if self.isFileExist(self.data_path):
            with open(self.data_path, 'rb') as f:
                players = pickle.load(f)  # read file and build object
                return players

    def isFileExist(self,file_path):
        if os.path.exists(file_path):
            if os.path.getsize(file_path):
                return 1 #文件存在且不为空
            else:
                return 0  #文件存在且为空
        else:
            return -1 #文件不存在


if __name__ == '__main__':
    a = Database()
    # a.insertDB('a',3000,1)
    # a.insertDB('任坤', 100, 1)
    # a.insertDB('b', 600, 1)
    # a.insertDB('c', 900, 1)
    # a.insertDB('f', 260, 1)
    # a.queryDB_ByField('name', 'f')
    # a.closeDB()
    # open('data\player.dat', 'wb')
    # b=DataDisk()
    # p=GamePlayer('da',200)
    # b.savePickleData(p)
    # c=b.loadPickleData()
    # print(c)
    # for i in c:
    #     print(i.name,i.point)
    # shelve.open('data\player.dat')
    # b=DataDisk()
    # p=GamePlayer('da',200)
    # b.saveShelveData(p)
    # c=b.loadShelveData()
    # print(c)
    # for i in c:
    #     print(i.name,i.point)

