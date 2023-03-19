# удаляем символы пунктуации и пробелы с правой стороны
def line_magic(comment):
    ban_symbols = ['.', ',', '-', ':', ';', '?', '!']
    for i in range(len(ban_symbols)):
        comment = comment.lower().replace(ban_symbols[i], "")
    return comment.rstrip()


# блок отвечает за замену слов и индекс
def replace_word(comment, old_word, new_word):
    result = line_magic(comment)
    old_word_index = result.lower().find(old_word.lower())
    if old_word_index == -1:
        print(f"Слово '{old_word}' не найдено в тексте")
        return
    else:
        print(f"Индекс слова '{old_word}' в тексте: {old_word_index}")
        result = result[:old_word_index] + new_word.lower() + result[old_word_index + len(old_word):]
        return result.capitalize()


# блок общения с пользователем
if __name__ == '__main__':
    s = input("Введите предложение с вашей любимой книги: ")
    old_word = input("Какое слово вы хотите заменить? ")
    new_word = input(f"На что вы хотите заменить слово '{old_word}'? ")
    replaced_text = replace_word(s, old_word, new_word)
    if replaced_text:
        print(replaced_text)
