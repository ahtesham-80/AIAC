def count_words(sentence):
    words = sentence.split()
    word_count = {}
    for word in words:
        word = word.lower().strip('.,!?;:"\'()[]{}')  # Normalize words
        if word:
            word_count[word] = word_count.get(word, 0) + 1
    return word_count

def main():
    sentence = input("Enter a sentence: ")
    frequencies = count_words(sentence)
    print("Word frequencies:", frequencies)

if __name__ == "__main__":
    main()