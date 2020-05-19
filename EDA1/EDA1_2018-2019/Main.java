import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
    	
    	Scanner scanner = new Scanner(System.in);
        System.out.print("Infix: ");
        String infix = scanner.nextLine();


        InfixToPost exemplo1 = new InfixToPost();
        EvalPostfix exemplo2 = new EvalPostfix();
        
        String postfix = exemplo1.convert(infix);
        int resultado = exemplo2.convert(postfix); 
        
        System.out.println("Postfix: " + postfix + "\nResultado: " + resultado);

    }
    	
    
    }

