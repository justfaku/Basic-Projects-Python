def palindromo(palabra):
	palabra = palabra.replace(' ', '')
	palabra = palabra.lower()

	palabra_invertida = palabra[::-1]

	if palabra == palabra_invertida:
		return True
	else:
		return False

#Función principal
def main():
	palabra = input('Ingrese una palabra: ')

	es_palindromo = palindromo(palabra)

	if es_palindromo:
		print('La palabra es palindromo')
	else:
		print('La palabra no es palindromo')
#Punto de entrada de la aplicación
if __name__ == '__main__':
	main()
