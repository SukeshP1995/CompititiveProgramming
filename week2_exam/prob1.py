MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..'}
inputs = [
        ["gin", "zen", "gig", "msg"],
        ["a", "z", "g", "m"],
        ["bhi", "vsv", "sgh", "vbi"],
        ["a", "b", "c", "d"],
        ["hig", "sip", "pot"]  
        ]
     
for inp_list in inputs:
    print(inp_list)
    print(len(set([''.join(MORSE_CODE_DICT[c] for c in inp.upper()) for inp in inp_list])))
