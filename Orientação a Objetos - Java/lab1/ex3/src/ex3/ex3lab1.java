
package ex3;

import java.util.Scanner;
public class ex3lab1 {


    public static void main(String[] args) {
        Scanner input = new Scanner (System.in);

        while (true){
            System.out.println("Exercício 3: Flíper");
            System.out.printf("Digite a posição da porta P (0 - Esquerda | 1 - Direita)");
            int p = input.nextInt();
            System.out.printf("Digite a posição da porta R (0 - Esquerda | 1 - Direita)");
            int r = input.nextInt();        
            
            if ( (r!=0 && r!=1) || (p!=0 && p!=1) )
                System.out.println("Valor inválido. As opções são 0 ou 1\n");
            
            else{
                if (p==0 && (r==1 || r==0) ){
                    System.out.println("A bolinha seguirá o caminho C\n");
                }
                else if (p==1){
                    if (r==1)
                        System.out.println("A bolinha seguirá o caminho A\n");
                    else if (r==0)
                        System.out.println("A bolinha seguirá o caminho B\n");

                }
            }
        }
    }
    
}
