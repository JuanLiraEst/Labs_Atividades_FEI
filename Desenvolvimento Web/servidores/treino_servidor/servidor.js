let http = require("http");
let express= require("express");

let app = express();
app.use(express.static("./publico"));

let server = http.createServer(app);

/*porta do serv*/
server.listen(8080);

console.log("Estamos online");