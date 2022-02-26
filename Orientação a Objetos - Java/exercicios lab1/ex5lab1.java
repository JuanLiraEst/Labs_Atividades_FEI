
package ex5;
import java.util.Scanner;
public class ex5lab1 {

    public static void main(String[] args) {
        
        Scanner input = new Scanner( System.in );
        
        //chamando
        int [] n ;
        
        //alocando espaço
        n = new int[5];
        for (int x=0;x<5;x++){
            System.out.printf("Digite o %dº número: ",x+1);
            int valor = input.nextInt();
            
            //condição do exercicio: números entre 1 e 30
            if (valor<1 || valor>30){
                System.out.println("Valor inválido! Só são aceitos números entre 1 e 30");
                x = x-1;
            }
            else
                n [x] = valor;
            
        }
        //for para correr toda a lista
        for (int y=0; y<5; y++){
            String ast = "*";
            
            //for para usar o valor da lista como qtde de asteriscos
            for (int z=0; z<n[y];z++){
                System.out.printf(ast);
            }
            System.out.printf("\n");
        }
    }
    
}
