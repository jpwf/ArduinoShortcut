from pyfirmata import Arduino, util
import os
from time import sleep

figma =' https://www.figma.com/files/recent?fuid=1073990296500635793'
notion = 'https://www.notion.so/Instagram-do-JPWF-49eb407b3d1d4e94ac56381869248711'
board = Arduino('COM9')
it = util.Iterator(board)
it.start()


figmaButton = board.get_pin('d:13:i')
notionButton = board.get_pin('d:12:i')

stateButton1 = True
stateButton2 = True


while True:
    Button1 = figmaButton.read()
    Button2 = notionButton.read()
    
    if Button1 == 0 and stateButton1:
        board.digital[10].write(1)
        os.system("start chrome {}".format(figma))
        sleep(1)
        board.digital[10].write(0)
    if Button2 == 0 and stateButton2:
        board.digital[9].write(1)
        os.system("start chrome {}".format(notion))
        sleep(1)
        board.digital[9].write(0)