from stack import Stack

def main():
    print_help()
    
    while True:
        raw = input('>')
        
        if raw == QUIT:
            break
        if raw == HELP:
            print_help()
        else:
            try:
                # Decimal -> Roman
                num = int(raw)
                
                # TODO: implement
                
                print(str(num))
                
            except ValueError:
                # Roman -> Decimal
                r_to_d(raw)

QUIT = 'q'
HELP = '?'
NUMERALS = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000 }

def r_to_d(raw):
    # TODO: check for invalid values (IIII, IIX, etc...)
    raw = raw.upper()
    
    vals = Stack()
    
    total = 0
    
    for c in raw:
        try:
            vals.push(NUMERALS[c])    
        except KeyError:
            print('\'{0}\' is not a valid Roman numeral.'.format(c))
            return 0
            
    if vals.isEmpty():
        return 0
        
    val = vals.pop()
    
    total = 0
    
    while not vals.isEmpty():     
        if val <= vals.peek():
            total += val
            
            val = 0            
        else:
            total += (val - vals.pop())
            
            val = 0
            
        if not vals.isEmpty():
            val = vals.pop()
    
    total += val
    
    return total
        
def print_help():
    print('Enter roman numeral to convert')
    print('Enter \'{0}\' to quit, or \'{1}\' for this help text.'.format(QUIT, HELP))
            
if __name__ == '__main__':
    main()