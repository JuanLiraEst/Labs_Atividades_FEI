// n esquecer do npm init, npm install express, npm install ejs, npm install body-parser, npm install mongoose
let http = require("http");
let express = require("express");
let bodyParser = require("body-parser");
let mongoose = require("mongoose");

var app = express();
app.set("view engine", "ejs"); // define qm vai interpretar os templates
app.set("views", "./views");
app.use(express.static("./public")); // onde está o conteúdo estático
app.use(bodyParser.urlencoded());
app.use(bodyParser.json());
//_______________________________________________
//Banco de dados Abaixo
let postSchema = new mongoose.Schema({
    dbtitulo: "String",
    dbresumo: "String",
    dbconteudo: "String",
});

let postModel = mongoose.model("Posts", postSchema);
//pedir pra ele se conectar a um db local
mongoose.connect("mongodb://localhost/Blog");

app.get("/", function(req,resp){
    postModel.find(function(erro, lista){
        resp.render("principal", {posts: lista});
    });
});
//_______________________________________________
app.get("/", function(req, resp){
    resp.render("principal")//renderizar a nossa pg
});

app.get("/criaPost", function(req, resp){
    resp.render("formulario");
});

app.post("/criaPost", function(req, resp){
    let titulo_servidor = req.body.titulo;
    let resumo_servidor = req.body.resumo;
    let conteudo_servidor = req.body.conteudo;

    let novo = new postModel({
        dbtitulo: titulo_servidor,
        dbresumo: resumo_servidor,
        dbconteudo: conteudo_servidor
    });

    novo.save();
    resp.render("mensagem");
});

var servidor = http.createServer(app);
servidor.listen(8080);

console.log("Tamo online")