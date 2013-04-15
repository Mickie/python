def read_grades(file):

    line=file.readline()
    while line !="\n":
        line=file.readline()

    grades=[]
    line=file.readline()
    while line !="":
        grade=line[line.rfind(" ")+1:]
        grades.append(float(grade))
    
        line=file.readline()
    return (grades)

def count_number(grades):
    count_grade_number=[0]*11
    for grade in grades:
        grade_range=int(grade//10)
        count_grade_number[grade_range]=count_grade_number[grade_range]+1
    return count_grade_number
        
    
