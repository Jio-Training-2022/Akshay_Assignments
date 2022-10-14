if __name__ == '__main__':
    N = int(input())
    l=0
    li=[]
    while l< N:
        ops=input().split()
        
        if "insert" in ops:
            li.insert(int(ops[1]),int(ops[2]))
        elif "print" in ops:
            print(li)
        elif "remove" in ops:
            li.remove(int(ops[1]))
        elif "append" in ops:
            li.append(int(ops[1]))
        elif "sort" in ops:
            li.sort()
        elif "pop" in ops:
            li.pop()
        elif "reverse" in ops:
            li.reverse()
        else:
            continue
        l+=1
