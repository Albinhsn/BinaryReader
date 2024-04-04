from curses import wrapper, newwin
from curses.textpad import Textbox, rectangle
from parser import Format

# Be able to define a format
#   Have count, or assumed to be entire file
#   Then just write a format with name:type
# Able to parse based on that format
# Switch displays between hex, the format, decimal etc
#   the format should be a table


def main(stdscr):
    file = open("./wave.bin", "rb").read().strip()
    stdscr.clear()

    height, width = stdscr.getmaxyx()
    is_hex = True
    editwin = newwin(height // 2, width // 2, 0, 0)
    box = Textbox(editwin)
    format: Format =Format() 
    while True:
        x = width // 2
        y = 0
        for i in file:
            f = f"0x{i:x} "


            x += 5
            if x >= width:
                x = width // 2
                y += 1
            if y < height:
                stdscr.addstr(y, x, f)

        is_hex = not is_hex
        stdscr.refresh()

        box.edit()
        format.parse(box.gather())

        key = stdscr.getkey()
        stdscr.erase()
        if key == 'q':
            break
        stdscr.refresh()


if __name__ == "__main__":
    wrapper(main)
