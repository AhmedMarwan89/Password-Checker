'''
In this project you should only turn on the project and write any passwords in the terminal 
and the project will check if it's strong password or not
and tell you how many times this password have been hacked 


To turn it on write this on your terminal (python passwordchecker.py  hello mohammed1990  mohammed87hj)
Those are three different passwords.



if you have trouble with understanding it call me on 
+9647708108023



'''



import hashlib
import requests
import sys

def get_response ( first5) :
    url = 'http://api.pwnedpasswords.com/range/' + first5 
    return  requests.get(url) 

def compare (hashes , hash_to_check )    :
    hashes = ( line.split(':') for line in hashes.text.splitlines())
    for h , count in hashes :
        if h == hash_to_check : 
            return count 

    return 0


def change (password) :
    password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper( )
    first5 , tail = password[:5] , password[5:]
    response = get_response(first5)
    return compare(response , tail) 


def main ( args) :
    for password in args :
        count = change(password)
        if count :
            print ( f' your pass word has hacked {count} times you should probably change it ')
        else :
            print ( 'your pssword now is perfect good working my friend ')
        print ( 'done \n  \n')



if __name__ == '__main__' :
    sys.exit ( main(sys.argv[1:]) ) 



    

