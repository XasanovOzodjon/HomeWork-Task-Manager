#kerakli kutubxonalar import qilish!
from os import system
import sys


#Global o'zgaruvchi va Listlar
Tasks = []
menu = """
========= Menu =========
1. Task qo'shish
2. Tasklarni ko'rish
3. Taskni o'chirish
4. Taskni yangilash
5. Chiqish
"""
#Foydalanuvchi 1 ni tanlaganda Task yaratuvchi Fungsiya
def add_task() -> None:
    """Ushbu fungsiya Yangi Task yaratish uchun. 
    !Task nomi 20 ta belgidan oshmasligi kerak
    !Agar hech narsa kiritmasdan Enter bosa kiritish yakunlanadi
    """
    global Tasks
    system("Clear")
    i = len(Tasks)+1
    print("Task qo'shishni to'xtatish uchun Enter ni bosing")
    
    while True:
        task = input(f"{i}-Task: ")
        
        if len(task) > 20:
            print("Task nomi 20 ta belgidan oshmasligi kerak!\n")
        else:
            if task == "":
                break
            else:
                Tasks.append(task)
                i += 1
                
    Tasks.sort()
        


def print_todos() -> None:
    """Ushbu fungsiya Mavjut Tasklarni chiqarish uchun. 
    !Agar Tasklar mavjud bulmasa "Sizda Hali Tasklar mavjud emas" yozuvini chiqaradi.
    """
    system("Clear")
    print("========= Tasks =========")
    
    if len(Tasks) == 0:
        print("Sizda Hali Tasklar mavjud emas")
               
    else:
        for task in Tasks:
            print(f"{Tasks.index(task) + 1} - {task}")


def delete_task() -> None:
    """Ushbu fungsiya Tasklarni o'chirish uchun. 
    !O'chirishni 2 xil turi mavjud. Yani 1 ta taskni o'chirish yoki barchasini
    !Agar foydalanuvchi o'chirmoqchi bulsa capcha dan o'tishi lozim
    """    

    global Tasks
    system("Clear")
    
    while True:
        print("========= Tasks =========")
        print("1 - 1ta Taskni o'chirish")
        print("2 - Barcha taskni o'chirish")
        print("3 - Bosh menuga qaytish")
        choice = input(">>>")
        
        if choice == "1":
            print_todos()
            index = int(input("\nO'chirmoqchi bulgan Task Raqamini kiriting: "))
            
            if index > len(Tasks) or index <= 0:
                system("Clear")
                print("Xato index kiritdingiz!")
                continue
            else:
                capcha(0, index)
                Tasks.pop(index - 1)
                system("Clear")
                print("Task o'chirildi!\n")
                
        elif choice == "2":
            capcha(1)
            Tasks.clear()
            system("Clear")
            print(" Barcha Tasklar o'chirildi!\n")
            
        elif choice == "3":
            main()
            
        else:
            system("Clear")
            print("Xatolik! Iltimos qaytatan harakat qilib ko'ring")         

            
def capcha(x, y = 0) -> None:
    """Ushbu fungsiya Tasklarni o'chirish ni tastiqlash uchun. 
    ! Foydalanuvchi o'chirishni tastiqlash uchun Xa ni tanlashi kerak
    !Bu parametrlar foydalanauvchi 1 ta taskni o'chirayaptimi yoki barchasini aniqlash uchun
    """    
    
    if x == 0:
        system("clear")
        choice = input(f"Siz rostan ham {y} raqamli Taskni o'chirmoqchimisiz\n(Xa/Yo'q):")
    else:
        choice = input(f"Siz rostan ham Barcha Tasklarni O'chirmoqchimisiz\n(Xa/Yo'q):")
    
    if choice.lower() == "yo'q":
        delete_task()
    if choice.lower() == "xa":
        return None
    else:
        capcha(x,y)
    
        
        
        
def update_task() -> None:
    """Ushbu fungsiya Tasklarni Nomini yangilash uchun. 
    ! Foydalanuvchi Nomini almashtirmoqchi bo'lgan taskni tanlaydi
    """
    global Tasks
    print_todos()
    index = int(input("\nQaysi taskni Nomini o'zgartirmoqchisiz: "))
    
    if index > len(Tasks) or index <= 0:
        system("Clear")
        print("Xato index kiritdingiz!")
        update_task()
    
    else:
        new_name = input(f"{index}-Task uchun Yangi nom kiriting: ")
        if len(new_name) > 20:
            print("Task nomi 20 ta belgidan oshmasligi kerak!\n")
        else:
            if new_name == "":
                print("Task nomi bo'sh bo'lmasligi kerak\n")
            else:
                Tasks[index-1] = new_name
                system("Clear")
                print(f"{index}-Task nomi: {new_name}ga O'zgartirildi!\n")



def main() -> None:
    """Dasturimizni asosiy kodi shu yerda yoziladi"""
    system("Clear")
    while True:
        print(menu)
        choice = input(">>>")

        if choice == "1":
            add_task()
        elif choice == "2":
            print_todos()
            input()
            system("clear")
        elif choice ==  "3":
            delete_task()
        elif choice == "4":
            update_task()
        elif choice == "5":
            system("Clear")
            sys.exit()
        else:
            system("Clear")
            print("Xatolik! Iltimos qaytatan harakat qilib ko'ring")

        
main()
