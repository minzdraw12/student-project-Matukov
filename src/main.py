from utils.helpers import greet


def main():
    name = input("Введите ваше имя: ")
    message = greet(name)
    print(message)


if __name__ == "__main__":
    main()