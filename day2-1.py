with open("day2-1i","r") as f:
    rl,gl,bl=12,13,14
    res=0
    for line in f.readlines():
        gameId=None
        l=5
        n=0
        for r in range(6,len(line)):
            c=line[r]
            if c==":":
                gameId=int(line[l:r])
            elif  c==" ":
                if line[l]==" ":
                    n=int(line[l+1:r])
                l=r
            elif c=="," or c==";" or c=="\n":
                color=line[l+1:r]
                l=r
                if color=="red":
                    # print(color,n,r)
                    if n>rl:
                        gameId=0
                        break
                elif color=="green":
                    if n>gl:
                        gameId=0
                        break
                elif color=="blue":
                    if n>bl:
                        gameId=0
                        break
        # print(rc,gc,bc)
        # print(gameId)
        res+=gameId
    print(res)

                


            
