s = input("Введите предложение с вашей любимой книги: ")
r = input("На какое слово вы хотите заменить?")

print(s.replace(b, r))



s = 'Hello word     '
s = s.strip()



# Удаляем символы . , - : ; ?
s = s.replace(".", "")
s = s.replace(",", "")
s = s.replace("-", "")
s = s.replace(":", "")
s = s.replace(";", "")
s = s.replace("?", "")