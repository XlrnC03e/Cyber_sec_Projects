# #from passlib.hash import md5_crypt as md5
# from passlib.hash import sha256_crypt as sha256
# from passlib.hash import sha512_crypt as sha512



import crypt
# This libary is used on older Unix programs, so its more flowed with Unix

def crackpass(crypted_pass):
    flag = 0
    file = open('./pass.txt', 'r')
    if crypted_pass == None:
        print('You didnt give the password')
        return
    salt = crypted_pass[0:2]
    for dic in file.readlines():
        word = dic.strip()
        cryptWord = crypt.crypt(word,salt = salt)
        if cryptWord == crypted_pass:
            print(f'[+] Password Found : {word}\nHash: {cryptWord}')
            flag+=10
            break
    if flag == 0:
        print('[-] Password Not Found: ', crypted_pass)

def run():
    try:
        print("how you want ot test/use me")
        mode = input('1. pre hashed passwords or \n 2. letter based passwords\n(1/2) ')
        if "2" in mode:
            s = input('Password: ')
            slt = input('Salt: ')
            crypted = crypt.crypt(s,salt = slt)
        elif "1" in mode:
            crypted = input("Hashed password: ")
        else:
            return

            crackpass(crypted)

    except (keyboardInterrupt, EOFError):
        pass




run()
