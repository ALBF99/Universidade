.data
msg:
.ascii "*************************************************************\n*** Calculadora Polaca Inversa                          "
.ascii"  ***\n*** Autores: Cláudia Dias (35308) e Ana Ferro (39872)     ***\n*** ASC 2017/2018                                      "
.asciiz"   ***\n*************************************************************\n"
msg_pilha:
.asciiz "Pilha:\n"
msg_vazia:
.asciiz "(vazia)\n"
seta_input:
.asciiz "-> "
quebra_linha:
.asciiz "\n \n"
swap:
.ascii "swap"
nega:
.ascii "neg"
dup:
.ascii "dup", ""
del:
.ascii "del"
off:
.ascii "off"
clear:
.ascii "clear"

s:
.space 256

.text
		addi $sp, $sp, -24
		la $t0, swap 
		lb $s0, 0($t0)
		sw $s0, 0($sp)
		la $t1, nega
		lb $s1, 0($t1)
		sw $s1, 4($sp)
		la $t2, dup
		lb $s2, 1($t2)
		sw $s2, 8($sp)
		la $t3, del
		lb $s3, 0($t3)
		sw $s3, 12($sp)
		la $t4, off
		lb $s4, 0($t4)
		sw $s4, 16($sp)
		la $t5, clear
		lb $s5, 0($t5)
		sw $s5, 20($sp)
	

MENSAGEM:
		li $v0, 4
		la $a0, msg
		syscall


MAIN:		
		lw $s0, 0($sp)
		lw $s1, 4($sp)
		lw $s2, 8($sp)
		lw $s3, 12($sp)
		lw $s4, 16($sp)
		lw $s5, 20($sp)
		addi $sp, $sp, -4
		sw $ra, 0($sp)
		jal PILHA
		nop
Main_loop:
		jal PEDIR_INPUT
		nop
		jal LER_INPUT
		nop
		j Main_loop
		nop

PEDIR_INPUT:
		la $a0, s
		li $a1, 256	
		li $v0, 8
		syscall
		jr $ra
		nop

	
LER_INPUT:	
		lb $t0, 0($a0)
		lb $t1, 1($a0)
		addi $a0, $a0, 1
		bne $t0, $s4, caseClear
		nop
		jal OFF
		nop
caseClear:	
		bne $t0, $s5, caseLer_input
		nop
		jal CLEAR
		nop
caseLer_input:	
		bne $t0,0x0020, casePilha
		nop
		jal LER_INPUT
		nop
casePilha:
		bne $t0, 0x000a, caseOperadores
		nop
		jal PILHA
		nop
caseOperadores:
		slti $t2, $t0, 0x0030
		beq $t2, $zero, caseOperadores2
		nop
		jal OPERADORES
		nop
caseOperadores2:
		slti $t2, $t0, 0x0060
		bne $t2, $zero, caseConversao
		nop
		jal OPERADORES
		nop
caseConversao:
		jal CONVERSAO
		nop
		
		

CONVERSAO:
		addi $t0, $t0, -48
		addi $sp, $sp, -4
		sw $t0, 0($sp)
		beq $t1, 0x0020,LER_INPUT
		nop
		beq $t1, 0x000a, PILHA
		nop
	
Algarismos_plus:			
		mul $t0, $t0, 0x000a          
		mflo $t2
		lb $t0, 0($a0)
		lb $t1, 1($a0)
		addi $t0, $t0, -48
		add $t0,$t2, $t0
		sw $t0, 0($sp)
		beq $t1, 0x000a, PILHA
		nop
		beq $t1, 0x0020,LER_INPUT
		addi $a0, $a0,1
		j Algarismos_plus
		nop
	
	
OPERADORES:	
		bne $t0, 0x002b,caseSub
		nop
		jal ADD
		nop
caseSub:
		bne $t0, 0x002d, caseMul
		nop
		jal SUB
		nop
caseMul:
		bne $t0, 0x002a, caseDiv
		nop
		jal MUL
		nop
caseDiv:
		bne $t0, 0x002f, caseSwap
		nop
		jal DIV
		nop
caseSwap:
		bne $t0, $s0, caseNeg
		nop
		jal SWAP
		nop
		
caseNeg:
		bne $t0, $s1, caseDup
		nop
		jal NEG
		nop
caseDup:
		bne $t1, $s2, caseDel
		nop
		jal DUP
		nop
caseDel:
		jal DEL
		nop
		
		
ADD:
		lw $a2, 0($sp) #primeiro numero
		lw $a3, 4($sp) #segundo numero
		add $v0, $a2, $a3 #soma
		sw $v0, 4($sp) # guardar no espaço acima
		addi $sp, $sp, 4 #tirar espaço na pilha
		j LER_INPUT
		nop
		

MUL:
		lw $a2, 0($sp) #primeiro numero
		lw $a3, 4($sp) #segundo numero
		mult $a2, $a3 #multiplica
		mflo $v0
		sw $v0, 4($sp) # guardar no espaço acima
		addi $sp, $sp, 4 #tirar espaço na pilha
		j LER_INPUT
		nop
		


SUB:
		lw $a2, 0($sp) #primeiro numero
		lw $a3, 4($sp) #segundo numero
		sub $v0, $a3, $a2 #subtrção
		sw $v0, 4($sp) # guardar no espaço acima
		addi $sp, $sp, 4 #tirar espaço na pilha
		j LER_INPUT
		nop
		

DIV:
		lw $a2, 0($sp) #primeiro numero
		lw $a3, 4($sp) #segundo numero
		div $a3, $a2
		mflo $v0  #divisão
		sw $v0, 4($sp) # guardar no espaço acima
		addi $sp, $sp, 4 #tirar espaço na pilha
		j LER_INPUT
		nop
		

DUP:
		lw $t0, 0($sp)				
		addi $sp, $sp, -4
		sw $t0, 0($sp)
		j LER_INPUT
		addi $a0, $a0, 2
		

NEG:
		lw $a1, 0($sp)
		sub $v0, $zero, $a1 
		sw $v0, 0($sp) 
		j LER_INPUT
		addi $a0, $a0, 2
		

SWAP:
		lw $a2, 0($sp)
		lw $a3, 4($sp)			
		sw $a2, 4($sp)
		sw $a3, 0($sp)
		j LER_INPUT
		addi $a0, $a0, 3
		


CLEAR:
		addi $sp, $zero, 0x7fffeffc
		li $v0, 4
		la $a0, msg_pilha
		syscall
		jal Pilha_vazia
		nop
		

DEL:
		addi $sp, $sp, 4
		j PILHA
		nop

OFF:		
		addi $sp, $sp, 24
		li $v0, 10
		syscall


PILHA:	
		li $v0, 4
		la $a0, msg_pilha
		syscall
		beq $sp,0x7fffefe0, Pilha_vazia 
		nop
		lw $a0, 0($sp)
		li $v0,1
		syscall
		lw $a0, 4($sp)
		bne $a0, $zero, Pilha_loop
		nop
		li $v0, 4
		la $a0, quebra_linha
		syscall
		li $v0, 4                   
		la $a0, seta_input
		syscall
		j Main_loop
		nop	
Pilha_loop:	
		li $v0, 4
		la $a0, quebra_linha
		syscall
		addi $sp, $sp, 4
		lw $a0, 0($sp)
		li $v0, 1
		syscall
		lw $a0, 4($sp)
		bne $a0, $zero, Pilha_loop
		nop
		addi $sp, $sp, -4
		li $v0, 4
		la $a0, quebra_linha
		syscall
		li $v0, 4                   
		la $a0, seta_input
		syscall
		j Main_loop
		nop
		jr $ra
		nop	
Pilha_vazia:	
		li $v0, 4
		la $a0, msg_vazia
		syscall
		li $v0, 4
		la $a0, quebra_linha
		syscall
		li $v0, 4                   
		la $a0, seta_input
		syscall
		j Main_loop
		nop
	
