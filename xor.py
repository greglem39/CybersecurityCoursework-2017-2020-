myFile = open("thelady.xml", "rb")

thisThing = myFile.read()

myFile.close()

thisThing = bytearray(thisThing)

#key = 0xAD1312

for i in range (0, len(thisThing), 3):
    thisThing[i] ^= 0xAD

for i in range (0, len(thisThing), 3):
    thisThing[i] ^= 0x13

for i in range (0, len(thisThing), 3):
    thisThing[i] ^= 0x12


myFile = open("decryptedLady.txt", "wb")

myFile.write(thisThing)

myFile.close()


#NEED TO BASE64 DECOODE THIS SHIT 
import base64
newFile = open("decryptedLady.txt", "r")

string = newFile.read()
#print string

string = base64.b64decode(string)
print string
