import os
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter.filedialog import asksaveasfilename


# # styles
# style = Style()
# style.configure("GRN.TLabel", background="#ACF059")
# style.configure("GRN.TFrame", background="#ACF059")
# style.configure("BLK.TFrame", background="#595959")

class Periods(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.dir_name = '...'
        self.file_new = '...'
        self.todo = False
        self.initUI()

    def initUI(self):
        def insert_txt(*args):
            self.quarter = var.get()
            self.year = combo.get()
            txt = periods[self.quarter] + ' ' + self.year
            lbPeriod['text'] = txt

        self.parent.title("Выбор параметров отчета")
        self.pack(fill=BOTH, expand=True)

        # ------------------------------------------------
        # Отчетный год
        yearFrame = Frame(self, height=60, bg='')
        yearFrame.pack(side='top', fill='x')

        lbYear = Label(yearFrame, text="Отчетный год:", width=16, anchor=W)
        lbYear.pack(side=LEFT, padx=5, pady=5)

        combo = Combobox(yearFrame, width=5)
        combo['values'] = (2020, 2021, 2022, 2023, 2024)
        combo.pack(side=LEFT, padx=5)

        combo.current(0)  # вариант по умолчанию
        self.year = combo.get()

        # ------------------------------------------------
        # Отчетный квартал
        quarterFrame = Frame(self, height=40, bg='')
        quarterFrame.pack(side='top', fill=X, ipady=5)

        lbQuarter = Label(quarterFrame, text="Отчетный квартал:", width=16, anchor=W)
        lbQuarter.pack(side=LEFT, anchor=N, padx=5)

        periods = {0: 'Год',
                   1: '1-ый квартал',
                   2: '2-ой квартал',
                   3: '3-ий квартал'}

        # выбора периода
        var = IntVar()
        var.set(1)  # значение по умолчанию
        R1 = Radiobutton(quarterFrame, text=periods[1], variable=var,
                         value=1, width=12, anchor=W, command=insert_txt)
        R1.pack(anchor=W, padx=5)
        R2 = Radiobutton(quarterFrame, text=periods[2], variable=var,
                         value=2, width=12, anchor=W, command=insert_txt)
        R2.pack(anchor=W, padx=5)
        R3 = Radiobutton(quarterFrame, text=periods[3], variable=var,
                         value=3, width=12, anchor=W, command=insert_txt)
        R3.pack(anchor=W, padx=5)
        R4 = Radiobutton(quarterFrame, text=periods[0], variable=var,
                         value=0, width=12, anchor=W, command=insert_txt)
        R4.pack(anchor=W, padx=5)

        self.quarter = var.get()
        # ------------------------------------------------
        # Итоги выбора периода
        infoFrame = Frame(self, height=40, bg='')
        infoFrame.pack(side='top', fill='x')

        lbInfo = Label(infoFrame, text="Выбран период:", width=16, anchor=W)
        lbInfo.pack(side=LEFT, anchor=N, padx=5, pady=10)

        # Стиль шрифта
        style = ttk.Style()
        style.configure('Info.TLabel', foreground='red', font=("Calibri", 11, "bold"))

        lbPeriod = ttk.Label(infoFrame, text="", width=30, anchor=W, style='Info.TLabel')
        lbPeriod.pack(side=LEFT, anchor=N, padx=5, pady=10)

        # Значения по умолчанию
        insert_txt()
        combo.bind("<<ComboboxSelected>>", insert_txt)

        # Выбор файла
        fileFrame = Frame(self, height=40, bg='')
        fileFrame.pack(side='top', fill='x')

        def file_dir():
            """ имя нового файла и путь к файлам отчетности"""
            self.file_new_name = asksaveasfilename(
                title="Имя нового файла отчетности...",
                filetypes=(("xlsx files", "*.xlsx"), ("All files", "*.*")))
            # Добавляем расширение файла
            if self.file_new_name.endswith('.xlsx'):
                pass
            else:
                self.file_new_name += '.xlsx'
            # путь к файлу
            self.dir_name = os.path.dirname(self.file_new_name)
            lbPath['text'] = self.dir_name
            # имя файла
            self.file_new = os.path.basename(self.file_new_name)
            lbFile['text'] = self.file_new

        buttFile = Button(fileFrame, text="Выбрать файлы...", width=16, anchor=W, command=file_dir)
        buttFile.grid(column=0, row=0, sticky=W, padx=5, pady=5)

        lbPathInfo = Label(fileFrame, text="Имя файла-xbrl:", width=16, anchor=W)
        lbPathInfo.grid(column=0, row=1, sticky=NW, padx=5)

        lbPathInfo = Label(fileFrame, text="Путь к файлам:", width=16, anchor=W)
        lbPathInfo.grid(column=0, row=2, sticky=NW, padx=5, pady=5)

        lbFile = Label(fileFrame, text=self.file_new, width=30, anchor=W)
        lbFile.grid(column=1, row=1, sticky=NW)

        lbPath = Label(fileFrame, text=self.dir_name, width=30, anchor=NW, height=3,
                       justify=LEFT, wraplength=200)
        lbPath.grid(column=1, row=2, rowspan=3, sticky=W, pady=5)

        # ------------------------------------------------
        # Кнопки выхода
        def doClose():
            self.todo = False
            print ('Close')
            self.parent.quit()
            # self.parent.destroy()
            quit()
        def doOK():
            self.todo = True
            print ('OK')
            # self.parent.quit()
            self.parent.destroy()

        closeButton = Button(self, text="Close", height=1, width=10, command=doClose)
        closeButton.pack(side=RIGHT, anchor=S, padx=5, pady=5)
        okButton = Button(self, text="OK", height=1, width=10, command=doOK)
        okButton.pack(side=RIGHT, anchor=S, padx=0, pady=5)




# ======================================================================
def main():
    root_period = Tk()
    root_period.geometry("360x350+600+300")
    period_set = Periods(root_period)
    root_period.mainloop()

    # проверяем как закрыто окно и выбран ли файл
    # если файл не выбран, то повторяем цикл
    try:
        if period_set.todo:
            if period_set.dir_name != "...":
                print(period_set.quarter, period_set.year)
                print(period_set.dir_name)
                print(period_set.file_new)
            else:
                print(f'Не выбраны файлы для формирования отчета!\n'
                      f'Попробуйте еще раз.')
                main()
        else:
            sys.exit()
    except AttributeError: # окно выбора закрыто не кнопкой
        sys.exit()
    except Exception as e:
        print(f'{e}')
        sys.exit()

    return period_set.year, \
           period_set.quarter, \
           period_set.dir_name, \
           period_set.file_new

if __name__ == '__main__':
   pass
