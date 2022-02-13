animation = {
    'Pokemon': "Pikachu",
    'Digimon': 'Agumon',
    'Yugioh': 'Black Magician'
}

word = input()
# if word in animation:
#     print(animation.get(word))
# else:
#     print("I don't know")
    
# print(animation[word] if word in animation else 'I don\'t know')

print(animation.get(word, "I don't know"))