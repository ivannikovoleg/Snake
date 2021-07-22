from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_high_score()
        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()
        self.read_high_score()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} High Score : {self.high_score}', align='center', font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.score = 0
        self.update_scoreboard()

    def read_high_score(self):
        with open('highscore.txt', 'r') as f:
            score = f.read()
        return int(score)

    def write_high_score(self):
        with open('highscore.txt', mode='w') as f:
            f.write(str(self.high_score))
