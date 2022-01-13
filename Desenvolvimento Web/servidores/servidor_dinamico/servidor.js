var http = require('http');
var express = require('express');
var bodyParser = require('body-parser');
/*importar body parser para o app.post la embaixo funcionar*/

var login_cadastro;
var senha_cadastro;

var app = express();

app.use(express.static('./public'));
/*duas linhas essenciais para trabalhar com post*/
app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());

/*meio de visualização usado*/
/*tudo que for visualização estará em ./views*/
/*n esquecer de jogar npm install ejs no terminal*/
app.set('view engine', 'ejs');
app.set('views','./views')

/*captura a solicitação do usuário , e devolve a página desejada*/
/* o get é usado para renderizar a página*/
/*capturando o pedido do usuário e renderizar o cadastra.ejs*/
app.get('/cadastra', function(requisicao, resposta){
    resposta.render('cadastrar');
});

/*para a pg logar*/
app.get(["/","/login"], function(req,resp){
    resp.render("logar");
});


app.post("/login", function(req, resp){
    let login = req.body.logar_login;
    let senha = req.body.logar_senha;
    if(login === login_cadastro && senha === senha_cadastro){
        let mensagem = "Sucesso!!"
        resp.render("resposta",{mensagem,login,senha})}
    else{
        let mensagem = "Falha!!"
        resp.render("resposta",{mensagem,login,senha})}
});

app.post("/cadastra_user",function(req,resp){
    login_cadastro = req.body.login; /*pegar o que está no input login no body do html*/
    senha_cadastro = req.body.senha;
    resp.write("<h1>Cadastrado com Sucesso!</h1><br><a href='/'>Login</a> ");
    resp.end(); /*pra pg n ficar carregando infinitamente*/
    console.log(login_cadastro);/*mostrar no terminal qnd for preenchido*/
    console.log(senha_cadastro);
});

let servidor = http.createServer(app);
servidor.listen(8080);

console.log("Tamo ON");