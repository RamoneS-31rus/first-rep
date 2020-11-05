class User:
    def __init__(self, first_name, second_name, balance):
        self.first_name = first_name
        self.second_name = second_name
        self.balance = balance
    def get_info(self):
        return 'Клиент: ' + self.first_name + ' ' + self.second_name + '.' + ' ' + 'Баланс: ' + str(self.balance)
class Database:
    def __init__(self):
        self.db = []
    def add_user(self, first_name, second_name, balance):
        user = User(first_name, second_name, balance)
        return self.db.append(user)
    def find_users(self, first_name):
        info_list = []
        for user in self.db:
            if user.first_name == first_name:
                info_list.append(user.get_info())
        return info_list
users_db = Database()
class UserInterface:
    def choise(self, input_type):
        if input_type == "1":
            first_name = input("Введите имя: ")
            second_name = input("Введите фамилию: ")
            balance = int(input("Введите сумму: "))
            return users_db.add_user(first_name,second_name,balance)
        elif input_type == "2":
            find_users = input("Введите имя: ")
            print(users_db.find_users(find_users))
        elif input_type == "3":
            return "STOP"
        else:
            print("Некорректный ввод")
    def loop(self):
        while True:
            print("Введите 1, если хотите добавить клиента в базу:")
            print("Введите 2, если хотите вывести информацию о клиенте:")
            mode = input("Введите 3, если хотите закончить работу с программой:")
            result = self.choise(mode)
            if result == "STOP":
                break
UI = UserInterface()
UI.loop()