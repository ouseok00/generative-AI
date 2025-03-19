"""
 if 조건문을 사용해서 사용자가 입력한 숫자가 짝수이면, 
"짝수입니다." 를 출력하고, 3의 배수이면, "3의 
배수입니다." 를 출력하는 프로그램을 만들어 보세요.

a = int(input("숫자를 입력하세요:"))

if a%2==0:
    print("짝수입니다")
if a%3==0:
    print("3의 배수입니다")

반복적으로 사용자가 입력한 숫자가 저장된 수보다 크면 
"틀렸습니다. 조금 더 작은수입니다." 를, 작으면 
"틀렸습니다. 조금 더 큰 수입니다." 를 출력하고, 같으면 
"맞았습니다."를 출력하고 종료하는 프로그램을 만들어 
보세요. (저장된 수는 = 23)

a = 23
number = 99999
while number != a :
    number = int(input("숫자를 입력하세요"))
    if number > a :
        print("틀렸습니다. 조금 더 작은수입니다.")
    elif number < a :
        print("틀렸습니다. 조금 더 큰 수수입니다.")
    else :
        print("맞았습니다")
        
"""
'''
1에서 1000 사이의 난수를 발생시킨 후 그 수를 추측하는 게임을 만들어보세요.
시도할 때마다 몇번째 시도인지 알려주고, 정답이 추측한 수보다 크면
"더 큰 수입니다"를 나타내고 정답이 추측한 수보다 작으면 "더 작은 수입니다"
를 나타내게 하세요. 정답을 맞추면 "맞았습니다"를 보여줍니다.
'''
'''
import random
a = random.randrange(1, 1001)
cnt =0

number = 0
while number != a :
    number = int(input("숫자를 입력하세요"))
    cnt +=1
    if number > a :
        print(f"{cnt}번째 시도입니다. 틀렸습니다. 조금 더 작은수입니다.")
    elif number < a :
        print(f"{cnt}번째 시도입니다. 틀렸습니다. 조금 더 큰 수수입니다.")
    else :
        print(f"{cnt}번째 시도입니다. 맞았습니다")
'''
'''
# This is my shopping list
                                                                                                                 shoplist = ['apple', 'mango', 'carrot', 'banana']
 shoplist = ['apple', 'mango', 'carrot', 'banana']
 print('I have', len(shoplist), 'items to 
purchase.')
 print('These items are: ', end='')
 for item in shoplist:
    print(item, end=' ')
print('\nI also have to buy rice.')
 shoplist.append('rice')
 print('My shopping list is now', shoplist)
 print('I will sort my list now')
 shoplist.sort()
 print('Sorted shopping list is', shoplist)
print('The first item I will buy is', shoplist[0])
 olditem = shoplist[0]
 del shoplist[0]
 print('I bought the', olditem)
 print('My shopping list is now', shoplist)

'''
'''
#제일 친한 친구 5명의 이름을 리스트에 저장했다가 출력하는 프로그램
friend_list = []
for i in range(5):
    friend_list.append(input("친구의 이름을 입력:"))
print(friend_list)
  

'''
'''
zoo = ('python', 'elephant', 'penguin')   
print('Number of animals in the zoo is', len(zoo))

new_zoo = 'monkey', 'camel', zoo
print('Number of cages in the new zoo is', len(new_zoo))
print('All animals in new zoo are', new_zoo)
print('Animals brought from old zoo are', new_zoo[2])
print('Last animal brought from old zoo is', new_zoo[2][2])
print('Number of animals in the new zoo is', \
     len(new_zoo)-1+len(new_zoo[2]))

       
'''
'''
ab = { 'Baram' : 'ludenscode@gmail.com',
        'Larry' : 'larry@wall.org',
        'Matsumoto' : 'matz@ruby-lang.org',
        'Spammer': 'spammer@hotmail.com'
    }
for name in ab:
    print(name)
'''
'''
ab = { 'Baram' : 'ludenscode@gmail.com',
        'Larry' : 'larry@wall.org',
        'Matsumoto' : 'matz@ruby-lang.org',
        'Spammer': 'spammer@hotmail.com'
    }
for name in ab:
    print(name)
for name in ab:
    print(name, ab[name])
'''
'''
ab = { 'Baram' : 'ludenscode@gmail.com',
        'Larry' : 'larry@wall.org',
        'Matsumoto' : 'matz@ruby-lang.org',
        'Spammer': 'spammer@hotmail.com'
    }
for name in ab:
    print(name)
for name in ab:
    print(name, ab[name])
for na me, address in ab.items():
    print(name, address)

'''
'''
# 20이상인 수만 고르기
temperatures = [2, 5, 8, 10, 50, 80, 12, 52, 99]

myTemp = []
for temp in temperatures:
    if temp >=20:
        myTemp.append(temp)
print(myTemp)
'''
'''
# 리스트로 된 값을 읽어서 평균과 표준편차를 반환하는 함수를 만들어보세요.

mydata =[10,50,20,88, 90]
def data_analysis(values):
    #평균구하기
    n=len(values)
    sum=0
    for i in range(n):
        sum +=values[i]
    m=sum /n
 #표준편차
    ss =0
    for i in range(n):
        ss+=(values[i]- m)**2
    sd =(ss/ (n-1))**0.5
    return(m, sd)
(mean, std) =data_analysis(mydata)
print(mean, std)
'''
# numpy를 사용한 리스트로 된 값을 읽어서 평균과 표준편차를 반환하는 함수를 만들어보세요.
import numpy as np
def np_analysis(values):
    mean=np.mean(values)
    std=np.std(values)
    return(mean,std)

mydata =[10,50,20,88, 90]
mean,std= np_analysis(mydata)
print(mean, std)
