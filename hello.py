
"""
import math

a = 983
b = 834

c = (a**2)+(b**2)
print(c)



s = "HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain."
a = 22
b = 27
c = 97
d = 102

first_phrase = ""
second_phrase = ""

while a <= b and c <= d:
    first_phrase += s[a]
    a += 1
    second_phrase += s[c]
    c += 1

print(first_phrase + " " + second_phrase)


second_phrase = ""
while c <= d:
    second_phrase += s[c]
    c += 1
print(second_phrase)



print(phrase)
print(s[a] + s[a+1] + s[a+2] + s[a+3])
print(s[a])
print(s[b])




s = "hp1J7SkBbjlHGWwfPAGYHRKLpLi2E3aR4lZSUGccPwG1Ya6HbAWIxPdWAHweOyVsBi1HwGnknAfp2YDC3GHo1cojTDcMonodonXyToGMpqRvmD6l2Bs7qIQ7PDLCqhTDqK9Myu53AYhuFBbRLaimegjKIstv7GJJjv6WOsBupETbC9aXKV0mcarnivorus7ehZm"
a = 91
b = 97
c = 180
d = 189

first_phrase = ""
second_phrase = ""

while a <= b:
    first_phrase += s[a]
    a += 1
while c <= d:
    second_phrase += s[c]
    c += 1

print(first_phrase + " " + second_phrase)

a = 22
b = 27
c = 97
d = 102
text =  'HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain'
print (text[a:b+1]+' '+text[c:d+1])

print(text[a:b+1],text[c:d+1])



# Conditions and Loops

a = 4352
b = 9108

list_of_odd_numb = []
list_of_even_numb = []
sum_of_all_odd = int()

for n in range(a,b):
    if n%2 == 1:
        sum_of_all_odd += n
        list_of_odd_numb.append(n)
    else:
        list_of_even_numb.append(n)

print(sum_of_all_odd)



# Working with FIles

text_file = open("rosalind_ini5.txt")

list_of_phrases = []
for phrase in text_file:
    list_of_phrases.append(text_file.readlines())
    for index in range(1,40):
        if index%2 == 0:
            print(list_of_phrases[index])
print(list_of_phrases)



for index in range(1000):
    if index % 2 == 1:
        print(text_file.readlines(index))




text_file = open("rosalind_ini5.txt", "r")
list_text = []

for phrase in text_file.readlines():
    list_text.append(phrase)
for index in range(len(list_text)):
    if index % 2 == 1:
        print(list_text[index])



amino_acidConversion = {
    "Ala": "Alanine",
    "Arg": "Arginine",
    "Asn": "Asparagine",
    "Asp": "Aspartic acid",
    "Cys": "Cysteine",
    "Glu": "Glutamic acid",
    "Gln": "Glutamine",
    "Gly": "Glycine",
    "His": "His",
    "Ile": "Isoleucine",
    "Leu": "Leucine",
    "Lys": "Lysine",
    "Met": "Methionine",
    "Phe": "Phenylalanine",
    "Pro": "Proline",
    "Ser": "Serine",
    "Thr": "Threonine",
    "Trp": "Tryptophan",
    "Tyr": "Tyrosine",
    "Val": "Valine",
}

print(amino_acidConversion.get("ler", "Not a valid amino acid abbreviation."))

amino_acidConversion["Ler"] = 1
amino_acidConversion["Ler"] += 1
print(amino_acidConversion)

"""



text_file = open("rosalind_ini6.txt", "r")
words_dictionary = {}

for word in text_file.readline().split():
    if word not in words_dictionary:
        words_dictionary[word] = 1
    else:
        words_dictionary[word] += 1

print(words_dictionary)
for key, value in words_dictionary.items():
    print(str(key) + " " + str(value))

