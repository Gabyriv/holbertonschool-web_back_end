const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer(async (req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });

  if (req.url === '/') {
    res.end('Hello Holberton School!\n');
  } else if (req.url === '/students') {
    try {
      const output = await countStudents(process.argv[2]);
      res.end(`This is the list of our students\n${output}`);
    } catch (error) {
      res.end(`${error.message}\n`);
    }
  }
});

app.listen(1245);

module.exports = app;
