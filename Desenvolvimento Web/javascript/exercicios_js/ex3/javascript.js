let i = Number(prompt("Insira 1, 2 ou 3:  "));

let a = Number(prompt("Insira um número"));
let b = Number(prompt("Insira um número"));
let c = Number(prompt("Insira um número"));

if(i ===1){
    if(a>=b&&b>=c){
        alert("Ordem crescente: "+c+", "+b+", "+a)
    }
    else if(a>=c&&c>=b){
        alert("Ordem crescente: "+b+", "+c+", "+a)
    }
    else if(b>=a&&a>=c){
        alert("Ordem crescente: "+c+", "+a+", "+b)
    }
    else if(b>=c&&c>=a){
        alert("Ordem crescente: "+a+", "+c+", "+b)
    }
    else if(c>=b&&b>=a){
        alert("Ordem crescente: "+a+", "+b+", "+c)
    }
    else if(c>=a&&a>=b){
        alert("Ordem crescente: "+b+", "+a+", "+c)
    }
}
else if(i ===2){
    if(a>=b&&b>=c){
        alert("Ordem decrescente: "+a+", "+b+", "+c)
    }
    else if(a>=c&&c>=b){
        alert("Ordem decrescente: "+a+", "+c+", "+b)
    }
    else if(b>=a&&a>=c){
        alert("Ordem decrescente: "+b+", "+a+", "+c)
    }
    else if(b>=c&&c>=a){
        alert("Ordem decrescente: "+b+", "+c+", "+a)
    }
    else if(c>=b&&b>=a){
        alert("Ordem decrescente: "+c+", "+b+", "+a)
    }
    else if(c>=a&&a>=b){
        alert("Ordem decrescente: "+c+", "+a+", "+b)
    }
}
else if(i ===3){
    if(a>=b&&b>=c){
        alert("O maior entre os dois: "+c+", "+a+", "+b)
    }
    else if(a>=c&&c>=b){
        alert("O maior entre os dois: "+b+", "+a+", "+c)
    }
    else if(b>=a&&a>=c){
        alert("O maior entre os dois: "+c+", "+b+", "+a)
    }
    else if(b>=c&&c>=a){
        alert("O maior entre os dois: "+a+", "+b+", "+c)
    }
    else if(c>=b&&b>=a){
        alert("O maior entre os dois: "+a+", "+c+", "+b)
    }
    else if(c>=a&&a>=b){
        alert("O maior entre os dois: "+b+", "+c+", "+a)
    }
}