var canvas = document.getElementById("canvaszao");
var ctx = canvas.getContext("2d");
let tecla = 0

let bloquin = {
    x : 0,
    y : 0,
    w : 50,
    h : 50};
let juan = new Image();
juan.src ="picture.jpg"

document.addEventListener("keydown",
    function (evento){
            tecla = evento.keyCode;
    });


function desenho() {
    ctx.clearRect(0, 0, canvas.width, canvas.height)


    ctx.drawImage(juan,bloquin.x, bloquin.y, bloquin.w, bloquin.h)

    if(tecla === 37){
        if(bloquin.x >= 0)
            bloquin.x-=1;
    }
    else if(tecla === 38){
        bloquin.y -= 1; //quadrado1.y = quadrado1.y - 1;
    }
    else if(tecla === 39){
        if(bloquin.x <= canvas.width-bloquin.w)
            bloquin.x += 1;
    }
    else if(tecla === 40){
        bloquin.y += 1;
    }
    requestAnimationFrame(desenho);

}
desenho()
