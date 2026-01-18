from curses import wrapper
import curses
from conway_system import ConwaySystem

def controles(stdscr, system):
    command = stdscr.getch()

    if 64 < command < 91:
        command += 7

    match command:
        case 113:
            exit()
        case 43:            
            system.refresh_rate -= 10
        case 45:
            system.refresh_rate += 10
        case 32:
            stdscr.nodelay(1)
            mainloop(stdscr, system)
            stdscr.nodelay(0)
        case curses.KEY_MOUSE:
            mouse_handle(stdscr, system)


def mainloop(stdscr, system):
    while True:
        c = stdscr.getch()
        
        if c == 32:
            break

        system.run_iteration()
        system.update_screen(stdscr)
        curses.napms(system.refresh_rate)
        stdscr.refresh()


def mouse_handle(screen, system):
    try:
        _, x, y, _, bstate = curses.getmouse()

        if bstate & curses.BUTTON1_CLICKED:
            system.paint(screen, y, x)
            system.update_screen(screen)
    
    except curses.error:
        pass


def main(stdscr):
    stdscr.clear()
    curses.start_color()
    mouse_mask = curses.mousemask(curses.ALL_MOUSE_EVENTS)

    curses.curs_set(0)
    
    curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    #default refresh rate of 60ms = 60fps
    y, x = stdscr.getmaxyx()
    system = ConwaySystem(y, x)

    system.update_screen(stdscr)
    while True:
        controles(stdscr, system)


wrapper(main)
