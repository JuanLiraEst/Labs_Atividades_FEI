let nota1 = prompt("Digite a nota lab: ");
let nota2= prompt("Digite a nota Av Semestral:");
let nota3 = prompt("Digite a nota do exame final: ");

let media = (nota1*2 + nota2*3 + nota3*5)/10

if(media>=0 && media<5) {
    alert("Conceito: E");
}
else if(media>=5 && media<6){
    alert("Conceito: D");
}
else if(media>=6 && media<7){
    alert("Conceito: C");
}
else if(media>=7 && media<8){
    alert("Conceito: B");
}
else if(media>=8 && media<=10){
    alert("Conceito: A");
}
