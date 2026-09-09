from calculation import calc
ob=calc()
while(True): 
    ch=ob.menu()   
    if ch==1:
        table=str(input("enter table name = "))
        ob.insert(table,ob.getData())
    elif ch==2:
        table=str(input("enter table name = "))
        name=str(input("enter namr or leave blank = "))
        id=input("enter id or leave blank = ")
        ob.show(ob.getdata(table,name,str(id)))

    elif ch==3:
        table=str(input("enter table name = "))
        name=str(input("enter namr or leave blank = "))
        id=input("enter id or leave blank = ")
        ob.delete(table,name,str(id))
    elif ch==4:
        print(ob.maxm(ob.curr))
    elif ch==5:
        print(ob.minm(ob.curr))  
    elif ch==6:
        print(ob.averagesale(ob.curr))
    elif ch==7:
        print(ob.totalsale(ob.curr))          
    else:
        print("!!!! Invalid choice !!!!")    