def count_words(test_file):
    #wordcount
    #Gary Wang & Michael Hu on 5.11

    data = open(test_file)

    list_of_words = []  # Create an empty list to store lists of [word, word count]
    dict_of_words = {}  # Create a dictionary to store word : word count pairs

    for line in data:
        line = line.rstrip()
        #remove the space at the end of the txt
        line = line.split(" ")
        #When there is a space, cut it into a new string
        list_of_words.extend(line)  # Extend list_of_words with all words from .txt
        #Line is a set of string
        for word in line:
            dict_of_words[word] = dict_of_words.get(word, 0) + 1

        #get function has two situation
        #if word exist in dictionary, value++
        #if not, add word in list and give it value of 0

    for word, count in dict_of_words.items():
        #item function produces two variable 
        print word, count


count_words("test.txt")
