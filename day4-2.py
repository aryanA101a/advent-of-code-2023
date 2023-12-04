with open("day4-2i", "r") as f:
    numberOfCopies={i+1:1 for i in range(218)}
    number = 0
    res = 0
    for line in f.readlines():

        points = 0
        w = True
        winning = set()
        for r in range(5, len(line)):
            c = line[r]
            if c == "|":
                w = False
            elif c.isnumeric():
                number = number*10+int(c)
                if (r == len(line)-1):
                    if number in winning:
                        points += 1

            elif (c == " " or c == "\n") and number != 0:
                if w:
                    winning.add(number)
                else:
                    if number in winning:
                        points += 1

                number = 0
            elif c == ":":
                cardNo=number
                number = 0
        for i in range(cardNo+1,cardNo+1+points):
            numberOfCopies[i]+=numberOfCopies[cardNo]
        res+=numberOfCopies[cardNo]
        
    print(res)
