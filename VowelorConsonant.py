x=str(raw_input("enter the letter"))
if x in( 'a','e','i','o','u'):
    print("The letter is vowel")
elif x in('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','z'):
    print("The letter is consonant")
else:
    print("The letter is invalid")
