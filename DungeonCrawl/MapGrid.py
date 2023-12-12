import random

class MapGrid:

    def __init__(self, width=30, height=15):
        self.width = width
        self.height = height
        self.walls = []

    def create_grid(self):
        self.map = [[] for y in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                self.map[y].append(". ")

        # posicion inicial del jugador
        self.player_x = 0
        self.player_y = 0
        # posición inicial del jugador
        self.map[self.player_y][self.player_x] = '$ '

        # entrada en la esquina superior izquierda
        self.start_x, self.start_y = 0, 0
        # salida en la esquina inferior derecha
        self.end_x, self.end_y = self.width - 1, self.height - 1
        # representa la salida
        self.map[self.end_y][self.end_x] = "> "

    def draw_grid(self):
        for y in range(self.height):
            for x in range(self.width):
                print(self.map[y][x], end=" ")
            print()

    def get_walls(self, pct=0.15):
        num_walls = round(self.width * self.height * pct)
        # tupla de dos valores
        coordinates = list()
        # obtener todas las coordenadas posibles excepto entrada y salida
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) != (self.start_x, self.start_y) and (x, y) != (self.end_x, self.end_y):
                    coordinates.append((x, y))
        # shuffle mezcla aleatoriamente la tupla
        random.shuffle(coordinates)
        # coger las primeras num_walls(67) elementos
        chosen = coordinates[:num_walls]

        for x, y in chosen:
            self.map[y][x] = "# "
            
    
    def move_player(self, direction):
       
        # calcular la nueva posicion del jugador
        new_x, new_y = self.player_x, self.player_y
        if direction == 'r' and self.player_x < self.width - 1:
            # derecha
            new_x += 1
        elif direction == 'l' and self.player_x > 0:
            # izquierda
            new_x -= 1
        elif direction == 'u' and self.player_y > 0:
            # arriba
            new_y -= 1
        elif direction == 'd' and self.player_y < self.height - 1:
            # abajo
            new_y += 1

        # verificar si la nueva posición está dentro de la lista de muros
        if self.map[new_y][new_x] != "# ":
            # limpiar la posición actual del jugador
            self.map[self.player_y][self.player_x] = ". "
            # actualizar la posición del jugador en el mapa
            self.player_x, self.player_y = new_x, new_y
            # volver a actulizar el simbolo del jugador
            self.map[self.player_y][self.player_x] = "$ "
        else:
            # la nueva posición es un muro, el jugador no se mueve
            print("There is a wall!")
        

        """
        # verificar si el jugador ha alcanzado la salida
        if map.player_x == map.end_x and map.player_y == map.end_y:
            print("You made it to the end!")
        """