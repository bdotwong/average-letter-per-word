import re
sentence = "Hi my name is Bryan"

def average_word():
    new_sentence = []
    words = re.findall(r'(\w+)', sentence)
    for letters in words:
        new_sentence.append([letters])
        sum_letters = sum(len(i) for i in words)
    sentence_length = len(new_sentence)
    average_word = sum_letters / sentence_length

    print(f'The number of words in the sentence is {sentence_length}. The number of letters is {sum_letters}. This makes the average letters per word in the sentence {average_word}.')
    print(average_word)
        

average_word()

