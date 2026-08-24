from query import connect
obj=connect()
while(True): 
    ch=obj.menu()   
    if ch==1:
        obj.insertData("safan2",obj.get())
    elif ch==2:
        data=obj.particulardata("safan2",str(input("Enter Name or leave blank = ")),str(input("Entere id or leave blank = "))) 
        obj.showData(data) 
    elif ch==3:
        obj.delete() 
    else:
        print("!!!! Invalid choice !!!!")    