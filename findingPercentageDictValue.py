if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    
selection = student_marks[query_name]

meanLst = sum(selection) / len (selection)
print(f"{meanLst:.2f}") # the formatting of 2 floating point numbers after decimal was useless i did it because hacker rank was expecting this 56.00 rather than 56.0 so bear with me
