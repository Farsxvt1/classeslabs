class Song:
    app_name = "Python Music Player"
    def __init__(self, title, length):
        self.title = title
        self.__length = length
    def play(self):
        return f"Playing {self.title}..."
    def info(self):
        return f"{self.title} - {self.__length} minutes"
    def __hidden_feature(self):
        return f"{self.title} has a secret remix version!"
    def reveal_secret(self):
        return self.__hidden_feature()
s1 = Song("Happy Tune", 3)
s2 = Song("Sad Melody", 5)
print(s1.play())
print(s2.info())
print(s1.reveal_secret())
print("Has title:", hasattr(s1, "title"))
print("Has __length:", hasattr(s1, "__length"))
print("Class name:", s1.__class__.__name__)
print("Module name:", s1.__class__.__module__)

