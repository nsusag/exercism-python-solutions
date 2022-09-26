def encode(numbers):
    output = []
    for number in numbers:
        # converts to binary
        mag = 1 
        while mag <= number // 2:
            mag *= 2
        print(mag)
        binarynum = []
        while mag > 0:
            if number >= mag:
                binarynum.append(1)
                number -= mag
            else:
                binarynum.append(0)
            print(number, mag, binarynum)
            mag = mag // 2
        
        # encodes
        while len(binarynum) % 7 != 0:
            binarynum.insert(0, 0)
        while len(binarynum) > 0:
            if len(binarynum) == 7:
                currentbyte = [0]
            else:
                currentbyte = [1]
            for i in range(0, 7):
                print(currentbyte)
                currentbyte.append(binarynum[i])
            del binarynum[0:7]
            
            # converts to decimal 
            base = 128
            number = 0
            for element in currentbyte:
                if element == 1:
                    number += base
                base = base // 2
            output.append(number)
    print(output)
    return output 

def decode(bytes_):
    output = []
    binarynum = []
    for byte in bytes_:
        mag = 128
        newbyte = byte
        while mag > 0: 
            if newbyte >= mag:
                if mag != 128:
                    binarynum.append(1)
                newbyte -= mag
            elif mag != 128:
                binarynum.append(0) 
            mag = mag // 2
        if byte < 128:
            num = 0
            mag = 2 ** (len(binarynum) - 1)
            for bit in binarynum:
                if bit == 1:
                    num += mag
                mag = mag // 2
            binarynum = []
            output.append(num)
    if output == []:
        raise ValueError("There is some issue with the input.")
    return output
        

decode([0x81, 0x80, 0x80, 0x0])
