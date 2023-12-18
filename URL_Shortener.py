import pyshorteners

def again():
    flag = 'Y'
    while(flag.lower() != "n" ):
        input_url = input("Input the URL ::: ")
        new_url = url_shortener(input_url)
        print(" The Shortened URL is :::")
        print(new_url)
        print()
        print("Enter Y to Continue ... To Exit, Enter N")
        flag = input("Enter Choice :::")

def url_shortener(input_url):
    shortener = pyshorteners.Shortener()
    shortened_url = shortener.tinyurl.short(input_url)
    return shortened_url

again()