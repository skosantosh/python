import re
# patterns = ['term1', 'term2']

text = ' this is a string with term1, not the other!'
"""
for pattern in patterns:
    print("I'm searching for : "+pattern)

    if re.search(pattern, text):
        print('Match!')
    else:
        print('No Match!')
"""
re.match = re.search('term1', text)

print(re.match.start())


split_term = '@'
email = 'user@gmail.com'.split('@')

print(email)
# print(re.split(split_term, email)) # doesn't work

# find matching
fultext = 'test pharase match in match middle match'
print(re.findall('match', fultext))


def multi_re_find(patterns, pharase):

    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat, pharase))
        print('\n')


test_pharase = 'sdsd..sssddd..sdddsddd...dssssss...sddddd'
# for best result try to uncommet each but run one at a time
# test_patterns = ['sd{1,3}']
# test_patterns = ['sd{3}']
# test_patterns = ['sd+']
test_patterns = ['s[sd]+']
multi_re_find(test_patterns, test_pharase)


test_pharasess = ' This is a string! But is has punctuation. How can we\
remove it?'
# for best result try to uncommet each but run one at a time
# test_patternss = ['[^!.?]+']
# test_patternss = ['[a-z]+']
test_patternss = ['[A-Z]+']
multi_re_find(test_patternss, test_pharasess)

test_pharasesss = 'This is a string! with number 123456 and symbol #hashtag '
# for best result try to uncommet each but run one at a time
# test_patternsss = [r'\d+'] # digit
# test_patternsss = [r'\D+'] # not digit
# test_patternsss = [r'\s+'] # white space
# test_patternsss = [r'\S+'] # non white space
# test_patternsss = [r'\w+']  # alpha numeric (letter and number)
test_patternsss = [r'\W+']  # non alpha numeric (letter and number)
multi_re_find(test_patternsss, test_pharasesss)
