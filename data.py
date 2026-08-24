from query import connect
obj=connect()
name=str(input("enter name = "))
id=str(input("enter id = "))
data=obj.particulardata("safan2",name,id)
obj.showData(data)