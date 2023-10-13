#!/usr/bin/env python3

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from string import punctuation, ascii_letters, digits
import re, random, time, argparse

parser = argparse.ArgumentParser(description="Paranoid password generator.   Generates passwords using RSA-gen output as dictionary. Couple random sleeps here and there to make it harder to predict (reverse-engineer) what was the password even if you have a full snapshot of PC memory + exact time of script execution.         You can set number of special characters or numbers equal to length, so it will just generate only random number string or random special character string (or combination) without any letters (but that would be not as random, since RSA wont be used).")
parser.add_argument(
    '-l',
    type=int,
    default=15,
    dest="length",
    help='INT. Length of password (default: 15, minimum: 7). OPTIONAL. Value less than 7 converted to 7'
)
parser.add_argument(
    '-n',
    type=int,
    default=3,
    dest="numbers",
    help='INT. How many digits should be in password (default: 3). OPTIONAL. Value less than 0 converted to 0'
)
parser.add_argument(
    '-s',
    type=int,
    default=3,
    dest="special",
    help='INT. How many special symbols should be in password (default: 3). OPTIONAL. Value less than 0 converted to 0'
)
parser.add_argument(
    '-nor',
    default=True,
    action='store_false',
    dest="remove",
    help='Switch to include symbols "!","@","$" in special symbol dictionary (by default they are not used). OPTIONAL'
)

parsedargs = parser.parse_args()
length = parsedargs.length
numbers = parsedargs.numbers
special = parsedargs.special
remove = parsedargs.remove

if length < 7:
    length = 7

if numbers < 0:
    numbers = 0

if special < 0:
    special = 0

if length < (numbers + special):
    print("ERROR: length is too short for speficied number of symbols, with given parameters it should be at least -l " + str(numbers + special))
    exit(1)
dig = ""
dig += digits
# sleep for 0.001-0.1 second for a bit more of a randomness
time.sleep((random.randrange(1, 100))/1000)
if length > (numbers + special):
    # generate rsa for a dictionary
    priv = rsa.generate_private_key(
      public_exponent=65537,
      key_size=2048,
    )
    # serialize dictionary
    txt = priv.private_bytes(
      encoding=serialization.Encoding.PEM,
      format=serialization.PrivateFormat.TraditionalOpenSSL,
      encryption_algorithm=serialization.NoEncryption()
    )
    # use regular alphabet too, if total number of letters should be more 42 or more.
    if (length - numbers - special) > 41:
        alphabet = ""
        alphabet += ascii_letters
    txt.splitlines()[0]
    txt = str(txt)
    txt = txt.replace('\\n', '')
    txt = txt[70:(len(txt)-70)]
    words = re.sub('[^A-Za-z]+', '', txt)
if remove == True:
    spec = re.sub("!|@", "", punctuation)
    # for some reason re.sub doesnt want to replace $, so regular replace too...
    spec = spec.replace('$', '')
else:
    spec = punctuation
    
finalchars = []
localdig = ""
localdig += dig

for i in range(numbers):
    if i < 10:
        time.sleep((random.randrange(1, 10))/1000)
        rchoice = random.choice(localdig)
        localdig = localdig.replace(rchoice,'')
        finalchars.append(rchoice)
    else:
        time.sleep((random.randrange(1, 10))/1000)
        finalchars.append(random.choice(dig))  
for i in range(special):
    if remove == True and i < 29:
        time.sleep((random.randrange(1, 10))/1000)
        rchoice = random.choice(spec)
        spec = spec.replace(rchoice,'')
        finalchars.append(rchoice)
        random.shuffle(finalchars)
    elif remove != True and i < 32:
        time.sleep((random.randrange(1, 10))/1000)
        rchoice = random.choice(spec)
        spec = spec.replace(rchoice,'')
        finalchars.append(rchoice)
        random.shuffle(finalchars)
    else:
        time.sleep((random.randrange(1, 10))/1000)
        finalchars.append(random.choice(punctuation))
        random.shuffle(finalchars)
for i in range(length - numbers - special):
    if i < 42:
        time.sleep((random.randrange(1, 10))/1000)
        rchoice = random.choice(words)
        words = words.replace(rchoice,'')
        finalchars.append(rchoice)
        random.shuffle(finalchars)
    else:
        time.sleep((random.randrange(1, 10))/1000)
        finalchars.append(random.choice(alphabet))
        random.shuffle(finalchars)
pwdstring = ''
for i in range(len(finalchars)):
    localen = len(finalchars)
    time.sleep((random.randrange(1, 10))/1000)
    symbolnum = random.randrange(0, localen)
    pwdstring += finalchars[symbolnum]
    finalchars.pop(symbolnum)
print(pwdstring)
exit(0)