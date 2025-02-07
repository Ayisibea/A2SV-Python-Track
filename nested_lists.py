if __name__ == '__main__':
    student = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        n_student = [score,name]
        student.append(n_student)
    student.sort()
    low = student[0][0]

    for i in range(len(student)):
        if student[i][0] > low:
            low = student[i][0]
            break 
    for i in range(len(student)):
        if student[i][0] == low:
            print(student[i][1])
    
