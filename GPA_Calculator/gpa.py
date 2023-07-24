import pandas as pd

def main():
    rows = getRows('GPA_Calculator/Grades.xlsx', 'Junior Year')
    points = 0.00
    totalcredits = 0
    for row in rows:
        difficulty = row[0]
        credits = row[2]
        totalcredits += credits
        grade = row[3]
        points += (gradepoints(grade) + difficultypoints(difficulty))*credits
    juniorgpa = points/totalcredits
    rows = getRows('GPA_Calculator/Grades.xlsx', 'Sophomore Year')
    points = 0.00
    totalcredits = 0
    for row in rows:
        difficulty = row[0]
        credits = row[2]
        totalcredits += credits
        grade = row[3]
        points += (  points(grade) + difficultypoints(difficulty))*credits
        print(row[1] + ": " + str(gradepoints(grade) + difficultypoints(difficulty)))
    sophomoregpa = points/totalcredits
    rows = getRows('GPA_Calculator/Grades.xlsx', 'Freshmen Year')
    points = 0.00
    totalcredits = 0
    for row in rows:
        difficulty = row[0]
        credits = row[2]
        totalcredits += credits
        grade = row[3]
        points += (inflatedpoints(grade) + difficultypoints(difficulty))*credits
    freshmengpa = points/totalcredits
    finalgpa = (sophomoregpa + freshmengpa)/2.0
    print(juniorgpa)
    print(sophomoregpa)
    print(freshmengpa)
    print(finalgpa)

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

def inflatedpoints(grade):
    point = 0.00
    if(grade == "A+"):
        point = (4.67)
    elif(grade == "A"):
        point = (4.33)
    elif(grade == "A-"):
        point = (4.0)
    elif(grade == "B+"):
        point = (3.67)
    elif(grade == "B"):
        point = (3.33)
    elif(grade == "B-"):
        point = (3.00)
    elif(grade == "C+"):
        point = (2.67)
    elif(grade == "C"):
        point = (2.33)
    elif(grade == "C-"):
        point = (2.00)
    elif(grade == "D+"):
        point = (1.67)
    elif(grade == "D"):
        point = (1.33)
    else:
        point = (0)
    return point

def gradepoints(grade):
    point = 0.00
    if(grade == "A+"):
        point = (4.33)
    elif(grade == "A"):
        point = (4.0)
    elif(grade == "A-"):
        point = (3.67)
    elif(grade == "B+"):
        point = (3.33)
    elif(grade == "B"):
        point = (3.0)
    elif(grade == "B-"):
        point = (2.67)
    elif(grade == "C+"):
        point = (2.33)
    elif(grade == "C"):
        point = (2.0)
    elif(grade == "C-"):
        point = (1.67)
    elif(grade == "D+"):
        point = (1.33)
    elif(grade == "D"):
        point = (1.0)
    else:
        point = (0)
    return point

def difficultypoints(difficulty):
    point = 0.00
    if(difficulty == "AP"):
        point = 2
    elif(difficulty == "Honors"):
        point = 1
    else:
        point = 0
    return point

main()