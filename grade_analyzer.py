

def process_scores(students):
    """Calculates the average score for each student."""
    averages = {}
    for name, scores in students.items():
        avg = sum(scores) / len(scores) if scores else 0
        averages[name] = round(avg, 2)
    return averages

def classify_grades(averages):
    """Assigns letter grades based on internal thresholds."""
    # Threshold variables
    A_MIN, B_MIN, C_MIN = 90, 75, 60
    
    classified = {}
    for name, avg in averages.items():
        if avg >= A_MIN:
            grade = 'A'
        elif avg >= B_MIN:
            grade = 'B'
        elif avg >= C_MIN:
            grade = 'C'
        else:
            grade = 'F'
        classified[name] = (avg, grade)
    return classified

def generate_report(classified, passing_avg=70):
    """Prints a formatted report and returns the pass count."""
    print("===== Student Grade Report =====")
    passed_count = 0
    total_students = len(classified)

    for name, (avg, grade) in classified.items():
        status = "PASS" if avg >= passing_avg else "FAIL"
        if status == "PASS":
            passed_count += 1
        
        # Formatting to ensure alignment
        print(f"{name:<10} | Avg: {avg:>6.2f} | Grade: {grade} | Status: {status}")

    print("================================")
    print(f"Total Students : {total_students}")
    print(f"Passed         : {passed_count}")
    print(f"Failed         : {total_students - passed_count}")
    
    return passed_count

if __name__ == "__main__":
    #Sample Input
    student_data = {
        "Alice": [85, 90, 78, 92],
        "Bob": [60, 65, 70, 55],
        "Clara": [95, 98, 92, 100]
    }

    # Sequential execution
    student_averages = process_scores(student_data)
    grade_data = classify_grades(student_averages)
    total_passed = generate_report(grade_data)
