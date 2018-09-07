from PyQt5.QtGui import QImage

from GameCfg import GameCfg


class CONST():
    CFG = GameCfg()  # load config file
    FrameImg = QImage("Graphics/windows/windows.png")
    LogoImg = QImage("Graphics/game/logo.png")
    DBImg = QImage("Graphics/game/db.png")
    WorldImg = QImage("Graphics/game/world.png")
    StartImg = QImage("Graphics/game/start.png")
    LevelImg = QImage("Graphics/game/level.png")
    ScoreImg = QImage("Graphics/game/score.png")
    RmlineImg = QImage("Graphics/game/rmline.png")
    ActImg = QImage("Graphics/game/rect.png")
    OverImg = QImage("Graphics/game/over.png")
    NumImge = QImage("Graphics/game/number.png")
    SetupImg = QImage("Graphics/game/setup.png")
    ProcessImg=QImage("Graphics/game/process.png")
    PauseImg=QImage("Graphics/game/pause.png")
    Act_Size = 32  # 方块像素
    GameSpeed=800

    NoShape = 0
    ZShape = 1
    SShape = 2
    LineShape = 3
    TShape = 4
    SquareShape = 5
    LShape = 6
    MirroredLShape = 7

    # 方块坐标表
    rectTable = (
        ((0, 0), (0, 0), (0, 0), (0, 0)),
        ((1, 0), (0, 0), (1, 1), (2, 1)),
        ((1, 1), (0, 1), (1, 0), (2, 0)),
        ((1, 0), (0, 0), (2, 0), (3, 0)),
        ((1, 0), (0, 0), (2, 0), (1, 1)),
        ((1, 0), (0, 0), (0, 1), (1, 1)),
        ((1, 0), (0, 0), (2, 0), (3, 0)),
        ((1, 1), (1, 0), (1, 2), (0, 2))
    )
