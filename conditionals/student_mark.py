
# Find:
#  Average marks
#  Highest marks
#  Lowest marks
# Har student ke liye grade print karo:
# Marks	Grade
# 90+	A
# 75–89	B
# 50–74	C
# <50	Fail
def student_mark_analyzer():
    student_dict = {}
    markList = []

    # Input
    for i in range(5):
        student_name = input("Enter student name: ")
        student_mark = int(input("Enter student mark: "))
        student_dict[student_name] = student_mark
        markList.append(student_mark)

    # Calculations
    total_mark = sum(markList)
    avg = total_mark / len(markList)
    highest = max(markList)
    lowest = min(markList)

    print("\n--- STUDENT REPORT ---")

    # Grades
    for name, marks in student_dict.items():
        if marks >= 90:
            grade = "A"
        elif marks >= 75:
            grade = "B"
        elif marks >= 50:
            grade = "C"
        else:
            grade = "Fail"

        print(f"{name} -> Marks: {marks}, Grade: {grade}")

    # Final summary
    print("\nAverage:", avg)
    print("Highest:", highest)
    print("Lowest:", lowest)


student_mark_analyzer()