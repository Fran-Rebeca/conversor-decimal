##############################################################################
# Projeto Interdisciplinar - Programação / Organização e Arquitetura dos Computadores
# Autores: Francielly Silva
# CTS em Análise e Desenvolvimento de Sistemas
# Turma - L
# 1º Semestre / 2022
# Campus Guarulhos 
##############################################################################

def Main( ):
	r = " "
	
	print("-" * 30)
	print(" " * 11 + "OPÇÕES")
	print("-" * 30)
	
	while (len(r) == 0) or (len(r) > 1) or (ord(r) < 49) or (ord(r) > 54):
		r = input("1 - Decimal para binário \n2 -" + 
		" Decimal para octal \n3 - Decimal para" +
		" hexadecimal  \n  Digite uma opção: ")
		print(" ")
		
		if (len(r) == 0) or (len(r) > 1) or (ord(r) < 49) or (ord(r) > 54):
			print("Entrada inválida. Digite apenas números de 1 a 3.")
			print(" ")
			
	Escolha(r)

def Escolha(r):		
	if r == "1":
		DecBin( )
		print(" ")
	
		
	elif r == "2":
		DecOct( )
		print(" ")

	elif r == "3":
		DecHex( )
		print(" ")
	
def DecBin( ):
	num = " "
	nb = [ ]
	
	print("-" * 30)
	print("     DECIMAL PARA BINÁRIO")
	print("-" * 30)
	
	while (not num.isnumeric( )):
		num = input("Número decimal: ")
		print(" ")
		if (not num.isnumeric( )):
			print("Entrada inválida. Digite apenas números.")
			print(" ")
			
	n = int(num)
	
	while n% 2 >= 0:
		if n < 2:
			nb.append(str(n))
			break
		q = n // 2
		rd = n % 2
		n = q
		nb.append(str(rd))
	print("Número binário: " + "".join(nb[::-1]))
	

			
def DecOct( ):
	num = " "
	oc = 0
	nb = [ ]
	no = [ ]
	tv = [ ]
	
	print("-" * 30)
	print("     DECIMAL PARA OCTAL")
	print("-" * 30)
	
	while (not num.isnumeric( )):
		num = input("Número decimal: ")
		print(" ")
		if (not num.isnumeric( )):
			print("Entrada inválida. Digite apenas números.")
			print(" ")
			
	n = int(num)
	
	while n % 2 >= 0:
		if n < 2:
			nb.append(str(n))
			break
		q = n // 2
		rd = n % 2
		n = q
		nb.append(str(rd))
			
	a = list(nb[x: x + 3] for x in range(0, len(nb), 3))
		
	for x in range(3):
		v = 2**x
		tv.append(v)
		
	for x in a:
		for y in range(len(x)):
			if x[y] == "1":
				oc += tv[y]
		no.append(str(oc))
		oc = 0
			
	print("Número octal: " + "".join(no[::-1]))
		
	
def DecHex( ):
	num = " "
	let = 55
	nb = [ ]
	hx = [ ]
	
	print("-" * 30)
	print("   DECIMAL PARA HEXADECIMAL")
	print("-" * 30)
	
	while (not num.isnumeric( )):
		num = input("Número decimal: ")
		print(" ")
		if (not num.isnumeric( )):
			print("Entrada inválida. Digite apenas números.")
			print(" ")
			
	n = int(num)
	
	while n % 16 >= 0:
		if n < 16:
			nb.append(n)
			break
		q = n // 16
		rd = n % 16
		n = q
		nb.append(rd)
		
	for x in nb:
		if x > 9:
			lt = chr(x + let)
			hx.append(lt)
		else:
			hx.append(str(x))
	print("Número hexadecimal: " + "".join(hx[::-1]))
	


esc = "S"
	
while esc == "S":
	Main( )
	
	esc = input("Deseja continuar? S/N \n").upper( )
	
	while (esc != "S") and (esc != "N"):
		print(" ")
		print("Entrada inválida.")
		print(" ")
		esc = input("Deseja continuar? S/N \n").upper( )
		print(" ")
		
	print(" ")
	
	if esc == "N":
		print("-" * 30)
		print(" " * 12 + "FIM")
		print("-" * 30)
