window.alert("Hello world!");
let name =window.prompt("Digite seu nome please");
window.alert("Salve, "+name+"! Tudo bem?");
let number=Number(window.prompt(name+", Digite um número, entre 0 e 10, " +
    "e eu te digo se ele está mais perto do 0 ou do 10"));

if(number<5){
    window.alert("Esse número é mais próximo do 0")
}

else if(number>5){
    window.alert("Esse número é mais próximo do 10")
}

else if(number===5){
    window.alert("Esse número está em perfeito equilíbrio entre os dois")
}


