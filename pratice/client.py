import pygame
from setting import Settings
def run_game():
    #初始化屏幕对象
    pygame.init()
    client_config = Settings()
    screen = pygame.display.set_mode((client_config.width, client_config.height))
    pygame.display.set_caption("test client")
    #开启主循环
    while True:
        #填充背景色
        screen.fill(client_config.bgc);
        #监听键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #让最近绘制的屏幕可见
        pygame.display.flip()
        
run_game()