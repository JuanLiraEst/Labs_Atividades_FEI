package ex6;


public class ex6lab1 {

 
    public static void main(String[] args) {
        
        for (int c1=1 ; c1<501; c1++){
            for (int c2 = 1 ; c2<501 ; c2++){
                for (int h = 1 ; h<501; h++){
                    int q_hip = h*h;
                    int q_cat = (c1*c1) + (c2*c2);
                    // se o pitágoras funcionar && não houver nenhum termo igual && o triplo estiver do menor pro maior
                    if (q_hip == q_cat  && (c1 != c2 && c1!= h) && h>c2 && c2>c1){
                        
                        System.out.printf("%d %d %d\n",c1,c2,h);
                    
                    }
                }
            }
    
        }
        
    }
    
}
