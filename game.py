import time
import random

class Game:
    def start():
        time.sleep(0.5)
        print('\n\nДобро пожаловать в игру!\n\n\n')
        time.sleep(1)
        
class Coin:
    def flip_coin():
        return random.randint(0, 1)

class Converter:
    coord_field = {'a1': 1, 'a2': 2, 'a3': 3, 'a4': 4, 'a5': 5, 'a6': 6, 'b1': 7, 'b2': 8, 'b3': 9, 'b4': 10, 'b5': 11, 'b6': 12, 'c1': 13, 'c2': 14, 'c3': 15, 'c4': 16, 'c5': 17, 'c6': 18, 'd1': 19, 'd2': 20, 'd3': 21, 'd4': 22, 'd5': 23, 'd6': 24, 'e1': 25, 'e2': 26, 'e3': 27, 'e4': 28, 'e5': 29, 'e6': 30, 'f1': 31, 'f2': 32, 'f3': 33, 'f4': 34, 'f5': 35, 'f6': 36}
    def convert(bi_coordinates):
        coord_field = {'a1': 1, 'a2': 2, 'a3': 3, 'a4': 4, 'a5': 5, 'a6': 6, 'b1': 7, 'b2': 8, 'b3': 9, 'b4': 10, 'b5': 11, 'b6': 12, 'c1': 13, 'c2': 14, 'c3': 15, 'c4': 16, 'c5': 17, 'c6': 18, 'd1': 19, 'd2': 20, 'd3': 21, 'd4': 22, 'd5': 23, 'd6': 24, 'e1': 25, 'e2': 26, 'e3': 27, 'e4': 28, 'e5': 29, 'e6': 30, 'f1': 31, 'f2': 32, 'f3': 33, 'f4': 34, 'f5': 35, 'f6': 36}
        try:
            return coord_field[bi_coordinates]
        except:
            pass
            
class Ship:
    def __init__(self):
        self.ship_1 = 3
        self.ship_2 = 2
        self.ship_3 = 2
        self.ship_4 = 1
        self.ship_5 = 1
        self.ship_6 = 1
        self.ship_7 = 1
class Grid:
    def __init__(self, name):
        self.name = name
        self.private_grid = {1: '_', 2: '_', 3: '_', 4: '_', 5: '_', 6: '_', 7: '_', 8: '_', 9: '_', 10: '_', 11: '_', 12: '_', 13: '_', 14: '_', 15: '_', 16: '_', 17: '_', 18: '_', 19: '_', 20: '_', 21: '_', 22: '_', 23: '_', 24: '_', 25: '_', 26: '_', 27: '_', 28: '_', 29: '_', 30: '_', 31: ' ', 32: ' ', 33: ' ', 34: ' ', 35: ' ', 36: ' ', 37: 'A', 38: 'B', 39: 'C', 40: 'D', 41: 'E', 42: 'F',43: '1', 44: '2', 45: '3', 46: '4', 47: '5', 48: '6'}
        self.public_grid = {1: '_', 2: '_', 3: '_', 4: '_', 5: '_', 6: '_', 7: '_', 8: '_', 9: '_', 10: '_', 11: '_', 12: '_', 13: '_', 14: '_', 15: '_', 16: '_', 17: '_', 18: '_', 19: '_', 20: '_', 21: '_', 22: '_', 23: '_', 24: '_', 25: '_', 26: '_', 27: '_', 28: '_', 29: '_', 30: '_', 31: ' ', 32: ' ', 33: ' ', 34: ' ', 35: ' ', 36: ' ', 37: 'A', 38: 'B', 39: 'C', 40: 'D', 41: 'E', 42: 'F',43: '1', 44: '2', 45: '3', 46: '4', 47: '5', 48: '6'}
        self.hit_grid = {1: '_', 2: '_', 3: '_', 4: '_', 5: '_', 6: '_', 7: '_', 8: '_', 9: '_', 10: '_', 11: '_', 12: '_', 13: '_', 14: '_', 15: '_', 16: '_', 17: '_', 18: '_', 19: '_', 20: '_', 21: '_', 22: '_', 23: '_', 24: '_', 25: '_', 26: '_', 27: '_', 28: '_', 29: '_', 30: '_', 31: ' ', 32: ' ', 33: ' ', 34: ' ', 35: ' ', 36: ' ', 37: 'A', 38: 'B', 39: 'C', 40: 'D', 41: 'E', 42: 'F',43: '1', 44: '2', 45: '3', 46: '4', 47: '5', 48: '6'}
        self.zanyato = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
        self.ship_checksum = []
        self.hit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
    
    
    
    def hit_target(self, target, coin):
        def universal_checker(coin):
            ctr = 0
            for i in range(1, 37):
                if self.public_grid[i] == 'X':
                    ctr += 1
            if ctr == 11:
                time.sleep(0.5)
                print('GAME OVER')
                time.sleep(0.5)
                if coin == 0:
                    time.sleep(0.2)
                    print('Вы победили!')
                    time.sleep(0.2)
                else:
                    time.sleep(0.2)
                    print('Победила машина!')
                    time.sleep(0.2)
                exit()

        def switch(coin):
            if coin == 0:
                return 1
            else:
                return 0
        if coin != 0:
            time.sleep(0.2)
            print('Компьютер ходит...')
            time.sleep(2)
        if self.private_grid[target] != '■':
            time.sleep(0.2)
            if coin == 0:
                print('\n\nМимо!\n\n')
            elif coin != 0:
                print('\n\nКомпьютер промазал!\n\n')
            time.sleep(2)
            self.public_grid[target] = '◦'
            try:
                self.hit.remove(target)
                return switch(coin)
            except:
                time.sleep(0.2)
                print('Вы уже ходили сюда... Противник получает фору!\n\n')
                time.sleep(2)
                pass
            
        else:
            time.sleep(0.2)
            print('\n\nПопадание!\n\n')
            time.sleep(2)
            self.public_grid[target] = 'X'
            if target in self.ship_checksum:
                clasterize(target)
                draw_borders(self.public_grid[target])
            universal_checker(coin)
            try:
                self.hit.remove(target)
                return coin
            except:
                time.sleep(0.2)
                print('\n\nВы спасовали... Ходит противник!\n\n')
                time.sleep(2)
                pass
    
    def place_the_ships(self, ship):
        self.claster_min = 1
        self.claster_max = 37
        def clasterize(current_spot):
            if current_spot < 7:
                self.claster_min = 1
                self.claster_max = 6
            elif current_spot < 13:
                self.claster_min = 7
                self.claster_max = 12
            elif current_spot < 19:
                self.claster_min = 13
                self.claster_max = 18
            elif current_spot < 25:
                self.claster_min = 19
                self.claster_max = 24
            elif current_spot < 31:
                self.claster_min = 25
                self.claster_max = 30
            else:
                self.claster_min = 31
                self.claster_max = 36
            
        def draw_borders():
            self.to_delete = []
            for i in range(1, 37):
                if self.private_grid[i] == '■':
                    clasterize(i)
                    if i+1 <= self.claster_max:
                        self.to_delete.append(i+1)
                        if i-6 > 0:
                            self.to_delete.append(i-5)
                    if i-1 >= self.claster_min:
                        self.to_delete.append(i-1)
                        if i-6 > 0:
                            self.to_delete.append(i-7)
                    if i-6 > 0:
                        self.to_delete.append(i-6)
                    if i+6 < 37:
                        self.to_delete.append(i+6)
                        if i+1 <= self.claster_max:
                            self.to_delete.append(i+7)
                        if i-1 >= self.claster_min:
                            self.to_delete.append(i+5)
            
            for a in(self.to_delete):
                if a not in self.zanyato:
                    pass
                else:
                    self.zanyato.remove(a)

        def draw_ship(direction, spot):
            #print(direction, spot)
            self.private_grid[spot] = '■'

            self.zanyato.remove(spot)
            if direction == 'right_2':
                self.private_grid[spot+1] = '■'
                self.private_grid[spot+2] = '■'
                self.ship_checksum.append([spot, spot+1, spot+2])
                self.zanyato.remove(spot+1)
                self.zanyato.remove(spot+2)
            elif direction == 'mid':
                self.private_grid[spot+1] = '■'
                self.private_grid[spot-1] = '■'
                self.ship_checksum.append([spot, spot+1, spot-1])
                self.zanyato.remove(spot+1)
                self.zanyato.remove(spot-1)
            elif direction == 'left_2':
                self.private_grid[spot-1] = '■'
                self.private_grid[spot-2] = '■'
                self.ship_checksum.append([spot, spot-1, spot-2])
                self.zanyato.remove(spot-1)
                self.zanyato.remove(spot-2)
            elif direction == 'down_2':
                self.private_grid[spot+12] = '■'
                self.private_grid[spot+6] = '■'
                self.ship_checksum.append([spot, spot+12, spot+6])
                self.zanyato.remove(spot+12)
                self.zanyato.remove(spot+6)
            elif direction == 'up_2':
                self.private_grid[spot-12] = '■'
                self.private_grid[spot-6] = '■'
                self.ship_checksum.append([spot, spot-12, spot+6])
                self.zanyato.remove(spot-12)
                self.zanyato.remove(spot-6)
            elif direction == 'mid_vert':
                self.private_grid[spot-6] = '■'
                self.private_grid[spot+6] = '■'
                self.ship_checksum.append([spot, spot-6, spot+6])
                self.zanyato.remove(spot-6)
                self.zanyato.remove(spot+6)
            elif direction == 'right':
                self.private_grid[spot+1] = '■'
                self.ship_checksum.append([spot, spot+1])
                self.zanyato.remove(spot+1)
            elif direction == 'left':
                self.private_grid[spot-1] = '■'
                self.ship_checksum.append([spot, spot-1])
                self.zanyato.remove(spot-1)
            elif direction == 'up':
                self.private_grid[spot-6] = '■'
                self.ship_checksum.append([spot, spot-6])
                self.zanyato.remove(spot-6)
            elif direction == 'down':
                self.private_grid[spot+6] = '■'
                self.ship_checksum.append([spot, spot+6])
                self.zanyato.remove(spot+6)
            elif direction == 'single_spot':
                self.ship_checksum.append([spot])
                pass
    
        possible_spot = random.choice(self.zanyato)
        clasterize(possible_spot)
        #print(possible_spot)

        possible_directions = []
        if ship > 2:
            if possible_spot+2 in self.zanyato  and possible_spot+2 <= self.claster_max:
                possible_directions.append('right_2')
            if possible_spot-1 in self.zanyato and possible_spot-1 >= self.claster_min:
                if possible_spot+1 in self.zanyato and possible_spot+1 <= self.claster_max:
                    possible_directions.append('mid')
            if possible_spot-2 in self.zanyato and possible_spot-2 >= self.claster_min:
                possible_directions.append('left_2')
            if possible_spot+12 in self.zanyato  and possible_spot+12 <= 37:
                possible_directions.append('down_2')
            if possible_spot-12 in self.zanyato  and possible_spot-12 >= 0:
                possible_directions.append('up_2')
            if possible_spot-6 in self.zanyato and possible_spot-6 >= 0:
                if possible_spot+6 in self.zanyato and possible_spot+6 <= 37:
                    possible_directions.append('mid_vert')
        
        elif ship == 2:
            if possible_spot+1 in self.zanyato  and possible_spot+1 <= self.claster_max:
                possible_directions.append('right')
            if possible_spot-1 in self.zanyato and possible_spot-1 >= self.claster_min:
                possible_directions.append('left')
            if possible_spot-6 in self.zanyato  and possible_spot-6 >= 0:
                possible_directions.append('up')
            if possible_spot+6 in self.zanyato  and possible_spot+6 <= 36:
                possible_directions.append('down')
                
        if ship == 1:
            possible_directions.append('single_spot')
        

        draw_ship(random.choice(possible_directions), possible_spot)
        draw_borders()

    def draw_private_grid(self):
        time.sleep(0.1)
        print(f'поле {self.name}')
        time.sleep(0.1)
        print('\n {42} {43} {44} {45} {46} {47}\n{36}{0}|{1}|{2}|{3}|{4}|{5}\n{37}{6}|{7}|{8}|{9}|{10}|{11}\n{38}{12}|{13}|{14}|{15}|{16}|{17}\n{39}{18}|{19}|{20}|{21}|{22}|{23}\n{40}{24}|{25}|{26}|{27}|{28}|{29}\n{41}{30}|{31}|{32}|{33}|{34}|{35}\n'.format(self.private_grid[1],self.private_grid[2],self.private_grid[3],self.private_grid[4],self.private_grid[5],self.private_grid[6],self.private_grid[7],self.private_grid[8],self.private_grid[9],self.private_grid[10],self.private_grid[11],self.private_grid[12],self.private_grid[13],self.private_grid[14],self.private_grid[15],self.private_grid[16],self.private_grid[17],self.private_grid[18],self.private_grid[19],self.private_grid[20],self.private_grid[21],self.private_grid[22],self.private_grid[23],self.private_grid[24],self.private_grid[25],self.private_grid[26],self.private_grid[27],self.private_grid[28],self.private_grid[29],self.private_grid[30],self.private_grid[31],self.private_grid[32],self.private_grid[33],self.private_grid[34],self.private_grid[35],self.private_grid[36],self.private_grid[37],self.private_grid[38],self.private_grid[39],self.private_grid[40],self.private_grid[41],self.private_grid[42],self.private_grid[43],self.private_grid[44],self.private_grid[45],self.private_grid[46],self.private_grid[47],self.private_grid[48]))
        time.sleep(0.1)
    def draw_public_grid(self):
        time.sleep(0.1)
        print(f'поле {self.name}')
        time.sleep(0.1)
        print('\n {42} {43} {44} {45} {46} {47}\n{36}{0}|{1}|{2}|{3}|{4}|{5}\n{37}{6}|{7}|{8}|{9}|{10}|{11}\n{38}{12}|{13}|{14}|{15}|{16}|{17}\n{39}{18}|{19}|{20}|{21}|{22}|{23}\n{40}{24}|{25}|{26}|{27}|{28}|{29}\n{41}{30}|{31}|{32}|{33}|{34}|{35}\n'.format(self.public_grid[1],self.public_grid[2],self.public_grid[3],self.public_grid[4],self.public_grid[5],self.public_grid[6],self.public_grid[7],self.public_grid[8],self.public_grid[9],self.public_grid[10],self.public_grid[11],self.public_grid[12],self.public_grid[13],self.public_grid[14],self.public_grid[15],self.public_grid[16],self.public_grid[17],self.public_grid[18],self.public_grid[19],self.public_grid[20],self.public_grid[21],self.public_grid[22],self.public_grid[23],self.public_grid[24],self.public_grid[25],self.public_grid[26],self.public_grid[27],self.public_grid[28],self.public_grid[29],self.public_grid[30],self.public_grid[31],self.public_grid[32],self.public_grid[33],self.public_grid[34],self.public_grid[35],self.public_grid[36],self.public_grid[37],self.public_grid[38],self.public_grid[39],self.public_grid[40],self.public_grid[41],self.public_grid[42],self.public_grid[43],self.public_grid[44],self.public_grid[45],self.public_grid[46],self.public_grid[47],self.public_grid[48]))
        time.sleep(0.1)





Game.start()
while True:
    player_grid = Grid('Игрока')
    player_ship = Ship()
    try:
        player_grid.place_the_ships(player_ship.ship_1)
        player_grid.place_the_ships(player_ship.ship_2)
        player_grid.place_the_ships(player_ship.ship_3)
        player_grid.place_the_ships(player_ship.ship_4)
        player_grid.place_the_ships(player_ship.ship_5)
        player_grid.place_the_ships(player_ship.ship_6)
        player_grid.place_the_ships(player_ship.ship_7)
        break
    except:
        pass

while True:
    pc_grid = Grid('Компьютера')
    pc_ship = Ship()
    try:
        pc_grid.place_the_ships(pc_ship.ship_1)
        pc_grid.place_the_ships(pc_ship.ship_2)
        pc_grid.place_the_ships(pc_ship.ship_3)
        pc_grid.place_the_ships(pc_ship.ship_4)
        pc_grid.place_the_ships(pc_ship.ship_5)
        pc_grid.place_the_ships(pc_ship.ship_6)
        pc_grid.place_the_ships(pc_ship.ship_7)
        break
    except:
        pass

player_grid.public_grid = player_grid.private_grid
time.sleep(0.5)
player_grid.draw_private_grid()
time.sleep(2)
pc_grid.draw_public_grid()
time.sleep(0.5)

time.sleep(0.2)
input('Орел или Решка? 0/1 ')
time.sleep(0.2)
if Coin.flip_coin() == 0:
    time.sleep(0.2)
    print('\n\nВы ходите первым!')
    time.sleep(0.2)
    coin = 0
else:
    time.sleep(0.2)
    print('\n\nКомпьютер ходит первым!')
    time.sleep(1)
    coin = 1

while True:
    if coin ==0:
        while True:
            pc_grid.draw_public_grid()
            time.sleep(0.2)
            raw_coordinates = input('Введите координаты ').lower()
            time.sleep(0.2)
            if raw_coordinates in Converter.coord_field:
                break
        else:
            pass
        coordinates = Converter.convert(raw_coordinates)
        coin = pc_grid.hit_target(coordinates, coin)
    else:
        coordinates = random.choice(player_grid.hit)
        coin = player_grid.hit_target(coordinates, coin)
        time.sleep(1)
        player_grid.draw_public_grid()
        time.sleep(1)
#        time.sleep(1)
#        pc_grid.draw_public_grid()
