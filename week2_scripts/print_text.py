def print_text(text, i):
    print(text)

def do_twice(f, v):
    for _ in range(2):
        f(v, 0)
    
def do_four(f, v):
    for _ in range(4):
        f(v, 0)

def draw_grid(rows, cols):
    # Draw the horizontal line
    def draw_horizontal():
        print('+', end='')
        for _ in range(cols):
            print('-' * 4, end='+')
        print()  # Move to the next line

    # Draw the vertical lines
    def draw_vertical():
        for _ in range(2):  # Each cell height
            print('|', end='')
            for _ in range(cols):
                print(' ' * 4, end='|')
            print()  # Move to the next line

    # Draw the full grid
    for _ in range(rows):
        draw_horizontal()  # Draw horizontal line
        draw_vertical()    # Draw vertical lines
    draw_horizontal()  # Draw the bottom line
