import json
import os
import csv

save = "save_file.json"
f_csv = "game_data.csv"


def gsave(vault_boy):
    with open(save, 'w') as saving:
        json.dump(save, saving)

def load():
    if not os.path.isfile('save'):
        return None
    with open('save') as load:
        data = json.load(load)
    return data

def delete():
    if os.path.isfile('save'):
        os.remove('save')

def csv_file(gamedata):
    data = ["nickname", "pocket"]
    if not os.path.isfile(f_csv):
        with open(f_csv, mode='w') as vault:
            writer = csv.DictWriter(vault, fieldnames = data)
            writer.writeheader()
    with open(f_csv, mode='a') as vault:
        writer = csv.DictWriter(vault, fieldnames = data)
        writer.writerow(gamedata)

while True: 
    nickname = input("Ваш никнейм: ")
    pocket = ["100 крышек", "стимулятор", "посылка X2", "бутылка воды", "злаковый батончик"]
    print ("У вас есть: 100 крышек, стимулятор, посылка X2, бутылка воды, недоеденный злаковый батончик")
    print("Ядерная пустошь, все окружающие вас постройки, оставшиеся после ядерной войны, нагоняют на вас тревогу.")
    print("Могут ли там быть рейдеры или обычная шпана, а может и того хуже - разведчики Анклава.")
    print("Пытаясь отвлечься от плохих мыслей вы смотрите на прекрасный рассвет.")
    print ("Наверное единственное, что осталось из хорошего после ядерной войны.")
    print("1)Продолжить поход 2)Продолжить смотреть на рассвет")
    print("3)сохранить игру 4)загрузить сохранение 5)Удалить сохранение")
    func = int(input("Что будете делать? "))
    if func > 5:
        print ("Неправильное действие")
        quit()
    elif func < 1:
        print ("Неправильное действие")
        quit()
    else:
        def go(func):
            match func:
                case 1:
                    print("Вы вернулись к работе курьером компании Мохавский экспресс.")
                case 2:
                    print("Из-за своей невнимательности, вас доганяет группа бандитов.")
                    print("Они вас не убьют, но сильно побьют, если вы не отдадите им деньги.  Даже если бы у вас было оружие, у вас не получилось бы отбиться.")
                    print("*Вы теряете все свои крышки*")
                    pocket.remove("100 крышек")
                case 3:
                    gsave(nickname)
                    print("Сохранение окончено")
                case 4:
                    saved_game = load()
                    if saved_game is not None:
                        nickname = saved_game['playername']
                        print("Игра загружена{nickname}")
                case 5:
                    delete()
                    print("Сохранение удалено")
            csv_file(nickname)
            gsave(nickname)
        go(func)

    print("Вы дошли до конечного места доставки, этим местом оказался небольшой военный лагерь.")
    print("По пути к палатке младшего лейтенанта, у одного из солдат вы видите занчок Братства Стали. ")
    print("Стоило ожидать, что это будут они, ведь их группы ходят неподалеку от лагеря.")
    print("На столе виден план других посылок. С его помощью можно понять что в других коробках, но не в вашей.")
    sclad = {"1": "5 пачек ментат", "2": "3 винта", "3": "100 пуль 5мм"}
    print(sclad)
    print("Вы как не любитель Братства Стали можете немного изменить их данные, чтобы им легко не было")
    hm = int(input("Хотите что-то поменять? 1-да 2-нет "))
    if hm == 2:
        print("Продолжим")
    elif func > 2:
        print ("Неправильное действие")
        quit()
    elif func < 1:
        print ("Неправильное действие")
        quit()
    else:
        print("Вас замечает один из солдат и просит отойти от списка с данными. Кажется, что он не понял что вы хотели сделать.")
    print("Вы дошли до палатки младшего лейтенанта")
    pocket.remove("посылка X2")
    print ("*Предмет: посылка был отдан (X2)*")
    print("Вы просите доплату за каждую посылку, ведь дорога была опасна")
    print("Сколько ядерных батарей вы хотите получить? ")
    GG = int(input())
    if GG > 100:
        print("Вам отказано в доплате")
    else:
        p = f"{GG * 2}"
        print("Вы получили ", p, " ядерных батарей")
        pocket.append(p+" ядерных батарей")
        print(pocket)

    print("Начинается атака рейдеров на лагерь.")
    print("1)Бежать 2)Взять лазерную винтовку со склада и начать сражаться 3)Взять винтовку и убежать")
    print("4)сохранить игру 5)загрузить сохранение 6)Удалить сохранение")
    func = int(input("Что будете делать? "))
    if func > 6:
        print ("Неправильное действие")
        quit()
    elif func < 1:
        print ("Неправильное действие")
        quit()
    else:
        def go(func):
            match func:
                case 1:
                    print ("Вы убежали, но вас ранили.")
                    quit()
                case 2:
                    print ("Вас убили, а ведь вы не успели даже зарядить оружие. ")
                    print("Не стройте из себя героя, это далеко не сказка.")
                    quit()
                case 3:
                    print ("Вам удалось украсть винтовку, но вас ранили")
                    pocket.append("лазерная винтовка")
                case 4:
                    gsave(nickname)
                    print("Сохранение окончено")
                case 5:
                    saved_game = load()
                    if saved_game is not None:
                        nickname = saved_game['playername']
                        print("Игра загружена{nickname}")
                case 6:
                    delete()
                    print("Сохранение удалено")
            csv_file(nickname)
            gsave(nickname)
        go(func)

    print("Хотите принять стимулятор? 1 - да 2 - нет")
    func = int(input("Что будете делать?"))
    if func > 5:
        print ("Неправильное действие")
        quit()
    elif func < 1:
        print ("Неправильное действие")
        quit()
    else:
        def go(func):
            match func:
                case 1:
                    print("Вы приняли стимулятор. Теперь вы чувствуете себя лучше")
                    pocket.remove("стимулятор")
                case 2:
                    print("Конец наступил раньше, чем ожидал главный герой. Вы ведь могли его спасти...")
                    quit()
                case 3:
                    gsave(nickname)
                    print("Сохранение окончено")
                case 4:
                    saved_game = load()
                    if saved_game is not None:
                        nickname = saved_game['playername']
                        print("Игра загружена{nickname}")
                case 5:
                    delete()
                    print("Сохранение удалено")
            csv_file(nickname)
            gsave(nickname)
        go(func)

    print("Становится все тише и тише. Вы решили посмотреть, что произошло")
    print("Рейдеры превзошли эту группу Братства Стали числом, они проиграли")
    print("Нужно бежать, но вы не решили как.")
    print("1)Тихо проскочить через лагерь, забрав посылку обратно 2) Обойти лагерь сбоку, прячась среди скал")
    print("3)сохранить игру 4)загрузить сохранение 5)Удалить сохранение")
    func = int(input("Что будете делать?"))
    if func > 6:
        print ("Неправильное действие")
        quit()
    elif func < 1:
        print ("Неправильное действие")
        quit()
    elif func == 6:
        print("Пасхалка открыта: вы нашли небольшой подземный бункер, вы съедаете все, что у вас есть, чтобы выжить")
        pocket.remove("бутылка воды")
        pocket.remove("злаковый батончик")
        print("На следующий день все утихло. Вы просто ушли обратно домой, наблюдая за уже сгоревшим лагерем.")
        print("Что вам удалось сохранить: ", pocket)
    else:
        def go(func):
            match func:
                case 1:
                    print("Вас убили, вы не смогли вернуть посылку")
                    quit()
                case 2:
                    print("Пройдя мимо лагеря, вы бедите от него подальше")
                    print("Появляется резкое чувство боли в вашем плече. Это оказалась пуля, вас все же заметили и не дали просто так уйти.")
                    print("Вы прячитесь среди скал это последние секунды жизни главного героя, умершего в ядерной пустыни.")
                    print("Что у вас было: ", pocket)
                case 3:
                    gsave(nickname)
                    print("Сохранение окончено")
                case 4:
                    saved_game = load()
                    if saved_game is not None:
                        nickname = saved_game['playername']
                        print("Игра загружена{nickname}")
                case 5:
                    delete()
                    print("Сохранение удалено")
            csv_file(nickname)
            gsave(nickname)
        go(func)

    print("-----FALLOUT-----")
    print("И помните: война никогда не меняется")
    print("Хотите повторить? 1 - да 2 - нет ")
    func = int(input("Что будете делать?"))
    if func > 2:
        print ("Неправильное действие")
        quit()
    elif func < 1:
        print ("Неправильное действие")
        quit()
    elif func == 2:
        print("Ну вот и всё")
        quit()
    else:
        print("И вперед, по новой")