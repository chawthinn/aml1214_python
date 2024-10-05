# Define draw_grid function that takes two arguments
def draw_grid(rows, cols):

    # Draw horizonal line
    def draw_horizontal():
        print('*', end='')
        for _ in range(cols):
            print('~' * 4, end='*')
        print()

    # Draw vertical line
    def draw_vertical():
        for _ in range(2):
            print('|', end='')
            for _ in range(cols):
                print(' ' * 4, end='|')
            print()
            
    # Draw the grid
    for _ in range(rows):
        draw_horizontal()
        draw_vertical()
    draw_horizontal()
