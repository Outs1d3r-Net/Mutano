#!/usr/bin/env python3

#################################
# Mutano                        #
# by: Outs1d3r-NET              #
# From: Desec Security Training #
#################################

## [+] ---> Libraries
import re
import sys
import os
import string
import datetime
from unicodedata import normalize

## [+] ---> Usage
if len(sys.argv) != 3:
    print('''
   _
  ( \                ..-----..__
   \.".        _.--"`  [   "  " ```"-._
    `. `"-..-"" `    "  " "   .  ;   ; `-"""-.,__/|/_
      `"-.;..-""`|"  `.  ".    ;     "  `    "   `"  `,
                 \ "   .    " .     "   ;   .`   . " 1 |
                  "." . "- . \    .`   .`  .   .\     `Y
                    "-." .   ].  "   ,    "    /"`""";:"
                      /Y   ".] "-._ /    " _.-"
                      \ "\_   ; (`"."."  ."/
                       " )` /  `."   .-"."
                        "\  \)."  .-"--"
                          `. `,_"`      Mutano v1.0
                            `.__)       by: Outs1d3r-NET
''')
    print("-"*80)
    print("\n[+] Usage:",sys.argv[0],"Simple-WORDLIST-input.txt Complex-WORDLIST-output.txt\n")
    print("-"*80)
    sys.exit(0)

## [+] ---> Logic
dic = {'aioO':'@100','aeioOs':'43100$','aeiou':'AEIOU','IilLsS':'1111$$'}
wordlist = open(str(sys.argv[2]), 'w')
wordtimes = datetime.datetime.now().strftime('%d/%m/%Y %Hh:%Mm:%Ss')
data = datetime.datetime.now()


def makeoutput (word):
	for n in range(1001):
		wordlist.write(word+str(n)+'\n')
		wordlist.write(word+'@'+str(n)+'\n')

def animalTransform (line):
	for i in dic:
		wordlist.write(line.translate(str.maketrans(i,dic[i]))+'\n')
		makeoutput(line.translate(str.maketrans(i,dic[i])))
		wordlist.write(line.translate(str.maketrans(i,dic[i]))+str(data.year)+'\n')
		wordlist.write(line.translate(str.maketrans(i,dic[i]))+'@'+str(data.year)+'\n')
		wordlist.write(line.translate(str.maketrans(i,dic[i])).upper()+'\n')
		makeoutput(line.translate(str.maketrans(i,dic[i])).upper())
		wordlist.write(line.translate(str.maketrans(i,dic[i])).upper()+str(data.year)+'\n')
		wordlist.write(line.translate(str.maketrans(i,dic[i])).upper()+'@'+str(data.year)+'\n')
		wordlist.write(line.translate(str.maketrans(i,dic[i])).lower()+'\n')
		makeoutput(line.translate(str.maketrans(i,dic[i])).lower())
		wordlist.write(line.translate(str.maketrans(i,dic[i])).lower()+str(data.year)+'\n')
		wordlist.write(line.translate(str.maketrans(i,dic[i])).lower()+'@'+str(data.year)+'\n')
		wordlist.write(line.translate(str.maketrans(i,dic[i])).capitalize()+'\n')
		makeoutput(line.translate(str.maketrans(i,dic[i])).capitalize())
		wordlist.write(line.translate(str.maketrans(i,dic[i])).capitalize()+str(data.year)+'\n')
		wordlist.write(line.translate(str.maketrans(i,dic[i])).capitalize()+'@'+str(data.year)+'\n')
		wordlist.write(line.translate(str.maketrans(i,dic[i])).title()+'\n')
		makeoutput(line.translate(str.maketrans(i,dic[i])).title())
		wordlist.write(line.translate(str.maketrans(i,dic[i])).title()+str(data.year)+'\n')
		wordlist.write(line.translate(str.maketrans(i,dic[i])).title()+'@'+str(data.year)+'\n')
		wordlist.write(line.translate(str.maketrans(i,dic[i])).swapcase()+'\n')
		makeoutput(line.translate(str.maketrans(i,dic[i])).swapcase())
		wordlist.write(line.translate(str.maketrans(i,dic[i])).swapcase()+str(data.year)+'\n')
		wordlist.write(line.translate(str.maketrans(i,dic[i])).swapcase()+'@'+str(data.year)+'\n')


def main():
	with open(sys.argv[1]) as file:
		for table in file:
			l = table.rstrip('\n')
			animalTransform(l)
	wordlist.close()

	with open(str(sys.argv[2]), 'r') as fp:
		clines = len(fp.readlines())

	print('''
                                 <\              _
                                   |\          _/{
                                    |\       _-   -_
                         /{        / `\   _-     - -_
                       _~  =      ( @  \ -        -  -_
                     _- -   ~-_   \( =\ \           -  -_
                   _~  -       ~_ | 1 :\ \      _-~-_ -  -_
                 _-   -          ~  |V: \ \  _-~     ~-_-  -_
              _-~   -            /  | :  \ \            ~-_- -_
           _-~    -   _.._      {   | : _-``               ~- _-_
        _-~   -__..--~    ~-_  {   : \:}
      =~__.--~~              ~-_\  :  /
                                 \ : /__
                                //`Y"-- |
                               <+        \       Mutano v1.0
                                 \       VV      by: Outs1d3r-NET
''')
	print("#"*80)
	print("[+] Wordlist as been created in:",str(os.path.realpath(sys.argv[2])),"\n[+] Date:",wordtimes,"\n[+] Lines:",str(clines))
	print("#"*80)

if __name__ == '__main__':
  main()
