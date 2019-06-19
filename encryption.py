import math, numpy
class encrption:

    def Encryption(self, message, myKey):

       # myMessage = "weneedmoresnownow"
        myMessage = message
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        #myKey = "securit"

        length = len(myMessage)
        rows = math.ceil(len(myMessage) / len(myKey))
        cols = len(myKey)
        pointer = 0
        pin = 0
        encryption_without_ordering = ''
        plain = ""
        cipher_text = [""] * len(myKey)
        matrix = [[''] * cols for i in range(rows)]
        for row in range(rows):
            for col in range(cols):
                if pointer < len(myMessage):
                    matrix[row][col] = myMessage[pointer]
                    pointer += 1
                else:
                    matrix[row][col] = letters[pin]
                    pin += 1
        print(matrix)

        for c in range(cols):
            for r in range(rows):
                encryption_without_ordering += matrix[r][c]
        print(encryption_without_ordering)
        for r in matrix:
            for c in r:
                plain += c
        print(plain)
        for column in range(len(myKey)):
            point = column
            while point < len(plain):
                cipher_text[column] += plain[point]
                print(cipher_text)
                point = point + len(myKey)

        key = list(myKey)
        key = numpy.array(key)
        cipher_text = numpy.array(cipher_text)
        index = key.argsort()
        cipher_text_array = cipher_text[index]
        cipher_text_list = list(cipher_text_array)
        print("".join(cipher_text_list))
       #print(length)
        return "".join(cipher_text_list)

