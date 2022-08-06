from os import rename, remove

inputFile = open("/home/mwirigi/Downloads/Whitney Houston - I Have Nothing (Official HD Video).mp4", 'rb')
outputFile = open("/home/mwirigi/Desktop/Whitney Houston - I Have Nothing (Official HD Video).mp4", 'wb')

msg = inputFile.read(10)

while len(msg):
    outputFile.write(msg)
    msg = inputFile.read(10)

inputFile.close()
outputFile.close()

#rename("/home/mwirigi/Desktop/Whitney Houston - I Have Nothing (Official HD Video).mp4","/home/mwirigi/Desktop/Whitney Houston - I Have Nothing.mp4")
#remove("/home/mwirigi/Desktop/Whitney Houston - I Have Nothing.mp4")

