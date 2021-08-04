#! /usr/bin/env python



import re
import mysrc
import glob
import math
import time
start_time = time.time()

def basicCheck(token):
    type=''
    varPtrn = re.compile(r"[a-zA-Z_][a-zA-Z0-9_]")  # variables
    headerPtrn = re.compile(r"\w[a-zA-Z]+[.]h")  # header files
    digitPtrn = re.compile(r'\d')
    floatPtrn = re.compile(r'\d+[.]\d+')

    if token in mysrc.keywords():
        # print(token + " KEYWORD")
        type="KEYWORD"
    elif token in mysrc.operators().keys():
        # print(token + " ", mysrc.operators()[token])
        type=mysrc.operators()[token]
    elif token in mysrc.delimiters():
        description = mysrc.delimiters()[token]
        if description == 'TAB' or description == 'NEWLINE':
            # print(description)
            type=description
        else:
            # print(token + " ", description)
            type=description
    elif re.search(headerPtrn, token):
        # print(token + " HEADER")
        type="HEADER"
    elif re.match(varPtrn, token) or "'" in token or '"' in token:
        # print(token + ' IDENTIFIER' )
        type="IDENTIFIER"
    elif re.match(digitPtrn, token):
        if re.match(floatPtrn, token):
            # print(token + ' FLOAT')
            type="FLOAT"
        else:
            # print(token + ' INT')
            type="INT"

    return type

def delimiterCorrection(line):
    tokens = line.split(" ")
    for delimiter in mysrc.delimiters().keys():
        for token in tokens:
            if token == delimiter:
                pass
            elif delimiter in token:
                pos = token.find(delimiter)
                tokens.remove(token)
                token = token.replace(delimiter, " ")
                extra = token[:pos]
                token = token[pos + 1 :]
                tokens.append(delimiter)
                tokens.append(extra)
                tokens.append(token)
            else:
                pass
    for token in tokens:
        if isWhiteSpace(token):
            tokens.remove(token)
        elif ' ' in token:
            tokens.remove(token)
            token = token.split(' ')
            for d in token:
                tokens.append(d)
    return tokens

def isWhiteSpace(word):
    ptrn = [ " ", "\t", "\n"]
    for item in ptrn:
        if word == item:
            return True
        else:
            return False

def hasWhiteSpace(token):
    ptrn = ['\t', '\n']
    if isWhiteSpace(token) == False:
        for item in ptrn:
            if item in token:
                result = "'" + item + "'"
                return result
            else:
                pass
    return False

def tokenize(path):
    alltokens=[]
    try:
        f = open(path).read()
        lines = f.split("\n")
        count = 0
        for line in lines:
            count = count + 1
            tokens = delimiterCorrection(line)
            for token in tokens:
                alltokens.append(basicCheck(token))
        filter_object = filter(lambda x: x != '', alltokens)
        return list(filter_object)

    except FileNotFoundError:
        print("\nInvald Path. Retry")
       

# def run():
#     path = input("Enter Source Code's Path: ")
#     tokenize(path)
#     again = int(input("""\n1. Retry\n2. Quit\n"""))
#     if again == 1:
#         run()
#     elif again == 2:
#         print("Quitting...")
#     else:
#         print('Invalid Request.')
#         run()

# run()


# print(tokenlist)










# a=['IDENTIFIER', 'IDENTIFIER', 'KEYWORD', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'KEYWORD', 'IDENTIFIER', 'SEMICOL', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'KEYWORD', 'IDENTIFIER', 'COLON', 'KEYWORD', 'IDENTIFIER', 'LCBRACE', 'COLON', 'TAB', 'KEYWORD', 'TAB', 'IDENTIFIER', 'KEYWORD', 'KEYWORD', 'MUL', 'IDENTIFIER', 'LCBRACE', 'LPAR', 'RPAR', 'IDENTIFIER', 'IDENTIFIER', 'SEMICOL', 'TAB', 'KEYWORD', 'TAB', 'RCBRACE', 'TAB', 'RCBRACE', 'SEMICOL', 'KEYWORD', 'IDENTIFIER', 'COLON', 'KEYWORD', 'IDENTIFIER', 'LCBRACE', 'COLON', 'TAB', 'KEYWORD', 'KEYWORD', 'MUL', 'IDENTIFIER', 'LCBRACE', 'TAB', 'KEYWORD', 'LPAR', 'RPAR', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'SEMICOL', 'TAB', 'KEYWORD', 'TAB', 'RCBRACE', 'TAB', 'RCBRACE', 'SEMICOL', 'KEYWORD', 'IDENTIFIER', 'COLON', 'KEYWORD', 'IDENTIFIER', 'LCBRACE', 'COLON', 'TAB', 'KEYWORD', 'KEYWORD', 'MUL', 'IDENTIFIER', 'LCBRACE', 'TAB', 'KEYWORD', 'LPAR', 'RPAR', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'SEMICOL', 'TAB', 'KEYWORD', 'TAB', 'RCBRACE', 'TAB', 'RCBRACE', 'SEMICOL', 'KEYWORD', 'IDENTIFIER', 'COLON', 'KEYWORD', 'IDENTIFIER', 'LCBRACE', 'COLON', 'TAB', 'KEYWORD', 'KEYWORD', 'MUL', 'IDENTIFIER', 'LCBRACE', 'TAB', 'KEYWORD', 'LPAR', 'RPAR', 'IDENTIFIER', 'IDENTIFIER', 'SEMICOL', 'TAB', 'KEYWORD', 'TAB', 'RCBRACE', 'TAB', 'RCBRACE', 'SEMICOL', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'KEYWORD', 'IDENTIFIER', 'LCBRACE', 'TAB', 'COLON', 'TAB', 'KEYWORD', 'MUL', 'IDENTIFIER', 'SEMICOL', 'TAB', 'KEYWORD', 'IDENTIFIER', 'SEMICOL', 'TAB', 'KEYWORD', 'SEMICOL', 'TAB', 'IDENTIFIER', 'COLON', 'TAB', 'KEYWORD', 'TAB', 'LPAR', 'IDENTIFIER', 'RPAR', 'LCBRACE', 'RCBRACE', 'COLON', 'COMMA', 'IDENTIFIER', 'IDENTIFIER', 'INT', 'TAB', 'LPAR', 'IDENTIFIER', 'KEYWORD', 'RPAR', 'IDENTIFIER', 'LCBRACE', 'LCBRACE', 'TAB', 'LPAR', 'IDENTIFIER', 'RPAR', 'INT', 'KEYWORD', 'ASSIGN', 'IDENTIFIER', 'SEMICOL', 'TAB', 'IDENTIFIER', 'ASSIGN', 'IDENTIFIER', 'KEYWORD', 'SEMICOL', 'TAB', 'LBRACE', 'RBRACE', 'IDENTIFIER', 'IDENTIFIER', 'SEMICOL', 'IDENTIFIER', 'SEMICOL', 'LCBRACE', 'TAB', 'LPAR', 'KEYWORD', 'RPAR', 'ASSIGN', 'INT', 'KEYWORD', 'ASSIGN', 'IDENTIFIER', 'IDENTIFIER', 'SEMICOL', 'TAB', 'LBRACE', 'RBRACE', 'IDENTIFIER', 'TAB', 'RCBRACE', 'TAB', 'TAB', 'RCBRACE', 'LCBRACE', 'TAB', 'KEYWORD', 'IDENTIFIER', 'TAB', 'ASSIGN', 'INT', 'SEMICOL', 'TAB', 'IDENTIFIER', 'ASSIGN', 'INT', 'SEMICOL', 'TAB', 'IDENTIFIER', 'TAB', 'IDENTIFIER', 'IDENTIFIER', 'SEMICOL', 'TAB', 'IDENTIFIER', 'TAB', 'TAB', 'RCBRACE', 'TAB', 'TAB', 'RCBRACE', 'IDENTIFIER', 'LCBRACE', 'TAB', 'IDENTIFIER', 'LPAR', 'KEYWORD', 'RPAR', 'IDENTIFIER', 'ASSIGN', 'IDENTIFIER', 'SEMICOL', 'TAB', 'IDENTIFIER', 'ASSIGN', 'IDENTIFIER', 'KEYWORD', 'SEMICOL', 'TAB', 'LBRACE', 'RBRACE', 'IDENTIFIER', 'IDENTIFIER', 'COMMA', 'IDENTIFIER', 'COMMA', 'MUL', 'SEMICOL', 'TAB', 'LPAR', 'KEYWORD', 'LPAR', 'IDENTIFIER', 'RPAR', 'IDENTIFIER', 'RPAR', 'KEYWORD', 'IDENTIFIER', 'TAB', 'TAB', 'TAB', 'RCBRACE', 'IDENTIFIER', 'ASSIGN', 'IDENTIFIER', 'LCBRACE', 'TAB', 'IDENTIFIER', 'LPAR', 'KEYWORD', 'RPAR', 'IDENTIFIER', 'LCBRACE', 'TAB', 'LPAR', 'IDENTIFIER', 'RPAR', 'ASSIGN', 'KEYWORD', 'ASSIGN', 'IDENTIFIER', 'SEMICOL', 'TAB', 'IDENTIFIER', 'IDENTIFIER', 'SEMICOL', 'TAB', 'LBRACE', 'RBRACE', 'KEYWORD', 'ASSIGN', 'IDENTIFIER', 'KEYWORD', 'SEMICOL', 'TAB', 'LBRACE', 'RBRACE', 'IDENTIFIER', 'IDENTIFIER', 'COMMA', 'IDENTIFIER', 'COMMA', 'MUL', 'SEMICOL', 'TAB', 'LPAR', 'IDENTIFIER', 'LPAR', 'KEYWORD', 'RPAR', 'IDENTIFIER', 'RPAR', 'KEYWORD', 'IDENTIFIER', 'TAB', 'TAB', 'RCBRACE', 'SEMICOL', 'TAB', 'KEYWORD', 'TAB', 'TAB', 'RCBRACE', 'TAB', 'LPAR', 'RPAR', 'LCBRACE', 'INT', 'AND', 'IDENTIFIER', 'INT', 'RPAR', 'LCBRACE', 'TAB', 'LPAR', 'IDENTIFIER', 'ASSIGN', 'ASSIGN', 'KEYWORD', 'ASSIGN', 'INT', 'SEMICOL', 'TAB', 'IDENTIFIER', 'IDENTIFIER', 'SEMICOL', 'TAB', 'KEYWORD', 'ASSIGN', 'INT', 'SEMICOL', 'TAB', 'IDENTIFIER', 'TAB', 'RCBRACE', 'TAB', 'TAB', 'RCBRACE', 'IDENTIFIER', 'COMMA', 'KEYWORD', 'IDENTIFIER', 'RPAR', 'LCBRACE', 'TAB', 'KEYWORD', 'LPAR', 'IDENTIFIER', 'KEYWORD', 'ASSIGN', 'IDENTIFIER', 'SEMICOL', 'TAB', 'LBRACE', 'RBRACE', 'IDENTIFIER', 'IDENTIFIER', 'TAB', 'RCBRACE', 'TAB', 'IDENTIFIER', 'IDENTIFIER', 'RPAR', 'LCBRACE', 'TAB', 'KEYWORD', 'LPAR', 'KEYWORD', 'TAB', 'LPAR', 'IDENTIFIER', 'RPAR', 'IDENTIFIER', 'LCBRACE', 'KEYWORD', 'IDENTIFIER', 'SEMICOL', 'TAB', 'IDENTIFIER', 'ASSIGN', 'SEMICOL', 'TAB', 'IDENTIFIER', 'ASSIGN', 'IDENTIFIER', 'SEMICOL', 'TAB', 'IDENTIFIER', 'IDENTIFIER', 'SEMICOL', 'TAB', 'LBRACE', 'RBRACE', 'KEYWORD', 'ASSIGN', 'IDENTIFIER', 'KEYWORD', 'SEMICOL', 'TAB', 'LBRACE', 'RBRACE', 'IDENTIFIER', 'IDENTIFIER', 'COMMA', 'IDENTIFIER', 'COMMA', 'MUL', 'SEMICOL', 'TAB', 'LPAR', 'KEYWORD', 'LPAR', 'IDENTIFIER', 'RPAR', 'IDENTIFIER', 'RPAR', 'KEYWORD', 'IDENTIFIER', 'SEMICOL', 'IDENTIFIER', 'SEMICOL', 'TAB', 'LPAR', 'KEYWORD', 'RPAR', 'LCBRACE', 'ASSIGN', 'IDENTIFIER', 'KEYWORD', 'ASSIGN', 'IDENTIFIER', 
#  'IDENTIFIER', 'SEMICOL', 'TAB', 'LBRACE', 'RBRACE', 'IDENTIFIER', 'TAB', 'RCBRACE', 'TAB', 'RCBRACE', 'LCBRACE', 'TAB', 'KEYWORD', 'IDENTIFIER', 'TAB', 'IDENTIFIER', 'IDENTIFIER', 'SEMICOL', 'TAB', 'IDENTIFIER', 'TAB', 'RCBRACE', 'TAB', 'RCBRACE', 'IDENTIFIER', 'LCBRACE', 'TAB', 'KEYWORD', 'LPAR', 'KEYWORD', 'RPAR', 'IDENTIFIER', 'LBRACE', 'RBRACE', 'IDENTIFIER', 'TAB', 'LPAR', 'IDENTIFIER', 'RPAR', 'LCBRACE', 'KEYWORD', 'IDENTIFIER', 'TAB', 'IDENTIFIER', 'TAB', 'SEMICOL', 'IDENTIFIER', 'IDENTIFIER', 'TAB', 'RCBRACE', 'KEYWORD', 'INT', 'TAB', 'LPAR', 'IDENTIFIER', 'RPAR', 'LCBRACE', 'KEYWORD', 'IDENTIFIER', 'IDENTIFIER', 'SEMICOL', 'TAB', 'IDENTIFIER', 'TAB', 'RCBRACE', 'LCBRACE', 'TAB', 'KEYWORD', 'SEMICOL', 'TAB', 'LBRACE', 'IDENTIFIER', 'RBRACE', 'IDENTIFIER', 'KEYWORD', 'TAB', 'RCBRACE', 'TAB', 'RCBRACE', 'KEYWORD', 'IDENTIFIER', 'TAB', 'KEYWORD', 'LPAR', 'KEYWORD', 'RPAR', 'IDENTIFIER', 'LBRACE', 'RBRACE', 'LCBRACE', 'KEYWORD', 'IDENTIFIER', 'RPAR', 'LCBRACE', 'TAB', 'LPAR', 'IDENTIFIER', 'KEYWORD', 'TAB', 'IDENTIFIER', 'IDENTIFIER', 'SEMICOL', 'TAB', 'IDENTIFIER', 'TAB', 'RCBRACE', 'LCBRACE', 'TAB', 'LPAR', 'KEYWORD', 'IDENTIFIER', 'RPAR', 'INT', 'KEYWORD', 'IDENTIFIER', 'IDENTIFIER', 'SEMICOL', 'TAB', 'IDENTIFIER', 'TAB', 'RCBRACE', 'LCBRACE', 'TAB', 'KEYWORD', 'SEMICOL', 'TAB', 'LBRACE', 'IDENTIFIER', 'RBRACE', 'IDENTIFIER', 'KEYWORD', 'TAB', 'RCBRACE', 'TAB', 'RCBRACE', 'TAB', 'IDENTIFIER', 'IDENTIFIER', 'RPAR', 'LCBRACE', 'TAB', 'KEYWORD', 'LPAR', 'KEYWORD', 'PLUS', 'INT', 'RPAR', 'SEMICOL', 'TAB', 'LPAR', 'IDENTIFIER', 'IDENTIFIER', 'ASSIGN', 'IDENTIFIER', 'SEMICOL', 'TAB', 'LBRACE', 'RBRACE', 'IDENTIFIER', 'IDENTIFIER', 'TAB', 'TAB', 'RCBRACE', 'TAB', 'IDENTIFIER', 'KEYWORD', 'LCBRACE', 'TAB', 'KEYWORD', 'LPAR', 'RPAR', 'IDENTIFIER', 'SEMICOL', 'TAB', 'KEYWORD', 'TAB', 'RCBRACE', 'IDENTIFIER', 'IDENTIFIER', 'OUT', 'LPAR', 'IDENTIFIER', 'COMMA', 'KEYWORD', 'IDENTIFIER', 'IDENTIFIER', 'RPAR', 'SEMICOL', 'TAB', 'IDENTIFIER', 'IDENTIFIER', 'IN', 'LPAR', 'KEYWORD', 'IDENTIFIER', 'IDENTIFIER', 'COMMA', 'KEYWORD', 'IDENTIFIER', 'RPAR', 'SEMICOL', 'TAB', 'IDENTIFIER', 'TAB', 'TAB', 'RCBRACE', 'SEMICOL', 'IDENTIFIER', 'IDENTIFIER', 'OUT', 'COMMA', 'KEYWORD', 'IDENTIFIER', 'LCBRACE', 'LPAR', 'IDENTIFIER', 'RPAR', 'IDENTIFIER', 'ASSIGN', 'INT', 'SEMICOL', 'IDENTIFIER', 'SEMICOL', 'LCBRACE', 'TAB', 'KEYWORD', 'LPAR', 'KEYWORD', 'RPAR', 'INC', 'OUT', 'SEMICOL', 'TAB', 'LBRACE', 'IDENTIFIER', 'RBRACE', 'IDENTIFIER', 'TAB', 'RCBRACE', 'IDENTIFIER', 'SEMICOL', 'TAB', 'KEYWORD', 'RCBRACE', 'IDENTIFIER', 'IN', 'IDENTIFIER', 'IDENTIFIER', 'COMMA', 'KEYWORD', 'IDENTIFIER', 'RPAR', 'LCBRACE', 'LPAR', 'KEYWORD', 'SEMICOL', 'IDENTIFIER', 'LCBRACE', 'TAB', 'KEYWORD', 'LPAR', 'KEYWORD', 'RPAR', 'INC', 'ASSIGN', 'INT', 'SEMICOL', 'ASSIGN', 'IDENTIFIER', 'SEMICOL', 'TAB', 'LBRACE', 'RBRACE', 'IDENTIFIER', 'TAB', 'RCBRACE', 'RCBRACE', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'KEYWORD', 'IDENTIFIER', 'LCBRACE', 'COLON', 'TAB', 'KEYWORD', 'IDENTIFIER', 'SEMICOL', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'TAB', 'IDENTIFIER', 'COLON', 'TAB', 'KEYWORD', 'IDENTIFIER', 'TAB', 'COLON', 'LCBRACE', 'TAB', 'LPAR', 'RPAR', 'LPAR', 'IDENTIFIER', 'RPAR', 'INT', 'IDENTIFIER', 'TAB', 'RCBRACE', 'IDENTIFIER', 'RPAR', 'LCBRACE', 'TAB', 'LPAR', 'IDENTIFIER', 'IDENTIFIER', 'SEMICOL', 'TAB', 'LPAR', 'RPAR', 'IDENTIFIER', 'IDENTIFIER', 'SEMICOL', 'SEMICOL', 'LCBRACE', 'TAB', 'LPAR', 'KEYWORD', 'LPAR', 'IDENTIFIER', 'RPAR', 'RPAR', 'ASSIGN', 'INT', 'KEYWORD', 'ASSIGN', 'SEMICOL', 'TAB', 'LBRACE', 'IDENTIFIER', 'LBRACE', 'RBRACE', 'RBRACE', 'IDENTIFIER', 'TAB', 'RCBRACE', 'TAB', 'TAB', 'RCBRACE', 'IDENTIFIER', 'KEYWORD', 'IDENTIFIER', 'IDENTIFIER', 'TAB', 'IDENTIFIER', 'RPAR', 'LCBRACE', 'TAB', 'LPAR', 'IDENTIFIER', 'IDENTIFIER', 'SEMICOL', 'TAB', 'LPAR', 'RPAR', 'IDENTIFIER', 'IDENTIFIER', 'SEMICOL', 'SEMICOL', 'LCBRACE', 'TAB', 'LPAR', 'KEYWORD', 'LPAR', 'IDENTIFIER', 'RPAR', 'RPAR', 'ASSIGN', 'INT', 'KEYWORD', 'ASSIGN', 'SEMICOL', 'TAB', 'LBRACE', 'IDENTIFIER', 'LBRACE', 'RBRACE', 'RBRACE', 'IDENTIFIER', 'TAB', 'RCBRACE', 'TAB', 'RCBRACE', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'KEYWORD', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'TAB', 'LCBRACE', 'TAB', 'LPAR', 'IDENTIFIER', 'RPAR', 'IDENTIFIER', 'IDENTIFIER', 'ASSIGN', 'KEYWORD', 'SEMICOL', 'IDENTIFIER', 'IDENTIFIER', 'TAB', 'KEYWORD', 'SEMICOL', 'SEMICOL', 'LCBRACE', 'TAB', 'LPAR', 'KEYWORD', 'LPAR', 'IDENTIFIER', 'RPAR', 'RPAR', 'ASSIGN', 'INT', 'KEYWORD', 'ASSIGN', 'INT', 'SEMICOL', 'LCBRACE', 'TAB', 'LPAR', 'KEYWORD', 'LPAR', 'IDENTIFIER', 'RPAR', 'RPAR', 'SEMICOL', 'KEYWORD', 'AND', 'IDENTIFIER', 'KEYWORD', 'AND', 'IDENTIFIER', 'IDENTIFIER', 'TAB', 'LPAR', 'RPAR', 'LCBRACE', 'LBRACE', 'IDENTIFIER', 'LBRACE', 'IDENTIFIER', 'LBRACE', 'IDENTIFIER', 'RBRACE', 'RBRACE', 'RBRACE', 'ASSIGN', 'ASSIGN', 'ASSIGN', 'KEYWORD', 'ASSIGN',
#   'KEYWORD', 'SEMICOL', 'TAB', 'IDENTIFIER', 'TAB', 'RCBRACE', 'KEYWORD', 'AND', 'AND', 'IDENTIFIER', 'IDENTIFIER', 'RPAR', 'LCBRACE', 'TAB', 'LPAR', 'IDENTIFIER', 'LBRACE', 'IDENTIFIER', 'LBRACE', 'IDENTIFIER', 'LBRACE', 'IDENTIFIER', 'RBRACE', 'RBRACE', 'RBRACE', 'ASSIGN', 'ASSIGN', 'KEYWORD', 'ASSIGN', 'IDENTIFIER', 'SEMICOL', 'TAB', 'LBRACE', 'RBRACE', 'IDENTIFIER', 'TAB', 'RCBRACE', 'TAB', 'RCBRACE', 'ASSIGN', 'KEYWORD', 'SEMICOL', 'TAB', 'IDENTIFIER', 'TAB', 'RCBRACE', 'IDENTIFIER', 'SEMICOL', 'KEYWORD', 'IDENTIFIER', 'TAB', 'KEYWORD', 'TAB', 'RCBRACE', 'RCBRACE', 'SEMICOL', 'KEYWORD', 'IDENTIFIER', 'IDENTIFIER', 'LCBRACE', 'LPAR', 'KEYWORD', 'RPAR', 'LBRACE', 'IDENTIFIER', 'RBRACE', 'COMMA', 'IDENTIFIER', 'LCBRACE', 'TAB', 'KEYWORD', 'LCBRACE', 'TAB', 'LPAR', 'IDENTIFIER', 'RPAR', 'INT', 'KEYWORD', 'OUT', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'TAB', 'IDENTIFIER', 'SEMICOL', 'IDENTIFIER', 'TAB', 'KEYWORD', 'SEMICOL', 'TAB', 'RCBRACE', 'IDENTIFIER', 'IDENTIFIER', 'TAB', 'IDENTIFIER', 'LPAR', 'IDENTIFIER', 'RPAR', 'SEMICOL', 'LBRACE', 'IDENTIFIER', 'RBRACE', 'INT', 'IDENTIFIER', 'ASSIGN', 'TAB', 'IDENTIFIER', 'SEMICOL', 'IDENTIFIER', 'TAB', 'IDENTIFIER', 'SEMICOL', 'IDENTIFIER', 'TAB', 'LPAR', 'RPAR', 'IDENTIFIER', 'SEMICOL', 'IDENTIFIER', 'IDENTIFIER', 'KEYWORD', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'KEYWORD', 
#  'IDENTIFIER', 'TAB', 'LCBRACE', 'TAB', 'KEYWORD', 'LPAR', 'RPAR', 'IDENTIFIER', 'KEYWORD', 'LPAR', 'RPAR', 'IDENTIFIER', 'LCBRACE', 'COMMA', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'TAB', 'IDENTIFIER', 'IDENTIFIER', 'SEMICOL', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'LPAR', 'RPAR', 'IDENTIFIER', 'IDENTIFIER', 'ASSIGN', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'KEYWORD', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'TAB', 'LPAR', 'IDENTIFIER', 'RPAR', 'SEMICOL', 'IDENTIFIER', 'SEMICOL', 'SEMICOL', 'LCBRACE', 'TAB', 'LPAR', 'KEYWORD', 'LPAR', 'IDENTIFIER', 'RPAR', 'RPAR', 'ASSIGN', 'INT', 'KEYWORD', 'OUT', 'SEMICOL', 'TAB', 'LBRACE', 'IDENTIFIER', 'RBRACE', 'IDENTIFIER', 'OUT', 'SEMICOL', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'TAB', 'LBRACE', 'IDENTIFIER', 'RBRACE', 'IDENTIFIER', 'TAB', 'RCBRACE', 'RCBRACE', 'SEMICOL', 'LPAR', 'IDENTIFIER', 'RPAR', 'RCBRACE', 'KEYWORD', 'LCBRACE', 'OUT', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'TAB', 'IDENTIFIER', 'SEMICOL', 'IDENTIFIER', 'TAB', 'RCBRACE', 'SEMICOL', 'TAB', 'LPAR', 'IDENTIFIER', 'RPAR', 'TAB', 'TAB', 'RCBRACE', 'MUL', 'IDENTIFIER', 'RPAR', 'LCBRACE', 'TAB', 'KEYWORD', 'LPAR', 'IDENTIFIER', 'OUT', 'TAB', 'LPAR', 'IDENTIFIER', 'RPAR', 'SEMICOL', 'IDENTIFIER', 'TAB', 'RCBRACE', 'RCBRACE']

# b=['IDENTIFIER', 'IDENTIFIER', 'KEYWORD', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'KEYWORD', 'IDENTIFIER', 'SEMICOL', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'KEYWORD', 'IDENTIFIER', 'COLON', 'KEYWORD', 'IDENTIFIER', 'LCBRACE', 'COLON', 'TAB', 'KEYWORD', 'TAB', 'IDENTIFIER', 'KEYWORD', 'KEYWORD', 'MUL', 'IDENTIFIER', 'LCBRACE', 'LPAR', 'RPAR', 'IDENTIFIER', 'IDENTIFIER', 'SEMICOL', 'TAB', 'KEYWORD', 'TAB', 'RCBRACE', 'TAB', 'RCBRACE', 'SEMICOL', 'KEYWORD', 'IDENTIFIER', 'COLON', 'KEYWORD', 'IDENTIFIER', 'LCBRACE', 'COLON', 'TAB', 'KEYWORD', 'KEYWORD', 'MUL', 'IDENTIFIER', 'LCBRACE', 'TAB', 'KEYWORD', 'LPAR', 'RPAR', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'SEMICOL', 'TAB', 'KEYWORD', 'TAB', 'RCBRACE', 'TAB', 'RCBRACE', 'SEMICOL', 'KEYWORD', 'IDENTIFIER', 'COLON', 'KEYWORD', 'IDENTIFIER', 'LCBRACE', 'COLON', 'TAB', 'KEYWORD', 'KEYWORD', 'MUL', 'IDENTIFIER', 'LCBRACE', 'TAB', 'KEYWORD', 'LPAR', 'RPAR', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'SEMICOL', 'TAB', 'KEYWORD', 'TAB', 'RCBRACE', 'TAB', 'RCBRACE', 'SEMICOL', 'KEYWORD', 'IDENTIFIER', 'COLON', 'KEYWORD', 'IDENTIFIER', 'LCBRACE', 'COLON', 'TAB', 'KEYWORD', 'KEYWORD', 'MUL', 'IDENTIFIER', 'LCBRACE', 'TAB', 'KEYWORD', 'LPAR', 'RPAR', 'IDENTIFIER', 'IDENTIFIER', 'SEMICOL', 'TAB', 'KEYWORD', 'TAB', 'RCBRACE', 'TAB', 'RCBRACE', 'SEMICOL', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'KEYWORD', 'IDENTIFIER', 'LCBRACE', 'TAB', 'COLON', 'TAB', 'KEYWORD', 'MUL', 'IDENTIFIER', 'SEMICOL', 'TAB', 'KEYWORD', 'IDENTIFIER', 'SEMICOL', 'TAB', 'KEYWORD', 'SEMICOL', 'TAB', 'IDENTIFIER', 'COLON', 'TAB', 'KEYWORD', 'TAB', 'LPAR', 'IDENTIFIER', 'RPAR', 'LCBRACE', 'RCBRACE', 'COLON', 'COMMA', 'IDENTIFIER', 'IDENTIFIER', 'INT', 'TAB', 'LPAR', 'IDENTIFIER', 'KEYWORD', 'RPAR', 'IDENTIFIER', 'LCBRACE', 'LCBRACE', 'TAB', 'LPAR', 'IDENTIFIER', 'RPAR', 'INT', 'KEYWORD', 'ASSIGN', 'IDENTIFIER', 'SEMICOL', 'TAB', 'IDENTIFIER', 'ASSIGN', 'IDENTIFIER', 'KEYWORD', 'SEMICOL', 'TAB', 'LBRACE', 'RBRACE', 'IDENTIFIER', 'IDENTIFIER', 'SEMICOL', 'IDENTIFIER', 'SEMICOL', 'LCBRACE', 'TAB', 'LPAR', 'KEYWORD', 'RPAR', 'ASSIGN', 'INT', 'KEYWORD', 'ASSIGN', 'IDENTIFIER', 'IDENTIFIER', 'SEMICOL', 'TAB', 'LBRACE', 'RBRACE', 'IDENTIFIER', 'TAB', 'RCBRACE', 'TAB', 'TAB', 'RCBRACE', 'LCBRACE', 'TAB', 'KEYWORD', 'IDENTIFIER', 'TAB', 'ASSIGN', 'INT', 'SEMICOL', 'TAB', 'IDENTIFIER', 'ASSIGN', 'INT', 'SEMICOL', 'TAB', 'IDENTIFIER', 'TAB', 'IDENTIFIER', 'IDENTIFIER', 'SEMICOL', 'TAB', 'IDENTIFIER', 'TAB', 'TAB', 'RCBRACE', 'TAB', 'TAB', 'RCBRACE', 'IDENTIFIER', 'LCBRACE', 'TAB', 'IDENTIFIER', 'LPAR', 'KEYWORD', 'RPAR', 'IDENTIFIER', 'ASSIGN', 'IDENTIFIER', 'SEMICOL', 'TAB', 'IDENTIFIER', 'ASSIGN', 'IDENTIFIER', 'KEYWORD', 'SEMICOL', 'TAB', 'LBRACE', 'RBRACE', 'IDENTIFIER', 'IDENTIFIER', 'COMMA', 'IDENTIFIER', 'COMMA', 'MUL', 'SEMICOL', 'TAB', 'LPAR', 'KEYWORD', 'LPAR', 'IDENTIFIER', 'RPAR', 'IDENTIFIER', 'RPAR', 'KEYWORD', 'IDENTIFIER', 'TAB', 'TAB', 'TAB', 'RCBRACE', 'IDENTIFIER', 'ASSIGN', 'IDENTIFIER', 'LCBRACE', 'TAB', 'IDENTIFIER', 'LPAR', 'KEYWORD', 'RPAR', 'IDENTIFIER', 'LCBRACE', 'TAB', 'LPAR', 'IDENTIFIER', 'RPAR', 'ASSIGN', 'KEYWORD', 'ASSIGN', 'IDENTIFIER', 'SEMICOL', 'TAB', 'IDENTIFIER', 'IDENTIFIER', 'SEMICOL', 'TAB', 'LBRACE', 'RBRACE', 'KEYWORD', 'ASSIGN', 'IDENTIFIER', 'KEYWORD', 'SEMICOL', 'TAB', 'LBRACE', 'RBRACE', 'IDENTIFIER', 'IDENTIFIER', 'COMMA', 'IDENTIFIER', 'COMMA', 'MUL', 'SEMICOL', 'TAB', 'LPAR', 'IDENTIFIER', 'LPAR', 'KEYWORD', 'RPAR', 'IDENTIFIER', 'RPAR', 'KEYWORD', 'IDENTIFIER', 'TAB', 'TAB', 'RCBRACE', 'SEMICOL', 'TAB', 'KEYWORD', 'TAB', 'TAB', 'RCBRACE', 'TAB', 'LPAR', 'RPAR', 'LCBRACE', 'INT', 'AND', 'IDENTIFIER', 'INT', 'RPAR', 'LCBRACE', 'TAB', 'LPAR', 'IDENTIFIER', 'ASSIGN', 'ASSIGN', 'KEYWORD', 'ASSIGN', 'INT', 'SEMICOL', 'TAB', 'IDENTIFIER', 'IDENTIFIER', 'SEMICOL', 'TAB', 'KEYWORD', 'ASSIGN', 'INT', 'SEMICOL', 'TAB', 'IDENTIFIER', 'TAB', 'RCBRACE', 'TAB', 'TAB', 'RCBRACE', 'IDENTIFIER', 'COMMA', 'KEYWORD', 'IDENTIFIER', 'RPAR', 'LCBRACE', 'TAB', 'KEYWORD', 'LPAR', 'IDENTIFIER', 'KEYWORD', 'ASSIGN', 'IDENTIFIER', 'SEMICOL', 'TAB', 'LBRACE', 'RBRACE', 'IDENTIFIER', 'IDENTIFIER', 'TAB', 'RCBRACE', 'TAB', 'IDENTIFIER', 'IDENTIFIER', 'RPAR', 'LCBRACE', 'TAB', 'KEYWORD', 'LPAR', 'KEYWORD', 'TAB', 'LPAR', 'IDENTIFIER', 'RPAR', 'IDENTIFIER', 'LCBRACE', 'KEYWORD', 'IDENTIFIER', 'SEMICOL', 'TAB', 'IDENTIFIER', 'ASSIGN', 'SEMICOL', 'TAB', 'IDENTIFIER', 'ASSIGN', 'IDENTIFIER', 'SEMICOL', 'TAB', 'IDENTIFIER', 'IDENTIFIER', 'SEMICOL', 'TAB', 'LBRACE', 'RBRACE', 'KEYWORD', 'ASSIGN', 'IDENTIFIER', 'KEYWORD', 'SEMICOL', 'TAB', 'LBRACE', 'RBRACE', 'IDENTIFIER', 'IDENTIFIER', 'COMMA', 'IDENTIFIER', 'COMMA', 'MUL', 'SEMICOL', 'TAB', 'LPAR', 'KEYWORD', 'LPAR', 'IDENTIFIER', 'RPAR', 'IDENTIFIER', 'RPAR', 'KEYWORD', 'IDENTIFIER', 'SEMICOL', 'IDENTIFIER', 'SEMICOL', 'TAB', 'LPAR', 'KEYWORD', 'RPAR', 'LCBRACE', 'ASSIGN', 'IDENTIFIER', 'KEYWORD', 'ASSIGN', 'IDENTIFIER', 'IDENTIFIER', 'SEMICOL', 'TAB', 'LBRACE', 'RBRACE', 'IDENTIFIER', 'TAB', 'RCBRACE', 'TAB', 'RCBRACE', 'LCBRACE', 'TAB', 'KEYWORD', 'IDENTIFIER', 'TAB', 'IDENTIFIER', 'IDENTIFIER', 'SEMICOL', 'TAB', 'IDENTIFIER', 'TAB', 'RCBRACE', 'TAB', 'RCBRACE', 'IDENTIFIER', 'LCBRACE', 'TAB', 'KEYWORD', 'LPAR', 'KEYWORD', 'RPAR', 'IDENTIFIER', 'LBRACE', 'RBRACE', 'IDENTIFIER', 'TAB', 'LPAR', 'IDENTIFIER', 'RPAR', 'LCBRACE', 'KEYWORD', 'IDENTIFIER', 'TAB', 'IDENTIFIER', 'TAB', 'SEMICOL', 'IDENTIFIER', 'IDENTIFIER', 'TAB', 'RCBRACE', 'KEYWORD', 'INT', 'TAB', 'LPAR', 'IDENTIFIER', 'RPAR', 'LCBRACE', 'KEYWORD', 'IDENTIFIER', 'IDENTIFIER', 'SEMICOL', 'TAB', 'IDENTIFIER', 'TAB', 'RCBRACE', 'LCBRACE', 'TAB', 'KEYWORD', 'SEMICOL', 'TAB', 'LBRACE', 'IDENTIFIER', 'RBRACE', 'IDENTIFIER', 'KEYWORD', 'TAB', 'RCBRACE', 'TAB', 'RCBRACE', 'KEYWORD', 'IDENTIFIER', 'TAB', 'KEYWORD', 'LPAR',
#   'KEYWORD', 'RPAR', 'IDENTIFIER', 'LBRACE', 'RBRACE', 'LCBRACE', 'KEYWORD', 'IDENTIFIER', 'RPAR', 'LCBRACE', 'TAB', 'LPAR', 'IDENTIFIER', 'KEYWORD', 'TAB', 'IDENTIFIER', 'IDENTIFIER', 'SEMICOL', 'TAB', 'IDENTIFIER', 'TAB', 'RCBRACE', 'LCBRACE', 'TAB', 'LPAR', 'KEYWORD', 'IDENTIFIER', 'RPAR', 'INT', 'KEYWORD', 'IDENTIFIER', 'IDENTIFIER', 'SEMICOL', 'TAB', 'IDENTIFIER', 'TAB', 'RCBRACE', 'LCBRACE', 'TAB', 'KEYWORD', 'SEMICOL', 'TAB', 'LBRACE', 'IDENTIFIER', 'RBRACE', 'IDENTIFIER', 'KEYWORD', 'TAB', 'RCBRACE', 'TAB', 'RCBRACE', 'TAB', 'IDENTIFIER', 'IDENTIFIER', 'RPAR', 'LCBRACE', 'TAB', 'KEYWORD', 'LPAR', 'KEYWORD', 'PLUS', 'INT', 'RPAR', 'SEMICOL', 'TAB', 'LPAR', 'IDENTIFIER', 'IDENTIFIER', 'ASSIGN', 'IDENTIFIER', 'SEMICOL', 'TAB', 'LBRACE', 'RBRACE', 'IDENTIFIER', 'IDENTIFIER', 'TAB', 'TAB', 'RCBRACE', 'TAB', 'IDENTIFIER', 'KEYWORD', 'LCBRACE', 'TAB', 'KEYWORD', 'LPAR', 'RPAR', 'IDENTIFIER', 'SEMICOL', 'TAB', 'KEYWORD', 'TAB', 'RCBRACE', 'IDENTIFIER', 'IDENTIFIER', 'OUT', 'LPAR', 'IDENTIFIER', 'COMMA', 'KEYWORD', 'IDENTIFIER', 'IDENTIFIER', 'RPAR', 'SEMICOL', 'TAB', 'IDENTIFIER', 'IDENTIFIER', 'IN', 'LPAR', 'KEYWORD', 'IDENTIFIER', 'IDENTIFIER', 'COMMA', 'KEYWORD', 'IDENTIFIER', 'RPAR', 'SEMICOL', 'TAB', 'IDENTIFIER', 'TAB', 'TAB', 'RCBRACE', 'SEMICOL', 'IDENTIFIER', 'IDENTIFIER', 'OUT', 'COMMA', 'KEYWORD', 'IDENTIFIER', 'LCBRACE', 'LPAR', 'IDENTIFIER', 'RPAR', 'IDENTIFIER', 'ASSIGN', 'INT', 'SEMICOL', 'IDENTIFIER', 'SEMICOL', 'LCBRACE', 'TAB', 'KEYWORD', 'LPAR', 'KEYWORD', 'RPAR', 'INC', 'OUT', 'SEMICOL', 'TAB', 'LBRACE', 'IDENTIFIER', 'RBRACE', 'IDENTIFIER', 'TAB', 'RCBRACE', 'IDENTIFIER', 'SEMICOL', 'TAB', 'KEYWORD', 'RCBRACE', 'IDENTIFIER', 'IN', 'IDENTIFIER', 'IDENTIFIER', 'COMMA', 'KEYWORD', 'IDENTIFIER', 'RPAR', 'LCBRACE', 'LPAR', 'KEYWORD', 'SEMICOL', 'IDENTIFIER', 'LCBRACE', 'TAB', 'KEYWORD', 'LPAR', 'KEYWORD', 'RPAR', 'INC', 'ASSIGN', 'INT', 'SEMICOL', 'ASSIGN', 'IDENTIFIER', 'SEMICOL', 'TAB', 'LBRACE', 'RBRACE', 'IDENTIFIER', 'TAB', 'RCBRACE', 'RCBRACE', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'KEYWORD', 'IDENTIFIER', 'LCBRACE', 'COLON', 'TAB', 'KEYWORD', 'IDENTIFIER', 'SEMICOL', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'TAB', 'IDENTIFIER', 'COLON', 'TAB', 'KEYWORD', 'IDENTIFIER', 'TAB', 'COLON', 'LCBRACE', 'TAB', 'LPAR', 'RPAR', 'LPAR', 'IDENTIFIER', 'RPAR', 'INT', 'IDENTIFIER', 'TAB', 'RCBRACE', 'IDENTIFIER', 'RPAR', 'LCBRACE', 'TAB', 'LPAR', 'IDENTIFIER', 'IDENTIFIER', 'SEMICOL', 'TAB', 'LPAR', 'RPAR', 'IDENTIFIER', 'IDENTIFIER', 'SEMICOL', 'SEMICOL', 'LCBRACE', 'TAB', 'LPAR', 'KEYWORD', 'LPAR', 'IDENTIFIER', 'RPAR', 'RPAR', 'ASSIGN', 'INT', 'KEYWORD', 'ASSIGN', 'SEMICOL', 'TAB', 'LBRACE', 'IDENTIFIER', 'LBRACE', 'RBRACE', 'RBRACE', 'IDENTIFIER', 'TAB', 'RCBRACE', 'TAB', 'TAB', 'RCBRACE', 'IDENTIFIER', 'KEYWORD', 'IDENTIFIER', 'IDENTIFIER', 'TAB', 'IDENTIFIER', 'RPAR', 'LCBRACE', 'TAB', 'LPAR', 'IDENTIFIER', 'IDENTIFIER', 'SEMICOL', 'TAB', 'LPAR', 'RPAR', 'IDENTIFIER', 'IDENTIFIER', 'SEMICOL', 'SEMICOL', 'LCBRACE', 'TAB', 'LPAR', 'KEYWORD', 'LPAR', 'IDENTIFIER', 'RPAR', 'RPAR', 'ASSIGN', 'INT', 'KEYWORD', 'ASSIGN', 'SEMICOL', 'TAB', 'LBRACE', 'IDENTIFIER', 'LBRACE', 'RBRACE', 'RBRACE', 'IDENTIFIER', 'TAB', 'RCBRACE', 'TAB', 'RCBRACE', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'KEYWORD', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'TAB', 'LCBRACE', 'TAB', 'LPAR', 'IDENTIFIER', 'RPAR', 'IDENTIFIER', 'IDENTIFIER', 'ASSIGN', 'KEYWORD', 'SEMICOL', 'IDENTIFIER', 'IDENTIFIER', 'TAB', 'KEYWORD', 'SEMICOL', 'SEMICOL', 'LCBRACE', 'TAB', 'LPAR', 'KEYWORD', 'LPAR', 'IDENTIFIER', 'RPAR', 'RPAR', 'ASSIGN', 'INT', 'KEYWORD', 'ASSIGN', 'INT', 'SEMICOL', 'LCBRACE', 'TAB', 'LPAR', 'KEYWORD', 'LPAR', 'IDENTIFIER', 'RPAR', 'RPAR', 'SEMICOL', 'KEYWORD', 'AND', 'IDENTIFIER', 'KEYWORD', 'AND', 'IDENTIFIER', 'IDENTIFIER', 'TAB', 'LPAR', 'RPAR', 'LCBRACE', 'LBRACE', 'IDENTIFIER', 'LBRACE', 'IDENTIFIER', 'LBRACE', 'IDENTIFIER', 'RBRACE', 'RBRACE', 'RBRACE', 'ASSIGN', 'ASSIGN', 'ASSIGN', 'KEYWORD', 'ASSIGN', 'KEYWORD', 'SEMICOL', 'TAB', 'IDENTIFIER', 'TAB', 'RCBRACE', 'KEYWORD', 'AND', 'AND', 'IDENTIFIER', 'IDENTIFIER', 'RPAR', 'LCBRACE', 'TAB', 'LPAR', 'IDENTIFIER', 'LBRACE', 'IDENTIFIER', 'LBRACE', 'IDENTIFIER', 'LBRACE', 'IDENTIFIER', 'RBRACE', 'RBRACE', 'RBRACE', 'ASSIGN', 'ASSIGN', 'KEYWORD', 'ASSIGN', 'IDENTIFIER', 'SEMICOL', 'TAB', 'LBRACE', 'RBRACE', 'IDENTIFIER', 'TAB', 'RCBRACE', 'TAB', 'RCBRACE', 'ASSIGN', 'KEYWORD', 'SEMICOL', 'TAB', 'IDENTIFIER', 'TAB', 'RCBRACE', 'IDENTIFIER', 'SEMICOL', 'KEYWORD', 'IDENTIFIER', 'TAB', 'KEYWORD', 'TAB', 'RCBRACE', 'RCBRACE', 'SEMICOL', 'KEYWORD', 'IDENTIFIER', 'IDENTIFIER', 'LCBRACE', 'LPAR', 'KEYWORD', 'RPAR', 'LBRACE', 'IDENTIFIER', 'RBRACE', 'COMMA', 'IDENTIFIER', 'LCBRACE', 'TAB', 'KEYWORD', 'LCBRACE', 'TAB', 'LPAR', 'IDENTIFIER', 'RPAR', 'INT', 'KEYWORD', 'OUT', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'TAB', 'IDENTIFIER', 'SEMICOL', 'IDENTIFIER', 'TAB', 'KEYWORD', 'SEMICOL', 'TAB', 'RCBRACE', 'IDENTIFIER', 'IDENTIFIER', 'TAB', 'IDENTIFIER', 'LPAR', 'IDENTIFIER', 'RPAR', 'SEMICOL', 'LBRACE', 'IDENTIFIER', 'RBRACE', 'INT', 'IDENTIFIER', 'ASSIGN', 'TAB', 'IDENTIFIER', 'SEMICOL', 'IDENTIFIER', 'TAB', 'IDENTIFIER', 'SEMICOL', 'IDENTIFIER', 'TAB', 'LPAR', 'RPAR', 'IDENTIFIER', 'SEMICOL', 'IDENTIFIER', 'IDENTIFIER', 'KEYWORD', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'KEYWORD', 'IDENTIFIER', 'TAB', 'LCBRACE', 'TAB', 'KEYWORD', 'LPAR', 'RPAR', 'IDENTIFIER', 'KEYWORD', 'LPAR', 'RPAR', 'IDENTIFIER', 'LCBRACE', 'COMMA', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'TAB', 'IDENTIFIER', 'IDENTIFIER', 'SEMICOL', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 
#   'LPAR', 'RPAR', 'IDENTIFIER', 'IDENTIFIER', 'ASSIGN', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'KEYWORD', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'TAB', 'LPAR', 'IDENTIFIER', 'RPAR', 'SEMICOL', 'IDENTIFIER', 'SEMICOL', 'SEMICOL', 'LCBRACE', 'TAB', 'LPAR', 'KEYWORD', 'LPAR', 'IDENTIFIER', 'RPAR', 'RPAR', 'ASSIGN', 'INT', 'KEYWORD', 'OUT', 'SEMICOL', 'TAB', 'LBRACE', 'IDENTIFIER', 'RBRACE', 'IDENTIFIER', 'OUT', 'SEMICOL', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'TAB', 'LBRACE', 'IDENTIFIER', 'RBRACE', 'IDENTIFIER', 'TAB', 'RCBRACE', 'RCBRACE', 'SEMICOL', 'LPAR', 'IDENTIFIER', 'RPAR', 'RCBRACE', 'KEYWORD', 'LCBRACE', 'OUT', 'IDENTIFIER', 'IDENTIFIER', 'IDENTIFIER', 'TAB', 'IDENTIFIER', 'SEMICOL', 'IDENTIFIER', 'TAB', 'RCBRACE', 'SEMICOL', 'TAB', 'LPAR', 'IDENTIFIER', 'RPAR', 'TAB', 'TAB', 'RCBRACE', 'MUL', 'IDENTIFIER', 'RPAR', 'LCBRACE', 'TAB', 'KEYWORD', 'LPAR', 'IDENTIFIER', 'OUT', 'TAB', 'LPAR', 'IDENTIFIER', 'RPAR', 'SEMICOL', 'IDENTIFIER', 'TAB', 'RCBRACE', 'RCBRACE']

# a=['IDENTIFIER','IDENTIFIER','KEYWORD','IDENTIFIER', 'IDENTIFIER', 'KEYWORD','IDENTIFIER','IDENTIFIER','KEYWORD','IDENTIFIER','IDENTIFIER','KEYWORD']
# b=['IDENTIFIER','IDENTIFIER','KEYWORD','IDENTIFIER','IDENTIFIER','KEYWORD','IDENTIFIER','IDENTIFIER','KEYWORD','IDENTIFIER','IDENTIFIER','KEYWORD']
# # a=['BEGINCLASS','VARDEF','BEGINMETHOD','VARDEF','ASSIGN','APPLY','BEGINWHILE','ASSIGN','ENDWHILE']
# # b=['BEGINCLASS','VARDEF','BEGINMETHOD','VARDEF','ASSIGN','APPLY','BEGINWHILE','ASSIGN','ENDWHILE']
# # b=['ASSIGN','APPLY','BEGINWHILE','ENDWHILE','BEGINCLASS','VARDEF']
# # a=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# a=['a','b','c','l']
# b=['a','b','c','g','f','x','v','b']
#a = ['1','2','3','4','5','6','7','8','9','1','3']
#b = ['3','4','5','2','1','7','8','9','1','3']

# def gct(a,b,minlength=1):
#     if len(a) == 0 or len(b) == 0:
#         return []
#     # if py>3.0, nonlocal is better
#     class markit:
#         a=[0]
#         minlen=2
#     markit.a=[0]*len(a)
#     markit.minlen=minlength

#     #output char index
#     out=[]

#        # To find the max length substr (index)
#     # apos is the position of a[0] in origin string
#     def maxsub(a,b,apos=0,lennow=0):
#         if (len(a) == 0 or len(b) == 0):
#             return []
#         if (a[0]==b[0] and markit.a[apos]!=1 ):
#             return [apos]+maxsub(a[1:],b[1:],apos+1,lennow=lennow+1)
#         elif (a[0]!=b[0] and lennow>0):
#             return []
#         return max(maxsub(a, b[1:],apos), maxsub(a[1:], b,apos+1), key=len)
#     while True:
#         findmax=maxsub(a,b,0,0)
#         if (len(findmax)<markit.minlen):
#             break
#         else:
            
#             for i in findmax:
#                 markit.a[i]=1
#             out+=findmax
            

#     return [ a[i] for i in out]


# len(a)
# len(b)





# print(a)
# print(b)


# print(gct(a,b))



# sim=len(gct(a,b))/min(len(a),len(b))*100
# # print(gct(a,b))

# sim=len(gct(a,b))/((len(a)+len(b))-len(gct(a,b)))*100

# print(sim)


def prepare_marks(tokens): # creates array with marked tokens
    tokens_arr = []
    for token in tokens:
        tokens_arr.append([token, False]) # marked as not compared
    return tokens_arr

def compare_words(word1, word2): # compare two words, should return 0 - 1
    return 1 if word1 == word2 else 0

def compare_tokens(n1, n2, tokens1, tokens2, compare_function): # compare two tokens
    try:
        if tokens1[n1][1] == tokens2[n2][1] == False: # both token are unmatched
            return compare_function(tokens1[n1][0], tokens2[n2][0])
    except IndexError: # do not check overflown values
        return False
    return False

def check_matches(matches, n1, n2): # check if matches are not overlaping
    # matches[1,2,3]: 1 pos of X token, 2 pos of Y token, 3 length of the match
    for n3, match in enumerate(matches):
        if (n1 >= match[0] and n1 <= match[0] + match[2] - 1) or (n2 >= match[1] and n2 <= match[1] + match[2] - 1):
            return False
    return True

# tokens1, tokens2 = ['string', .... ]
# minimal match - minimal number of tokens in a match
# treshold (includes) - treshold decides if match should continue
# compare function - def func(value 1, value 2) returns 0-1 (1 - match, 0 - no match)

def token_comparison(l,tokens1, tokens2, minimal_match = 5, threshold = 1
                    , compare_function = compare_words, score_array = False, use_score = False):
    tiles = []
    switched = False
    tokens1_arr = prepare_marks(tokens1)
    tokens2_arr = prepare_marks(tokens2)
    if len(tokens2_arr) < len(tokens1_arr): # optimalization - shorter array should be base for comparison
        tokens1_arr, tokens2_arr = tokens2_arr, tokens1_arr
        switched = True
    maxMin = True
    while maxMin:
        max_match = minimal_match
        matches = []
        for n1, [token1, match1] in enumerate(tokens1_arr):
            if not match1:
                for n2, [token2, match2] in enumerate(tokens2_arr):
                    if not match2:
                        sim_result = 0
                        com_result = 0
                        if score_array:
                            score_arr = []
                        else:
                            score_arr = None
                        comparison_result = compare_tokens(n1, n2, tokens1_arr, tokens2_arr, compare_function)
                        while comparison_result >= threshold:
                            sim_result += 1
                            com_result += comparison_result
                            if score_array:
                                score_arr.append(comparison_result)
                            comparison_result = compare_tokens(n1 + sim_result, n2 + sim_result, tokens1_arr, tokens2_arr, compare_function)
                        if use_score:
                            if com_result == max_match:
                                if check_matches(matches, n1, n2):
                                    matches.append([n1, n2, sim_result, com_result, score_arr])
                            elif com_result > max_match:
                                max_match = com_result
                                matches = [[n1, n2, sim_result, com_result, score_arr]]
                        else:
                            if sim_result == max_match:
                                if check_matches(matches, n1, n2):
                                    matches.append([n1, n2, sim_result, com_result, score_arr])
                            elif sim_result > max_match:
                                max_match = sim_result
                                matches = [[n1, n2, sim_result, com_result, score_arr]]
        
        for match in matches: # Match matched tokens
            for token_pos in range(0,match[2]):
                tokens1_arr[match[0] + token_pos][1] = True # marks as compared
                tokens2_arr[match[1] + token_pos][1] = True # marks as compared
            tile = {
                'tok_1_pos': match[0],
                'tok_2_pos': match[1],
                'length': match[2],
                'score': match[3],
            }
            l = l + match[2]
            if score_array:
                tile['score_array'] = match[4]
            tiles.append(tile)

        if max_match <= minimal_match:
            maxMin = False

    if switched: # reverse to original order
        for tile in tiles:
            tile['tok_1_pos'], tile['tok_2_pos'] = tile['tok_2_pos'], tile['tok_1_pos']
    # print(l)
    return l

# a=tokenize('files/94af2a2865a513c89bcf6d500bc5e782.cpp')
# b=tokenize('files/721bee33a7d5ac158d598091c642b45f.cpp')



def readallcpp():
    filenames = glob.glob('files/*.cpp')
    return filenames

def compareall():
    allsimis=[]
    
    allfiles=readallcpp()

    for i in range(len(allfiles)):
        for j in range(i + 1, len(allfiles)):
            pairsimi={
                'Doc1':'',
                'Doc2':'',
                'similarity':'',
            }    
            # compare(allfiles[i], allfiles[j])
            a=''
            b=''
            a=tokenize(allfiles[i])
            b=tokenize(allfiles[j])
            sim=(token_comparison(0,a, b, minimal_match=1)/((len(a)+len(b))-token_comparison(0,a, b, minimal_match=1)))*100
            pairsimi['Doc1']=allfiles[i].replace('files\\', '')  
            pairsimi['Doc2']=allfiles[j].replace('files\\', '')
            pairsimi['similarity']=math.floor(sim)
            allsimis.append(pairsimi)
            # allsimis.append(sim)    
    return(allsimis)




# sim=len(gct(a,b))/((len(a)+len(b))-len(gct(a,b)))*100

# print(token_comparison(0,a, b, minimal_match=1))

# sim=(token_comparison(0,a, b, minimal_match=1)/((len(a)+len(b))-token_comparison(0,a, b, minimal_match=1)))*100

# print(sim)







#/////////////////////////////////////
# a=allfiles[0]
# b=allfiles[1]

# aa=tokenize(a)
# bb=tokenize(b)

# sim=(token_comparison(0,aa, bb, minimal_match=1)/((len(aa)+len(bb))-token_comparison(0,aa, bb, minimal_match=1)))*100


# print(sim)

print(compareall())
print("--- %s seconds ---" % (time.time() - start_time))

