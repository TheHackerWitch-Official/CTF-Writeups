# picoCTF crackme-py

## Problem Description
[crackme.py](https://mercury.picoctf.net/static/db4b9e7a2862c320aa6b40e3551406bd/crackme.py)

## The Solution
Once you've downloaded crackme.py, open it in a text editor. The contents of the file are listed below.

    # Hiding this really important number in an obscure piece of code is brilliant!
    # AND it's encrypted!  
    # We want our biggest client to know his information is safe with us.
    bezos_cc_secret = "A:4@r%uL`M-^M0c0AbcM-MFE0d_a3hgc3N"

    # Reference alphabet
    alphabet = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
            "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"



    def decode_secret(secret):
        """ROT47 decode

        NOTE: encode and decode are the same operation in the ROT cipher family.
        """

        # Encryption key
        rotate_const = 47

        # Storage for decoded secret
        decoded = ""

        # decode loop
        for c in secret:
            index = alphabet.find(c)
            original_index = (index + rotate_const) % len(alphabet)
            decoded = decoded + alphabet[original_index]

        print(decoded)



    def choose_greatest():
        """Echo the largest of the two numbers given by the user to the program

        Warning: this function was written quickly and needs proper error handling
        """

        user_value_1 = input("What's your first number? ")
        user_value_2 = input("What's your second number? ")
        greatest_value = user_value_1 # need a value to return if 1 & 2 are equal

        if user_value_1 > user_value_2:
            greatest_value = user_value_1
        elif user_value_1 < user_value_2:
            greatest_value = user_value_2

        print( "The number with largest positive magnitude is "
            + str(greatest_value) )



    choose_greatest()


Take note of the following: 
1. There is a secret in the code (bezos_cc_secret)
2. The secret is encoded in ROT47
3. decode_secret() can decode the secret, but is never called.

Replace `choose_greatest()` with `decode_secret(bezos_cc_secret)` to decrypt the flag.

Execute the following command to grab the flag: `python3.crackme.py > flag.txt`

The flag will be saved in a text file called *flag.txt.*

## Flag
##### picoCTF{1|\/|_4_p34|\|ut_502b984b}
