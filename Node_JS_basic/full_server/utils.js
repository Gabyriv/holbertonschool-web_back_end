const fs = require('fs').promises;

const readDatabase = async (filePath) => {
  try {
    const data = await fs.readFile(filePath, 'utf8');
    const lines = data.trim().split('\n');
    const students = lines.slice(1).filter(line => line.trim()); // Remove header and empty lines
    
    const fields = {};
    students.forEach(student => {
      const [firstname, lastname, age, field] = student.split(',');
      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(firstname);
    });
    
    return fields;
  } catch (error) {
    throw new Error('Cannot load the database');
  }
};

module.exports = { readDatabase };