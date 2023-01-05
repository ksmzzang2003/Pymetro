import pygame, random, time
from pygame.locals import *
from station_data import *
from edge_data import *

# for line, edges in edge.items():
#     for edge in edges:
#         fromstop = edge["from"]
#         tostop = edge["to"]
#         if fromstop in station and tostop in station : 
#             if (tostop in station[fromstop]["connected"]) == False : 
#                 station[fromstop]["connected"].append(tostop); 
#             tmp = fromstop; 
#             fromstop = tostop
#             tostop = tmp
#             if (tostop in station[fromstop]["connected"]) == False : 
#                 station[fromstop]["connected"].append(tostop); 
        

WIDTH = 1500
HEIGHT = 750
TIME = 10
FACTOR = 18 * 30 * TIME
TICK = 20
STATION_NUM = 0
COLOR_MODE = 0  #배경 색을 바꿀 수 있다. 곧, 전반적으로 흑백이 반전된다.

pygame.init()

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Subway System")
myFont=pygame.font.SysFont("arial", 10, False, False)
clock = pygame.time.Clock()

def color(line):  #각 노선 별로 고유의 색을 지정해준다.
    if line == 4:
        return (44,158,222)
    elif line == 2:
        return (60,180,74)
    elif line == 9:
        return (206,164,58)
    elif line == 7:
        return (105,114,21)
    elif line == "수인분당":
        return (255,206,51)
    elif line == 1 or line == "광명셔틀" or line == "경인선":
        return (38,60,150)
    elif line == 3:
        return (255,115,0)
    elif line == 5:
        return (137,54,224)
    elif line == "경의중앙":
        return (124,196,165)
class Train():  #열차에 대한 class이다.
    def __init__(self, line, orientation ):
        self.line = line
        self.destination = 0  #향하고 있는 역이다.
        self.prev = -1  #방금 지나친 역이다.
        line_destinations = {
            "상행": {
                4: "한대앞",
                2: "뚝섬",
                9: "올림픽공원",
                7: "용마산",
                "수인분당": "모란",
                1: "군포",
                "경인선": "역곡",
                3: "오금"
            },
            "하행": {
                4: "동대문",
                2: "영등포구청",
                9: "염창",
                7: "까치울",
                "수인분당": "청량리",
                1: "종각",
                "경인선": "종각",
                3: "종로3가"
            }
        }

        self.destination = line_destinations[orientation][line]
        #양 끝 점에서만 열차를 출발할 수 있도록 했다. 때문에 상행이냐, 하행이냐에 따라 시작하는 위치가 바뀐다.
        #본 코드는 출발점을 정해주는 코드이다.
        self.location = list(station[self.destination]["pos"])
        self.xvel = 0
        self.yvel = 0
        self.capacity = 0  #노선에 따라 열차 용량이 다르기 때문에 그 차이를 주는 과정이다.
        if line == 1 or line == 2 or line == 3 or line == 4 or line == "경인선":
            self.capacity = 160*10
        elif line == 7 or line == "경의중앙":
            self.capacity = 160*8
        elif line == 8 or line == 9 or line == "수인분당":
            self.capacity = 160*6
        self.embarked = 0
        self.heading = []
        for i in range(STATION_NUM):
            self.heading.append(0)

    def update(self): #열차 위치가 이동한다.
        self.location[0] += self.xvel
        self.location[1] += self.yvel

    def next_station(self):  #특정 역에 도착한 열차가 목적지를 바꾼다.
        if len(station[self.destination]["connected"]) ==1:
            self.prev = -1
        for stop in station[self.destination]["connected"]:
            if self.line in station[stop]["line"] and stop != self.prev:
                self.prev = self.destination
                self.destination = stop
                self.xvel = (station[stop]["pos"][0]-station[self.prev]["pos"][0]) / TIME
                self.yvel = (station[stop]["pos"][1]-station[self.prev]["pos"][1]) / TIME
                self.xvel = int(round(self.xvel))
                self.yvel = int(round(self.yvel))
                break

def sq(su):
    return su*su

station_number = []
for key in station.keys():
    station_number.append(key)
STATION_NUM = len(station_number)

line_numbers = {
    "수인분당": 10,
    "경인선": 11,
    "경의중앙": 12
}

train = [[] for _ in range(15)]  # Create a list of 15 empty lists

lines = [4, 2, 9, 7, "수인분당", 1, "경인선", 3]
for line in lines:
    if line in line_numbers:
        index = line_numbers[line]
    else:
        index = line
    train[index].append(Train(line, "상행"))
    train[index].append(Train(line, "하행"))


Snumber_dict = {}
for i in range(STATION_NUM):
    Snumber_dict[station_number[i]] = i

#역간 거리를 구하기 위하여 플로이드-와샬 알고리즘을 진행한다.
dist = [[1000 for j in range(STATION_NUM)] for i in range(STATION_NUM)]
for i in range(STATION_NUM):
    dist[i][i] = 0

for key, value in station.items():
    for stop in value["connected"]:
        dist[Snumber_dict[key]][Snumber_dict[stop]] = 1
        dist[Snumber_dict[stop]][Snumber_dict[key]] = 1

for k in range(STATION_NUM):
    for i in range(STATION_NUM):
        for j in range(STATION_NUM):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

run = True
while run:
    clock.tick(TICK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(event)
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  #노선의 양 끝점을 클릭하면 열차가 추가된다.
            stations = {
                "한대앞": (4, "상행"),
                "동대문": (4, "하행"),
                "뚝섬": (2, "상행"),
                "영등포구청": (2, "하행"),
                "올림픽공원": (9, "상행"),
                "염창": (9, "하행"),
                "용마산": (7, "상행"),
                "까치울": (7, "하행"),
                "모란": ("수인분당", "상행"),
                "청량리": ("수인분당", "하행"),
                "군포": (1, "상행"),
                "종각": (1, "하행"),
                "역곡": ("경인선", "상행"),
                "종각": ("경인선", "하행"),
                "오금": (3, "상행"),
                "종로3가": (3, "하행")
            }

            for station_name, (line, orientation) in stations.items():
                if sq(event.pos[0] - station[station_name]["pos"][0]) + sq(event.pos[1] - station[station_name]["pos"][1]) < 25:
                    if line in line_numbers:
                        index = line_numbers[line]
                    else:
                        index = line
                    train[index].append(Train(line, orientation))



    for i in train:
        for object in i:  #열차가 역에 도착한 상황을 확인한다.
            if station[object.destination]["pos"][0] == object.location[0] and station[object.destination]["pos"][1] == object.location[1]:
                object.next_station()

                #승객들이 열차에서 내린다. 환승을 목적으로 내리는 경우 역의 대기 인원이 추가된다.
                object.embarked -= object.heading[Snumber_dict[object.prev]]
                object.heading[Snumber_dict[object.prev]] = 0
                for key in station.keys():
                    if dist[Snumber_dict[object.destination]][Snumber_dict[key]] >= dist[Snumber_dict[object.prev]][Snumber_dict[key]]:
                        object.embarked -= object.heading[Snumber_dict[key]]
                        station[object.prev]["waiting"] += object.heading[Snumber_dict[key]]
                        object.heading[Snumber_dict[key]] = 0

                #승객들이 열차에 탄다. 내가 가고자 하는 역에 대해, 열차가 가고자 하는 역과의 거리가 현재 역과의 거리보다 짧으면 열차를 탄다.
                Boarding_Passenger = min(object.capacity - object.embarked, station[object.prev]["waiting"])
                Boarding_Passenger = max(Boarding_Passenger, 0)
                Possible_Passenger = 0
                for key in station.keys():
                    if dist[Snumber_dict[object.destination]][Snumber_dict[key]] < dist[Snumber_dict[object.prev]][Snumber_dict[key]]:
                        Possible_Passenger += station[key]["passenger"]
                for key in station.keys():
                    if dist[Snumber_dict[object.destination]][Snumber_dict[key]] < dist[Snumber_dict[object.prev]][Snumber_dict[key]]:
                        obj_to_key = int(round(Boarding_Passenger * station[key]["passenger"] / Possible_Passenger)) 
                        # 가정 : obj -> key 인원 = obj 승하차량 * (key 승하차량 / 전체 승하차량)
                        object.heading[Snumber_dict[key]] += obj_to_key
                        object.embarked += obj_to_key
                        station[object.prev]["waiting"] -= obj_to_key


            object.update()
            pygame.draw.rect(screen,color(object.line),[object.location[0],object.location[1]-10,10,10])  #열차와 열차에 탑승한 승객 수를 표시한다.
            text = myFont.render(str(object.embarked), True, (COLOR_MODE,COLOR_MODE,COLOR_MODE))
            screen.blit(text, [object.location[0],object.location[1]-25])


    for key, value in station.items(): #각 역을 선으로 이어주며 대기하는 승객 수를 표시한다.
        pygame.draw.circle(screen, (255,0,0), value["pos"],5)
        value["waiting"] += station[key]["passenger"] // FACTOR
        text = myFont.render(value["name"], True, (COLOR_MODE,COLOR_MODE,COLOR_MODE))
        text1 = myFont.render(str(value["waiting"]), True, (COLOR_MODE,COLOR_MODE,COLOR_MODE))

        imsi = list(value["pos"])
        imsi[0] -= 25
        imsi[1] += 5
        screen.blit(text, imsi)
        imsi[0] += 25
        imsi[1] += 10
        screen.blit(text1, imsi)
        for i in value["line"]:
            for stop in value["connected"]:
                if i in station[stop]["line"]:
                    pygame.draw.line(screen, color(i),value["pos"],station[stop]["pos"])

    pygame.display.update()
    screen.fill((255-COLOR_MODE,255-COLOR_MODE,255-COLOR_MODE))
    
pygame.quit()
