# ----------------------first-------------------
# winning_num= 10
# guess_num= int(input('Enter two number for win :  '))

# if(guess_num==winning_num):
#     print('You win')
# elif(guess_num>winning_num):
#     print('TOO high')
# else:
#     print('TOO low')     

# -----------------------second----------------
u_name= input('Enter your name :  ')
u_age= int(input('Enter yout age : '))


if (u_name[0] == 'j' or u_name[0] == 'J') and u_age > 10:
    print('You can watch')
else:
    print('You are not elligible')
