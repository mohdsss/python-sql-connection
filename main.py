from CRUD import connect
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
    elif ch==4:
        print(obj.maxm(obj.cur))
    elif ch==5:
        print(obj.minm(obj.cur))  
    elif ch==6:
        print(obj.averagesale(obj.cur))
    elif ch==7:
        print(obj.totalsale(obj.cur))          
    else:
        print("!!!! Invalid choice !!!!")    