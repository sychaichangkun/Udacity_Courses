# --------------
# User Instructions
#
# Write a function, compile_word(word), that compiles a word
# of UPPERCASE letters as numeric digits. For example:
# compile_word('YOU') => '(1*U + 10*O +100*Y)' 
# Non-uppercase words should remain unchaged.

def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    # Your code here.
    res = '('
    length = len(word)
    if not re.search('[A-Z]', word):
        return word
    for i in range(length):
        res += str(10**i) + '*' + word[length - 1 - i]
        if i != length - 1:
            res += '+'
    res+=')'    
    return res
