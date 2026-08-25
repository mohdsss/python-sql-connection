import mysql.connector as con
from calculation import calc
class connect(calc):
    def __init__(self):
        self.conn=con.connect(host="localhost"
                             ,user="root"
                             , password="safan2008"
                             ,database="safan")
        self.cur=self.conn.cursor()
    def menu(self):
        print("1. Add New Sale")
        print("2. Delete Sale")
        print("3. Show sale(optional with name and id)")
        print("4. Max sale users")
        print("5. Min sale users")
        print("6. Average sale")
        print("7. Total sale")
        ch=int(input("Enter your Choice = "))
        return ch
    def get(self):
        username=str(input("enter your name = "))
        sale=int(input("enter your sale = "))
        city=str(input("enter your city = "))
        return [username,sale,city]


    def insertData(self,table, lst):
        query="insert into " + table + " set username='"  +lst[0]+"' ,sal='"+str(lst[1])+"',city='"+lst[2]+"'"
        self.cur.execute(query)
        self.conn.commit()

    def showData(self, data):
        for row in data:
            print(row[1] + "   " +str(row[2]) +"   " + row[3])

    def particulardata(self,table,name="",id=""):
        if(id=="" and name==""):
            query="select * from "+table
        elif(id!="" and name!=""):
            query="select * from "+table+" where id='"+str(id)+"' and username='"+name+"'"
        elif(id=="" and name!=""):
            query="select * from "+table+" where username='"+name+"'"
        else:
            query="select * from "+table+" where id="+str(id)
        self.cur.execute(query)  
        data=self.cur.fetchall()
        return data

    def __del__(self):
        self.conn.close()
    def delete(self):
        name=str(input("enter name to delete = "))
        query="delete from safan2 where username='"+name+"'"
        self.cur.execute(query)
        self.conn.commit()




        
        

