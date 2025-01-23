const fs = require('fs').promises;

const countStudents = async (path) => {
  try {
    const data = await fs.readFile(path, 'utf8');
    const lines = data.trim().split('\n');
    const students = lines.slice(1).filter((line) => line.trim()); // Remove header and empty lines

    let output = `Number of students: ${students.length}\n`;

    const fields = {};
    students.forEach((student) => {
      const [firstname, lastname, age, field] = student.split(',');
      if (!fields[field]) {
        fields[field] = { count: 0, students: [] };
      }
      fields[field].count += 1;
      fields[field].students.push(firstname);
    });

    for (const field in fields) {
      output += `Number of students in ${field}: ${fields[field].count}. List: ${fields[field].students.join(', ')}\n`;
    }

    console.log(output.trim());
    return output;
  } catch (error) {
    throw new Error('Cannot load the database');
  }
};

module.exports = countStudents;
