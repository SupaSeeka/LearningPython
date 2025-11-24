const { createServer } = require('node:http');

const hostname = '127.0.0.1';
const port = 3000;

const users = {};

const saveHtml = `
<!DOCTYPE html>
<html>
    <head>
        <title>Save Info</title>
    </head>
    <body>
        <h2>Save Your Info</h2>
        <form method="POST">
            <input name="username" placeholder="Username" required><br><br>
            <input name="age" placeholder="Age" required><br><br>
            <input name="sex" placeholder="Sex" required><br><br>
            <input type="submit" value="Save">
        </form>
    </body>
</html>
`;

const retrieveHtml = `
<!DOCTYPE html>
<html>
    <head>
        <title>Get Info</title>
    </head>
    <body>
        <h2>Get User Info</h2>
        <form method="POST">
            <input name="username" placeholder="Username" required><br><br>
            <input type="submit" value="Get Info">
        </form>
    </body>
</html>
`;

const server = createServer((req, res) => {
  if (req.method === 'POST') {
    let body = '';
    req.on('data', chunk => body += chunk);
    req.on('end', () => {
      const data = Object.fromEntries(new URLSearchParams(body));
      
      if (req.url === '/retrieve') {
        const user = users[data.username];
        if (user) {
          res.end(`Found: ${JSON.stringify(user)}`);
        } else {
          res.end('User not found');
        }
      } else {
        users[data.username] = data;
        console.log('Saved:', users);
        res.writeHead(302, { 'Location': '/' });
        res.end();
      }
    });
  } else {
    if (req.url === '/retrieve') {
      res.end(retrieveHtml);
    } else {
      res.end(saveHtml);
    }
  }
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});