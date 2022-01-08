let altura = prompt("Digite sua altura: ");
let peso = prompt("Digite seu peso: ");

if(altura<1.20 && peso<=60){
    alert("Classificação: A");
}

else if(altura>=1.20 && altura<=1.70 && peso<=60){
    alert("Classificação: B");
}

else if(altura>1.70 && peso<=60){
    alert("Classificação: C");
}

else if(altura<1.20 && peso>60 && peso<=90){
    alert("Classificação: D");
}

else if(altura<=1.70 && altura>=1.20 && peso>60 && peso<=90){
    alert("Classificação: E");
}

else if(altura>1.70 && peso>60 && peso<=90){
    alert("Classificação: F");
}

else if(altura<1.20 && peso>90){
    alert("Classificação: G");
}

else if(1.70>=altura && altura>=1.20 && peso>90){
    alert("Classificação: H");
}

else if(1.70<altura && peso>90){
    alert("Classificação: I")
}





