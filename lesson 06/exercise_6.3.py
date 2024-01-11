def countletter(word, letter):
  
  count = 0

  for character in word:
    if character == letter:
      count = count + 1
  return(count)

word = input("Please type a word: ")
letter = input("Please type a letter: ")

count = countletter(word, letter)

print(count)