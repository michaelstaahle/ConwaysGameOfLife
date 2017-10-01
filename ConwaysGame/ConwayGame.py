from GraphGrid import *
import pygame

class ConwayGame:
    def __init__(self, screen):
        self.__screen = screen
        self.__startpos = None
        self.__stoppos = None
        # Defining some colors
        self.__BLACK = (0, 0, 0)
        self.__WHITE = (255, 255, 255)
        self.__GREEN = (0, 255, 0)
        self.__RED = (255, 0, 0)
        # This sets the WIDTH and HEIGHT of each grid location
        self.__WIDTH = 20
        self.__HEIGHT = 20
        # This sets the margin between each cell
        self.__MARGIN = 5

    def DrawGrid(self, Grid, nrow, ncolumn):
        # Set the background collor
        self.__screen.fill(self.__BLACK, rect = (0,0,1255,755))
        for row in range(nrow):
            for column in range(ncolumn):
                Vertex_ij = Grid.GetVertex(str(row) + ',' + str(column))

                if Vertex_ij.GetLifeStatus() == 0:
                    color = self.__WHITE
                else:
                    color = self.__GREEN

                pygame.draw.rect(self.__screen,
                                 color,
                                 [(self.__MARGIN + self.__WIDTH) * column + self.__MARGIN,
                                  (self.__MARGIN + self.__HEIGHT) * row + self.__MARGIN,
                                  self.__WIDTH,
                                  self.__HEIGHT])

    def text_objects(self, text, font):
        TextSurface = font.render(text, True, self.__BLACK)
        return TextSurface, TextSurface.get_rect()


    def DrawButtons(self):
        pygame.draw.rect(self.__screen, self.__GREEN, (20, 765, 60, 40))
        pygame.draw.rect(self.__screen, self.__RED, (100, 765, 60, 40))
        pygame.draw.rect(self.__screen, self.__WHITE, (180, 765, 60, 40))

        SmallText = pygame.font.Font('freesansbold.ttf', 20)

        TextSurf_start, TextRect_start = self.text_objects('Start', SmallText)
        TextSurf_stop, TextRect_stop = self.text_objects('Stop', SmallText)
        TextSurf_clear, TextRect_clear = self.text_objects('Clear', SmallText)

        TextRect_start.center = (20+60/2, 765+40/2)
        TextRect_stop.center = (100 + 60 / 2, 765 + 40/2)
        TextRect_clear.center = (180 + 60 / 2, 765 + 40/2)

        self.__screen.blit(TextSurf_start, TextRect_start)
        self.__screen.blit(TextSurf_stop, TextRect_stop)
        self.__screen.blit(TextSurf_clear, TextRect_clear)

    def DeadOrAlive(self, Grid, pos):
        column = pos[0] // (self.__WIDTH + self.__MARGIN)
        row = pos[1] // (self.__HEIGHT + self.__MARGIN)

        Vertex = Grid.GetVertex(str(row) + ',' + str(column))
        if Vertex.GetLifeStatus() == 0:
            Vertex.SetLifeStatus(1)
        else:
            Vertex.SetLifeStatus(0)
        return Grid


    def ConGame(self, Grid):
        mainloop = True
        Gameloop = True
        clock = pygame.time.Clock()
        while Gameloop:
            clock.tick(4)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Gameloop = False
                    mainloop = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if pos[1] < 755:
                        Grid = self.DeadOrAlive(Grid, pos)
                    elif 100 < pos[0] < 160 and 765 < pos[1] < 805:
                        Gameloop = False
                    else:
                        pass

            VertexList = Grid.GetVertecies()
            LiveNeighborsList = Grid.GetLiveNeighbors()
            for Vertex in VertexList:
                if Vertex.GetLifeStatus() == 0 and LiveNeighborsList[Vertex.GetKey()] != 3:
                    pass
                elif Vertex.GetLifeStatus() == 1 and LiveNeighborsList[Vertex.GetKey()] < 2:
                    Grid.GetVertex(Vertex.GetKey()).SetLifeStatus(0)
                elif Vertex.GetLifeStatus() == 1 and LiveNeighborsList[Vertex.GetKey()] > 3:
                    Grid.GetVertex(Vertex.GetKey()).SetLifeStatus(0)
                elif Vertex.GetLifeStatus() == 1 and 1 < LiveNeighborsList[Vertex.GetKey()] < 4:
                    pass
                elif Vertex.GetLifeStatus() == 0 and LiveNeighborsList[Vertex.GetKey()] == 3:
                    Grid.GetVertex(Vertex.GetKey()).SetLifeStatus(1)

            self.DrawGrid(Grid, 30, 50)
            pygame.display.flip()

        return (Grid, mainloop)

    def ClearGrid(self, Grid):
        for Vertex in Grid.GetVertecies():
            Vertex.SetLifeStatus(0)
        return Grid

    def run(self):
        pygame.init()
        # Set title of screen
        pygame.display.set_caption("Conway's Game of Life")
        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()
        Grid = GridGraph.CreateGrid(30,50)
        mainloop = True
        while mainloop:
            # Limit frame speed to 50 FPS
            clock.tick(50)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # User clicks the mouse. Get the position
                    pos = pygame.mouse.get_pos()

                    if pos[1] < 755:
                        Grid = self.DeadOrAlive(Grid,pos)

                    elif 20 < pos[0] < 60 and 765 < pos[1] < 785:
                        (Grid, mainloop) = self.ConGame(Grid)

                    elif 180 < pos[0] < 240 and 765 < pos[1] < 785:
                        Grid = self.ClearGrid(Grid)

                    else:
                        pass

            self.DrawGrid(Grid,30,50)
            self.DrawButtons()
            pygame.display.flip()

        pygame.quit()

if __name__ == '__main__':
    WINDOW_SIZE = (1255, 795)
    screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

    CG = ConwayGame(screen)
    CG.run()






