class Info():
    author = "Isabel Christidis"
    def __init__(self, game_title):
        self.title = game_title

    def welcome(self):
        print(f"welcome to {self.title}!")

    @staticmethod
    def info():
        print(f"Copyright Isabel Christidis")
        print("Type anything to start")

    @classmethod
    def credits(cls):
        print('Thank you for playing!')
        print(f'Made by {cls.author}')
