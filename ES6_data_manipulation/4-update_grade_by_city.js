export default function updateStudentGradeByCity(students, city, newGrades) {
  return students.filter((student) => student.location === city).map((student) => {
    const studentGrade = newGrades.find((grade) => grade.studentId === student.id);
    let newStudent = { ...student };

    if (studentGrade) {
      newStudent = { ...newStudent, grade: studentGrade.grade };
    } else {
      newStudent = { ...newStudent, grade: 'N/A' };
    }

    return newStudent;
  });
}
