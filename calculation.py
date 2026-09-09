from Library import library
class calc(library):
    def menu(self):
            print("1. Add New Sale")
            print("2. Show sale(optional with name and id)")
            print("3. Delete Sale with name and id")
            print("4. Max sale users")
            print("5. Min sale users")
            print("6. Average sale")
            print("7. Total sale")
            ch=int(input("Enter your Choice = "))
            return ch
    def maxm(self,cur):
        query="select sal from safan2"
        cur.execute(query)
        data=cur.fetchall()
        values=[]
        for i in data:
            values.append(i[0])   
        maximum=max(values)    
        query="select * from safan2 where sal="+str(maximum)
        cur.execute(query)
        data=cur.fetchall()
        return data
    def minm(self,cur):
        query="select sal from safan2"
        cur.execute(query)
        data=cur.fetchall()
        value=[]
        for j in data:
            value.append(j[0])
        minimum=min(value)    
        query="select * from safan2 where sal="+str(minimum)
        cur.execute(query)
        data=cur.fetchall()
        return data
    def averagesale(self,cur):
        query="select sal from safan2"
        cur.execute(query)
        data=cur.fetchall()
        values=[]
        for i in data:
            values.append(i[0])
        average=sum(values)/len(values)
        return average
    def totalsale(self,cur):
        query="select sal from safan2"
        cur.execute(query)
        data=cur.fetchall()
        values=[]
        for i in data:
            values.append(i[0])

        total=sum(values)
        return total


    

