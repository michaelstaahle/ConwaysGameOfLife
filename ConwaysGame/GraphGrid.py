class GridVertex:
    def __init__(self, key, LifeStatus=0):
        self.__LifeStatus = LifeStatus
        self.__key = key
        self.__ListOfNeighbors = []

    def AddNeighbor(self,Vert):
        self.__ListOfNeighbors.append(Vert)

    def GetLifeStatus(self):
        return self.__LifeStatus

    def SetLifeStatus(self, status):
        self.__LifeStatus = status

    def LiveNeighbors(self):
        NLiveNeighbors = 0
        for elm in self.__ListOfNeighbors:
            NLiveNeighbors += elm.GetLifeStatus()
        return NLiveNeighbors

    def NumNieghbors(self):
        return len(self.__ListOfNeighbors)

    def GetKey(self):
        return self.__key

    def GetNeighbors(self):
        return self.__ListOfNeighbors


class GridGraph:
    def __init__(self):
        self.__VertexDic = {}

    def AddVertex(self,key):
        NewVertex = GridVertex(key)
        self.__VertexDic[key] = NewVertex

    def AddConnection(self,V1,V2):
        if V1 not in self.__VertexDic:
            self.AddVertex(V1)
        if V2 not in self.__VertexDic:
            self.AddVertex(V2)
        self.__VertexDic[V1].AddNeighbor(self.__VertexDic[V2])
        self.__VertexDic[V2].AddNeighbor(self.__VertexDic[V1])

    def GetVertex(self,key):
        return self.__VertexDic[key]

    def GetVertecies(self):
        return self.__VertexDic.values()

    def GetLiveNeighbors(self):
        LiveNeighborsDic = {}
        for vertex in self.__VertexDic.values():
            LiveNeighborsDic[vertex.GetKey()] = vertex.LiveNeighbors()
        return LiveNeighborsDic

    @classmethod
    def CreateGrid(cls, nrows, ncolumns):
        Grid = GridGraph()
        Grid.AddVertex('00')
        for i in range(nrows):
            for j in range(ncolumns):
                if i == 0 and j == 0:
                    Grid.AddConnection('0,0','0,1')
                    Grid.AddConnection('0,0','1,0')
                    Grid.AddConnection('0,0','1,1')
                elif i == 0 and j != 0 and j != ncolumns-1:
                    Grid.AddConnection('0' + ',' + str(j), '0' + ',' + str(j+1))
                    Grid.AddConnection('0' + ',' + str(j), '1' + ',' + str(j+1))
                    Grid.AddConnection('0' + ',' + str(j), '1' + ',' + str(j))
                    Grid.AddConnection('0' + ',' + str(j), '1' + ',' + str(j-1))
                elif i == nrows-1 and j == ncolumns-1:
                    pass
                elif j == ncolumns-1:
                    Grid.AddConnection(str(i) + ',' + str(j), str(i+1) + ',' + str(j))
                    Grid.AddConnection(str(i) + ',' + str(j), str(i + 1) + ',' + str(j-1))

                elif i != nrows-1 and j == 0:
                    Grid.AddConnection(str(i) + ',' + '0', str(i+1) + ',' + '0')
                    Grid.AddConnection(str(i) + ',' + '0', str(i+1) + ',' + '1')
                    Grid.AddConnection(str(i) + ',' + '0', str(i) + ',' + '1')
                elif i == nrows-1 and j != ncolumns-1:
                    Grid.AddConnection(str(i) + ',' + str(j), str(i) + ',' + str(j+1))
                else:
                    Grid.AddConnection(str(i) + ',' + str(j), str(i+1) + ',' + str(j+1))
                    Grid.AddConnection(str(i) + ',' + str(j), str(i) + ',' + str(j + 1))
                    Grid.AddConnection(str(i) + ',' + str(j), str(i + 1) + ',' + str(j))
                    Grid.AddConnection(str(i) + ',' + str(j), str(i + 1) + ',' + str(j - 1))
        return Grid

    def __iter__(self):
        return iter(self.__VertexDic.values())





