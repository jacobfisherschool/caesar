#MMXIX
#Caesar cipher encrypter / decrypter / brute-force by Jacob Fisher

#Globals
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#Select operation
def mode():
      while True:
            #Prompt user to select an operation
            print()
            operation = str(input("Enter 'e' to encrypt, 'd' to decrypt, 'b' to brute force, 'h' for help or 'exit' to terminate the program: ")).lower()
            if operation == "d" or "e" or "b" or 'm' or 'h':
                  break
      return operation

#Encrypt string
def encrypt():
      #Locals
      plaintext = ""
      ciphertext = ""
      key = 0
      foreign = False

      #Input verification
      while True:
            plaintext = input("Please enter the unencrypted string: ").upper() #Remove '.upper()' if your alphabet utilises any lowercase characters
            if len(plaintext) > 0:
                  break
      while True:
            #Ask user for encryption key to encrypt the plaintext
            key = int(input("Please enter the key desired to encrypt the string: "))
            if key > 0 and key < len(alphabet):
                  break
      print()

      #Decrypt ciphertext
      for i in range(len(plaintext)):
            if plaintext[i] in alphabet:
                  #Handle wrap-around
                  if alphabet.find(plaintext[i]) + key >= len(alphabet):
                        ciphertext += str(alphabet[(alphabet.find(plaintext[i]) + key) - len(alphabet)])
                  else:
                        ciphertext += str(alphabet[alphabet.find(plaintext[i]) + key])
            else:
                  #Warn user that the string cannot be fully encrypted
                  ciphertext += str(plaintext[i])
                  if foreign == False:
                        print("Foreign letters included in ciphertext — string cannot be fully encrypted.")
                        foreign = True

      #Output plaintext
      return ciphertext

#Decrypt string
def decrypt():
      #Locals
      ciphertext = ""
      plaintext = ""
      key = 0
      foreign = False

      #Input verification
      while True:
            ciphertext = input("Please enter the encrypted string: ").upper() #Remove '.upper()' if your alphabet utilises any lowercase characters
            if len(ciphertext) > 0:
                  break
      while True:
            #Ask user for encryption key to decode the ciphertext
            key = int(input("Please enter the key used to encrypt the string: "))
            if key > 0 and key < len(alphabet):
                  break

      #Decrypt ciphertext
      for i in range(len(ciphertext)):
            if ciphertext[i] in alphabet:
                  #Handle wrap-around
                  if alphabet.find(ciphertext[i]) - key < 0:
                        plaintext += str(alphabet[(alphabet.find(ciphertext[i]) - key) + len(alphabet)])
                  else:
                        plaintext += str(alphabet[alphabet.find(ciphertext[i]) - key])
            else:
                  #Warn user that the string cannot be fully encrypted because of foreign characters
                  plaintext += str(ciphertext[i])
                  if foreign == False:
                        print("Foreign letters included in ciphertext — string cannot be fully decrypted.")
                        foreign = True

      #Output plaintext
      return plaintext

#Brute force ciphertext
def brute():
      #Locals
      ciphertext = ""
      plaintext = ""
      foreign = False

      #Input verification
      while True:
            ciphertext = input("Please enter the encrypted string: ").upper() #Remove '.upper()' if your alphabet utilises any lowercase characters
            if len(ciphertext) > 0:
                  break

      for key in range(0,len(alphabet)):
            plaintext = ""
            for i in range(len(ciphertext)):
                  if ciphertext[i] in alphabet:
                        #Handle wrap-around
                        if alphabet.find(ciphertext[i]) - key < 0:
                              plaintext += str(alphabet[(alphabet.find(ciphertext[i]) - key) + len(alphabet)])
                        else:
                              plaintext += str(alphabet[alphabet.find(ciphertext[i]) - key])
                  else:
                        #Ignore foreign characters
                        plaintext += str(ciphertext[i])
            print("Using key " + str(key) + ": " + plaintext)

def main():
      while True:
            print("Please ensure that the alphabet used to encrypt matches that of the one used to decrypt / brute-force. Alphabet in use is: " + alphabet)
            operation = mode()
            if operation == "d":
                  print("Decrypted string: '" + str(decrypt()) + "'")
            elif operation == "e":
                  print("Encrypted string: '" + str(encrypt()) + "'")
            elif operation == "b":
                  brute()
            elif operation == "h":
                  print("Made by Jacob Fisher, MMXIX")
                  print("")
                  print("Please email 16fisherj@nks.kent.sch.uk if any bugs are found.")
            elif operation == "exit":
                  print("Program terminated")
                  break
            else:
                  print("Incorrect input")
            print()
            print()

if __name__ == "__main__":
      main()
