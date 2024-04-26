password='Anuja'
attempts=3
while attempts > 0:
    user_input=input('enter the password')
    if user_input == password:
        print('welcome')
        break
    else:
        attempts-=1
        if attempts > 0:
            print(f"wrong password!you have {attempts} ")
        else:
            print('account blocked')
            break

    