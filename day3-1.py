#sliding window

def isSpecial(c: str):
    return not c.isnumeric() and not c.isalpha() and c!= "." and c!= "\n"


with open("day3-1i", "r") as f:
    lines = f.readlines()
    res=0
    for lineIdx in range(len(lines)):
        line = lines[lineIdx]
        l = 0

        isPartNo = False
        for r in range(len(line)):
            c = line[r]

            if c.isnumeric():
                #vertical adj
                if ((lineIdx-1 >= 0 and isSpecial(lines[lineIdx-1][r])) or (lineIdx+1 < len(lines) and isSpecial(lines[lineIdx+1][r]))):
                    isPartNo = True
                

            else:
                if (r-l > 1):
                    #horizontal adj
                    if ((not line[l].isnumeric() and isSpecial(line[l])) or (isSpecial(line[r]))):
                        isPartNo = True
                    #diagonal
                    if not line[l].isnumeric():
                        if ((lineIdx-1 >= 0 and isSpecial(lines[lineIdx-1][l])) or (lineIdx+1 < len(lines) and isSpecial(lines[lineIdx+1][l]))):
                            isPartNo = True
                    if ((lineIdx-1 >= 0 and isSpecial(lines[lineIdx-1][r])) or (lineIdx+1 < len(lines) and isSpecial(lines[lineIdx+1][r]))):
                        isPartNo = True
                    number = int(line[l:r]) if line[l].isnumeric() else int(
                        line[l+1:r])
                    
                    if(isPartNo):
                        res+=number
                l = r
                isPartNo = False
    print(res)
