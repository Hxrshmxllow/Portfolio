import pandas as pd

def main():
    rows = getRows('GPA_Calculator/Soham-Gradebook.xlsx', 'Junior Year')
    totalpoints = 0.00
    totalclasses = 0
    classes = 0
    points = 0.00
    for row in rows:
        difficulty = row[0]
        grade = row[3]
        points += gradepoints(grade) + difficultypoints(difficulty)
        totalpoints += gradepoints(grade) + difficultypoints(difficulty)
        totalclasses += 1
        classes += 1
    juniorgpa = points/classes
    rows = getRows('GPA_Calculator/Soham-Gradebook.xlsx', 'Sophomore Year')
    classes = 0
    points = 0.00
    for row in rows:
        difficulty = row[0]
        grade = row[3]
        points += gradepoints(grade) + difficultypoints(difficulty)
        totalpoints += gradepoints(grade) + difficultypoints(difficulty)
        totalclasses += 1
        classes += 1
    sophomoregpa = points/classes
    rows = getRows('GPA_Calculator/Soham-Gradebook.xlsx', 'Freshmen Year')
    classes = 0
    points = 0.00
    for row in rows:
        difficulty = row[0]
        grade = row[3]
        points += gradepoints(grade) + difficultypoints(difficulty)
        totalpoints += gradepoints(grade) + difficultypoints(difficulty)
        totalclasses += 1
        classes += 1
    freshmengpa = points/classes
    print("Freshmen Gpa: " + str(freshmengpa))
    print("Sophomore Gpa: " + str(sophomoregpa))
    print("Junior Gpa: " + str(juniorgpa))
    finalgpa = totalpoints/totalclasses
    print("Final Gpa: " + str(finalgpa))



def getRows(excel_file, sheet_name, start_row = 1):
    excel_data = pd.read_excel(excel_file, sheet_name, header=None)
    #print(excel_data)
    size = excel_data.shape
    row_num = size[0]
    datax = []
    for i in range(start_row, row_num):
        data = excel_data.iloc[i].values.tolist()
        datax.append(data)
    return datax

def gradepoints(grade):
    point = 0.00
    if(grade == "A+"):
        point = (4.0)
    elif(grade == "A"):
        point = (4.0)
    elif(grade == "A-"):
        point = (3.7)
    elif(grade == "B+"):
        point = (3.3)
    elif(grade == "B"):
        point = (3.0)
    elif(grade == "B-"):
        point = (2.7)
    elif(grade == "C+"):
        point = (2.3)
    elif(grade == "C"):
        point = (2.0)
    elif(grade == "C-"):
        point = (1.7)
    elif(grade == "D+"):
        point = (1.3)
    elif(grade == "D"):
        point = (1.0)
    else:
        point = (0)
    return point

def difficultypoints(difficulty):
    point = 0.00
    if(difficulty == "AP"):
        point = 0.0
    elif(difficulty == "Honors"):
        point = 0.0
    else:
        point = 0
    return point

main()