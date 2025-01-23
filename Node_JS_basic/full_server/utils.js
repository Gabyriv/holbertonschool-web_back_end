import fs from 'fs';

const readDatabase = (filePath) => {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf8', (err, data) => {
      if (err) {
        reject(Error('Cannot load the database'));
      }
      if (data) {
        const lines = data.toString().split('\n');
        const studentGroups = {};
        const dbFieldNames = lines[0].split(',');
        const studentPropNames = dbFieldNames.map((field) => field.trim());

        for (const line of lines.slice(1)) {
          if (line) {
            const studentRecord = line.split(',');
            const studentPropValues = studentRecord.map((field) => field.trim());
            const field = studentPropValues[studentPropNames.indexOf('field')];
            const firstName = studentPropValues[studentPropNames.indexOf('firstname')];

            if (!studentGroups[field]) {
              studentGroups[field] = [];
            }
            studentGroups[field].push(firstName);
          }
        }
        resolve(studentGroups);
      }
    });
  });
};

export default readDatabase;
