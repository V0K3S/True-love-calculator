#Truelove calculator
lover1 = input('what is your name? ')
lover2 = input('what is your lovers name? ')

lovers = lover1.lower() + lover2.lower()
count_t = lovers.count('t')
count_r = lovers.count('r')
count_u = lovers.count('u')
count_e = lovers.count('e')
count_l = lovers.count('l')
count_o = lovers.count('o')
count_v = lovers.count('v')
count_e = lovers.count('e')

lovescore = count_t + count_r + count_u + count_e + count_l + count_o + count_v + count_e 
print ('your love score is ' + str(lovescore))

if lovescore < 3:
   print('No love here') 
elif 3< lovescore < 6:
   print('Budding love')
elif 5<  lovescore < 9:
   print('True love <3')
elif 9< lovescore < 10:
   print('VETERAN LOVE!!!')
elif lovescore > 10:
   print('Get married ASAP!!!')