# parpg
Paranoid Password Generator.   

TLDR: Minimalistic Python script to generate passwords, that uses generated RSA as dictionary instead of regular ascii_letters.  

Longer version:
In theory, having some insight on environment in which random-generating software was executed, one can predict (or reverse-engineer if you would like) what was generated with that generation.

As a little excercise of getting myself familiar with Python i wrote this script.
Script generates RSA, trims it a bit and uses given text as a dictionary for picking random letters for passwword.

To not make it excessivly long description i will put main features here:

- Script doesnt use any dependencies, only imports standart python features.
- Symbols do not repeat themselves in generated password (if number of letters is less than 42 (not total length of password!), number of special symbols is less than 29 and number of numbers is less than 10 (obviously because there is not much digits))
- Here and there random sleep used to make it even less predictable. I used microseconds, so it wont be noticable unless you will try to generate some password with 1000+ length.
- Default parameters are: length - 15, numbers to put in password - 3, special symbols to put -3.
- Default parameters could be overriden by using switches when executing script or just simply by edititng script yourself.
- !!! By default script do not use symbols "!", "@" and "$" for generation. I decided that those are to common.. you can override this behavior by adding switch "-nor".

Command line options:  

  -h, --help  show help message and exit  
  
  -l LENGTH   INT. Length of password (default: 15, minimum: 7). OPTIONAL. Value less than 7 converted to 7  
  
  -n NUMBERS  INT. How many digits should be in password (default: 3). OPTIONAL. Value less than 0 converted to 0  
  
  -s SPECIAL  INT. How many special symbols should be in password (default: 3). OPTIONAL. Value less than 0 converted to 0  
  
  -nor        Switch to include symbols "!","@","$" in special symbol dictionary (by default they are not used). OPTIONAL


  Tested only with Python3, so probably doesnt work with python2 (im to lazy to test)
  
