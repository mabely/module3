class Calculator(object):
    def add(self, x, y):
        try:
            result = float(x) + float(y)
            return result
        except (ValueError, SyntaxError):
            print('Numbers only please')
        
Calculator.add(2,2)



