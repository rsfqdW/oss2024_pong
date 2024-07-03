from gameobject import window_height as HEIGHT
from gameobject import window_width as WIDTH


class GameLogic:
    """
    Game logic of Pong game
    Attributes:
        - ball: A Ball object
        - paddle_left: A Paddle object positioned in left side
        - paddle_right: A Paddle object positioned in right side
    Methods:
        - reset(): resets ball and paddles
        - update(): updates the game board for the next frame
        - ball_falls_left(): returns True if ball exceeds the left side of the screen
        - ball_falls_right(): returns True if ball exceeds the right side of the screen
        - ball_hits_wall(): returns True if ball hits the top or bottom wall
        - ball_hits_paddle(): returns True if ball hits any of the paddles
    """
    def __init__(self, ball, paddle_left, paddle_right):
        self.ball = ball
        self.paddle_left = paddle_left
        self.paddle_right = paddle_right
        self.reset()

    def reset(self):
        self.ball.reset()
        self.paddle_left.reset()
        self.paddle_right.reset()

    def ball_falls_left(self): # <-- TODO: complete this function. check if self.ball.position[0] goes below 0
        if self.ball.position[0] < 0: # x 좌표가 0보다 작으면(왼쪽 경계를 넘어간 경우)
            return True

    def ball_falls_right(self): # <-- TODO: complete this function. check if self.ball.position[0] exceeds WIDTH
        if self.ball.position[0] > WIDTH : # x좌표가 화면 창의 너비(WIDTH)보다 크면(오른쪽 경계를 넘어간 경우)
            return True
    def ball_hits_wall(self): # <-- TODO: complete this function. check if self.ball.position[1] goes beyond 0 or HEIGHT
        # Check if the ball hits the top or bottom walls
        if self.ball.position[1] <= 0 or self.ball.position[1] + self.ball.size[1] >= HEIGHT:
            return True

        # Check if the ball hits the left paddle
        if self.ball.velocity[0] < 0 and self.ball.is_collision(self.paddle_left):
            self.ball.velocity[0] = -self.ball.velocity[0]  # Reverse X-axis velocity
            return True

        # Check if the ball hits the right paddle
        if self.ball.velocity[0] > 0 and self.ball.is_collision(self.paddle_right):
            self.ball.velocity[0] = -self.ball.velocity[0]  # Reverse X-axis velocity
            return True

        return False


    def ball_hits_paddle(self):
        return self.ball.is_collision(self.paddle_left) or self.ball.is_collision(self.paddle_right)

    def update(self):
        self.ball.update()
        self.paddle_left.update()
        self.paddle_right.update()
        
        if self.ball_falls_left(): #왼쪽에 점수 주고 리셋
            self.paddle_left.score += 1
            self.reset()
        if self.ball_falls_right(): #오른쪽에 점수 주고 리셋
            self.paddle_right.score += 1
            self.reset()
            
            
        # <-- TODO: Complete the following
        if self.ball_hits_wall():
           self.ball.velocity[1] = -self.ball.velocity[1]

        """ 
        check the conditions for the following and apply appropriate actions:
        IF ball falls left
            - score of the right paddle goes up
            - resets game
        IF ball falls right
            - score of the left paddle goes up
            - resets game
        IF ball hits wall
            - Y-axis velocity (i.e., self.ball.velocity[1]) reverses
        IF ball hits paddle
            - X-axis velocity reverses
        """

