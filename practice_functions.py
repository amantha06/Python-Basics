import math
def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        if a < b:
            return a
        else: 
            return b
    else:
        if a > b:
            return a
        else:
            return b



def makes_twenty(c,d):
    if c + d == 20:
        return True
    else:
        return False


def olemacdonald(name):
    firstL = name[0]
    between = name[1:3]
    fourthL = name[3]
    last = name[4:]


    return firstL.upper() + between + fourthL.upper() + last


def master_yooda(text):
    store = text.split()
    reverse = store[::-1]
    return ' '.join(reverse)


def almost_there(num):
    if num >= 90 and num <= 110:
        return True
    elif num >= 190 and num <= 210:
        return True
    
    return False

def has_33(numbers):
    for i in range(0,len(numbers)-1):
        if numbers[i] == 3 and numbers[i + 1] == 3:
            return True
    return False 

def paper_doll(word):
    add_letter = ' '
    for char in word:
        add_letter += char*3
    return add_letter

def blackjack(num1, num2, num3):
    if num1 + num2 + num3 <= 21:
        return num1 + num2 + num3
    elif num1 + num2 + num3 > 21:
        if num1 == 11 or num2 == 11 or num3 == 11:
            return num1 + num2 + num3 - 10
        return "BUST"

def summer69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total

def jamesbond(spytext):
    
    code = [0,0,7,'x']
    for i in spytext:
        if i == code[0]:
            code.pop(0)
    
    return len(code) == 1


def count_primes(num):

    if num < 2:
        return 0
    

    primes = [2]
    x = 3

    while x <= num: 
        for y in primes:
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

def vol(rad):
    volume = rad * rad * rad
    volume = volume * math.pi
    volume = volume * 4
    volume = volume / 3
    return volume

def check(num,low,high):
    checklist = []
    while low < high:    
        low += 1
        checklist.append(low)
    for i in checklist:
        if num == i:
            return True

    return False


def caplow(text):
    numcap = 0
    numlow = 0
    for i in text:
        if i.isupper:
            numcap += 1
        elif i.islower:
            numlow += 1

    print(f'Lowercase Count: {numlow}')
    print(f'Uppercase Count: {numcap}')
    
    
def unique_list(lst):
    return list(set(lst))    


def multiple(numbers):
    total = 1
    for num in numbers:
        total = total*num
    return total        

def palindrome(s):
    s = s.replace(" ", "")
    if s == s[::-1]:
        return True
    
    return False
                



print(lesser_of_two_evens(10,5))
print(makes_twenty(10,15))
print(olemacdonald('macdonald'))
print(master_yooda('I am master yoda'))
print(almost_there(15))
print(has_33([3, 3, 1, 5, 3]))
print(paper_doll('hello'))
print(blackjack(11, 6, 5))
print(summer69([1,1,6,2,3,9,1]))
print(jamesbond([1,2,0,3,7,9,8]))
print(count_primes(100))
print(vol(2))
print(check(5,2,7))
caplow("LinaLin")
print(unique_list([1,1,1,1,1,1,2,2,2,2,3,3,4,4,5,5]))
print(multiple([1,2,3,4,4]))
print(palindrome("race car"))

