from pyfirmata import Arduino, util
import os
from time import sleep

figma =' https://www.figma.com/files/recent?fuid=1073990296500635793'
notion = 'https://www.notion.so/Instagram-do-JPWF-49eb407b3d1d4e94ac56381869248711'
board = Arduino('/dev/ttyUSB1')
it = util.Iterator(board)
it.start()


figmaButton = board.get_pin('d:13:1')
notionButton = board.get_pin('d:12:1')

stateButton1 = True
stateButton2 = True
board.digital[10].write(0)

while True:
    stateButton1 = figmaButton.read()
    stateButton2 = notionButton.read()
    
    if stateButton1 == 1:
        board.digital[10].write(1)
        print("button 1 pressed")
        sleep(1)
        board.digital[10].write(0)
    elif stateButton2 == 1:
        board.digital[9].write(1)
        print("button 2 pressed")
        sleep(1)
        board.digital[9].write(0)
