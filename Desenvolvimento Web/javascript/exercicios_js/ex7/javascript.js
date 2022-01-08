let base= prompt("Digite o valor da base do triângulo");
let altura = prompt("Digite o valor da altura do triângulo");

if(base<=0 ||altura<=0){
    alert("Erro! Valor inválido.")
}
else{
    let area= (base*altura)/2
    alert("A área do triângulo equivale a "+area)
}