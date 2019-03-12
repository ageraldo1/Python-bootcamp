import re

str = '''
Adam Wayne, the conqueror, 
with his face flung back and his mane like a lion's, 

stood with his great sword point upwards, 

the red raiment of his office 


flapping around him like the red wings of an archangel. And the King saw, he knew not how, something new and overwhelming. The great green trees and the great red robes swung together in the wind. The preposterous masquerade, born of his own mockery, towered over him and embraced the world. This was the normal, this was sanity, this was nature, and he himself, with his rationality, and his detachment and his black frock-coat, he was the exception and the accident a blot of black upon a world of crimson and gold.
'''

pattern = re.compile(r'\w+')  # words
matches = pattern.finditer(str)

word_count = len(tuple(matches))
print (f"Approximate Word Count : {word_count}")


pattern = re.compile(r'[^\.\!\?]*[\.\!\?]')
matches = pattern.finditer(str)

sentence_count = len(tuple(matches))
print (f"Approximate Sentence Count : {sentence_count}")

pattern = re.compile(r'[A-Za-z]')
matches = pattern.finditer(str)
letter_count = len(tuple(matches))
print (f"Average Letter Count : {letter_count/word_count:,.1f}")

sentence_len = len(re.split("(?<=[.!?]) +", str))
print (re.split("(?<=[.!?]) +", str))

print (f"Average Sentence Length : {word_count/sentence_len:,.1f}")

#pattern = re.compile('(?<=[.!?]) +')
#matches = pattern.finditer(str)
#print(len(tuple(matches)))
#print (sentence_len)
#print (tuple(matches))


#matches = pattern.finditer(str)
#print (matches.groups())
