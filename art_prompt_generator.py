#program will generate one word to help give art ideas

import random
file = open('/users/pichayapatjumpholwong/desktop/coding_projects/art_words', 'r')
art_words = file.read().split('\n')
pick_word = random.choice(art_words)
print(pick_word)



