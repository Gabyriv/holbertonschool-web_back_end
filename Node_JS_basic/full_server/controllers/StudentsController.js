const { readDatabase } = require('../utils');

class StudentsController {
  static async getAllStudents(request, response) {
    try {
      const fields = await readDatabase(process.argv[2]);
      let output = 'This is the list of our students\n';
      
      // Sort fields alphabetically (case insensitive)
      const sortedFields = Object.keys(fields).sort((a, b) => 
        a.toLowerCase().localeCompare(b.toLowerCase())
      );
      
      sortedFields.forEach(field => {
        output += `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}\n`;
      });
      
      response.status(200).send(output.trim());
    } catch (error) {
      response.status(500).send(error.message);
    }
  }

  static async getAllStudentsByMajor(request, response) {
    const { major } = request.params;
    
    if (major !== 'CS' && major !== 'SWE') {
      response.status(500).send('Major parameter must be CS or SWE');
      return;
    }
    
    try {
      const fields = await readDatabase(process.argv[2]);
      if (!fields[major]) {
        response.status(500).send('Major not found');
        return;
      }
      
      response.status(200).send(`List: ${fields[major].join(', ')}`);
    } catch (error) {
      response.status(500).send(error.message);
    }
  }
}

module.exports = StudentsController;
