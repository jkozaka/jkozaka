
import random
##### CONFIG AREA

words = 5 #amount of words to generate
syllables = 3 #amount of syllables
struct = [True,False] #true is consoant #false is vowel.
            #if consoan is x, and structure is [true ,true], syllable is xx. not new randoms

cons = 1 #amount of consoants in syllable
vows = 1 #amount of vowels in syllable

##### CODE

consoants = "bcdfghjklmnpqrstvwxyz" #config possible
vowels = "aeiou"                    #

output = []

for x in range(0,words):
    word = []

    for a in range(0,syllables): #add syllables

        syllable = [] #
        consoant = [] # filled later
        vowel = []    #

        for b in range(0,cons): #add consoants
            consoant.append(random.choice(consoants))

        for c in range(0,vows): #add vowels
            vowel.append(random.choice(vowels))

        for d in range(0,len(struct)): #builds syllable

            if struct[d]: #if consoant
                syllable.append("".join(consoant))

            else: #if vowel
                syllable.append("".join(vowel))

        word.append("".join(syllable)) #adds syllable to word

    output.append("".join(word)) #adds word to output

print(" ".join(output))
