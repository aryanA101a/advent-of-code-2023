def parseNumber(idx:int,line:str)->int:
    while(idx-1>=0 and line[idx-1].isnumeric()):
        idx-=1
    number=0
    while(line[idx].isnumeric()):
        number=number*10+int(line[idx])
        idx+=1
    return number



with open("day3-2i", "r") as f:
    lines = f.readlines()
    res=0
    for lineIdx in range(len(lines)):
        line = lines[lineIdx]

        for cIdx in range(len(line)):
            c = line[cIdx]
            if c=="*":
                adjPartNumbers=set()

                #horizontal adj
                if(cIdx>0 and line[cIdx-1].isnumeric()):
                    adjPartNumbers.add(parseNumber(cIdx-1,line))
                if(cIdx<len(line) and line[cIdx+1].isnumeric()):
                    adjPartNumbers.add(parseNumber(cIdx+1,line))

                #vertical adj
                if (lineIdx-1 >= 0 and lines[lineIdx-1][cIdx].isnumeric()):
                    adjPartNumbers.add(parseNumber(cIdx,lines[lineIdx-1]))
                if (lineIdx+1 < len(lines) and lines[lineIdx+1][cIdx].isnumeric()):
                    adjPartNumbers.add(parseNumber(cIdx,lines[lineIdx+1]))

                #diagonal
                if (lineIdx-1 >= 0 and cIdx-1>=0 and lines[lineIdx-1][cIdx-1].isnumeric()):
                    adjPartNumbers.add(parseNumber(cIdx-1,lines[lineIdx-1]))
                if (lineIdx+1 < len(lines) and cIdx-1>=0 and lines[lineIdx+1][cIdx-1].isnumeric()):
                    adjPartNumbers.add(parseNumber(cIdx-1,lines[lineIdx+1]))
                if (lineIdx-1 >= 0 and cIdx+1<len(lines[lineIdx-1]) and lines[lineIdx-1][cIdx+1].isnumeric()):
                    adjPartNumbers.add(parseNumber(cIdx+1,lines[lineIdx-1]))
                if (lineIdx+1 < len(lines) and cIdx+1<len(lines[lineIdx+1]) and lines[lineIdx+1][cIdx+1].isnumeric()):
                    adjPartNumbers.add(parseNumber(cIdx+1,lines[lineIdx+1]))
                
                if len(adjPartNumbers)==2:
                    product=1
                    for n in adjPartNumbers:
                        product*=n
                    res+=product





            
    print(res)
