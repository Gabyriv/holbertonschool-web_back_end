export default function updateStudentGradeByCity(students, city, newGrades) {
  return students.filter((student) => student.location === city).map((student) => {
    const student_grade = newGrades.find((grade) => grade.studentId === student.id);
    if (student_grade) {
      student.grade = student_grade.grade;
    } else {
      student.grade = 'N/A';
    }
    return student;
  });
}
