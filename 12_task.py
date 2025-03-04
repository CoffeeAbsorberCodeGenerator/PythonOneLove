# s = '5'*65
# while '333' in s or '555' in s:
#     if '555' in s:
#         s = s.replace('555', '3', 1)
#     else:
#         s = s.replace('333', '5', 1)
# print(s)

# s = '563'*121
# while '56' in s or '3333' in s:
#     s = s.replace('56', '3', 1)
#     s = s.replace('3333', '3', 1)
# print(s)

# for c in range(41, 100):
#     s = '1'*c
#     while '111' in s:
#         s = s.replace('111', '2', 1)
#         s = s.replace('222', '1', 1)
#     if s == '11':
#         print(c)
#         break

# count = 0
# for c in range(1, 100):
#     s = '1'*c
#     while '111' in s:
#         s = s.replace('111', '2', 1)
#         s = s.replace('222', '3', 1)
#         s = s.replace('333', '1', 1)
#         if s == '321':
#             print(c)
#             count += 1
# print("Ответ: " + str(count))

# for c in range(201, 500):
#     s = '5'*c
#     while '555' in s or '888' in s:
#         s = s.replace('555', '8', 1)
#         s = s.replace('888', '55')
#     if s.count('5') == s.count('8'):
#         print(c)
#         break

# minim = 100000
# for c in range(51, 1000):
#     s = '1'*c
#     while '111' in s:
#         s = s.replace('111', '22', 1)
#         s = s.replace('222', '11', 1)
#     if s.count('1') == 1:
#         print(c)
#         break

# s = '>' + '1'*28 + '2'*18 + '3'*35
# while '>1' in s or '>2' in s or '>3' in s:
#     if '>1' in s:
#         s = s.replace('>1', '22>', 1)
#     if '>2' in s:
#         s = s.replace('>2', '2>1', 1)
#     if '>3' in s:
#         s = s.replace('>3', '1>2', 1)
# print(sum(map(int, s[:-1])))

# def simple(m):
#     c = 0
#     for i in range(2, m):
#         if m % i == 0:
#             c += 1
#             return False
#     if c == 0:
#         return True
#
# for n in range(1, 100):
#     s = '>' + '0'*39 + '1'*n + '2'*39
#     while '>1' in s or '>2' in s or '>0' in s:
#         if '>1' in s:
#             s = s.replace('>1', '22>', 1)
#         if '>2' in s:
#             s = s.replace('>2', '2>', 1)
#         if '>0' in s:
#             s = s.replace('>0', '1>', 1)
#     if simple(sum(map(int, s[:-1]))):
#         print(n)
#         break

# for a in range(1, 100):
#     for b in range(1, 100):
#         for c in range(1, 100):
#             s = '0' + '1'*a + '2'*b + '3'*c
#             while '01' in s or '02' in s or '03' in s:
#                 s = s.replace('01', '2302', 1)
#                 s = s.replace('02', '10', 1)
#                 s = s.replace('03', '201', 1)
#             if s.count('1') == 58 and s.count('2') == 23 and s.count('3') == 15:
#                 print(b)
#                 break






