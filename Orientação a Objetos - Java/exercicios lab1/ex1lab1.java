
package ex1;

import java.util.Scanner;
public class ex1lab1 {


    public static void main(String[] args) {
        
        while(true){
            Scanner input = new Scanner( System.in );
            int l;
            System.out.println("\n");
            System.out.printf("Digite o número de lados do quadrado:");
            l = input.nextInt(); 
            
            if (l==1)
                System.out.println("*");
            
            else if(l>1 && l<21){
                String ast = "*";
                String esp =" ";

                for (int x=0;x<l;x++){
                    System.out.printf(ast);}
                System.out.printf("\n");


                for (int z = 0; z<l-2; z++){
                    for (int y=0;y<l;y++){
                        if (y==0)
                            System.out.printf(ast);

                        else if (y+1== l)//x mais um igual a lado
                            System.out.printf(ast);
                        else
                            System.out.printf(esp);
                    }
                    System.out.printf("\n");
                }

                for (int x=0;x<l;x++){
                    System.out.printf(ast);}
                
            }
            else
                System.out.println("Valor inválido! O quadrado deve ter comprimento entre 1 e 20");
        }
    }
}