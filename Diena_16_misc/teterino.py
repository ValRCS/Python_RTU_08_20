# IMPORTANT: THIS IS THE MAIN FILE, MADE FOR EVALUATION!!! THE OTHER ONE IS JUST FOR FUN, A HUMBLE BEGINNING
#
# Teterino v2,
# by Agris V
# Last edited: 26-Jun-2022
# coded in Python 3.10
#
# INFO:
# If the game window is too big, reduce MULT in Configuration below
# Control keys can be changed in Configuration below
import tkinter
from math import floor
from time import sleep
from random import randint
from datetime import datetime as dt
from keyboard import is_pressed


# Configuration, some of these are somewhat tuned, changing them can have unexpected results and visual weirdness
FPS = 60  # frames per second
MULT = 1.5  # multiplier for display size
BLOCK = floor(20 * MULT)  # size of a single block
PANEL_WIDTH = 8  # width of the side panel, in blocks, MIN 6
PANEL_HEIGHT = 16  # height of the side panel, in blocks, MIN 15
DROP_X = 4  # figure drop start x coordinate, [1 .. WIDTH-4]
WIDTH = 10  # width of the playfield, in blocks, MIN 6
HEIGHT = 20  # height of the playfied, in blocks, MIN 10
WINDOW_LEFT = 50  # window distance from left screen side
WINDOW_TOP = 50  # window distance from screen top
WINDOW_WIDTH = (WIDTH + PANEL_WIDTH + 3) * BLOCK
WINDOW_HEIGHT = max((HEIGHT + 2) * BLOCK, (PANEL_HEIGHT + 2) * BLOCK)
SLEEP_TIME = 1 / FPS
SP = floor(1 * MULT)  # for spacing between playfield blocks
KEYDELAY = 15  # key action delay after the first hit
KEYSPEED = 5  # key action delay after concurrent hits
DROP_BASE = 0.5  # base figure drop speed, blocks per second
DROP_LEVEL = 0.25  # figure drop speed increase per level
TRANSITION = 0.5  # seconds of transition when deleting lines
LINES_PER_LEVEL = 10  # lines to clear for level up
POINTS_PER_BLOCK = 10  # base points per single block

# control keys for the game
CONTROLS = {
    'left': 'a',  # move left / decrease start level on start or when game over
    'right': 'd',  # move right / increase start level on start or when game over
    'rotate': 's',  # rotate, just rotate the figure
    'drop': 'w',  # temporary speed up figure descent
    'pause': 'p',  # start game / pause / unpause
    'quit': 'y'  # quit on title / when game over / while paused
}

# prepare figures
# THEORETICALLY funky ones can be added here :)
# each line here is X lists of X elements representing X times X matrix of a single figure
ALL_FIGURES = [
    [[0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0]],  # long piece
    [[0, 1, 0], [1, 1, 1], [0, 0, 0]],  # T piece
    [[1, 0, 0], [1, 1, 1], [0, 0, 0]],  # reverse L piece
    [[0, 0, 1], [1, 1, 1], [0, 0, 0]],  # L piece
    [[0, 1, 1], [1, 1, 0], [0, 0, 0]],  # Z piece
    [[1, 1, 0], [0, 1, 1], [0, 0, 0]],  # reverse Z piece
    [[1, 1], [1, 1]],  # square
    # [[0, 1, 0], [0, 1, 0], [0, 1, 0]],  # straight 3-piece
    # [[1, 0], [1, 1]],  # corner 3-piece
    # [[1, 0], [1, 0]],  # straight 2-piece
    # [[1]]  # a single block
]

# colors
# fig - colors for figures, should have as many as there are figures or will have random colors there
# block - deposited block color, changes on level change
COLOR = {
    'title': 'Purple',
    'panel': 'Gray',
    'label': 'Black',
    'level': 'Purple',
    'points': 'Green',
    'lines': 'Blue',
    'special': 'Red',  # overlay message
    'none-i': 'Black',  # for empty blocks
    'none-o': 'Black',
    'del-i': '#00cc00',  # for blocks being deleted
    'del-o': '#009900',
    'fig-i': ['#7f0000', '#7f3f3f', '#7f7f00', '#7f007f', '#007f7f', '#007f00', '#00007f'],
    'fig-o': ['#bf0000', '#bf5f5f', '#bfbf00', '#bf00bf', '#00bfbf', '#00bf00', '#0000bf'],
    'block-i': ['#5f0000', '#005f00', '#00005f', '#3f3f00', '#3f003f', '#003f3f'],
    'block-o': ['#9f0000', '#009700', '#00009f', '#7f7f00', '#7f007f', '#007f7f'],
    'border': ['#7f7f7f', '#efefef', '#3f3f3f', '#1f1f1f', '#cfcfcf']
}

# TODO perhaps make Figure class and move figure functions there ...


# returns random new figure form the figure list and corresponding or random color index
def figure_get_new():
    index = randint(0, len(ALL_FIGURES) - 1)
    if index > min(len(COLOR['fig-i']), len(COLOR['fig-o'])):
        color = randint(0, min(len(COLOR['fig-i']), len(COLOR['fig-o']))-1)
    else:
        color = index
    return ALL_FIGURES[index], color


# returns figure rotated anti-clockwise
def figure_rotate(figure):
    rotated = [list(each) for each in zip(*figure)]
    return rotated[::-1]


# returns collision data
def is_collision(figure, frame, posx, posy):
    for figy in range(len(figure)):
        for figx in range(len(figure)):
            if figure[figy][figx] == 0:
                continue
            x = posx + figx
            y = posy + figy
            # use clock notation for wall collisions
            if y < 0:
                return True, 12  # collide with top
            elif y >= HEIGHT:
                return True, 6   # collide with bottom
            elif x < 0:
                return True, 9   # collide with left wall
            elif x >= WIDTH:
                return True, 3   # collide with right wall
            elif frame[y][x] == 1:
                return True, 99  # collide with existing block
    return False, 0


# adds figure blocks to the frame blocks
def figure_settle(figure, frame, posx, posy):
    for y in range(len(figure)):
        for x in range(len(figure)):
            if figure[y][x] == 1:
                frame[posy+y][posx+x] = 1


# key parsing returns True when key is first pressed, and every few frames after some small delay if key is held
# actions ingame happen only when the parse returns True
def key_parse(key, hold=0, delay=KEYDELAY, speed=KEYSPEED):
    if is_pressed(key):
        hold += 1
        if hold == 1 or (hold >= delay and ((hold-delay)/speed).is_integer()):
            return True, hold
        else:
            return False, hold
    else:
        return False, 0


# function to draw a single border box
# TODO maybe border could be made prettier
def draw_border(canvas, x1, y1, x2, y2):
    t = (x2 - x1) / 5
    canvas.create_polygon(x1, y1, x2, y1, x2-t, y1+t, x1+t, y1+t, fill=COLOR['border'][1], width=0)
    canvas.create_polygon(x2, y1, x2, y2, x2-t, y2-t, x2-t, y1+t, fill=COLOR['border'][2], width=0)
    canvas.create_polygon(x2, y2, x1, y2, x1+t, y2-t, x2-t, y2-t, fill=COLOR['border'][3], width=0)
    canvas.create_polygon(x1, y2, x1, y1, x1+t, y1+t, x1+t, y2-t, fill=COLOR['border'][4], width=0)
    canvas.create_rectangle(x1+t, y1+t, x2-t, y2-t, fill=COLOR['border'][0], width=0)


# makes a single inactive block
# all blocks are present in the game all the time, inactive ones just need to be the same color as background
def make_block(canvas, x1, y1, x2, y2, fill=COLOR['none-i'], line=COLOR['none-o']):
    block = canvas.create_rectangle(x1, y1, x2, y2, fill=fill, outline=line, width=floor(MULT), tags='block')
    return block


# places label on the panel
def place_text(canvas, text, x, y, col='Black', font='Helvetica', size=str(floor(15*MULT)), style='bold',
               anchor='nw', align='center'):
    label = canvas.create_text(x, y, fill=col, font=(font, size, style), text=text, anchor=anchor, justify=align)
    return label


def main_loop(window, canvas):
    # if player closes the window, end game without throwing an error
    def end_game():
        nonlocal game_state
        game_state = 'quit'
    window.protocol("WM_DELETE_WINDOW", end_game)

    # draw border, just once, this is here to stay and not change, like, forever
    # first there are the top and bottom horizontal borders and corners
    t = max(HEIGHT + 2, PANEL_HEIGHT + 2)
    for i in range(WIDTH + PANEL_WIDTH + 3):
        draw_border(canvas, i*BLOCK, 0, (i+1)*BLOCK, BLOCK)
        draw_border(canvas, i*BLOCK, (t-1)*BLOCK, (i+1)*BLOCK, t*BLOCK)
    # now there's left and right vertical border and the line between playfield and stats panel
    t = WIDTH + 1
    t1 = WIDTH + PANEL_WIDTH + 2
    for i in range(max(HEIGHT, PANEL_HEIGHT)):
        draw_border(canvas, 0, (i+1)*BLOCK, BLOCK, (i+2)*BLOCK)
        draw_border(canvas, t*BLOCK, (i+1)*BLOCK, (t+1)*BLOCK, (i+2)*BLOCK)
        draw_border(canvas, t1*BLOCK, (i+1)*BLOCK, (t1+1)*BLOCK, (i+2)*BLOCK)
    # lastly, there's fill below playfield if it is made shorter than stats panel
    if PANEL_HEIGHT - HEIGHT > 0:
        for y in range(PANEL_HEIGHT - HEIGHT):
            for x in range(WIDTH):
                draw_border(canvas, (x+1)*BLOCK, (y+HEIGHT+1)*BLOCK, (x+2)*BLOCK, (y+HEIGHT+2)*BLOCK)

    # draw panel background and labels
    panel = canvas.create_rectangle((WIDTH+2)*BLOCK, BLOCK, (WIDTH+PANEL_WIDTH+2)*BLOCK,
                                    (max(HEIGHT, PANEL_HEIGHT)+1)*BLOCK, fill=COLOR['panel'], tags='panel', width=2)
    place_text(canvas, 'TETERINO', (WIDTH+(PANEL_WIDTH/2)+2)*BLOCK, 2.5*BLOCK, col=COLOR['title'],
               anchor='center', size=str(floor(MULT*22)))
    place_text(canvas, 'NEXT', (WIDTH+3)*BLOCK, 4*BLOCK, col=COLOR['label'])
    place_text(canvas, 'LEVEL', (WIDTH+3)*BLOCK, 10*BLOCK, col=COLOR['label'])
    place_text(canvas, 'POINTS', (WIDTH+3)*BLOCK, 12*BLOCK, col=COLOR['label'])
    place_text(canvas, 'LINES', (WIDTH+3)*BLOCK, 14*BLOCK, col=COLOR['label'])
    label_level = place_text(canvas, '1', (WIDTH+PANEL_WIDTH+1)*BLOCK, 11*BLOCK, col=COLOR['level'], anchor='ne')
    label_points = place_text(canvas, '0', (WIDTH+PANEL_WIDTH+1)*BLOCK, 13*BLOCK, col=COLOR['points'], anchor='ne')
    label_lines = place_text(canvas, '0', (WIDTH+PANEL_WIDTH+1)*BLOCK, 15*BLOCK, col=COLOR['lines'], anchor='ne')
    txt = f'Press {CONTROLS["pause"].upper()} to start\n{CONTROLS["quit"].upper()} to quit'
    label_main = place_text(canvas, txt, WINDOW_WIDTH/2, WINDOW_HEIGHT/2,
                            col=COLOR['special'], anchor='center')

    # prepare play frame and next figure frame
    frame = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
    draw_frame = [[make_block(canvas, (x+1)*BLOCK+SP, (y+1)*BLOCK+SP, (x+2)*BLOCK-SP, (y+2)*BLOCK-SP)
                   for x in range(WIDTH)] for y in range(HEIGHT)]
    draw_next = [[make_block(canvas, (x+3+WIDTH)*BLOCK+SP, (y+5)*BLOCK+SP, (x+4+WIDTH)*BLOCK-SP, (y+6)*BLOCK-SP,
                             fill=COLOR['panel'], line=COLOR['panel']) for x in range(5)] for y in range(5)]
    for y in range(HEIGHT):
        for x in range(WIDTH):
            canvas.tag_lower(draw_frame[y][x])
    for y in range(5):
        for x in range(5):
            canvas.tag_lower(draw_next[y][x])
    canvas.tag_lower(panel)

    # initialize controls
    con = {'left': False, 'right': False, 'rotate': False, 'drop': False, 'pause': False, 'quit': False,
           'left-t': 0, 'right-t': 0, 'rotate-t': 0, 'drop-t': 0, 'pause-t': 0, 'quit-t': 0}

    # variables
    game_state = 'title'
    game_progress, game_level, game_points, game_lines, game_speed = 0, 1, 0, 0, 0
    f_reconfigure, can_drop, level_changed = False, True, False
    bc, fc, fcn = 0, 0, 0  # color indexes for blocks and figures
    figure, next_figure = [], []  # useless line, pleases pyCharm
    posx, posy, kill_lines, level_lines, add_points, add_level = DROP_X, 0, 0, 0, 0, 0  # useless line, pleases pyCharm
    timer_prev = dt.now().microsecond

    while True:
        # detect if control keys are pressed or being held
        # already includes checks for key hold delays
        con['left'], con['left-t'] = key_parse(CONTROLS['left'], con['left-t'])
        con['right'], con['right-t'] = key_parse(CONTROLS['right'], con['right-t'])
        con['rotate'], con['rotate-t'] = key_parse(CONTROLS['rotate'], con['rotate-t'])
        con['drop'], con['drop-t'] = key_parse(CONTROLS['drop'], con['drop-t'], 10000)
        con['pause'], con['pause-t'] = key_parse(CONTROLS['pause'], con['pause-t'], 10000)
        con['quit'], con['quit-t'] = key_parse(CONTROLS['quit'], con['quit-t'], 10000)

        # manage game state logic, overlay message and key actions out of main play
        if game_state == 'quit':  # quit the game
            window.destroy()
            break
        if game_state == 'over':  # game over screen, can change levels, start and quit the game
            if con['pause']:
                game_state = 'start'
                con['pause'] = False
                canvas.itemconfig(label_main, text='')
                if not level_changed:
                    game_level = 1
            elif con['quit']:
                game_state = 'quit'
            elif con['left']:
                game_level -= 1 if game_level > 1 else 0
                level_changed = True
            elif con['right']:
                game_level += 1 if game_level < 60 else 0
                level_changed = True
            canvas.itemconfig(label_level, text=str(game_level))
        if game_state == 'pause':  # when game is paused, can resume or quit the game
            if con['pause']:
                game_state = 'run'
                canvas.itemconfig(label_main, text='')
                con['pause'] = False
            elif con['quit']:
                game_state = 'quit'
        if game_state == 'run' and con['pause']:  # when game is running, can pause, main actions are not here
            game_state = 'pause'
            canvas.itemconfig(label_main, text='P A U S E')
            con['pause'] = False
        if game_state == 'title':  # on start screen, can start, quit or change levels
            if con['pause']:
                game_state = 'start'
                canvas.itemconfig(label_main, text='')
                con['pause'] = False
            elif con['quit']:
                game_state = 'quit'
            elif con['left']:
                game_level -= 1 if game_level > 1 else 0
            elif con['right']:
                game_level += 1 if game_level < 60 else 0
            canvas.itemconfig(label_level, text=str(game_level))
        if game_state == 'start':  # when new game starts
            frame = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
            next_figure, fcn = figure_get_new()
            figure, fc = figure_get_new()
            posx, posy = DROP_X, 0
            game_progress = 0
            kill_lines = 0
            game_lines = 0
            level_lines = LINES_PER_LEVEL
            game_points = 0
            add_points = 0
            can_drop = True
            game_speed = 1 / (DROP_LEVEL * game_level + DROP_BASE)
            bc = randint(0, min(len(COLOR['block-i']), len(COLOR['block-o']))-1)
            game_state = 'run'
            f_reconfigure = True

        # manage left and right movement
        if game_state == 'run' and (con['left'] or con['right']) and not(con['left-t'] and con['right-t']):
            if con['left']:
                move = -1
            else:
                move = 1
            collide, collide_id = is_collision(figure, frame, posx+move, posy)
            if not collide:
                posx += move
                f_reconfigure = True

        # manage rotation, with a 'fix' of max 2 blocks, if rotation would collide with a wall, aka bounce off wall
        if game_state == 'run' and con['rotate']:
            fix = 0
            while fix < 3:
                collide, collide_id = is_collision(figure_rotate(figure), frame, posx+fix, posy)
                if collide:
                    if collide_id == 3:
                        fix -= 1
                    elif collide_id == 9:
                        fix += 1
                    else:
                        break
                else:
                    figure = figure_rotate(figure)
                    posx += fix
                    f_reconfigure = True
                    break

        # manage fast drop, temporary speeding up dhe figure drop
        if can_drop:
            if con['drop-t'] > 0:
                game_speed = 1 / (DROP_LEVEL * 40 + DROP_BASE)
            else:
                game_speed = 1 / (DROP_LEVEL * game_level + DROP_BASE)
        else:
            if con['drop-t'] == 0:
                can_drop = True

        # manage figure automatic descent
        if game_state == 'run' and game_progress >= game_speed:
            game_progress -= game_speed
            collide, collide_id = is_collision(figure, frame, posx, posy+1)
            if not collide:  # cand drop
                posy += 1
            elif collide_id == 6 or collide_id == 99:  # can't drop, freeze
                figure_settle(figure, frame, posx, posy)
                can_drop = False
                game_speed = 1 / (DROP_LEVEL * game_level + DROP_BASE)
                game_state = 'trans'
                game_progress = 0
            f_reconfigure = True

        # manage figure transition, line destruction, stats update
        if game_state == 'trans':
            if kill_lines == 0:  # fires first and once, whenever transition is entered
                # check if full lines have formed and mark them for deletion
                for y, line in enumerate(frame):
                    if sum(line) == WIDTH:
                        kill_lines += 1
                        for x in range(WIDTH):
                            frame[y][x] = 2
                # no full lines thus just make a new figure and play, if it is not blocked, otherwise end the game
                if kill_lines == 0:
                    figure, fc, posx, posy = next_figure, fcn, DROP_X, 0
                    if is_collision(figure, frame, posx, posy)[0]:
                        game_state = 'over'
                        canvas.itemconfig(label_main, text='G A M E   O V E R')
                        level_changed = False
                    else:
                        game_state = 'run'
                    next_figure, fcn = figure_get_new()
                    game_progress = 0
                else:  # there are full lines so start the small transition pause and do stats
                    add_points = kill_lines**2 * WIDTH * POINTS_PER_BLOCK
                    if game_lines + kill_lines >= level_lines:
                        add_level = 1
                        level_lines += LINES_PER_LEVEL
                        bc = bc + 1 if bc < min(len(COLOR['block-i']), len(COLOR['block-o'])) - 1 else 0
                    else:
                        add_level = 0
                f_reconfigure = True
            else:  # fires after the first check while waiting for line deletion, then deletes and resumes
                if game_progress > TRANSITION:
                    for y, line in enumerate(frame):
                        if sum(line) > WIDTH:
                            frame = frame[:y] + frame[y+1:]
                            frame.insert(0, [0 for _ in range(WIDTH)])
                    figure, fc, posx, posy = next_figure, fcn, DROP_X, 0
                    next_figure, fcn = figure_get_new()
                    game_progress = 0
                    game_state = 'run'
                    game_points += add_points
                    game_lines += kill_lines
                    game_level += add_level
                    add_points = 0
                    game_speed = 1 / (DROP_LEVEL * game_level + DROP_BASE)
                    kill_lines = 0
                    f_reconfigure = True

        # reconfigure visual state of blocks and labels
        if f_reconfigure:
            # the main playfield
            for y in range(HEIGHT):
                for x in range(WIDTH):
                    if frame[y][x] == 0:  # inactive blocks -> background color
                        canvas.itemconfig(draw_frame[y][x], fill=COLOR['none-i'], outline=COLOR['none-o'])
                    elif frame[y][x] == 2:  # blocks about to be deleted
                        canvas.itemconfig(draw_frame[y][x], fill=COLOR['del-i'], outline=COLOR['del-o'])
                    elif frame[y][x] == 1:  # normal blocks
                        canvas.itemconfig(draw_frame[y][x], fill=COLOR['block-i'][bc], outline=COLOR['block-o'][bc])
            # the current figure on the playfield
            if not game_state == 'trans':
                for y, line in enumerate(figure):
                    for x, cell in enumerate(line):
                        if cell == 1:
                            canvas.itemconfig(draw_frame[posy+y][posx+x], fill=COLOR['fig-i'][fc],
                                              outline=COLOR['fig-o'][fc])
            # the prewiev of the next figure
            if game_state == 'run' or 'pause' or 'trans':
                tl = len(next_figure)
                ty = 0 if tl > 3 else 1
                for y in range(5):
                    for x in range(5):
                        tc = next_figure[y-ty][x] if 0 <= y-ty < tl and 0 <= x < tl else 0
                        if tc == 1:
                            canvas.itemconfig(draw_next[y][x], fill=COLOR['fig-i'][fcn], outline=COLOR['fig-o'][fcn])
                        else:
                            canvas.itemconfig(draw_next[y][x], fill=COLOR['panel'], outline=COLOR['panel'])
            # the stats labels
            if add_points > 0:
                canvas.itemconfig(label_points, text=f'+{add_points}   {game_points}')
                if add_level > 0:
                    canvas.itemconfig(label_level, text=f'+{add_level}   {game_level}')
                canvas.itemconfig(label_lines, text=f'+{kill_lines}   {game_lines}')
            else:
                canvas.itemconfig(label_level, text=str(game_level))
                canvas.itemconfig(label_points, text=str(game_points))
                canvas.itemconfig(label_lines, text=str(game_lines))
            f_reconfigure = False

        # fps related
        window.update()
        sleep(0.00001)  # artificial slowdown or the game just might run too fast
        timer = dt.now().microsecond
        if timer > timer_prev:
            timer_delta = timer - timer_prev
        else:
            timer_delta = 1_000_000 + timer - timer_prev
        timer_prev = timer
        timer_delta /= 1_000_000
        if game_state == 'run' or game_state == 'trans':
            game_progress += timer_delta
        if timer_delta < SLEEP_TIME:
            sleep(SLEEP_TIME - timer_delta)


main_window = tkinter.Tk()
main_window.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{WINDOW_LEFT}+{WINDOW_TOP}')
main_window.resizable(False, False)
main_window.title('Teterino')
main_canvas = tkinter.Canvas(main_window)
main_canvas.configure(background=COLOR['none-i'])
main_canvas.pack(fill='both', expand=True)

main_loop(main_window, main_canvas)
