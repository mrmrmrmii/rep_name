# class Vehicle:
#
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
# Bus = Vehicle('School Volvo',180,12)
#
# print(Bus.name, Bus.max_speed, Bus.mileage)
# from fileinput import filename
#
#
# # class Vehicle:
# #     def __init__(self, name, max_speed, mileage):
# #         self.name = name
# #         self.max_speed = max_speed
# #         self.mileage = mileage
# #
# #     def seating_capacity(self, capacity):
# #         return f"The seating capacity of a {self.name} is {capacity} passengers"
# #
# # Bus = Vehicle('Bus',1,1)
# # print(Bus.seating_capacity(50))
#
#
# # class MediaPlayer():
# #     def open(self, file):
# #         self.filename = file
# #     def play(self):
# #         print(f'Воспроизведение {self.filename}')
# # media1= MediaPlayer()
# # media2= MediaPlayer()
# # media1.open('filemedia1')
# # media2.open('filemedia2')
# # media1.play()
# # media2.play()
#
# #5
# # class Graph():
# #     LIMIT_Y=[0,10]
# #     def set_data(self, data):
# #         self.data = data
# #     def draw(self):
# #         n = []
# #         for m in self.data:
# #             if m >= self.LIMIT_Y[0] and m <= self.LIMIT_Y[1]:
# #                 n.append(str(m))
# #         #l = ' '.join(n)
# #         print(*n)
# # g1= Graph()
# # g1.set_data([10,-5,100,20,0,80,45,2,5,7])
# # g1.draw()
#
#
# #7
# import sys
# class StreamData():
#     def create(self, fields, lst_values):
#         if len(fields) != len(lst_values):
#             return False
#         for i, g in enumerate(fields):
#             setattr(self, g,lst_values[i])
#         return True
#
# class StreamReader:
#     FIELDS = ('id', 'title', 'pages')
#
#     def readlines(self):
#         lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
#         sd = StreamData()
#         res = sd.create(self.FIELDS, lst_in)
#         return sd, res
#
#
# sr = StreamReader()
# data, result = sr.readlines()

#9
class DataBase():
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def select(self,a , b):
        if b >= len(self.lst_data) - 1:
            b = len(self.lst_data) - 1
        return self.lst_data[a:b+1]
    def insert(self, data:list[str]):
        for x in data:
            x = x.split()
            d = {}
            for i, v in enumerate(self.FIELDS):
                d[v] = x[i]
            self.lst_data.append(d)
lst_in = ['1 Серг 35 12000', '2 Utq 48 12344']
DataBase.lst_data.append('2 dfs 21312 123')
a = DataBase()
a.insert(lst_in)
print(a.select(0,3))

