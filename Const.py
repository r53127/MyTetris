from GameCfg import GameCfg


class CONST():
    CFG = GameCfg()  # load config file
    FrameImg = "Graphics/windows/windows.png"
    LogoImg = "Graphics/game/logo.png"
    DBImg = "Graphics/game/db.png"
    WorldImg = "Graphics/game/world.png"
    StartImg = "Graphics/game/start.png"
    LevelImg = "Graphics/game/level.png"
    ScoreImg = "Graphics/game/score.png"
    RmlineImg = "Graphics/game/rmline.png"
    ActImg = "Graphics/game/rect.png"
    BackImg = "Graphics/Backgroud/screen1.jpg"
    OverImg = "Graphics/game/over.png"
    NumImge = "Graphics/game/number.png"
    SetupImg = "Graphics/game/setup.png"
    ProcessImg="Graphics/game/process.png"
    Act_Size = 32  # 方块像素

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
