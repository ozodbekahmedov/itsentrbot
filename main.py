# ism = input('ism kiritng>>>')
# print(f'asalomu alaykum: {ism}')
#
# birinchison = int(input('birinchi soni kiritng>>'))
# ikkinchison = int(input('ikkinchi soni kiritng>>'))
# uchunchison = int(input('uchinchi soni kiritng>>'))
# natija = birinchison + ikkinchison +uchunchison
# print(natija)
import random

#
# olma = 50
# bola = 6
# natija = olma//bola
# print(natija)

#
# son = int(input('son kirtng>>'))
# natija = son + 1
# natija2 = son - 1
# print(f'keyingi son: {son}-{natija} \noldingi son: {son}-{natija2}')
















# son = list(map(int,input().split()))
# son.sort()
# print(sum(son[0:-1], sum(son[1:])))



#
# son = int(input('son:'))
# daraja = 0
# count = 0
# for i in range(son+1):
#   a = 2 ** i
#   if a < son+1:
#     count = i
#     daraja = a
# print(draja)
# print(count)

# boyi = 6
# eni = 4
# chuqurligi = 3
# litr = 1000 * boyi * eni * chuqurligi
# s = 2*(boyi + eni)*chuqurligi + boyi*eni
# print(f'{s}>>>kv.m kafel kerak')
# print(f'{litr}>>>litr suv kerak')



# #
# archa = int(input('nechi qator bolsin>>'))
# for i in range(archa):
#     for archa1 in range(archa - i):
#         print()
#     for archa1 in range(2 * i + 1):
#         print('+', end=' ')
#     print()

# son = int(input('son kirting:'))
# a = list(son)
# n = int(input('son kirtng'))
# nat = n//25
# nat2 = n//100
# print(f'kgda>>{nat}, snt{nat2}')

# son = int(input('son kirtng'))
# son1 = int(input('son kirtng'))
# son3 = int(input('son kirtng'))
# son4 = int(input('son kirtng'))
# son2 = son+son1+son3+son4
# son5 = son2/4
# print(son5)


# son = int(input('son krting:'))
# son1 = int(input('son kirtng'))
# son2 = int(input('son kirtng'))
# son3 = (son+son1+son2)/2
# son4 = son3//3
# print(son4)

# #
# # son = int(input('son kirting:'))
# if son%2==1:
#     print('toq')
# else:
#     print('juft')
#
# tomon= int(input('1 tomonini kirtng'))
# tomon1 = int(input('2chi tomonini kirtng'))
# if tomon==tomon1:
#     print('kvadrat')
#
# else:
#     print('bu kvadrat emas')
#
# son = int(input('son kirtng'))
# if len(str(son)) == 4:
#     print('bu tort honali son:')
#
# else:
#     print('bu tort honalison emas ')


# son = int(input('son kirtng>>'))
# if son / 2:
#     print('qoldisz')
#
# else:
#     print('bu qoldiqli:')
# son = int(input("Istalgan son kiriting: "))
# if son>=0:
#     print("Musbat son")
# else:
#     print("Manfiy son")


# son = int(input('son kirtng>>'))
# if son // 2:
#     print('qoldiqsiz:')
# else:
#     print('qoldiqliz')



#
# son = int(input('son kirtng>>'))
# son2 = int(input('son kirtng:'))
# if son / son2:
#     print('qolqsz bolinadi:')
# else:
#     print('qoldiqli bolinadi:')

#
# a = int(input("a ni kiriting: "))
# b = int(input("b ni kiriting: "))
#
# if b < a:
#     temp = b
#     b = a
#     a = temp
#
# print("a =", a)
# print("b =", b)
# soz = 'abcd'
#
# a1 = soz[1:] + soz[0:2]
# #
#
# print(a1)

#
# sonlar = int(input('sonl vergul bilan:'))
#
# for i in sonlar:
#     son = [i]
#     print(son)



#
# sonlar = 31, 1, 0, -12
# if sonlar > 1:
#     print(sonlar)
# else:
#     print('dddf')
#
#
# a = 4
# b = 2
# s = 24
# d = s/(a+b)
# f = (s-12)/(a+b)
# print(d)
#
# print(f)


# royhat = ['oq', 'qizil','kok', 'pushti', 'qora', 'yashil']
# del royhat[1]
# print(royhat)
#
# royhat = ['oq', 'qizil','kok', 'pushti', 'qora', 'yashil']
# royhat.remove(royhat[1])
# print(royhat)

#
# royhat = ['oq', 'qizil','kok', 'pushti', 'qora', 'yashil']
# rang = royhat.pop(1)
# print(royhat)


#
#
# son = ['1', '2', '3', '4', '5']
# random.shuffle(son)
# print(son)
# son = float(int(input('son kirtng:')))
# if son >= 0:
#     print('musbat:')
#
#
# else:
#     print('manfiy:')
# son = int(input('yil kirtng:'))
# a = 2
# b = 5.25
# natija = b * a
# son1 = 2023
# son2 = son1-son
# yil = son2/2
# print(yil)
# a = {  'sichqon'
#         'sigr',
#         'yolbars',
#         'quyon',
#         'baliq',
#         'ilon',
#          'ot', }
# son = int(input('yil kiritng:'))
# a = (son+9)
#
# if a % 12 == 0:
#     print('tongiz')
#
# def muchaltopish(muchal):
#     if muchal % 12 == 0:
#         muchal = "maymun"
#     elif muchal % 12 == 1:
#         muchal = "tovuq"
#     elif muchal % 12 == 2:
#         muchal = "kuchuk"
#     elif muchal % 12 == 3:
#         muchal = "to'ng'iz"
#     elif muchal % 12 == 4:
#         muchal = "sichqon"
#     elif muchal % 12 == 5:
#         muchal = "sigir"
#     elif muchal % 12 == 6:
#         muchal = "yo'lbars"
#     elif muchal % 12 == 7:
#         muchal = "quyon"
#     elif muchal % 12 == 8:
#         muchal = "baliq"
#     elif muchal % 12 == 9:
#         muchal = "ilon"
#     elif muchal % 12 == 10:
#         muchal = "ot"
#     else:
#         muchal = "qo'y"
#     return muchal
# yil = int(input('yilingizni kiriting:'))
# print(f"Sizning muchalingiz {muchaltopish(yil)}")
#


# soz = input('matn kiritng')
# soz2 = input('qaysi harfni olmoqchsz:')
# print('orginal satr')
# print(soz)
# for i in soz:
#     if i == soz2:
#         print(i)

# def soz(soz):
#     soz2 = len(soz)
#     if soz2 < 3:
#         if soz[-3:] == 'ing':
#             soz += 'Iy'
#         else:
#             soz += 'ing'
# soz2 = input('soz kiritng:')
# print(soz(soz2))

# kun = int(input('tugilgan kunizni kiritng:'))
# oy =input('tugilgan oyingizni kirtng:')
# if oy == 'dekabrga':
#     burj = 'oqotar'
#     if (kun<22):
#     else: 'tog echkisi'
# elif oy=='yamvarga':
#     burj = 'tog echkisi'
#     if (kun<20):
#     else: 'qovga'
# elif oy == 'febralga':
#     burj = 'qovga'
#     if (kun<19):
#     else: 'baliq'
#
# elif oy == 'mart':
#     burj = 'baliq'
#     if (kun<21):
#     else:'qoy'
# elif oy == 'aprel':
#     burj = 'qoy'
#     if (kun<20):
#     else:'buzoq'
# elif oy == 'may':
#     burj = 'buzoq'
#     if (kun<21):
#     else:'egizaklar'
# elif oy == 'iyun':
#     burj = 'egizaklar'
#     if (kun < 21):
#     else:'qisqich baqa'
# elif oy == 'iyul':
#     burj = 'qisqich baqa'
#     if (kun<23):
#     else:'arslon'
# elif oy == 'avgust':
#     burj = 'arslan'
#     if(kun<23):
#     else:'parizot'
# elif oy == 'sentabr':
#     burj = 'parizot'
#     if (kun <23):
#     else:'tarozi'
# elif oy == 'oktabr':
#     burj = 'tarozi'
#     if (kun <23):
#     else: 'chayon'
# elif oy == 'nayabr':
#     burj = 'chayon'
#     if (kun<22) ':
#     else 'oqotar
# print(f'burjing iz {burj}')
# print('febral Mart Aprel May Iyun Iyul Avgust Sentabr Oktabr Dekabr Yanvar')
# oy = input('oy kiritng:')
# if oy == 'febral':
#     print('fevral oyida 28/29 kun bor')
# elif oy in ('Aprel', 'Iyun', 'Sentabr', 'Nayabr'):
#     print('bu oyda 30 kun bor')
# elif oy in ('Yanvar', 'Mart', 'May', 'Iyul', 'Avgust', 'Oktabr', 'Dekabr'):
#     print('bu oyda 31 kun bor')
# else:
#     print('oy nomi hato')
# ism = input('ism kiritng:')
# if len(ism) <= 3:
#     print('notogri ism:')
# else:
#     print('akut nomi band:')
#
# nomer = int(input('nomerizni kirtng:'))
# if

# kun = int(input('tugilgan kunizni kiritng:'))
# oy = input('tugilgan oyingizni kirtng:')
# burj = ''
# if oy == 'dekabr' and kun >= 20 and kun <= 31 or oy == 'yanvar' and kun <= 19:
#     burj = 'oqotar'
# #
# elif oy == 'yanvar' and kun >= 20 and kun <= 31 or oy == 'fevral' and kun <= 19:
#     burj = 'tog echkisi'
#
# elif oy == 'fevral' and kun >= 20 and kun <= 29 or oy == 'mart' and kun <= 19:
#     burj = 'qavga'
# elif oy == 'mart' and kun >= 20 and kun <= 30 or oy == 'aprel' and kun <= 19:
#     burj = 'baliq'
#
# elif oy == 'aprel' and kun >= 20 and kun <= 31 or oy == 'may' and kun <= 19:
#     burj = 'qoy'
#
# elif oy == 'may' and kun >= 20 and kun <= 31 or oy == 'iyun' and kun <= 19:
#     burj = 'buzoq'
#
# elif oy == 'iyun' and kun >= 20 and kun <= 30 or oy == 'iyul' and kun <= 19:
#     burj = 'egizaklar'
#
# elif oy == 'iyul' and kun >= 20 and kun <= 30 or oy == 'avgust' and kun <= 19:
#     burj = 'qisqich baqa'
#
# elif oy == 'ovgust' and kun >= 20 and kun <= 31 or oy == 'sentabr' and kun <= 19:
#     burj = 'arslon'
#
# elif oy == 'sentabr' and kun >= 20 and kun <= 30 or oy == 'oktabr' and kun <= 19:
#     burj = 'parizot'
#
# elif oy == 'oktabr' and kun >= 20 and kun <= 31 or oy == 'nayabr' and kun <= 19:
#     burj = 'tarozi'
#
# elif oy == 'fevral' and kun >= 20 and kun <= 30:
#     burj = 'chayon'

# son = {1: 10, 2:20, 3:30, 4:40, 5:50, 6:60}
# i = int(input('son kirtng'))
# if i in son:
#     print('bu son mavjud>')
# else:
#     print('mavjud emas:')
# print('kalitlar>>> a, b, s, d')
# a = {'a':1, 'b':2, 's':3, 'd':4}
# i = input('kalit kiritng')
# if i in a:
#     del a[i]
# # print(a)
# a = 1, 2, 3, 4, 5, 6, 7, 8, 9
# for i in a:
#     print(str(i)*i)

# son = int(input('nechtalik bolsin:'))
# for i in range(son):
#     for s in range(i):
#         print('*', end='')
#     print('')
#
# for i in range(son, 0,-1):
#     for s in range(i):
#         print('*', end='')
#     print('')


#
# son = range(51)
# a = ''
# for i in son:
#     a = son + i
#     print(a)
#4.1
# son = list(range(11, 100, 2))
# suma = sum(son)
# print(suma)
# print(son)
#
# 4.2
# while True:
#     son = input('son:')
#     if son.isdigit():
#         print('raqam')
#     elif son == 'stop':
#         break
#     else:
#         print('raqam kirting')
#
# son = input('son kirtng:')
# if son.isdigit():
#     lst = []
#     for i in son:
#         lst.append(int(i))
#     lst.sort()
#     print(f'kota sonlar {lst[-1]}')
#     print(f'kichik sonlar: {list[0]}')


# sonlar = list(input('son'))
# birxonali = []
# ikkixonali = []
# for i in sonlar:
#     i = str(i)
#     if len(i) == 1 and '2' in i:
#         birxonali.append(int(i))
#     elif len(i) == 2 and '2' in i:
#         ikkixonali.append(int(i))
# print(f'xonalar soni 1 \n'
#       f'2 raqami qatnashgan sonlar {birxonali}')
# print(f'xonalar soni 2\n'
#       f'2 raqami qatnashgan sonlar
# soz1 = []
# soz =input('soz:')
# for i in soz:
#     soz1.append(len(i,i))
#     print(soz1)
#     soz1,sort()
#
# soz = input('soz ').split()
# uzunlik = []
# for i in  soz:
#     uzunlik.append((len(i), i)
# uzunlik.sort()
# uzunsz = uzunlik[-1][1]
# uzunligi = uzunlik[-1][1]
# print(f'{uzunligi}\n'
#       f'{uzmsz}')

# file = open('data.txt', 'r')
# 4.17
# sonlar = [10, 20, 30, 40, 7]
# for i in sonlar:
#     if i > 0[:3]:
#         summa = sum(sorted(i))
# print('sonlar', sonlar)
# print(f"yigind: {summa}")

# import random
# for i in range(1,100):
#     if i % 2 == 0,10
#     random.randrange(i)
# print(random)
#
# sonlar = input().split()
# sonlar = list(map(int, sonlar))
#
# lst = []
# for i in sonlar:
#     if i >0:
#         lst.append(i)
# lst.sort()
# print(sum(lst[:3]))

# sonlar = list(map(int))
#
# # a = [['a'], ['b'], ['s'], ['d']]
# print(f'{a[:1]}\n{a[:2]}\n{a[:3]}')

#
# son = input('sonlar kirtng').split()
# son1 = input('sonlar kirtng').split()
# for i in son:
#     if i in son1:
#         print(i)


# son = int(input('sonlar kiritng>>'))
# a = {}
# for i in range(1,son+1):
#     a = i*i
#     print(a)

# son = input('2 honali son kirtng>>')
# if son%5 ==0:
# sonlar = [34, 1, 0, -23, 12, -88]
# for i in sonlar:
#     if i >0:
#         print(f'musbat sonlar>>{i}')
#
# print(f'royhat>>{sonlar}')

#
# son = in
# qiymat = []
# for i in son:
#     if i == 4:
#         qiymat.append(i)
#         print(i)


# son = input('son kirtng>>')
# son1 = input('son kirtng>>')
# if son[:0] == son1[:0]:
#     if son[-1:] == son1[-1:]:
#         print('togri')
#     else:
#         print('notogri')


# son =  input('son kirtng').split()
# son2 = 0
# son3 = 0
# for i in son:
#     if int(i) %2:
#         son2+=1
#     else:
#         son3+=1
# print(f'toq sonlar>> {son2}')
# print(f'juf sonlar>> {son3}')
#
# son =  input('son kirtng>>')
# SON = 0
# for i in son:
#     if int(i) == 1:
#         print('I')
#     elif int(i) == 2:
#         print('II')
#     elif int(i) == 3:
#         print('III')
#     elif int(i) == 4:
#         print('IV')
#     elif int(i) == 5:
#         print('V')
#     elif int(i) == 6:
#         print('VI')
#     elif int(i) == 7:
#         print('VII')
#     elif int(i) == 8:
#         print('VIII')
#     elif int(i) == 9:
#         print('IX')
#     elif int(i) == 10:
#         print('X')
#     elif int(i) == 20:
#         print('XX')
#
# for i in range(10):
#     if i == 3 or i == 6:
#         continue
#     print(i)
# son = int(input('son kirtng>>'))
# son2 = int(input('ikkinchi son kirtng'))
# son3 = int(input('uchinchi son kirtng'))
# son4 = son,son2,son3
#
# soz = input('soz kirtng:')
# for i in soz:
#     if i == soz[:4].upper():
#         print(i)
# son = input('son kirtng:')
# son2 = 0
# for i in son:
#     if i.isdigit() == True:
#         son1 = int(i)
#         son3 = son + son2
# print(son)

soz = input('soz kirtng>')
for i in soz:
    if i == 1:
        if i > 1:
            print(soz)



def dsas():
    pass
