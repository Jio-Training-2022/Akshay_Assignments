if __name__ == '__main__':
    rs=[]
    scr=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        rs+=[[name, score]]
        scr+=[score]
    sorted_list=sorted(list(set(scr)))[1]
    for n,m in sorted(rs):
        if m==sorted_list:
            print(n)
