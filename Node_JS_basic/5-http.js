const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer(async (req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });

  if (req.url === '/') {
    res.end('Hello Holberton School!\n');
  } else if (req.url === '/students') {
    if (process.argv[2] !== null) {
      const message = 'This is the list of our students\n';
      try {
        const output = await countStudents(process.argv[2]);
        res.end(`${message}${output.join('\n')}`);
      } catch (error) {
        res.end(`${message}${error.message}\n`);
      }
    }
  } else {
    res.write('Not Found');
    res.end();
  }
});

app.listen(1245);

module.exports = app;
