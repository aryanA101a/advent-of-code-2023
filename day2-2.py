with open("day2-2i","r") as f:
    res=0
    for line in f.readlines():
        rc,gc,bc=0,0,0
        l=5
        n=0
        for r in range(6,len(line)):
            c=line[r]
             
            if  c==" ":
                if line[l]==" ":
                    n=int(line[l+1:r])
                l=r
            elif c=="," or c==";" or c=="\n":
                color=line[l+1:r]
                l=r
                if color=="red":
                    # print(color,n,r)
                    rc=max(rc,n)
                elif color=="green":
                    gc=max(gc,n)
                elif color=="blue":
                    bc=max(bc,n)
        # print(rc*gc*bc)
        res+=rc*gc*bc
    print(res)

                


            
