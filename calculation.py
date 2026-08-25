class calc:
    def max(self,cur):
        query="select sale from safan2"
        cur.execute(query)
        max=0
        data=cur.fetchall()
        for i in data:
            if(i>max):
                max=i
        query="select * from safan2 where sale='"+max+"'"
        data=cur.fetchall()
        return data
    def min(self,cur):
        query="select sale from safan2"
        cur.execute(query)
        max=0
        data=cur.fetchall()
        for i in data:
            if(i<max):
                max=i
        query="select * from safan2 where sale='"+max+"'"
        data=cur.fetchall()
        return data
    def averagesale(self,cur):
        query="select sale from safan2"
        cur.execute(query)
        data=cur.fetchall()
        average=sum(data)/len(data)
        return average
    def totalsale(self,cur):
        query="select sale from safan2"
        cur.execute(query)
        data=cur.fetchall()
        total=sum(data)
        return total




    

