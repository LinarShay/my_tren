import time
import hashlib

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self._hash_password(password)
        self.age = age

    def _hash_password(self, password):
        return int(hashlib.sha256(password.encode()).hexdigest(), 16)

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self):
        nickname = input("Введите имя пользователя: ")
        password = input("Введите пароль: ")
        hashed_password = int(hashlib.sha256(password.encode()).hexdigest(), 16)

        for user in self.users:
            if user.nickname == nickname:
                if user.password == hashed_password:
                    self.current_user = user
                    print(f"Добро пожаловать, {user.nickname}!")
                else:
                    print("Неверный пароль. Выход из аккаунта.")
                    self.log_out()
                return
        print("Пользователь не найден.")

    def register(self):
        nickname = input("Введите имя пользователя для регистрации: ")
        password = input("Введите пароль: ")
        age = int(input("Введите возраст: "))

        if any(user.nickname == nickname for user in self.users):
            print(f"Пользователь {nickname} уже существует.")
        else:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = new_user
            print(f"Пользователь {nickname} зарегистрирован и вошёл в систему.")

    def log_out(self):
        if self.current_user:
            print(f"Пользователь {self.current_user.nickname} вышел из системы.")
        self.current_user = None
        print("Программа завершена.")
        exit()

    def add(self, *videos):
        for video in videos:
            if video.title not in [v.title for v in self.videos]:
                self.videos.append(video)

    def get_videos(self, search_word):
        search_word = search_word.lower()
        return [video.title for video in self.videos if search_word in video.title.lower()]

    def watch_video(self):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        video_title = input("Список видео:\n-Лучший язык программирования 2024 года;\n-Для чего девушкам парень "
                            "программист?\nСкопируйте полное название интересующего вас материала и введите ниже↓.\nВведите название видео: ")

        for video in self.videos:
            if video.title == video_title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

                print(f"Начинаем просмотр: {video.title}")
                for second in range(video.time_now + 1, video.duration + 1):
                    print(second, end=' ', flush=True)
                    time.sleep(1)
                print("\nКонец видео")
                video.time_now = 0
                return

        print("Видео не найдено.")


# Пример использования:
ur = UrTube()

# Добавление видео вручную
ur.add(
    Video('Лучший язык программирования 2024 года', 10),
    Video('Для чего девушкам парень программист?', 5, adult_mode=True)
)

print("Доступные видео: ", ur.get_videos(''))  # Вывод всех видео

while True:
    if not ur.current_user:
        print("\n1. Вход")
        print("2. Регистрация")
    print("3. Просмотр видео")
    print("4. Выход из аккаунта")

    choice = input("Выберите действие: ")

    if choice == '1' and not ur.current_user:
        ur.log_in()
    elif choice == '2' and not ur.current_user:
        ur.register()
    elif choice == '3':
        ur.watch_video()
    elif choice == '4':
        ur.log_out()
    else:
        print("Неверный выбор. Попробуйте снова.")
