export default function updateStudentGradeByCity(students, city, newGrades) {
  return students.filter((student) => student.location === city).map((student) => {
    const studentGrade = newGrades.find((grade) => grade.studentId === student.id);
    if (studentGrade) {
      student.grade = studentGrade.grade;
    } else {
      student.grade = 'N/A';
    }
    return student;
  });
}
