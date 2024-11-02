def single_root_words(root_word, *other_words):


    same_words = []

    for word in other_words:

        word_lower = word.lower()

        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word)

    return same_words

result1 = single_root_words("Able", "Disablement", "Table", "Enable", "Fox", "Read")
result2 = single_root_words("fix", "prefix", "suffix", "transfix", "fixture", "table")

print("Результат 1:", result1)
print("Результат 2:", result2)