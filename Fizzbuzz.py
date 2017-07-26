#for i in range(100):
   # count = i + 1
  #  if count % 3 == 0:
      #print('Fizz')
 #   else:
#        print(count)



#for i in range(101):
 #   count = i + 1
  #  if count % 3 == 0:
   #     print('Fizz')
   # elif count % 5 == 0:
    #    print('buzz')
  #  else:
   #     print(count)


for i in range(101):
    count = i + 1
    if count % 3 == 0:
        if count % 5 == 0:
            print('fizzbuzz')
        else:
            print(count)
    count = i + 1
    if count % 3 == 0:
        print('Fizz')
    elif count % 5 == 0:
        print('buzz')
    else:
        print(count)
