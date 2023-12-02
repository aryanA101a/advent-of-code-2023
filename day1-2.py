numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


class Trie:
    def __init__(self):
        self.children = [None]*26
        self.terminal = None

    def addWord(self, word: str):
        cur = self
        for c in word:
            if cur.children[ord(c)-ord("a")] is None:
                cur.children[ord(c)-ord("a")] = Trie()
            cur = cur.children[ord(c)-ord("a")]
        cur.terminal = word
    

def searchWord(idx:int,node:Trie,line:str):
    if(node.terminal !=None):
        return node.terminal
    if(idx>len(line)-1 or not line[idx].isalpha() or node.children[ord(line[idx])-ord("a")] is None):
        return None
    return searchWord(idx+1,node.children[ord(line[idx])-ord("a")],line)


trie=Trie()
for num in numbers.keys():
    trie.addWord(num)


with open("day1-2i", "r") as input:
    res = 0
    for line in input.readlines():
        n1, n2 = -1, -1

        for i in range(len(line)):
            x = line[i]
            if x.isnumeric():
                if n1 < 0:
                    n1 = n2 = int(x)
                else:
                    n2 = int(x)
            elif x.isalpha():
                word=searchWord(i,trie,line)
                if word != None:
                    if n1<0:
                        n1=numbers[word]
                    else:
                        n2=numbers[word]

        res += n1*10+n2

    print(res)

