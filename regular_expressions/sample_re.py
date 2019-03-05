import re

print (re.search('ORA-', 'this is a sunny day'))

patterns = ['term1', 'term2']
text = 'This is a string with term1, but not with the other term'

for pattern in patterns:
    print (f"Searching for {pattern} in: \n {text}")

    # check for match
    if re.search(pattern, text):
        print ("\nMatch found\n")
    else:
        print ("\nMatch not found\n")

match = re.search(patterns[0], text)
print (match)
print (match.start())
print (match.end())


#2
split_term = "@"
phrase = "What is your email, is it hello@gmail.com?"

print (re.split(split_term, phrase))
print (phrase.split(split_term))


#3
print (re.findall('match', 'Here is one match, here is anoter match'))


#4 
def multi_re_find(patterns, phrase):
    for pattern in patterns:
        print (f"Searching the phrase using the re-check {pattern}")
        print (re.findall(pattern, phrase))
        print ("\n")

test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns = ['sd*',          # s followed by zero or more d's
                 'sd+',          # s followed by one or more d's
                 'sd?',          # s followed by zero or one d's
                 'sd{3}',        # s followed by three d's
                 'sd{2,3}',      # s followed by two to three d's
                ]

multi_re_find(test_patterns, test_phrase)
