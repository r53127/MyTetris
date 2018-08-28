'''
游戏逻辑
'''

class GameService():
    def __init__(self,dto):
        self.dto=dto

    def gameTest(self):
        self.dto.nowPoint += 1
        print(self.dto.nowPoint)