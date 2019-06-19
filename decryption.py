import math,numpy

class decryption:

    def Decryption(self, text, key):
        #text = "newerodocenbwonmwdesa"
        #key = "securit"

        rows = math.ceil(len(text)/len(key))
        cols = len(key)
        pointer = 0
        decrypt=""
        new = [""]*cols
        pnt = 0
        abcd = ""
        for i in range(cols):
           for j in range(rows):
                new [i] += text[pnt]
                pnt += 1
        print (new)
        keylist = list(key)
        keylist = numpy.array(keylist)
        index = keylist.argsort()
        x =zip(list(index), new )
        z = [d for _, d in sorted(x)]
        print(z)
        cipher = "".join(z)
        matrix = [[""] * cols for i in range(rows) ]
        for column in range(cols):
            for row in range(rows):
                if pointer < len(cipher):
                    matrix[row][column] = cipher[pointer]
                    pointer += 1
                else:
                    break
        print(matrix)
        for r in range(rows):
            for c in range(cols):
                decrypt += matrix[r][c]
        print(decrypt)
        return decrypt
