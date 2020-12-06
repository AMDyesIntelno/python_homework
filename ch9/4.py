singer_song = {"zhangsan": "1.mp3", "lisi": "2.mp3", "wangwu": "3.mp3"}


class MusicPlayer:
    def __init__(self):
        self.song_list = []
        self.singer_list = []
        self.is_paused = False
        self.song_number = 0
        for i in singer_song.keys():
            self.singer_list.append(i)
            self.song_list.append(singer_song[i])

    def list_music(self):
        for i in self.song_list:
            print(i)

    def play(self):
        if self.is_paused:
            self.is_paused = False
            print("已暂停")
        else:
            self.is_paused = True
            print("当前播放", self.song_list[self.song_number])

    def next_song(self):
        self.song_number = (self.song_number + 1) % len(self.song_list)
        self.is_paused = False
        self.play()

    def choice_menu(self, choice):
        if choice == '1':
            self.list_music()
        elif choice == '2':
            self.play()
        elif choice == '3':
            self.next_song()


a = MusicPlayer()
while 1:
    choice = input()
    if choice == "q" or choice == "quit":
        break
    a.choice_menu(choice)