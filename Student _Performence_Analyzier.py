import pandas as pd

data = pd.read_csv("C:/Users/HP/Downloads/Codes/Learning/numpy_learning/Student Performence Analyzier/Students.csv")
data_dict = data.to_dict(orient="records")  
top = []
st = 0
for record in data_dict:
    print(f"Student {st+1} Name: {record['Name']}")
    subjects = ["Math", "Science", "English", "Computer"]
    marks = []
    st += 1
    for subject in subjects:
        mark = record.get(subject, 0)
        marks.append(mark)
        per = (mark / 100) * 100 
        print(f" Subject: {subject}  |  Marks: {mark}/100  |  Percentage: {per}%")
    total_marks = sum(marks)
    top.append(total_marks)
    total_per = (total_marks / 400) * 100
    print()
    if total_per >= 90:
        print(f"    Total Marks: {total_marks} |  Percentage: {total_per}%  | Grade: A")
        print("                    **Excellent Performance**                       ")
    elif 80 <= total_per <90:
        print(f"    Total Marks: {total_marks} |  Percentage: {total_per}%  | Grade: B")
        print("                      **Good Performance**                          ")
    elif 75 <= total_per < 80:
        print(f"    Total Marks: {total_marks} |  Percentage: {total_per}%  | Grade: C")
        print("                      **Fair Performance**                          ")    
    elif 70 <= total_per < 75:
        print(f"    Total Marks: {total_marks} |  Percentage: {total_per}%  | Grade: D")
        print("                      **Bad Performance**                 ")
    else: 
        print(f"    Total Marks: {total_marks} |  Percentage: {total_per}%  | Grade: F")
        print("                      **Poor Performance**              ")    
    print()

print("              *** Toppers *** ")
for i in range(3):
    maxim = max(top)     
    topper = top.index(maxim)
    top.remove(maxim)
    print(f"       Top mark {i+1}: {maxim} at index {topper}")
print()

    # For Subjects
subjects = ["Math", "Science", "English", "Computer"]
sub = []

for subject in subjects:
    subject_marks = data[subject]
    marks_list = subject_marks.to_list()
    total = sum(marks_list)
    sub.append(total)
print("              *** Subjects ***")
for i in range(4):
    high = max(sub)
    pers = (high / 9900) * 100
    index = sub.index(high)
    print(f"{subjects[index]} has highest total marks: {high} | Percentage : {pers}% ")
    sub[index] = -1


    






     