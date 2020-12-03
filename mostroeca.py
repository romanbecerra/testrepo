import random
print('Te encontraste con el mostro de Ecatepec.')
print('Tendrás que pelear para salvar tu vida.')
print('...\n')

mostro= 20
vida=20
pelea= True
while pelea:
	atk1 = random.randint(0,5)
	atk2= random.randint(0,5)
	if input('escribe golpe para golpear ')== 'golpe': 					   	
		mostro=mostro-atk1
	print('le queda esto de vida al mostro: ')
	print(mostro)
	vida=vida-atk2
	print('el mostro te atacó, te queda esto de vida: ')
	print(vida)
	if mostro<vida:
		print("le estás ganando")
	if mostro>vida:
		print("te está ganando")
	elif mostro==vida:
		print('empatados')
		
	if vida <=0:
		print('te mató y se llevó tu cartera.')
		break
	elif mostro<=0:
		print('lo mataste y su clika se vengó')
		break
