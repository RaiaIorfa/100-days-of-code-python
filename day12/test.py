# Target is the number up to which we count
def fizz_buzz(target):
    target += 1
    for num in range(1,target):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
    
fizz_buzz(15)


u_alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
l_alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
special_char = ['!','@','#','$','%','^','&','*','(',')','_']

password_lenght = int(input("How long do you want "))

def password_gen(pass_len, l_aplha=0, u_alpha=0, num=0, u_char=0):
    return