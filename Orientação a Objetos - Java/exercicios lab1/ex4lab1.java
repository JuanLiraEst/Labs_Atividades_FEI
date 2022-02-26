package ex4;

import java.util.Scanner;

public class ex4lab1 {

    public static void main(String[] args) {
        Scanner input = new Scanner (System.in);
        

        System.out.println("Digite salário atual");
        float sal = input.nextFloat();  

        if(sal<0)
            System.out.println("Valor inválido!\n");

        else if (sal>=0 && sal<=400.00){
            
            float novo_sal = sal + sal * 15/100 ;
            float reajuste = novo_sal - sal;

            System.out.printf("Novo salário: %.2f\n",novo_sal);     
            System.out.printf("Reajuste ganho: %.2f\n",reajuste);   
            System.out.printf("Em percentual: 15");      
        }  
  
        else if (sal>=400.01 && sal<=800.00){
            float novo_sal = sal + sal * 12/100 ;
            float reajuste = novo_sal - sal;

            System.out.printf("Novo salário: %.2f\n",novo_sal);     
            System.out.printf("Reajuste ganho: %.2f\n",reajuste);   
            System.out.printf("Em percentual: 12");              
        }
        else if (sal>=800.01 && sal<=1200.00){
            float novo_sal = sal + sal * 10/100 ;
            float reajuste = novo_sal - sal;

            System.out.printf("Novo salário: %.2f\n",novo_sal);     
            System.out.printf("Reajuste ganho: %.2f\n",reajuste);   
            System.out.printf("Em percentual: 10");   
        }
        else if (sal>=1200.01 && sal<=2000.00){
            float novo_sal = sal + sal * 7/100 ;
            float reajuste = novo_sal - sal;

            System.out.printf("Novo salário: %.2f\n",novo_sal);     
            System.out.printf("Reajuste ganho: %.2f\n",reajuste);   
            System.out.printf("Em percentual: 7");   
        }
        else{
            float novo_sal = sal + sal * 4/100 ;
            float reajuste = novo_sal - sal;

            System.out.printf("Novo salário: %.2f\n",novo_sal);     
            System.out.printf("Reajuste ganho: %.2f\n",reajuste);   
            System.out.printf("Em percentual: 4");   
        }   
    }
    

    
}
