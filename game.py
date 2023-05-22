from pynput.keyboard import Key, Listener, KeyCode

map = [
    [0, 0, 0],
    [0, 'x', 0],
    [0, 0, 0]
]

pos = [0, 0]

for row, row_item in enumerate(map):
    for col, col_item in enumerate(row_item):
        if col_item == 'x':
            pos[0] = row
            pos[1] = col


def on_press(key):
    if key == KeyCode.from_char('w'):
        print("Key w")
    elif KeyCode.from_char('s'):
        print("Key s")
    elif KeyCode.from_char('a'):
        print("Key a")
    elif KeyCode.from_char('d'):
        print("Key d")
    else :
        print("Others")

# with Listener(on_press=on_press) as Listener:
#     Listener.join()
