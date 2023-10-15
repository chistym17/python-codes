import pyautogui

n = int(input("Enter rows "))

sx = 100
sy= 100
block_size = 10

for i in range(0,n):
    blocks = n - i
    start_row = sx - (blocks * block_size) // 2

    for j in range(blocks):
        x = start_row+ (j * block_size)
        y = sy- (i * block_size)
        pyautogui.moveTo(x,y)
        pyautogui.click()

pyautogui.pause = True
