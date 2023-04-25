import json
from tkinter import *
from tkinter.ttk import Label, Combobox
from tkinter import messagebox as mb

from HW_1.CreateProducts import names_string, itemMachin, names
from HW_1.Product.Products import HotDrink, Product
from HW_1.Product.VandingMashine import VendingMachine


class Window:
    """Создание интерфейса"""
    def __init__(self, width=400, height=500, title="VendingMachine", resizable=(False, False),
                 icon="C:/Users/Yurgenich/Desktop/PYTHON/OOP_seminare_python/HW_1/image/vending.ico"):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+200+200")
        self.root.resizable(resizable[0], resizable[1])
        if icon:
            self.root.iconbitmap(icon)
        self.product_names = names_string
        # flat, groove, raised, ridge, solid, or sunken
        self.top_frame = LabelFrame(self.root, borderwidth=3, width=400,
                                    height=250, text="Выберите продукт", labelanchor="n", relief="ridge")

        self.top_frame.pack(pady=30)
        self.bottom_frame = LabelFrame(self.root, borderwidth=3, width=400,
                                       height=250, text="Внесите сумму", labelanchor="n", relief="ridge")
        self.bottom_frame.pack()

        self.selected_item = StringVar()
        self.combobox = Combobox(self.top_frame, values=self.product_names, state="readonly",
                                 textvariable=self.selected_item)
        self.combobox.pack(padx=10, pady=20, side=LEFT)
        self.combobox.bind("<<ComboboxSelected>>", self.combo_selected)

        # Отображение цены продукта
        self.prod_price = StringVar(value=f"Цена: {0} руб.")

        # Поле покупки продукта
        self.money_entry = Entry(self.bottom_frame)
        self.money_entry.pack(pady=10)

        self.buy_button = Button(self.bottom_frame, text="Купить", command=self.buy_product, image="HW_1/image/pay.ico")
        self.buy_button.pack()
        # Создание кнопки "EXIT"
        Button(self.bottom_frame, text="EXIT", width=20, bg="#E4DFEC", command=self.exit).pack(side=BOTTOM, pady=20, padx=10)

    def draw_widgets(self):
        """Добавление виджетов"""
        # img = PhotoImage(file="HW_1/image/pay.ico")
        # self.icon_label = Label(self.top_frame, image=img)
        # self.icon_label.image = img  # сохраняем ссылку на изображение, чтобы избежать сборки мусора
        # self.icon_label.pack(side=LEFT, padx=10)

        Message(self.top_frame, textvariable=self.prod_price, width=100).pack(side=LEFT)



    def combo_selected(self, event=None):
        """Метод определения какой, товар выбрал Пользователь"""
        selected_item = self.combobox.get()
        print("Выбрано:", selected_item)

        for prod in itemMachin.get_prod_all():
            if prod.name == selected_item:
                self.prod_price.set(f"Цена: {prod.price} руб.")
                print(self.prod_price.get())
                self.message.configure(text=f"Цена: {prod.price} руб.")
                break

    def buy_product(self):
        money = self.money_entry.get()
        selected_item = self.combobox.get()
        for prod in itemMachin.get_prod_all():
            if prod.name == selected_item:
                if float(money) >= prod.price:
                    mb.showinfo("Покупка", f"Вы купили {prod.name}")
                else:
                    mb.showerror("Ошибка", "Недостаточно денег")
                break

    def change_label(self):
        self.label.configure(text="Оплачено", bg="#66FF99")

    def show_parameters(self):
        state = ("inactive", "active")
        text = ""

        for name, var in self.parameters:
            text += f"{name} is {state[var.get()]}\n"
        mb.showinfo("Parameters", text)

    def check_bags(self):
        text = ""
        if self.cofe_var.get():
            text += "Вы купили кофе"
        else:
            text += "Вы не купили кофе"

    def exit(self):
        """Определение параметров выхода"""
        choice = mb.askyesno("Выход", "Хотите выйти?")
        if choice:
            self.root.destroy()

    def run(self):
        """Мотод запуска программы"""
        self.draw_widgets()
        self.root.mainloop()

    def create_child(self, width, height, title="VendingMachine", resizable=(False, False), icon=None):
        """Создание дочернего окна"""
        ChildWindow(self.root, width, height, title, resizable, icon)


class ChildWindow:
    """Класс дочернего окна"""

    def __init__(self, parent, width, height, title="Child", resizable=(False, False), icon=None):
        self.root = Toplevel(parent)
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+200+200")
        self.root.resizable(resizable[0], resizable[1])
        if icon:
            self.root.iconbitmap(icon)

        self.root.grab_set()

    def grab_focus(self):
        self.root.grab_set()
        self.root.focus_set()
        self.root.wait_window()
