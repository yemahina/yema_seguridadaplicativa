palabra = input("introduce tu palabra ")

if (palabra[::-1].lower() == palabra.lower()):
  print("tu palabra es un palindromo ")
else:
 print("tu palabra no es un palindromo ")
