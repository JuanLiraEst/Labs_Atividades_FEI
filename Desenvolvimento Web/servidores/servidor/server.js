let http = require('http');
let express = require('express');

let app = express();

app.use(express.static('./publico'))

let server = http.createServer(app);
server.listen(8080);

console.log("Funcionando")