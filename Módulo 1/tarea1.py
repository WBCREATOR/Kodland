text = input("Escriba un texto de máximo 10 caracteres: ")

if len(text) > 9:
  text = text[:9] + '...'
else:
  pass

print(text)
  
