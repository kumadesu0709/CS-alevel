dickens = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only."

dickens = dickens.replace(',', '')      # Remove any commas and full stops by replacing them with empty strings
dickens = dickens.replace('.', '')
dickens = dickens.lower()               # Convert to lowercase
word_list = dickens.split()              # Create a list of words. By default split at every ' ' character.

word_frequency = {}
for word in word_list:
    if word not in word_frequency:
        word_frequency[word] = 1
    else:
        word_frequency[word] = word_frequency[word] + 1
#print (word_frequency)

#for word in sorted(word_frequency):
 #   print(word, word_frequency[word]) #sort by alphabet

#for word in sorted(word_frequency, key=word_frequency.get, reverse = True):
    #print(word, word_frequency[word])
    

words = sorted(word_frequency, key=word_frequency.get, reverse = True)

for word in words[:5]:
    print(f"'{word}' appeared {word_frequency[word]} times")