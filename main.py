from flask import Flask, render_template, redirect, url_for, request
from students import Student


students = []

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def student_page():
    if request.method == "POST":
        student_id = request.form.get("student-id", "")
        student_first_name = request.form.get("student-first-name", "")
        student_last_name = request.form.get("student-last-name", "")
        new_student = Student(student_first_name, student_last_name, student_id)
        students.append(new_student)
        
        return redirect(url_for("students_page"))
        
    return render_template("index.html", students=students)
    
if __name__ == "__main__":
    app.run(debug=True)

