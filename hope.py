text = input('Введите текст со скобками: ')
while '(' in text or ')' in text:
    beginning_of_text = text.find('(')
    if beginning_of_text != -1:
        if text[beginning_of_text:beginning_of_text+2] == '((':
            end_of_text = text.find('))', beginning_of_text)
            if end_of_text != -1:
                text = text[:beginning_of_text] + text[end_of_text+2:]
            else:
                text = text[:beginning_of_text]
        else:
            end_of_text = text.find(')', beginning_of_text)
            if end_of_text != -1:
                text = text[:beginning_of_text] + text[end_of_text+1:]
            else:
                text = text[:beginning_of_text]
    else:
        end_of_text = text.find(')')
        if end_of_text != -1:
            text = text[end_of_text+1:]

print(text)
