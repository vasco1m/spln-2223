import ply.lex as lex

literals = [':', '-', '+', '\n']
tokens = ['ID', 'ID_LING', 'VAL', 'LINHA_B']

t_ANY_ignore =" "

def t_ID(t):
    r'\w+(?= *:)'

def t_ID_LING(t):
    r'\w+(?= *-)'
    return t

def t_VAL(t):
    r'[^\+\-\:\n ]+[^\+\-\:\n]*'
    return t

def t_LINHA_B(t):
    r'\n\n'
    return t

lexer = lex.lex()
