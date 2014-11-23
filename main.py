from stack import Stack
from collections import OrderedDict

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
                print(d_to_r(int(raw)))
                
            except ValueError:
                # Roman -> Decimal
                val = r_to_d(raw)
                
                if val <= 0:
                    print('please enter a valid roman numeral')
                else:
                    print(str(val))

QUIT = 'q'
HELP = '?'

NUMERALS = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100, 
    'D' : 500, 
    'M' : 1000 
    }

VALUES = OrderedDict(sorted({
    1 : 'I',
    4 : 'IV',
    5 : 'V',
    9 : 'IX',
    10 : 'X',
    40 : 'XL',
    50 : 'L', 
    90 : 'XC', 
    100 : 'C', 
    400 : 'CD', 
    500 : 'D', 
    900 : 'CM', 
    1000 : 'M' 
    }.items()))

def d_to_r(num):
    if num <= 0 or num >= 5000:
        return ''
    
    out = ''
    
    while num != 0:
        d_val = 0
        r_val = ''
        
        for k, v in VALUES.items():
            if k <= num:
                d_val = k
                r_val = v
            else:
                break
                
        num -= d_val
        out += r_val
            
    return out

def r_to_d(raw):
    # TODO: check for invalid values (IIII, IIX, etc...)
    raw = raw.upper()
    
    vals = Stack()
    
    total = 0
    
    for c in raw:
        try:
            vals.push(NUMERALS[c])    
        except KeyError:
            return -1
            
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