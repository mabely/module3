# Try/except
try:
    f = open('testfile.txt')
except Exception:
    print('Error!')

# Multiple exceptions
try:
    f = open('testfile.txt')
    s1 = not_exist
except FileNotFoundError:
    print('Sorry, the file does not exist')
except Exception:
    print('Something is wrong after open function')

# Printing exception as detected
try:
    f = open('testfile.txt')
    # s1 = not_exists #WHAT IS THIS FOR?
except Exception as e:
    print(e)

# Try, exception, else - else is for if no exception
try:
    f = open('testfile.txt')
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()

# Finally 
try:
    f = open('testfile')
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print('Executing finally!')

# Ex of raising exceptions. Here, I want the file contents to be printed, unless the file specified is 'test.txt' (which in this case, it is)
try:
    with open('test.txt', 'r') as f:
        f_text = f.read()
        if f.name == 'test.txt':
            # it's better to raise specific errors than generic
            raise OSError('that is the wrong file!')
except Exception as e:
    print(e, 'this is the except block')
# try does not work so else does not
else:
    print(f_text)
finally:
    print('this is the end!')


