import random

def jugar(vidas, maximo):
	numero_random = random.randint(1, maximo)
	numero_elegido = None

	while numero_random != numero_elegido:
		print('============================================================')
		numero_elegido = int(input(f'Adivina el número del 1 al {maximo}: '))

		if numero_random < numero_elegido:
			print('============================================================')
			print('Elige un número menor')
			vidas -= 1

		elif numero_random > numero_elegido:
			print('============================================================')
			print('Elige un número mayor')
			vidas -= 1

		if vidas == 0:
			print('============================================================')
			print('GAME OVER')
			break

		print('============================================================')
		print(f'Te quedan {vidas} vidas')

	if numero_random == numero_elegido:
		print('============================================================')
		print('¡Ganaste!')

def main():
	while True:
		print('============================================================')
		main_menu = """Bienvenido a Adivina el Número.
Elige la opción que desees.
1-Jugar
2-Salir
:"""
		opcion = input(main_menu)

		if opcion == '1':
			print('============================================================')
			print('Elige el número de vidas y el número máximo a adivinar.')
			print('============================================================')
			vidas = int(input('Vidas: '))
			numero_maximo = int(input('Número máximo: '))
			jugar(vidas, numero_maximo)
		elif opcion == '2':
			print('El programa se cerrará')
			break

		else:
			print('============================================================')
			print('Ingrese una opción válida')

if __name__ == '__main__':
	main()