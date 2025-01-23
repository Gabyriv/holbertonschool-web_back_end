const fs = require('fs');

function countStudents(path) {
  try {
    // Read file synchronously
    const data = fs.readFileSync(path, 'utf8');

    // Split into lines and remove empty lines
    const lines = data.trim().split('\n');
    const students = lines.slice(1).filter(line => line.trim()); // Remove header and empty lines

    console.log(`Number of students: ${students.length}`);

    // Group students by field
    const fields = {};
    students.forEach(student => {
      const [firstname, , , field] = student.split(',');
      if (!fields[field]) {
        fields[field] = { count: 0, students: [] };
      }
      fields[field].count += 1;
      fields[field].students.push(firstname);
    });

    // Print results for each field
    for (const field in fields) {
      if (Object.prototype.hasOwnProperty.call(fields, field)) {
        console.log(`Number of students in ${field}: ${fields[field].count}. List: ${fields[field].students.join(', ')}`);
      }
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
