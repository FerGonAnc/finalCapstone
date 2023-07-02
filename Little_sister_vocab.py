# Task 23 - Preparing for interviews
# Compulsory Task 2 - Little sister’s vocab

# 1. Add a prefix to a word
# Here I declared the  function 'add_prefix_un(word)' that add the string "un" to the word input by the user.

word = input("Insert a word to add a prefix 'un': ")

def add_prefix_un(word):
    return "un" + str(word)

print(add_prefix_un(word))

# 2. Add prefixes to word groups
# Here I declared the function 'make_word_groups(vocab_words)' that takes the first element of the list.
# Then crate another list with the rest of elements
# And finally adds the first prefix (first element) to each of the other elements of the group 

vocab_words = ['en', 'close', 'joy', 'lighten']

def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    words = vocab_words[1:]
    prefixed_words = [prefix + word for word in words]
    word_groups = [prefix] + prefixed_words
    return ' :: '.join(word_groups)

print("\nThe string with the prefix applied: ")
print(make_word_groups(vocab_words))

# 3. Remove a suffix from a word
# Here I declared the function 'remove_suffix_ness(word2)' that takes the root of the word in case finishes with 'ness'
# Then if the root of the word doesn't finishes with 'i', return the root.
# However, if the root of the word finishes with 'i', adds a 'y' at the end

word2 = input("\nInsert a word to delete the suffix 'ness': ")

def remove_suffix_ness(word2):
    if word2.endswith("ness"):
        root_word = word2[:-4]
        if root_word[-1] == 'i':
            return root_word[:-1] + 'y'
        else:
            return root_word
    else:
        return word2
       
print(remove_suffix_ness(word2))

# 4. Extract and transform a word.
# Here I declared the function 'adjective_to_verb(sentence, index):' that spilts the sentence by each word.
# Then following the index, takes the word that is going to be the verb
# The function then ad 'en' to the adjective and converts it in a verb

sentence = "It got dark as the sun set."
index = 2

def adjective_to_verb(sentence, index):
    words = sentence.split()
    adjective = words[index]
    verb = adjective + 'en'
    return verb

print("\nThe extracted adjective as a verb: ")
print("The original sentence is: "+ sentence)
print(adjective_to_verb(sentence, index))