if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    tot_score = list(student_marks[query_name])    
per = sum(tot_score)/len(tot_score);
print("%.2f" % per); 
