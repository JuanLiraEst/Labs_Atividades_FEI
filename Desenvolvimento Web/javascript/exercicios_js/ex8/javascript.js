let qtde= Number(prompt("Quantos números deseja digitar?"))
let base = 1
let soma = 0
let maior= 0
let menor = 0
let pares = 0
let qtdpares = 0
let qtdimpares = 0

while(base<=qtde){
    /*soma*/
    var numeros =Number(prompt("Digite o "+base+"º número:"));
    soma = soma+numeros;
    base= base+1;

    /*maior*/
    if(numeros>maior){
        maior=numeros;
    }

    if(numeros<maior) {
        menor = numeros;
    if(numeros===1){
        menor=1;
    }
    }

    /*pares*/
    if(numeros%2===0) {
        pares = pares + numeros
        qtdpares+=1
    }
    else {
        qtdimpares += 1;
    }
}


let media = (soma/qtde).toFixed(2);
let mediapares = (pares/qtdpares).toFixed(2);
let porcimpares = ((qtdimpares*100)/qtde).toFixed(2);




alert("Você digitou "+qtde+" números");
alert("A soma desses "+qtde+" números é igual a "+soma);
alert("A média desses números é igual a "+media);

alert("O maior número é "+maior);
alert("O menor número é "+menor);
alert("A média dos números pares é igual a "+mediapares);
alert("A porcentagem de números ímpares é igual a "+porcimpares+"%")
prompt('Digite "SAIR" para finalizar')

