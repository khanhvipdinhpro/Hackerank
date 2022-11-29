# Dictionary + Srting format
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    if n >=2 and n <= 10:
     for _ in range(n):
        a = 0
        b = 0
        c = 0
        name, *line = input().split()
        scores = list(map(float, line))
        if len(scores) == 3:
         for i in scores:
          if i  < 0 or i > 100:
            c = i
         if c  < 0 or c > 100: 
          pass
         else:
           for x in scores:
            b = a + x
            a = b            
           ave_scores = (b / len(scores))
           student_marks[name] = scores
           student_marks[name] = ave_scores
     query_name = input()
     query_ave = student_marks[query_name]
     lamtron = "{:.2f}"
     print(lamtron.format(query_ave))
