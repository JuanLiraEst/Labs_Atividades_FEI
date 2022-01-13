function somar(){
    let n1 = Number(prompt("Digite um número: "))
    let n2 = Number(prompt("Digite o outro: "))
    let soma = n1+n2;
    alert("O resultado é "+soma);
}

function subtrair(){
    let n1 = Number(prompt("Digite um número: "))
    let n2 = Number(prompt("Digite o outro: "))
    let subtr = n1-n2;
    alert("O resultado é "+subtr);
}

function dividir(){
    let n1 = Number(prompt("Digite um número: "))
    let n2 = Number(prompt("Digite o outro: "))
    let resultado = (n1/n2).toFixed(2);
    alert("O resultado é "+resultado);
}

function multiplicar(){
    let n1 = Number(prompt("Digite um número: "))
    let n2 = Number(prompt("Digite o outro: "))
    let mult = n1*n2;
    alert("O resultado é "+mult);
}