import collections

# Split word at first space if any
def p_split(S):
    if ' ' in S:
        return [S[:S.find(' ')], S[S.find(' ')+1:]]
    else:
        return S

# Variable to store all commands
log = {}

var = {}

# Read program, i.e. red input into log
while True:
    S = input()
    
    if 'END' in S:
        break
    
    s = p_split(S)
    log[s[0]] = s[1]
    
log = collections.OrderedDict(sorted(log.items()))

# Parse log
for k in log:
    print(k, log[k])
    
    # Let
    
    # Print
