"LAB_9"
#ЗАМЕЧАНИЕ: ДАННЫЙ КОД СОЗДАЕТ 2 ПАПКИ В ДИРЕКТОРИИ, В КОТОРОЙ ТАКЖЕ ХРАНЯТСЯ 5 КАРТИНОК.
#ОН НАКЛАДЫВАЕТ ФАЛЬТР НА 5 КАРТИНОК, И ПОМЕЩАЕТ ИХ В ПАПКУ 'EDITED_PICS',
#А ОРИГИНАЛЫ ЭТИХ КАРТИНОК - В ПАПКУ 'ORIGINAL_PICS'

#ПО-ДРУГОМУ НИКАК НЕ ПОЛУЧАЛОСЬ ВЫПОЛНИТЬ ПОСТАВЛЕННУЮ ЗАДАЧУ, К СОЖАЛЕНИЮ

# 9.1 & 9.2 ОДНИМ КОДОМ
def p1p2():
    from pathlib import Path
    from PIL import Image, ImageFilter
    import shutil

    this_dir = Path.cwd()
    filenames = Path(this_dir).glob('*.jpg') # ЕСЛИ НУЖНО ОБРАБОТАТЬ ДРУГОЙ ФОРМАТ ФАЙЛОВ, ТО ПРОСТО ВМЕСТО JPG ПИШЕМ ДРУГОЕ РАСШИРЕНИЕ

    z0 = Path('edited_pics').mkdir(parents=True, exist_ok=True)
    z1 = Path('original_pics').mkdir(parents=True, exist_ok=True)
    z = this_dir.joinpath('edited_pics')
    new_path = Path(str(z))

    for file in filenames:
        with Image.open(file) as img:
            img.load()
            shutil.copy(Path(file), 'C:/LAB_9/original_pics')
            new_img = img.filter(ImageFilter.FIND_EDGES)
            new_img.save(Path(str(file)))
            new_img.save(Path(shutil.move(file, new_path)))


def p3():
    import csv

    file = open("data.csv", "r")
    data = list(csv.reader(file, delimiter=","))
    print("Нужно купить:")
    for i in data:
        print(f"{i[0]} - {i[1]} шт. за {i[2]} руб.")
    print(f"Итоговая сумма: {sum([int(i[1]) * int(i[2]) for i in data])} руб.")
    file.close()
p3()
