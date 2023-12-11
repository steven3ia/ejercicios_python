import random

class MapGrid:

    def __init__(self, width=30, height=15):
        self.width = width
        self.height = height
        self.walls = []
        self.map = [[]]

    def draw_grid(self):
        self.map = [['. ' for x in range(self.width)] for y in range(self.height)]
    """
    def draw_grid(self):
        self.map = [[0 for x in range(self.width)] for y in range(self.height)]
        for x in range(self.height):
            for y in range(self.width):       
                map[x][y] = ". "           
        #print(map)
    """
    def get_walls(self, pct=0.15):
        num_walls = round(self.width * self.height * pct)

        chosen = list()

        for i in range(num_walls):
            y = random.randint(0, self.height - 1)
            x = random.randint(0, self.width - 1)

            

            chosen.append((x, y))
            
            self.map[y][x] = "# "
            
        print(self.map)

