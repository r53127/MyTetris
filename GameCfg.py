import xml.dom.minidom as dom
from Const import CONST
import LayerClass


class GameCfg():

    def __init__(self):
        doc = dom.parse(CONST.CfgFile).documentElement
        attrlist = doc.getElementsByTagName('frame')
        self.window_width=attrlist[0].getAttribute('width')
        self.window_heitht=attrlist[0].getAttribute("height")
        self.layers=[]
        layerlist=doc.getElementsByTagName('layer')
        for layer in layerlist:
            cls=layer.getAttribute('class')
            x=layer.getAttribute('x')
            y=layer.getAttribute('y')
            w=layer.getAttribute('w')
            h=layer.getAttribute('h')
            creator=getattr(LayerClass,cls)# reflect
            self.layers.append(creator(int(x), int(y), int(w), int(h)))


class LayerCfg():
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h

    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getW(self):
        return self.w


if __name__ == '__main__':
    GameCfg().CfgReader()