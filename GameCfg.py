import xml.dom.minidom as dom

class GameCfg():
    def __init__(self):
        #read cfg file
        doc = dom.parse("config/cfg.xml").documentElement
        attrlist = doc.getElementsByTagName('frame')
        self.window_width=attrlist[0].getAttribute('width')
        self.window_heitht=attrlist[0].getAttribute("height")
        self.padding = int(attrlist[0].getAttribute("padding"))
        self.cornersize = int(attrlist[0].getAttribute("cornersize"))
        self.layerscfg=[]
        layerlist=doc.getElementsByTagName('layer')
        for layer in layerlist:
            classname=layer.getAttribute('class')
            x=int(layer.getAttribute('x'))
            y=int(layer.getAttribute('y'))
            w=int(layer.getAttribute('w'))
            h=int(layer.getAttribute('h'))
            self.layerscfg.append(LayerCfg(classname,x,y,w,h))


class LayerCfg():
    def __init__(self,classname,x,y,w,h):
        self._classname=classname
        self._x=x
        self._y=y
        self._w=w
        self._h=h

    @property
    def classname(self):
        return self._classname

    @property
    def x(self):
        return self._x
    @x.setter
    def x(self,value):
        if not isinstance(value, int):
            raise ValueError('x must be an integer!')
        self._x=value

    @property
    def y(self):
        return self._y
    @y.setter
    def y(self,value):
        if not isinstance(value, int):
            raise ValueError('y must be an integer!')
        self._y=value

    @property
    def w(self):
        return self._w
    @w.setter
    def w(self,value):
        if not isinstance(value, int):
            raise ValueError('w must be an integer!')
        self._w=value

    @property
    def h(self):
        return self._h
    @h.setter
    def h(self,value):
        if not isinstance(value, int):
            raise ValueError('h must be an integer!')
        self._h=value

