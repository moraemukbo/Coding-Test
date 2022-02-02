#1000 A+B
from bdb import Breakpoint


input_data = input().split(' ')
# 1 3
A = int(input_data[0])
B = int(input_data[1])
print(A + B)

#1001 A-B
input_data = input().split(' ')
A = int(input_data[0])
B = int(input_data[1])
print(A - B)

#1008 A/B
input_data = input().split(' ')

A = int(input_data[0])
B = int(input_data[1])
print(A / B)

#1330 두 수 비교하기
jungsu = input().split(" ")
A = int(jungsu[0])
B = int(jungsu[1])
if A>B:
    print(">")
elif A<B:
    print("<")
else:
    print("==")

#2163 초콜릿자르기
n, m = map(int, input("").split())

print(n*m-1)

#2438 별찍기-1
n = int(input())

for i in range(1,n + 1):
    for j in range(0,i):
        print("*", end="")
    print()

#2439 별찍기-2
N = int(input())
1<= N <= 100

for i in range(1,N+1):
    print(' '*(N-i)+'*'*i)

#2557 HELLO WORLD
print("Hello World!")

#2558 A+B-2
a = int(input())
b = int(input())
print (a+b)

#2588 곱셈
a = int(input()) 
b = int(input()) 
b1 = int(b/100) 
b2 = int((b/10)%10) 
b3 = int(b%10) 
print(a*b3) 
print(a*b2) 
print(a*b1) 
print(a*b3 + a*b2*10 + a*b1*100)

#2739 구구단
n =int(input())
for i in range(1,10):
    print('{0} * {1} = {2}'.format(n, i , n*i))

#2741 n찍기
n= int(input())
for i in range(1,n+1):
    print(i)

#2742 기찍n
n=int(input())
for i in range(n,0,-1):
    print(i)

#2753 윤년
year=int(input())
if (year/4==0 and year/100!=0) or year/400==0:
    print("1")
else:
    print("0") 

#2884 알람시계
time =input().split()
H =int(time[0])
M =int(time[1])

M -=45
if M <0:
    H-=1 
    M+=60
    if H<0:
        H=23
        
print(str(H),str(M))

#3046 R2
input_data = input().split(" ")
a =int(input_data[0]) 
b =int(input_data[1] )
c=2*b-a
print(c)

#10951 A+B-4
while 1:
    a, b= map(int, input().split())
    print(a + b)

#5717 상근이의 친구들
while 1: 
    M,F = map(int, input().split()) 
    if M==0 and F==0:
        break 
    else:
        print(M+F)

#8393 합
sum = 0
n = int(input())
for i in range(1,n+1):
    sum+=i
print(sum)

#9498 시험성적
score =int(input())
if 90<=score<=100:
    print("A")
elif 80<=score<=89:
    print("B")
elif 70<=score<=79:
    print("C")
elif 60<=score<=69:
    print("D")
else:
    print("F")
    
#10171 고양이
print("\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \(__)|")

#10172 개
print('|\\_/|')
print('|q p|   /}')
print('( 0 )\"\"\"\\')
print("|\"^\"`    |")
print("||_/=\\\\__|")

#10430 나머지
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)

#10718
print("강한친구 대한육군")
print("강한친구 대한육군")

#10869 사칙연산
himdulda = input().split(" ")
A = int(himdulda[0])
B = int(himdulda[1])
print(A + B) 
print(A - B)
print(A * B)
print(A // B)
print(A % B)

#10871
input_data = input().split(" ")
n=int(input_data[0])
x=int(input_data[1])

a = list(map(int, input().split(" ")))
for i in a:
    if x>i:
        print(i)

#10950
test_case= int(input())

for i in range(test_case):
    input_data = input().split(' ')
    A = int(input_data[0])
    B = int(input_data[1])
    print(A + B) 

#10952 A+B-5
while 1:
    a, b= map(int, input().split())
    if a==0 and b ==0:
        break
    else:
        print(a + b)

#10998 
input_data = input().split(' ')
A = int(input_data[0])
B = int(input_data[1])
print(A * B)

#11021 a+b -7
t = int(input())
for i in range(t):
    i+=1
    a, b = map(int,input().split())
    print ("Case #%s: %s" %(i, a + b))

#11022 a+b-8
T = int(input())

for i in range(1,T+1):
    a,b = map(int, input().split())
    c=a+b
    
    print('Case #'+str(i)+':',str(a),'+',str(b),'=',c)
    
#14681 사분면
x=int(input())
y=int(input())
if x>0 and y>0:
    print(1)
elif x>0 and y<0:
    print(4)
elif x<0 and y>0:
    print(2)
else :
    print(3)

#15552 빠른 a+b
import sys

test_case=int(input())
for i in range(test_case):
    input_data = sys.stdin.readline().rstrip().split(' ')
    A = int(input_data[0])
    B = int(input_data[1])
    print(A + B)