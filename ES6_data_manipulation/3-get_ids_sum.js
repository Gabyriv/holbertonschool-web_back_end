export default function getStudentsIdsSum(students) {
  return students.reduce((id, students) => id + students.id, 0);
}
