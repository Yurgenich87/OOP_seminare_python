from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox as mb
from tkinter.ttk import Notebook
from HW_1.VendingMachine.Product.CreateProducts import names_string, itemMachin


class Window:
    """Создание интерфейса"""
    def __init__(self, width=400, height=600, title="VendingMachine", resizable=(False, False),
           icon="C:\\Users\\Yurgenich\\Desktop\\PYTHON\\OOP_seminare_python\\HW_1\\VendingMachine\\image\\vending.ico"):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+200+200")
        self.root.resizable(resizable[0], resizable[1])
        if icon:
            self.root.iconbitmap(icon)

                # Создание виджетов на вкладке "VendingMachine"
        self.top_frame = LabelFrame(self.root, borderwidth=3, width=100,
                                    height=200, text="Выберите продукт", labelanchor="n", relief="ridge")
        self.bottom_frame = LabelFrame(self.root, borderwidth=3, width=400,
                                       height=200, text="Внесите сумму", labelanchor="n", relief="ridge")

        self.exit_frame = LabelFrame(self.root, borderwidth=0, width=400,
                                     height=200, text="", labelanchor="n", relief="ridge")

        # Параметры поля выбора продукта
        self.product_names = names_string
        self.selected_item = StringVar()
        self.combobox = Combobox(self.top_frame, values=self.product_names, state="readonly",
                                 textvariable=self.selected_item)
        self.combobox.bind("<<ComboboxSelected>>", self.combo_selected)

        # Создание переменной цены продукта
        self.prod_price = StringVar(value=f"Цена: {0} руб.")
        self.message = Message(self.top_frame, textvariable=self.prod_price, width=100)

        # Создание поля покупки продукта
        self.money_entry = Entry(self.bottom_frame)
        self.buy_icon = PhotoImage(file="C:\\Users\\Yurgenich\\Desktop\\PYTHON\\OOP_seminare_python"
                                        "\\HW_1\\VendingMachine\image\\pay.png").subsample(10, 10)
        self.buy_button = Button(self.bottom_frame, text="Купить", image=self.buy_icon, compound="left",
                                 command=self.buy_product)
        # Кнопка "EXIT"
        self.exit_bottom = Button(self.exit_frame, text="EXIT", width=20, bg="#E4DFEC",\
                                 command=self.exit)


    def draw_widgets(self):
        """Добавление виджетов"""
        # Рамка выбора продукта
        self.top_frame.pack(pady=30)

        # Рамка покупки продукта
        self.bottom_frame.pack()

        # Поле выбора продукта
        self.combobox.pack(padx=10, pady=20, side=LEFT)

        # Поле цены продукта
        self.message.pack(side=RIGHT)

        # Поле ввода денег
        self.money_entry.pack(pady=10, padx=10)

        # Кнопка покупки
        self.buy_button.pack(padx=10)

        # Кнопка "exit"
        self.exit_frame.pack(pady=30)
        self.exit_bottom.pack(side=BOTTOM, pady=20, padx=10)


    def draw_menu(self):
        menu_bar = Menu(self.root)

        # pay_menu = Menu(menu_bar, tearoff=0)
        # pay_menu.add_command(lable="Магазин", command=self.pay_file)
        exit_menu = Menu(menu_bar, tearoff=0)
        exit_menu = Menu(lable="Выйти", command=self.exit)


    def combo_selected(self, event=None):
        """Метод определения какой, товар выбрал Пользователь"""
        selected_item = self.combobox.get()
        print("Выбрано:", selected_item)

        # Изменение цены товара, в зависимости от выбора пользователя
        for prod in itemMachin.get_prod_all():
            if prod.name == selected_item:
                self.prod_price.set(f"Цена: {prod.price} руб.")
                print(self.prod_price.get())
                self.message.configure(text=f"Цена: {prod.price} руб.")
                break

    def buy_product(self):
        """Отображает всплывающее меню после внесения суммы"""
        money = self.money_entry.get()
        selected_item = self.combobox.get()
        for prod in itemMachin.get_prod_all():
            if prod.name == selected_item:
                if float(money) == prod.price:
                    mb.showinfo("Покупка", f"Вы купили {prod.name}")
                elif float(money) > prod.price:
                    mb.showinfo("Покупка", f"Вы купили\nВаша сдача: {float(money) - prod.price} руб.")
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




