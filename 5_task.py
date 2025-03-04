# for n in range(1, 1000):
#     n2 = bin(n)[2:]
#     if n % 2 == 0:
#         n2 += '10'
#     else:
#         n2 += '01'
#     r = int(n2, 2)
#     if r > 200:
#         print(n)
#         break


# for n in range(1, 1000):
#     n2 = bin(n)[2:]
#     n2 += str(n2.count("1") % 2)
#     n2 += str(n2.count("1") % 2)
#     r = int(n2, 2)
#     if r > 123:
#         print(r)
#         break


# for n in range(1, 1000):
#     n2 = bin(n)[2:]
#     n2 += n2[-1]
#     n2 += str(bin(n)[2:].count("1") % 2)
#     n2 += str(1 - n2.count("1") % 2)
#     r = int(n2, 2)
#     if r > 553:
#         print(n)
#         break


# for n in range(1, 1000):
#     n2 = bin(n)[2:]
#     if n % 2 != 0:
#         n2 += "0"
#     else:
#         n2 = "1" + n2
#     if n2.count("1") % 2 == 0:
#         n2 += "1"
#     else:
#         n2 += "0"
#     r = int(n2, 2)
#     if r > 300:
#         print(n)
#         break


# for n in range(1, 1000):
#     n2 = bin(n)[2:]
#     if n % 2 == 0:
#         n2 = "1" + n2 + "10"
#     else:
#         n2 = "11" + n2 + "0"
#     r = int(n2, 2)
#     if r > 130:
#         print(r)
#         break


# for n in range(1, 1000):
#     n2 = bin(n)[2:]
#     if n % 2 == 0:
#         n2 += str(bin(n2.count("1"))[2:])
#     else:
#         n2 = "1" + n2 + "00"
#     r = int(n2, 2)
#     if r > 401:
#         print(n)
#         break


# for n in range(1, 4000):
#     n2 = bin(n)[2:] #двоичная запись n
#     s = 0
#     #находим сумму цифр десятичной записи числа n:
#     for k in str(n):
#         s += int(k)
#     if s % 2 != 0:
#         n2 += "1" #если нечет
#     else:
#         n2 += "0" #если чет
#     s2 = 0
#     #находим сумму цифр десятичной записи нового числа n2:
#     for m in str(int(n2, 2)):
#         s2 += int(m)
#     if s2 % 2 != 0:
#         n2 += "1" #если нечет
#     else:
#         n2 += "0" #если чет
#     r = int(n2, 2)
#     if r > 1234:
#         print(r)
#         break


# for n in range(1, 1000):
#     n2 = bin(n)[2:]
#     #три последние цифры числа n это остаток от деления на 1000
#     if n % 3 == 0:
#         n2 += n2[-3:]
#     else:
#         n2 += bin((n % 3)*3)[2:]
#     r = int(n2, 2)
#     if r > 99:
#         print(n)
#         break


# for n in range(1000, 10000):
#     ns = str(n)
#     sum1 = int(ns[0]) + int(ns[1])
#     sum2 = int(ns[2]) + int(ns[3])
#     if sum1 > sum2:
#         s = str(sum1) + str(sum2)
#     else: s = str(sum2) + str(sum1)
#     if int(s) == 1412:
#         print(n)

# for n in range(100, 1000):
#     ns = str(n)
#     sum1 = int(ns[0]) + int(ns[1])
#     sum2 = int(ns[1]) + int(ns[2])
#     if sum1 > sum2:
#         s = str(sum1) + str(sum2)
#     else: s = str(sum2) + str(sum1)
#     if int(s) == 157:
#         print(n)

# for n in range(100, 1000):
#     ns = str(n)
#     if int(ns[0])*int(ns[1]) <= int(ns[1])*int(ns[2]):
#         s = str(int(ns[0])*int(ns[1])) + str(int(ns[1])*int(ns[2]))
#     else:
#         s = str(int(ns[1]) * int(ns[2])) + str(int(ns[0]) * int(ns[1]))
#     if int(s) == 621:
#         print(n)

# for n in range(1000, 10000):
#     ns = str(n)
#     s1 = int(ns[0]) + int(ns[1])
#     s2 = int(ns[1]) + int(ns[2])
#     s3 = int(ns[2]) + int(ns[3])
#     a = sorted([s1, s2, s3])
#     r = str(a[0]) + str(a[1])
#     if int(r) == 1215:
#         print(n)

# for y in range(100, 1_000):
#     ys = str(y)
#     sum3 = 4 + int(ys[2])
#     sum2 = 9 + int(ys[1])
#     sum1 = 6 + int(ys[0])
#     a = sorted([sum1, sum2, sum3])
#     s = str(a[2]) + str(a[1]) + str(a[0])
#     if s == '11108':
#         print(y)

# c = 0
# for x in range(10, 100):
#     y = str(x % 4) + str(x % 3) + str(x % 2)
#     if y == '200':
#         c += 1
# print(c)


# for n in range(1, 1000):
#     n2 = f'{n:b}'
#     if n % 2 == 0:
#         n2 += '01'
#     else: n2 += '10'
#     r = int(n2, 2)
#     if r > 130:
#         print(r)
#         break

# for n in range(1, 1000):
#     n2 = f'{n:b}'
#     for i in range(2):
#         if n2.count('1') % 2 == 0:
#             n2 += '0'
#         else: n2 += '1'
#     r = int(n2, 2)
#     if r > 184:
#         print(n)
#         break

# n всегда идут по возрастанию
# r - нет, используем min/max или список

# a = []
# for n in range(1, 1000):
#     n2 = f'{n:b}'
#     n2_2 = n2 + n2[-1]
#     if n2.count('1') % 2 == 0: n2_2 += '0'
#     else: n2_2 += '1'
#     if n2_2.count('1') % 2 == 0: n2_2 += '0'
#     else: n2_2 += '1'
#     r = int(n2_2, 2)
#     if r > 105:
#         a.append(r)
# print(min(a))

# for n in range(2, 1000):
#     n2 = f'{n:b}'
#     n2 += n2[-2]
#     n2 += n2[1]
#     r = int(n2, 2)
#     if r > 100:
#         print(n)
#         break

# for n in range(1, 1000):
#     ns = str(n)
#     ns += ns[-1]
#     n2 = f'{int(ns):b}'
#     if n2.count('1') % 2 == 0: n2 += '0'
#     else: n2 += '1'
#     r = int(n2, 2)
#     if r > 413:
#         print(n)
#         break

# for n in range(2, 81):
#     n2 = f'{n:b}'
#     for i in range(3):
#         if n2.count('1') == n2.count('0'):
#             n2 += n2[-1]
#         elif n2.count('1') > n2.count('0'):
#             n2 += '0'
#         else: n2 += '1'
#     r = int(n2, 2)
#     if r % 2 == 0 and r % 4 != 0:
#         print(n)

# for n in range(1, 1000):
#     n2 = f'{n:b}'
#     if n % 2 == 0:
#         n2 += f'{n2.count('1'):b}'
#     else: n2 = '1' + n2 + '00'
#     r = int(n2, 2)
#     if r > 215:
#         print(n)
#         break

# for n in range(1, 1000):
#     n2 = f'{n:b}'
#     if n2.count('1') % 2 == 0:
#         n2 = '10' + n2[2:] + '0'
#     else: n2 = '11' + n2[2:] + '1'
#     r = int(n2, 2)
#     if r >= 16:
#         print(n)
#         break

# a = []
# for n in range(1, 1000):
#     n2 = f'{n:b}'
#     if n % 3 == 0:
#         n2 += n2[-2:]
#     else:
#         n2 += f'{(n % 3)*3:b}'
#     r = int(n2, 2)
#     if r >= 195:
#         a.append(r)
# print(min(a))

# a = []
# for n in range(1, 1000):
#     n2 = f'{n:b}'
#     if n2.count('1') % 3 == 0:
#         n2 += f'{(n2.count('1')%5):b}'
#     else:
#         n2 = '1' + n2 + '10'
#     r = int(n2, 2)
#     if r > 89:
#         a.append(r)
# print(min(a))

# 1
# for n in range(1000, 10_000):
#     ns = str(n)
#     sum1 = int(ns[0]) + int(ns[1])
#     sum2 = int(ns[1]) + int(ns[2])
#     sum3 = int(ns[2]) + int(ns[3])
#     a = sorted([sum1, sum2, sum3])
#     r = str(a[1]) + str(a[2])
#     if r == '1115':
#         print(n)

# 2
# for y in range(999, 99, -1):
#     ys = str(y)
#     sum1 = int(ys[0]) + 4
#     sum2 = int(ys[1]) + 8
#     sum3 = int(ys[2]) + 6
#     a = sorted([sum1, sum2, sum3])
#     r = str(a[2]) + str(a[1]) + str(a[0])
#     if r == '13107':
#         print(y)
#         break

# 3
# for x in range(10, 100):
#     y = str(x % 7) + str(x % 2) + str(x % 5)
#     if y == '312':
#         print(x)

# 4
# a = []
# for n in range(2, 1000):
#     if n % 2 == 0:
#         n /= 2
#     else: n -= 1
#     if n % 5 == 0:
#         n /= 5
#     else: n -= 1
#     if n % 9 == 0:
#         n /= 9
#     else: n -= 1
#     if n == 6:
#         a.append(n)
# print(len(a))

# 5
# for n in range(1, 1000):
#     n2 = f'{n:b}'
#     if n % 2 == 0:
#         n2 += '10'
#     else: n2 += '11'
#     r = int(n2, 2)
#     if r > 105:
#         print(n)
#         break

# 6
# for n in range(1, 1000):
#     n2_st = f'{n:b}'
#     n2 = n2_st + n2_st[-1]
#     if n2_st.count('1') % 2 == 0:
#         n2 += '0'
#     else: n2 += '1'
#     if n2.count('1') % 2 == 0:
#         n2 += '0'
#     else: n2 += '1'
#     r = int(n2, 2)
#     if r > 108:
#         print(n)
#         break

# 7
# a = []
# for n in range(1, 1000):
#     n2 = f'{n:b}'
#     for i in range(2):
#         n2 += str(n2.count('1') % 2)
#     r = int(n2, 2)
#     if r < 130:
#         a.append(r)
# print(max(a))

# 8
# for n in range(2, 1000):
#     n2 = f'{n:b}'
#     n2 += n2[1]
#     n2 += n2[-2]
#     r = int(n2, 2)
#     if r > 120:
#         print(n)
#         break

# 9
# for n in range(1, 1000):
#     ns = str(n)
#     ns += ns[0]
#     n2 = f'{int(ns):b}'
#     if n2.count('1') % 2 == 0:
#         n2 += '1'
#     else: n2 += '0'
#     r = int(n2, 2)
#     if r > 204:
#         print(n)
#         break

# 10
# for n in range(2, 200):
#     n2 = f'{n:b}'
#     for i in range(3):
#         if n2.count('1') == n2.count('0'):
#             n2 += n2[-1]
#         elif n2.count('1') > n2.count('0'):
#             n2 += '0'
#         else: n2 += '1'
#     r = int(n2, 2)
#     if r % 2 == 0 and r % 4 != 0:
#         print(n)

# 11
# a = []
# for n in range(1, 13):
#     n2 = f'{n:b}'
#     if n % 2 == 0:
#         n2 = '10' + n2
#     else: n2 = '1' + n2 + '00'
#     r = int(n2, 2)
#     a.append(r)
# print(max(a))

# 12
# a = []
# for n in range(1, 1000):
#     n2 = f'{n:b}'
#     if n % 3 == 0:
#         n2 += n2[-3:]
#     else: n2 += f'{((n % 3)*3):b}'
#     r = int(n2, 2)
#     if r > 151:
#         a.append(r)
# print(min(a))

# a = []
# for n in range(1, 1000):
#     n2 = f'{n:b}'
#     if n2.count('1') % 2 == 0:
#         n2 = '10' + n2[2:] + '0'
#     else:
#         n2 = '11' + n2[2:] + '1'
#     r = int(n2, 2)
#     if r < 35:
#         a.append(n)
# print(max(a))

# for n in range(1000, 10000):
#     ns = str(n)
#     n1 = int(ns[:-1])
#     n2 = int(ns[1:])
#     r = max(n1, n2) - min(n1, n2)
#     if r == 415:
#         print(n)
#         break

# for n in range(456_789_012, 123_456_790, -1):
#     if n % 2 != 0:
#         n2 = f'{n:b}'
#         if n % 2 == 0:
#             n2 = '11' + n2
#         else:
#             n2 = '1' + n2 + '10'
#         r = int(n2, 2)
#         print(n, r)
#         break

# a = set()
# for n in range(10, 1001):
#     n2 = f'{n:b}'
#     partN2 = n2[1:]
#     for i in range(0, len(partN2)):
#         if partN2[i] == 0:
#             partN2 = partN2[i+1:]
#         if partN2[i] == 1:
#             break
#     partN = int(partN2, 2)
#     a.add(n - partN)
# print(len(a))





