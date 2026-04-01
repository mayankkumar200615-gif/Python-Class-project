import csv

filename = "students.csv"


# Function to add student data
def add_student():
    name = input("Enter student name: ")

    math = int(input("Enter Math marks: "))
    english = int(input("Enter English marks: "))
    science = int(input("Enter Science marks: "))

    avg = (math + english + science) / 3

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

    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, math, english, science, round(avg, 2), grade])

    print("Student record saved successfully ✅")


# Function to view all students
def view_students():
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)

            print("\nStudent Records Table 📊\n")
            print("Name\tMath\tEnglish\tScience\tAverage\tGrade")

            for row in reader:
                print("\t".join(row))

    except FileNotFoundError:
        print("No records found yet!")


# Function to analyze performance
def analyze_data():
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)

            highest_avg = 0
            topper = ""

            print("\nStudents needing improvement (Average < 75):")

            for row in reader:
                avg = float(row[4])

                if avg > highest_avg:
                    highest_avg = avg
                    topper = row[0]

                if avg < 75:
                    print(row[0], "-", avg)

            print("\nTop Performer 🏆:", topper, "-", highest_avg)

    except FileNotFoundError:
        print("No data available for analysis.")


# Main menu
while True:

    print("\n===== Academic Performance System =====")
    print("1. Add Student Record")
    print("2. View Student Records")
    print("3. Analyze Performance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        analyze_data()

    elif choice == "4":
        print("Program closed successfully 📁")
        break

    else:
        print("Invalid choice! Try again.")