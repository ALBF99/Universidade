
public class InfixToPost {
	
	String infix;
	
	public InfixToPost() {
		
	}
	
	private boolean isOperador (String incognita){
     if(incognita.equals("+")||incognita.equals("-")||incognita.equals("*")||incognita.equals("/")||incognita.equals("(")|| incognita.equals(")")) {
    	 return true;
     }else {
    	 return false;
     }
    }
	
	public String printStack() {
		return null; 
	}
	
	private int precedencia(String elemento,String peek) {

		if (( elemento.equals("*") || elemento.equals("/")) && (peek.equals("+") || peek.equals("-"))) {
			return 1;
		}else if (( elemento.equals("*") || elemento.equals("/")) && (peek.equals("*") || peek.equals("/"))) {
			return 2;
		}else if (( elemento.equals("+") || elemento.equals("-")) && (peek.equals("+") || peek.equals("-"))) {
			return 2;
		} else if ((elemento.equals("*")|| elemento.equals("/") || elemento.equals("+") || elemento.equals("-")) && (peek.equals("inicio" ))) {
			return 1;
		}else if (( elemento.equals("+")|| elemento.equals("-"))&& (peek.equals("*")|| peek.equals("/"))) {
			return 2;
		}else if ((elemento.equals("*")|| elemento.equals("/") || elemento.equals("+") || elemento.equals("-")) && (peek.equals("(" ))) {
			return 1;
		} else  {
			return 0;
		}
		} 

		
	 
	
	public String convert(String infix) {
		
		String postfix = "";
		
		ArrayStack<String> pilha = new ArrayStack<>(infix.length());
		pilha.push("inicio");
		
		
		for(int i = 0; i< infix.length(); i++) {
 
			String elemento = Character.toString(infix.charAt(i));
			
		
			if (isOperador(elemento)) {
				 
				int operacao = precedencia(elemento,pilha.peek());
				
				if (operacao == 1) { 
					
					pilha.push(elemento);
				
				}else if(operacao == 2) {
					
					postfix += pilha.pop();
					pilha.push(elemento);
				
				}else {
					if (elemento.equals("(")) {
				
						pilha.push(elemento);
				
					}else if (elemento.equals(")")) {
		
						while (!pilha.peek().equals("(") ) {
							postfix += pilha.pop();
						}
						pilha.pop();
							}}
			
			}else {
				postfix += elemento;
			}}
			
				
		
		while ( pilha.peek() != "inicio") {
			postfix += pilha.pop();
		}
	 
	return postfix;
}
}
	


