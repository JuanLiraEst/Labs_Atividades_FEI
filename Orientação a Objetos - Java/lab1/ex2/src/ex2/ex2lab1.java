
package ex2;
import java.util.Scanner;
public class ex2lab1 {

    public static void main(String[] args) {
        Scanner input = new Scanner ( System.in );
        double valor = 0;   
        int n, q;
        while (true){


            System.out.printf("Digite o número do produto: ");
            n = input.nextInt();
            
            if (n<1){
                System.out.printf("Valor vendido: %.2f\n",valor);
                break;}
            else if (n>5){
                System.out.printf("Valor vendido: %.2f\n",valor);
                break;
            }
            else{
                System.out.printf("Digite a quantia vendida do produto %d: ",n);

                q = input.nextInt();

                switch (n){
                    case 5:
                        valor = valor + (6.87*q); 
                        break;
                    case 4:
                        valor = valor + (4.49*q);   
                        break;
                    case 3:
                        valor = valor + (3.98*q);
                        break;
                    case 2:
                        valor = valor + (4.50*q);
                        break;
                    case 1:
                        valor = valor + (2.98*q);
                        break;
                    

                }
            }
            

            
        }

    }

    
}
