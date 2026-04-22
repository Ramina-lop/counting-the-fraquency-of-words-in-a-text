def get_text():
    return input("Введите текст:\n")


def clean_text(text):
    text = text.lower()
    text = text.replace(",", "").replace(".", "").replace("!", "").replace("?", "")
    return text


def get_words(text):
    return text.split()


def count_words(words):
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


def find_word(words, target):
    found_words = []

    for word in words:
        if target in word:
            found_words.append(word)

    return found_words


def highlight_text(words, target):
    result = []

    for word in words:
        if target in word:
            result.append(word.upper())  # ВЫДЕЛЕНИЕ КАПСОМ
        else:
            result.append(word)

    return " ".join(result)


def unique_words(words):
    return len(set(words))


def top_words(word_count):
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:3]


def show_menu():
    print("\n📊 Выберите действие:")
    print("1 — Найти слово")
    print("2 — Самые частые слова")
    print("3 — Общее количество слов")
    print("4 — Уникальные слова")


def main():
    text = get_text()
    text = clean_text(text)
    words = get_words(text)
    word_count = count_words(words)

    show_menu()
    choice = input("Ваш выбор: ")

    if choice == "1":
        target = input("Введите слово для поиска: ").lower()
        result = find_word(words, target)

        print(f"\n🔍 Найдено {len(result)} совпадений:")

        if len(result) > 0:
            print("Слова:")
            unique_found = set(result)
            for word in unique_found:
                print("-", word)

            highlighted = highlight_text(words, target)
            print("\n📄 Текст с выделением:")
            print(highlighted)

        else:
            print("Совпадений не найдено")

    elif choice == "2":
        top = top_words(word_count)
        print("\n🔥 Топ слов:")
        for word, count in top:
            print(f"{word} — {count}")

    elif choice == "3":
        print(f"\nВсего слов: {len(words)}")

    elif choice == "4":
        print(f"\nУникальных слов: {unique_words(words)}")

    else:
        print("Неверный выбор")


main()