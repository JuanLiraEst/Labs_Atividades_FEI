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
let lojaSchema = new mongoose.Schema({
    dbid: "String",
    dbnome: "String",
    dbmarca: "String",
    dbquant: "String",
});
let lojaModel = mongoose.model("Posts", lojaSchema);
//pedir pra ele se conectar a um db local
mongoose.connect("mongodb://localhost/Loja");

app.get("/", function(req,resp){
    resp.render("principal");
});

app.get("/cad", function(req,resp){
    resp.render("cadastrar");
})

app.get("/src", function(req,resp){
    resp.render("buscar");
})

app.get("/att", function(req,resp){
    resp.render("atualizar");
})

app.get("/del", function(req,resp){
    resp.render("deletar");
})

app.post("/cadastro", function(req, resp){
    let id_servidor = req.body.i_d;
    let nome_servidor = req.body.produto;
    let marca_servidor = req.body.marca;
    let quant_servidor = req.body.quantidade;

    let novo = new lojaModel({
        dbid: id_servidor,
        dbnome: nome_servidor,
        dbmarca: marca_servidor,
        dbquant: quant_servidor,
    });

    novo.save();
    resp.end();
});
app.get("/cadastro", function(req,resp){
    resp.render("mensagem")
})

var servidor = http.createServer(app);
servidor.listen(8080);


console.log("online")