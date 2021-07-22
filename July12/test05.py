'''
00000
0
00000
0
00000
'''

# for문: 1번
# for i in range(1,6):
#     if i % 2==0:
#         print('0')
#     else:
#         print('00000')

#이중for문
# for i in range(5): #0~4번째열까지
#     if i % 2==0:
#         for j in range(5):
#             print(0, end='')
#         print()
#     else:
#         print(0)

'''
00000
    0
00000
    0
00000
'''

# for i in range(1,6):
#     if i % 2 !=0:
#         for j in range(5):
#             print(0, end='')
#         print()
#     else:
#         print('    0')

'''      
  12345     = j
1 00000
2 0
3 00000
4 0
5 00000
"
i
'''
for i in range(5):
    if i % 2 == 0:
        for _ in range(5):
            print(0, end='')
        print()
    else:
        print(0)