class CesarAlgorithm:
    def __init__(self, key):
        self.key = key
    
    def encodeCesar(self, message):
        if (message.isupper() == False):
            message = message.upper()
        
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        cryptographicMessage = ""
    
        for letter in message:
            letterPosition = alphabet.find(letter);
            arrayPosition = (letterPosition + self.key) % 26
            cryptographicMessage = cryptographicMessage + alphabet[arrayPosition]

        return cryptographicMessage

if __name__ == '__main__':
    cesar = CesarAlgorithm(2)
    message = cesar.encodeCesar("Zebra")
    print (message)