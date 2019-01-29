def DataBundlePurchase(true_pin, balance):
    print('Welcome to The Phone People!')
    try:
        if pin_attempts(true_pin):
            if menu(balance) == 1:
                return True, balance
        elif pin_attempts(true_pin) == False:
            return 'Your account has been locked, please contact us at 020 123 456.','account_locked'
        else:
            print('not sure what happened there')
            return False, None
        
    except SyntaxError:
        ('An error occurred with the syntax')
    except TypeError:
        ('A type error occurred')
    except ValueError:
        ('A value error occurred')
    except Exception as e:
        print(e)
        return False

# Main pin checking function, calling 'check_pin which asks for pin
def pin_attempts(true_pin):
    try:
        if check_pin(true_pin):
            return True
        print('\nPlease try again (second attempt)')
        if check_pin(true_pin):
            return True
        print('\nPlease try again (final attempt)')
        if check_pin(true_pin):
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False

# Pin checking 
def check_pin(true_pin):
    attempt = input('Enter your pin: ')
    try:
        if attempt == true_pin:
            return True
        elif attempt != true_pin:
            if len(attempt) != 4:
                raise ValueError('\n(Hint: the pin is 4 digits long)')
            return False
        else:
            raise Exception('Oops something happened whilst checking your pin, please wait for assistance')
    except Exception as e:
        print(e)
        return False

def menu(balance):
    print('Would you like to:\n1 Check balance\n2 Purchase data bundle\n')
    try:
        selection = int(input('Enter 1/2: '))
        # ADD THE ERROR WHILE LOOP!
        # while (TypeError, ValueError):
        #     ('Something went wrong there, please type 1 or 2')
        
    except Exception as e:
        print(e)
    else:
        if selection == 1:
            print('You have {} remaining in your account'.format(balance))
        elif selection == 2:
            if mob_num_check():
                # FUNCTION FOR TOP UP
                print('func for top up to come')
            elif mob_num_check() == False:
                print('Mobile number verification failed')
                # RETURN TO MAIN MENU?

def mob_num_check():
    try:
        mob1 = 1111
        mob2 = 2222
        print('*****')
# CURRENTLY THE ERRORS DO NOT WORK RE LENGTH 
        while mob1 != mob2:
            mob1 = int(input('Enter your mobile number: '))
            if len(str(mob1)) == 4:
                mob2 = int(input('Confirm your mobile number: '))
            if len(str(mob1)) != 4:
                # CHANGE ABOVE TO 11!
                raise ValueError('\n(Hint: please enter 11 digits)')
        if mob1 == mob2:
            return True
    except (TypeError, ValueError):
        print('Oops something went wrong!')

    except Exception as e:
        print(e)
