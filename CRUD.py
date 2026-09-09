from abc import abstractmethod

import mysql.connector

class myLib:
    def __init__(self):
        try:
            self.conn=mysql.connector.connect(host="localhost",
                                        user="root",
                                        password="safan2008",
                                        database="safan")
            self.curr=self.conn.cursor()
        except Exception as e:
            print("Error " + e)

    @abstractmethod
    def insert(self,table, mydic):
        pass

    
class library(myLib):
    def insert(self, table, mydic):
        try:    
            super().insert(table, mydic)
            query="insert into " +table + " set "
            for key,value in mydic.items(): 
                if(type(value)==int):   
                    query+= key + " = " + str(value) + ", "
                else:
                    query+= key + " = '" + value + "', "
            query=query[:len(query)-2]    
            self.curr.execute(query)
            self.conn.commit()
            return True
        except Exception as e:
            print("Error " + str(e))
            return False
        
    def getData(self):
        name=input("Enter a name :")
        sal=int(input("Enter a sale :"))
        city=input("Enter a City :")
        data={"username":name,"sal":sal,"city":city}
        return data

    def getdata(self,table,name="",id=""):
        try:
            if(id=="" and name==""):
                query="select * from "+table
            elif(id!="" and name!=""):
                query="select * from "+table+" where id='"+str(id)+"' and username='"+name+"'"
            elif(id=="" and name!=""):
                query="select * from "+table+" where username='"+name+"'"
            else:
                query="select * from "+table+" where id="+str(id)
            self.curr.execute(query)  
            data=self.curr.fetchall()
            return data
        except Exception as e:
            print("ERROR = "+str(e))
    def show(self,data):
        for i in data:
            print(i)        
    def delete(self,table,name="",id=""):
        try:

            if(id=="" and name==""):
                query="delete from "+table
            elif id!="" and name!="":
                query="delete from "+table+" where username='"+name+"' and id="+str(id)
            elif name!="" and id=="":
                query="delete from "+table+" where username='"+name+"'"
            else:
                query ="delete * from "+table+" where id= "+str(id)
            self.curr .execute(query)
            self.conn.commit() 
        except Exception as e:
            print("ERROR = ",e)


        
        

