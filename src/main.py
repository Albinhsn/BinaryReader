from curses import wrapper

# Read in and display a binary file in hex
# Be able to define a format
# Able to parse based on that format


def main(stdscr):
    file = open("./wave.bin", "rb").read().strip()
    # Clear screen
    stdscr.clear()

    x = 0
    y = 0
    _, width = stdscr.getmaxyx()
    for i in file:
        f = f"0x{i:x} "

        stdscr.addstr(y, x, f)

        x += len(f)
        if x >= width:
            x = 0
            y += 1

    stdscr.refresh()
    stdscr.getkey()


wrapper(main)
