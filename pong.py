import arcade 
from rocket import Rocket 
from ball import Ball 



class Game(arcade.Window) :
    def __init__(self):
        super().__init__(width = 750 , height = 500 , title ="PONG 2023")
        arcade.set_background_color(arcade.color.DARK_GREEN)
        self.player_1 = Rocket(30 , self.height//2 , arcade.color.YELLOW , "player1")
        self.player_2 = Rocket(self.width - 30 , self.height//2 , arcade.color.RED , "player2") 
        self.ball = Ball(self)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_outline(self.width//2 , self.height//2 , self.width -20 , self.height - 20 , color= arcade.color.WHITE , border_width= 5)
        arcade.draw_line(self.width//2 , 10 , self.width//2 , self.height -10 , color= arcade.color.WHITE , line_width= 5)
        self.player_1.draw()
        self.player_2.draw()
        self.ball.draw()
        arcade.draw_text(f"Score: {self.player_1.score}", 15, 20, arcade.color.WHITE, font_size= 18 ,font_name= 'arial', bold=True)
        arcade.draw_text(f"Score: {self.player_2.score}", 620, 20, arcade.color.WHITE, font_size= 18 ,font_name= 'arial', bold=True)

    def on_mouse_motion(self , x : int , y:int , dx: int , dy: int):
        
        if self.player_1.height//2 +10< y < self.height - self.player_1.height//2 -5 :
            self.player_1.center_y = y


    def on_update(self , delta_time : float):
        self.ball.move()
        if self.player_2.height//2 +10 < self.player_2.center_y < self.height - self.player_2.height//2 -5 :
            self.player_2.move(self , self.ball)

        if self.ball.center_y < 30 or self.ball.center_y > self.height - 30 :
            self.ball.change_y *= -1

        if arcade.check_for_collision(self.player_1 , self.ball):
            self.ball.change_x *= -1

        if arcade.check_for_collision(self.player_2 , self.ball):
            self.ball.change_x *= -1

        if self.ball.center_x < 0 :
            self.player_2.score += 1
            del self.ball
            self.ball = Ball(self)

        if self.ball.center_x > self.width :
            self.player_1.score += 1
            del self.ball
            self.ball = Ball(self)
        

game = Game()
arcade.run()