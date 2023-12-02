with open("d11i","r") as input:
    res=0
    for line in input.readlines():
        n1,n2=-1,-1
        
        for i in range(len(line)):
            x=line[i]
            if x.isnumeric():
                if n1<0:
                    n1=n2=int(x)
                else:
                    n2=int(x)
        res+=n1*10+n2

            
    print(res)
        
        
            

