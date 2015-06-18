#!/usr/bin/env python
import numpy as np
import sys

class Markov():
    
    def __init__(self):
        self.options = {} #word keys with next possible words
        self.counts = {} #word keys with number of times they appear
        self.starts = {} #word keys at start of line with number of times
    
    def get_text(self, fn, n=2):
        '''gets list of words in text and makes key tuples from the words at 
        the start of lines. n is number of words in key'''
        text = [] 
        with open(fn, 'r') as f:
            for line in f:
                line = line.strip()
                wds = line.split(" ")
                
                if len(wds) >= n: #ignore lines with fewer than n words
                    st = tuple(wds[:n]) #get starting words
                    if st in self.starts:
                        self.starts[st][0] += 1
                    else:
                        self.starts[st] = [1] #I don't remember why it's a list
                    text += wds
        return text #list of words in a text 
    
    def get_words(self, text, n=2):
        '''generates key tuples from text and counts the occurences of their 
           next words n is number of words in key'''
        #words = []
        text += "#" #marks the end of file
        for i in range (len(text)-(n-1)-1): #in order to not overflow text
            segment = tuple(text[i:i+n]) #n word keys
            if segment not in self.options:
                self.options[segment] = [text[i+n]]
                self.counts[segment] = [1]
            else:
                if text[i+n] in self.options[segment]:
                    for j in range(len(self.options[segment])):
                        if self.options[segment][j] == text[i+n]:
                            self.counts[segment][j] +=1 #update option count
                else:
                    self.options[segment].append(text[i+n]) #add new word option
                    self.counts[segment].append(1) #add count for new option
            #words.append(segment)
        #return words

    def generate(self, num, n=2):
        '''generate a total of num words. this method actually generates the new
        word string from the given text and generated probabilities'''
        
        startsli =  self.start_probs() #create probabilities for starting words
        self.probs(self.counts) #modify counts from ints into probabilities
        if num <= n: #if generating fewer words than words in key tuples
            er = "please generate more than %s words or enter a smaller n" % n 
            return er
        else:
            outlist = []
            ch = np.random.choice(len(startsli[0]), p=startsli[1])
            newwords = startsli[0][ch] #startsli[0] is list of keys
            for m in range(n):
                outlist.append(startsli[0][ch][m]) #unpack start tuple words
            for i in range(num-n):
                if newwords in self.options: #if key exists
                    words = newwords
                    nextwords = self.options[words]
                    nextprobs = self.counts[words]
                    ch = np.random.choice(len(nextwords), p=nextprobs)
                    new = []
                    for j in range(n-1, 0, -1):
                        new.append(newwords[-j])
                    new.append(nextwords[ch])
                    newwords = tuple(new)
                    outlist.append(nextwords[ch])
                else:
                    print "chain might have reached the end of file character"
                    print newwords #show the key that doesn't exist in dict
                    break
            outstring = " ".join(outlist)
            return outstring #return generated text

    def start_probs(self):
        '''generate probabilities for the words that start lines'''
        total = 0
        startsli = [[],[]] #this is strange, but works
        for key in self.starts:
            total += self.starts[key][0]
        for key in self.starts:
            startsli[0].append(key)
            startsli[1].append(self.starts[key][0]/float(total))
        return startsli

    def probs(self, dct):
        '''modifies the given dictionary (only self.counts works right now)
        from int counts into probabilities'''
        for key in dct:
            total = 0
            for v in dct[key]:
                total += v
            for v in range(len(dct[key])):
               dct[key][v] = dct[key][v]/float(total)
               

    def run_markov(self, filename, num, n=2):
        '''runs all the methods in the proper order'''
        text = mk.get_text(filename, n)
        mk.get_words(text, n)
        outtext = mk.generate(num, n)
        return outtext
        
if __name__ == "__main__":
    #print sys.argv
    
    mk = Markov()
    filename = sys.argv[1]
    try:
        num = int(sys.argv[2])
    except ValueError:
        print("Not a number")

    n = 2 #looks like I didn't need to keep setting a default n. oh well
    
    #optional 3rd argument of how many words should be used in tuple keys to 
    # generate the next word
    if len(sys.argv) == 4:
       try:
           n = int(sys.argv[3])
       except ValueError:
           print("Not a number")

    print mk.run_markov(filename, num, n)
