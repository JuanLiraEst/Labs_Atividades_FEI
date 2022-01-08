var canvas = document.getElementById("myCanvas");
var ctx = canvas.getContext("2d");

function desenhoRetangulo(){
    ctx.fillStyle = "blue";
    ctx.fillRect(0,0,50,50); /*pts do vertice do canto sup esq , largura. altura*/

    /*vermelho da ponta*/
    ctx.fillStyle = "red";
    ctx.fillRect(250,0,300,50);

    /*vermelho da meiuca*/
    ctx.fillStyle = "red";
    ctx.fillRect(110,150,40,40);

    /*ciano da esquerda*/
    ctx.fillStyle = "cyan";
    ctx.fillRect(0,120,30,60);

    /*ciano da direita*/
    ctx.fillStyle = "cyan";
    ctx.fillRect(270,135,30,30);

    /*amarelo*/
    ctx.fillStyle = "yellow";
    ctx.fillRect(0,240,60,60);

    /*preto*/
    ctx.fillStyle = "black";
    ctx.fillRect(240,240,60,60);

    /*branco do amarelo*/
    ctx.fillStyle = "white";
    ctx.fillRect(30,240,30,30);

    /*branco do preto*/
    ctx.fillStyle = "white";
    ctx.fillRect(240,240,30,30);




}
function desenhoLinha(){
    /*verde*/
    ctx.beginPath(); /*começo de um caminho*/
    ctx.moveTo(0,150); /*onde começa*/
    ctx.lineTo(300,150)/* pra onde vai*/
    ctx.strokeStyle = "#8BC089";
    ctx.lineWidth = "2"
    ctx.stroke()

    /*vermelha*/
    ctx.beginPath();
    ctx.moveTo(300,0);
    ctx.lineTo(150,150);
    ctx.strokeStyle = "red";
    ctx.lineWidth = "1"
    ctx.stroke()

    /*azul*/
    ctx.beginPath();
    ctx.moveTo(0,0);
    ctx.lineTo(150,150);
    ctx.strokeStyle = "blue";
    ctx.lineWidth = "1"
    ctx.stroke()

    /*cinza*/
    ctx.beginPath();
    ctx.moveTo(150,150);
    ctx.lineTo(150,260);
    ctx.strokeStyle = "grey";
    ctx.stroke()

}
function desenhoArco(){
    /*arco 180º do meio*/
    ctx.beginPath();
    ctx.strokeStyle = "#69A373";
    ctx.arc(150,150,60,-Math.PI,0);/*-pi pra inverter o start e o meio arco n parecer uma tigela*/
    ctx.lineWidth = "3"
    ctx.stroke();

    ctx.fill();

    /*45º da esquerda*/
    ctx.beginPath();
    ctx.strokeStyle = "#69A373";
    ctx.arc(150,150,80,-Math.PI,-0.75*Math.PI);
    ctx.stroke();
    ctx.fill();

    /*45º da direita*/
    ctx.beginPath();
    ctx.strokeStyle = "#69A373";
    ctx.lineWidth = "3"
    ctx.arc(150,150,80,-0.25*Math.PI,0);
    ctx.stroke();
    ctx.fill();

    /*90 graus canto inferior esquerdo*/
    ctx.beginPath();
    ctx.strokeStyle = "#6FA27C";
    ctx.lineWidth = "3"
    ctx.arc(150,300,80,-Math.PI,-0.5*Math.PI);/*-pi pra inverter o start e o meio arco n parecer uma tigela*/
    ctx.stroke();
    ctx.fill();

    /*90 graus canto inferior direito*/
    ctx.beginPath();
    ctx.strokeStyle = "#6FA27C";
    ctx.lineWidth = "3"
    ctx.arc(150,300,60,-0.5*Math.PI,0);/*-pi pra inverter o start e o meio arco n parecer uma tigela*/
    ctx.stroke();
    ctx.fill();

    /* circulo ciano perto do meio*/
    ctx.beginPath();
    ctx.strokeStyle = "blue";
    ctx.fillStyle = "cyan"
    ctx.arc(150,120,12,0,2*Math.PI);/*coordenada do centro, raio*/
    ctx.stroke();
    ctx.fill();

    /*meio ciano de baixo*/
    ctx.beginPath();
    ctx.strokeStyle = "#6FA27C";
    ctx.fillStyle = "cyan"
    ctx.arc(150,300,40,-Math.PI,0);/*-pi pra inverter o start e o meio arco n parecer uma tigela*/
    ctx.stroke();
    ctx.fill();

    /*amarelo da esq*/
    ctx.beginPath();
    ctx.strokeStyle = "green";
    ctx.fillStyle = "yellow"
    ctx.arc(75,220,12,0,2*Math.PI);/*coordenada do centro, raio*/
    ctx.stroke();
    ctx.fill();

    /*amarelo da dir*/
    ctx.beginPath();
    ctx.strokeStyle = "green";
    ctx.fillStyle = "yellow"
    ctx.arc(225,220,12,0,2*Math.PI);/*coordenada do centro, raio*/
    ctx.stroke();
    ctx.fill();





}
function texto(){
    ctx.font = "20px Arial";
    ctx.fillStyle = "black";
    ctx.textAlign = "center"
    ctx.fillText("Canvas",canvas.width/2,50);

}

desenhoRetangulo()
desenhoArco()
desenhoLinha()
texto()