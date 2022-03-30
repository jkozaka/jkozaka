
import random
##### CONFIG AREA

words = 5 #amount of words to generate
syllables = 2 #amount of syllables
struct = [True,False] #true is consoant #false is vowel.

cons = 1 #amount of consoants in syllable
vows = 1 #amount of vowels in syllable

##### CODE

consoants = "bcdfghjklmnpqrstvwxyz" #config possible
vowels = "aeiou"                    #

output = []

for x in range(0,words):
    word = []

    for a in range(0,syllables): #add syllables

        syllable = [] # filled later

        for d in range(0,len(struct)): #builds syllable

            consoant = []
            vowel = []

            if struct[d]: #if consoant

                for b in range(0,cons): #add consoants

                    consoant.append(random.choice(consoants))

                syllable.append("".join(consoant))
                consoant = []

            else: #if vowel

                for c in range(0,vows): #add vowels

                    vowel.append(random.choice(vowels))

                syllable.append("".join(vowel))
                vowel = []


        word.append("".join(syllable)) #adds syllable to word

    output.append("".join(word)) #adds word to output

print(" ".join(output))
