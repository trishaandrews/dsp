# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0

import re
import string

def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.

    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """
    base_str = "Number of donuts: "
    final_str = ""
    if count >= 10:
        final_str = base_str  + "many"
    else:
        final_str = base_str +"%d" % count
        
    return final_str

def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    s_end = ""
    if len(s) < 2:
        pass
    else:
        s_end = s[:2] + s[-2:]
    
    return s_end


def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
    letter = s[0]
    end_str = letter
    for i in range(1,len(s)):
        if s[i] == letter:
            end_str += "*"
        else:
            end_str += s[i]
    return end_str

def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    a1 = a[:2]
    a2 = a[2:]
    b1 = b[:2]
    b2 = b[2:]
    mix1 = b1 + a2
    mix2 = a1 + b2
    end = mix1 + " " + mix2
    
    return end

def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    
    end = ""
    if len(s) < 3:
        end = s
    else:
        if s[-3:] == "ing":
            end = s + "ly"
        else:
            end = s + "ing"
    return end


def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """

    #use re instead of plain split because of ! in "This dinner is good!"
    slist = re.findall(r"[\w']+|[.,!?;]", s)
    bad_i = None
    not_i = None
    end = ""

    for w in range(len(slist)):
        if slist[w] == "bad":
            bad_i = w
        elif slist[w] == "not":
            not_i = w
   
    if not_i < bad_i:
        slist[not_i] = "good"
        for i in range(not_i+1, bad_i+1):
            slist[i] = ""
        for j in range(len(slist)):
            if slist[j] != "" and slist[j] != " ":
                if j != 0 and slist[j] not in string.punctuation:
                    end += " " + slist[j]
                else:
                    end += slist[j]
    else:
        end = s
    return end
    


def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    end = ""
    
    a1, a2 = divide(a)
    b1, b2 = divide(b)

    end = a1 + b1 + a2 + b2

    return end

def divide(a):
    '''
    Divides string into halves for the front_back method
    '''
    a1, a2 = "", ""
    length = len(a)
    if length%2 == 0:
        a1 = a[:length/2]
        a2 = a[-length/2:]
    else:
        a1 = a[:length/2 + 1]
        a2 = a[-length/2 + 1:]
   
    return a1, a2
