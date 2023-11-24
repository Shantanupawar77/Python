a='hi'
b=a.replace('h','')
print(b)



# a=int(input())
# if(a==0):
#     print(0)
# else:
#     x1=0
#     x2=1
#     n=1
#     while(x2<=a):
#         if(x2==a):
#             print(n)
#             break
        
#         x1=x2
#         x2=x1+x2
#         n+=1
#     else:
#         print(-1)


# a = int(input())
# if a == 0:
#     print(0)
# else:
#     fib_prev, fib_next = 0, 1
#     n = 1
#     while fib_next <= a:
#         if fib_next == a:
#             print(n)
#             break
#         fib_prev, fib_next = fib_next, fib_prev + fib_next
#         n += 1
#     else:
#         print(-1)
# a=[int(s) for s in input().split()]
# index_max=0
# index_min=0
# for i in range(1,len(a)):
#     if(a[i]>a[index_max]):
#         index_max=i
#     if(a[i]<a[index_min]):
#         index_min=i
#     a[index_max],a[index_min]=a[index_min],a[index_max]
# print(' '.join([str(i) for i in a]))
# def power(a,n):
#     res=1
#     for i in range(abs(n)):
#         res*=i
#         if(n>=0):
#             return res
#         else:
#             return 1/res
# print(power(float(input())),int(input()))

# def power(a,n):
#     res=1
#     for i in range(abs(n)):
#         res*=a
#         if(n>=0):
#             return res
#         else:
#             return 1/res
# print(power(float(input()),int(input())))


# def power(a, n):
#     res = 1
#     for i in range(abs(n)):
#         res *= a
#         if n >= 0:
#             return res
#         else:
#             return 1 / res
# print(power(float(input()), int(input())))

# def capitalize(word):
#     first_letter_small=word[0]
#     first_letter_big=chr(ord(first_letter_small)-ord('a') +ord('A'))
#     return first_letter_big+word[1:]
# sourse=input().split()
# res=[]
# for word in sourse:
#     res.append(capitalize(word))
# print(' '.join(res))
# def power(a,n):
#     if(n==0):
#         return 1
#     else:
#         return power(a,n-1)
# print(float(input()),int(input()))
# print(len(set(input().split)) & (set(input().split())))
# print(len(set(input().split())) & set(input().split()))

# print(len(set(input().split()) & set(input().split())))
# print(len(set(input().split()) & set(input().split())))
from collections import defaultdict
latin_to_english = defaultdict(list)
for i in range(int(input())):
    english_word, latin_translations_chunk = input().split(' -')
    latin_translations = latin_translations_chunk.split(', ')
    for latin_word in latin_translations:
        latin_to_english[latin_word].append(english_word)
 
print(len(latin_to_english))
for latin_word, english_translations in sorted(latin_to_english.items()):
    print(latin_word + ' - ' + ', '.join(english_translations))

n = 8
x = []
y = []
for i in range(n):
    new_x, new_y = [int(s) for s in input().split()]
    x.append(new_x)
    y.append(new_y)
correct = True
for i in range(n):
    for j in range(i + 1, n):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            correct = False
if correct:
    print('NO')
else:
    print('YES')





n, k = [int(s) for s in input().split()]
bahn = ['I'] * n
for i in range(k):
    left, right = [int(s) for s in input().split()]
    for j in range(left - 1, right):
        bahn[j] = '.'
print(''.join(bahn))




from collections import defaultdict
latin_to_english = defaultdict(list)
for i in range(int(input())):
    english_word, latin_translations_chunk = input().split(' -')
    latin_translations = latin_translations_chunk.split(', ')
    for latin_word in latin_translations:
        latin_to_english[latin_word].append(english_word)
 
print(len(latin_to_english))
for latin_word, english_translations in sorted(latin_to_english.items()):
    print(latin_word + ' - ' + ', '.join(english_translations))