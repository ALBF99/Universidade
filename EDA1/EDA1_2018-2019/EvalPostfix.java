public class EvalPostfix  {
	
	private boolean isOperador (String s){
	     if(s.equals("+")||s.equals("-")||s.equals("*")||s.equals("/")||s.equals("(")|| s.equals(")")) {
	    	 return true;
	     }else {
	    	 return false;
	     }
	    }

	public int convert(String postfix) {
		
		int infix = 0,algarismo = 0, algarismo1 = 0 , algarismo2 = 0;
		
		ArrayStack<Integer> pilhaOperandos = new ArrayStack<>(postfix.length());
		
		
			for(int i = 0; i< postfix.length(); i++) {
			 
			String elemento = Character.toString(postfix.charAt(i));
			if (isOperador(elemento)) {
				
				algarismo2 = pilhaOperandos.pop();
				algarismo1 = pilhaOperandos.pop();
				
			
				switch(elemento) {
				case "+":
					infix = algarismo1+algarismo2;
					break;
				case "-":
					infix = algarismo1 - algarismo2;
					break;
				case "*":
					infix = algarismo1 * algarismo2;
					break;
				case "/":
					infix = algarismo1 / algarismo2;
					break;
					
				default:
                      System.out.println("Operador Invalida");
				}
				
				pilhaOperandos.push(infix);
				
			}else {
				algarismo = Integer.valueOf(elemento);
				pilhaOperandos.push(algarismo);
			}
			}
		
		return infix;
	}

}	

