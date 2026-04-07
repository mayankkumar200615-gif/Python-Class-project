import pandas as pd
import matplotlib.pyplot as plt
import os

filename = "students_60_named.xlsx"

# ================= FILE CHECK =================
if not os.path.exists(filename):
    print("Excel file not found ❌")
    exit()


# ================= HELPER FUNCTIONS =================
def get_subject_columns(df):
    options = [
        ["Math", "English", "Science", "Computer", "SST", "Physics"],
        ["Math", "English", "Science", "Comp", "SST", "Phy"]
    ]
    for opt in options:
        if all(col in df.columns for col in opt):
            return opt
    return None


def get_attendance_columns(df):
    options = [
        ["Math_Att", "Eng_Att", "Sci_Att", "Comp_Att", "SST_Att", "Phy_Att"],
        ["Math_Att", "English_Att", "Science_Att", "Computer_Att", "SST_Att", "Physics_Att"]
    ]
    for opt in options:
        if all(col in df.columns for col in opt):
            return opt
    return None


# ================= ADD STUDENT =================
def add_student():
    df = pd.read_excel(filename)
    df.columns = df.columns.str.strip()

    try:
        name = input("Enter student name: ").strip()

        math = int(input("Math: "))
        english = int(input("English: "))
        science = int(input("Science: "))
        computer = int(input("Computer: "))
        sst = int(input("SST: "))
        physics = int(input("Physics: "))

        math_att = int(input("Math Att: "))
        eng_att = int(input("English Att: "))
        sci_att = int(input("Science Att: "))
        comp_att = int(input("Computer Att: "))
        sst_att = int(input("SST Att: "))
        phy_att = int(input("Physics Att: "))

        math_teacher = input("Math teacher: ")
        eng_teacher = input("English teacher: ")
        sci_teacher = input("Science teacher: ")
        comp_teacher = input("Computer teacher: ")
        sst_teacher = input("SST teacher: ")
        phy_teacher = input("Physics teacher: ")

    except:
        print("Invalid input ❌")
        return

    avg = (math + english + science + computer + sst + physics) / 6

    if avg >= 90:
        grade = "A+"
    elif avg >= 80:
        grade = "A"
    elif avg >= 70:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    else:
        grade = "D"

    new_student = {
        "Name": name,
        "Math": math,
        "English": english,
        "Science": science,
        "Computer": computer,
        "SST": sst,
        "Physics": physics,
        "Average": round(avg, 2),
        "Grade": grade,
        "Math_Att": math_att,
        "Eng_Att": eng_att,
        "Sci_Att": sci_att,
        "Comp_Att": comp_att,
        "SST_Att": sst_att,
        "Phy_Att": phy_att,
        "Math_Teacher": math_teacher,
        "Eng_Teacher": eng_teacher,
        "Sci_Teacher": sci_teacher,
        "Comp_Teacher": comp_teacher,
        "SST_Teacher": sst_teacher,
        "Phy_Teacher": phy_teacher
    }

    df = pd.concat([df, pd.DataFrame([new_student])], ignore_index=True)
    df.to_excel(filename, index=False)

    print("Student added successfully ✅")


# ================= VIEW =================
def view_students():
    df = pd.read_excel(filename)
    df.columns = df.columns.str.strip()

    print("\n===== Student Records 📊 =====\n")
    print(df)


# ================= ANALYZE =================
def analyze_data():
    df = pd.read_excel(filename)
    df.columns = df.columns.str.strip()

    print("\nStudents needing improvement 📉:")
    weak = df[df["Average"] < 75]

    for _, row in weak.iterrows():
        print(row["Name"], "-", row["Average"])

    att_cols = get_attendance_columns(df)
    subjects = get_subject_columns(df)

    if att_cols and subjects:
        for _, row in df.iterrows():
            for i in range(len(subjects)):
                if row[att_cols[i]] < 75:
                    print(row["Name"], "- Low attendance in", subjects[i])

    print("\nClass Average:", round(df["Average"].mean(), 2))

    topper = df.loc[df["Average"].idxmax()]
    print("Topper:", topper["Name"], "-", topper["Average"])


# ================= RANKING =================
def student_ranking():
    df = pd.read_excel(filename)
    df.columns = df.columns.str.strip()

    df = df.sort_values(by="Average", ascending=False)
    df["Rank"] = range(1, len(df) + 1)

    print("\n===== Ranking 🏆 =====\n")
    print(df[["Rank", "Name", "Average"]])


# ================= EXAM REPORT =================
def exam_report():
    df = pd.read_excel(filename)
    df.columns = df.columns.str.strip()

    print("Available names:", df["Name"].tolist())

    name = input("Enter student name: ")

    student = df[df["Name"].astype(str).str.strip().str.lower() == name.strip().lower()]

    if student.empty:
        print("Student not found ❌")
        return

    print("\n===== Exam Report 📄 =====")
    print(student.iloc[0])


# ================= RESULT GRAPH =================
def result_graph():
    df = pd.read_excel(filename)
    df.columns = df.columns.str.strip()

    print("Available names:", df["Name"].tolist())

    name = input("Enter student name: ")

    student = df[df["Name"].astype(str).str.strip().str.lower() == name.strip().lower()]

    if student.empty:
        print("Student not found ❌")
        return

    subjects = get_subject_columns(df)

    if subjects is None:
        print("Column error ❌")
        print(df.columns)
        return

    marks = student[subjects].iloc[0].values

    plt.figure()
    plt.bar(subjects, marks)
    plt.title("Marks Graph")
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.show()


# ================= ATTENDANCE GRAPH =================
def attendance_graph():
    df = pd.read_excel(filename)
    df.columns = df.columns.str.strip()

    print("Available names:", df["Name"].tolist())

    name = input("Enter student name: ")

    student = df[df["Name"].astype(str).str.strip().str.lower() == name.strip().lower()]

    if student.empty:
        print("Student not found ❌")
        return

    subjects = get_attendance_columns(df)

    if subjects is None:
        print("Column error ❌")
        print(df.columns)
        return

    attendance = student[subjects].iloc[0].values

    plt.figure()
    plt.plot(subjects, attendance)
    plt.title("Attendance Graph")
    plt.xlabel("Subjects")
    plt.ylabel("Attendance %")
    plt.show()


# ================= MENU =================
while True:
    print("\n===== Smart Academic System =====")
    print("1. Add Student")
    print("2. View Records")
    print("3. Analyze")
    print("4. Ranking")
    print("5. Exam Report")
    print("6. Marks Graph")
    print("7. Attendance Graph")
    print("8. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        analyze_data()
    elif choice == "4":
        student_ranking()
    elif choice == "5":
        exam_report()
    elif choice == "6":
        result_graph()
    elif choice == "7":
        attendance_graph()
    elif choice == "8":
        print("Closed ✅")
        break
    else:
        print("Invalid choice ❌")