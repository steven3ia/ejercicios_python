from MapGrid import MapGrid

map = MapGrid()

map.create_grid()
map.get_walls()

while (map.player_x, map.player_y) != (map.end_x, map.end_y):
    # dibujar el mapa
    map.draw_grid()
    # recoger el movimiento del jugador
    movement = input("Which way? (r, l, u, d): ")
    # mover al jugador
    map.move_player(movement)
print("You made it to the end!")
