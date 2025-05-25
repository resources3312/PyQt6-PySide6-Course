"""

    ПРАКТИЧЕСКОЕ ПОСОБИЕ ПО ОСНОВНЫМ ЭЛЕМЕНТАМ ФРЕЙМВОРКА PySide6
    
    Автор: Дич А.А

    Дата создания: 25-05-2025

    Описание:

        Данное пособие прежде всего предназначено для студентов владеющих
        базовыми концепциями языка программирования Python, и желающих 
        расширить свои навыки владения данным языком, посредством изучения
        крупных фреймворков, таких как PySide6. Тем кто сталкивается с данным
        фреймворком впервые рекомендуется осваивать материал в том порядке,
        который установлен внутри пособия, потому что в противном случае
        могут возникнуть проблемы с пониманием написанного 

        Все описанные в данном пособии объекты фреймворка имеют следующую
        структуру:
            
            Название объекта
            |
            |— Описание объекта
            |
            |— Подробная схема объекта, с возможными ссылками на предыдущие объекты
            |
            |— Тело объекта с поясняющими комментариями

        В заключение можно сказать, что даже разработчики данного фреймворка в полной
        мере не знают всех аспектов его устройства, поэтому при использовании данного
        материала в образовательных целях, рекомендуется дополнять полученные знания
        информацией из сторонних источников для формирования собственного взгляда на
        изученный материал

        Копирование, распространение и любой другой вид использования данного материала
        разрешен только при указании авторства
        
"""
from sys import argv
from time import sleep
from PySide6.QtCore import Qt, QDate
from PySide6.QtGui import QFont, QIcon, QAction, QStandardItem, QStandardItemModel
from PySide6.QtWidgets import (

QApplication, QMainWindow, QWidget,


QHBoxLayout, QVBoxLayout,  QGridLayout, QFormLayout, 


QLabel, QLineEdit, QPushButton, QSpinBox, QDoubleSpinBox,

QCheckBox, QRadioButton, QListWidget, QScrollBar, 

QComboBox, QSlider, QTimeEdit, QDateEdit, 

QDateTimeEdit, QCalendarWidget, QProgressBar, QFontComboBox,

QTextEdit, QPlainTextEdit, QTextBrowser, QSplitter,

QMdiArea, QMdiSubWindow, QDockWidget, QToolBox, QLCDNumber, QDial,

QFileDialog, QInputDialog, QFontDialog, QDialog, 

QMessageBox,

QTabWidget, QTabBar,

QTableView, QAbstractItemView,
QHeaderView
)



class BasicWindow(QMainWindow):
    def __init__(self):
        """
        Описание:
            
            BasicWindow представляет собой простейшее приложение
            c графическим интерфейсом PySide6, являясь пустым окном
            с установленным названием, размером и иконкой.
            
            Данный класс имеет следующую структуру:

            Конструктор (__init__(self))
            |            
            |— Метод super().__init__() для инициализации 
            |  родительского класса QMainWindow
            |
            |— Метод setWindowTitle(title: str) для установки заголовка 
            |  окна
            |
            |— Метод resize(width: int, height: int) который служит 
            |  для установки начальных размеров окна, однако оставляет
            |  пользователю возможность масштабировать окно. Чтобы запретить
            |  пользователю масштабировать окно, следует вместо метода resize()
            |  использовать метод setFixedSize(width: int, height: int) с идентич-
            |  ными параметрами
            |
            |— Метод setWindowIcon(QIcon(icon_path: str)) используется для установки
            |  иконки окна, в качестве параметров принимает обьект QIcon() с указанным
            |  путем до изображения что было выбрано в качестве иконки. Рекомендуется
            |  использовать изображения в форматах ico или png разрешение которых не 
            |  превышает 256x256 пикселей
            |
        """
        super().__init__() # Инициализируем родительский класс QMainWindow
        self.setWindowTitle("Empty Window") # Устанавливаем заголовок окна
        self.resize(750, 750) # Указываем размер текущего окна с возможностью масштабирования
        self.setWindowIcon(QIcon("./qt.ico")) # Устанавливаем иконку текущего окна 


class QHBoxLayoutExample(QMainWindow):
    def __init__(self):
        """
        Описание
            QHBoxLayoutExample представляет собой приложение с графическим интерфейсом
            на PySide6. В данном приложении мы рассмотрим принцип работы одного из так
            называемых 'классов макетов'. Вышеупомянутые объекты используются для
            позиционирования элементов внутри родительского виджета, а также различаются
            по типам позицизионирования. В качестве примера можно привести класс QHBoxLayout

            QHBoxLayout — является одним из макетов доступных в рамках фреймворка
            PySide6. Как можно понять из названия отличается от прочих макетов горизонтальным
            позиционированием элементов т.е дочерние элементы распределяются по абстрактной 
            горизонтальной линии внутри родительского виджета



        Структура класса QHBoxLayoutExample
        |
        |————Конструктор(__init__(self))
             |
             |— Метод super().__init__() для инициализации
             |  родительского класса QMainWindow
             |
             |— Метод setWindowTitle(title: str) См.описание BasicWindow
             |  
             |— Метод setFixedSize(width: int, height: int) См.описание BasicWindow
             |
             |— Метод setWindowIcon(QIcon(icon_path: str)) См.описание BasicWindow
             |
             |— Метод addWidget(widget: QWidget) экземпляра класса QHBoxLayout, служит
             |  добавления элемента в родительский макет
             |
             |— Метод addWidget(widget: QWidget) экземпляра класса QHBoxLayout, служит
             |  добавления элемента в родительский макет
             |
             |— Метод addWidget(widget: QWidget) экземпляра класса QHBoxLayout, служит
             |  добавления элемента в родительский макет
             |
             |— Метод addWidget(widget: QWidget) экземпляра класса QHBoxLayout, служит
             |  добавления элемента в родительский макет
             |
             |— Метод setLayout(layout: QHBoxLayout) класса QWidget. Используется для установки макета для
             |  и принимает в качестве значения обьект ранее упомянутого макета, в нашем
             |  случае QVBoxLayout
             |
             |— Метод setCentralWidget(widget: QWidget) класса QMainWindow. С помощью него мы имеем возможность
             |  установить главный (родительский) виджет нашего окна. В качестве параметров принимает
             |  объект QWidget

        """
        super().__init__() # Инициализируем родительский класс QMainWindow
        self.setWindowTitle("QHBoxLayout Example") # Устанавливаем заголовок текущего окна
        self.setWindowIcon(QIcon("./qt.ico")) # Устанавливаем иконку текущего окна c помощью класса QIcon
        self.setFixedSize(500, 50) # Устанавливаем фиксированный размер текущего окна
        
        self.widget = QWidget() # Инициализируем объект QWidget
        self.hBoxLayout = QHBoxLayout() # Инициализируем объект QHBoxLayout


        self.hBoxLayout.addWidget(QPushButton("Button 0")) # Добавляем в макет экземпляр класса QPushButton
        self.hBoxLayout.addWidget(QPushButton("Button 1")) # Добавляем в макет экземпляр класса QPushButton
        self.hBoxLayout.addWidget(QPushButton("Button 2")) # Добавляем в макет экземпляр класса QPushButton
        self.hBoxLayout.addWidget(QPushButton("Button 3")) # Добавляем в макет экземпляр класса QPushButton 
        self.hBoxLayout.addWidget(QPushButton("Button 4")) # Добавляем в макет экземпляр класса QPushButton

        self.widget.setLayout(self.hBoxLayout) # Устанавливаем hBoxLayout в качестве макета родительского виджета с помощью метода setLayout()
        self.setCentralWidget(self.widget) # Устанавливаем widget в качестве главного виджета экземпляра класса QMainWindow

class QVBoxLayoutExample(QMainWindow):
    """
        Описание

            QVBoxLayoutExample представляет собой приложение с графическим интерфейсом
            на PySide6. Демонстрирует принцип работы макета QVBoxLayout

            QVBoxLayout — является одним из макетов доступных в рамках фреймворка
            PySide6. Антогоничен по функционалу макету QHBoxLayout, осуществляя позиционирование
            элементов по абстрактной вертикальной линии внутри родительского виджета

        Пример использования данного макета, а также структура класса QVBoxLayoutExample
        представлены нижe

        Структура класса QVBoxLayoutExample
        |
        |————Конструктор(__init__(self))
             |
             |— Метод super().__init__() для инициализации
             |  родительского класса QMainWindow
             |
             |— Метод setWindowTitle(title: str) См.описание BasicWindow
             |  
             |— Метод setFixedSize(width: int, height: int) См.описание BasicWindow
             |
             |— Метод setWindowIcon(QIcon(icon_path: str)) См.описание BasicWindow
             |
             |— Метод addWidget(widget: QWidget) экземпляра класса QVBoxLayout, служит
             |  добавления элемента в родительский макет
             |
             |— Метод addWidget(widget: QWidget) экземпляра класса QVBoxLayout, служит
             |  добавления элемента в родительский макет
             |
             |— Метод addWidget(widget: QWidget) экземпляра класса QVBoxLayout, служит
             |  добавления элемента в родительский макет
             |
             |— Метод setLayout(layout: QHBoxLayout) класса QWidget. Используется для установки макета для
             |  и принимает в качестве значения обьект ранее упомянутого макета, в нашем
             |  случае QVBoxLayout
             |
             |— Метод setCentralWidget(widget: QWidget) класса QMainWindow. С помощью него мы имеем возможность
             |  установить главный (родительский) виджет нашего окна. В качестве параметров принимает
             |  объект QWidget

        """
    def __init__(self):
        super().__init__() # Инициализируем родительский класс QMainWindow
        self.setWindowTitle("QVBoxLayout Example") # Устанавливаем заголовок текущего окна
        self.setWindowIcon(QIcon("./qt.ico")) # Устанавливаем иконку текущего окна c помощью класса QIcon
        self.setFixedSize(350, 500) # Устанавливаем фиксированный размер текущего окна
         
        self.widget = QWidget() # Инициализируем объект QWidget
        self.vBoxLayout = QVBoxLayout() # Инициализируем объект QVBoxLayout

        self.vBoxLayout.addWidget(QPushButton("Button 0")) # Добавляем в макет экземпляр класса QPushButton
        self.vBoxLayout.addWidget(QPushButton("Button 1")) # Добавляем в макет экземпляр класса QPushButton
        self.vBoxLayout.addWidget(QPushButton("Button 2")) # Добавляем в макет экземпляр класса QPushButton
        
        self.widget.setLayout(self.vBoxLayout) # Устанавливаем vBoxLayout в качестве макета родительского виджета с помощью метода setLayout()
        self.setCentralWidget(self.widget) # Устанавливаем widget в качестве главного виджета экземпляра класса QMainWindow


class QGridLayoutExample(QMainWindow):
    """
        Описание
            
            QGridLayoutExample представляет собой приложение с графическим интерфейсом
            на PySide6. Предназначено для демонстрации использования макета QGridLayout
            
            QGridLayout — представляет собой один из макетов доступных в рамках фреймворка
            PySide6. Используется для позиционирования виджетов внутри родительского виджета
            по абстрактной сетке.

        Пример использования данного макета и структура класса QGridLayoutExample
        представлены ниже

        
        Структура класса QGridLayoutExample
        |
        |————Конструктор(__init__(self))
             |
             |— Метод super().__init__() для инициализации
             |  родительского класса QMainWindow
             |
             |— Метод setWindowTitle(title: str) См.описание BasicWindow
             |  
             |— Метод setFixedSize(width: int, height: int) См.описание BasicWindow
             |
             |— Метод setWindowIcon(QIcon(icon_path: str)) См.описание BasicWindow
             |
             |— Метод addWidget(widget: QWidget, row: int, column: int) экземпляра класса QGridLayout, служит
             |  добавления элемента в родительский макет. В рамках макета QGridLayout, также принимает в качестве
             |  значений индексы строки и столбца куда должен быть инкапсулирован виджет
             |
             |— Метод addWidget(widget: QWidget, row: int, column: int) экземпляра класса QGridLayout, служит
             |  добавления элемента в родительский макет. В рамках макета QGridLayout, также принимает в качестве
             |  значений индексы строки и столбца куда должен быть инкапсулирован виджет
             |
             |— Метод addWidget(widget: QWidget, row: int, column: int) экземпляра класса QGridLayout, служит
             |  добавления элемента в родительский макет. В рамках макета QGridLayout, также принимает в качестве
             |  значений индексы строки и столбца куда должен быть инкапсулирован виджет
             |
             |— Метод addWidget(widget: QWidget, row: int, column: int) экземпляра класса QGridLayout, служит
             |  добавления элемента в родительский макет. В рамках макета QGridLayout, также принимает в качестве
             |  значений индексы строки и столбца куда должен быть инкапсулирован виджет
             |
             |— Метод setLayout(layout: QHBoxLayout) класса QWidget. Используется для установки макета для
             |  и принимает в качестве значения обьект ранее упомянутого макета, в нашем
             |  случае QVBoxLayout
             |
             |— Метод setCentralWidget(widget: QWidget) класса QMainWindow. С помощью него мы имеем возможность
             |  установить главный (родительский) виджет нашего окна. В качестве параметров принимает
             |  объект QWidget

        """
    def __init__(self):
        super().__init__() # Инициализируем родительский класс QMainWindow
        self.setWindowTitle("QGridLayout Example") # Устанавливаем заголовок текущего окна
        self.setWindowIcon(QIcon("./qt.ico")) # Устанавливаем иконку текущего окна c помощью класса QIcon
        self.setFixedSize(500, 500) # Устанавливаем фиксированный размер текущего окна
        
        self.widget = QWidget() # Инициализируем объект QWidget
        self.gridLayout = QGridLayout() # Инициализируем объект QGridLayout

        self.gridLayout.addWidget(QPushButton("R0-C0"), 0, 0) # Добавляем в макет экземпляр класса QPushButton
        self.gridLayout.addWidget(QPushButton("R1-C1"), 1, 1) # Добавляем в макет экземпляр класса QPushButton
        self.gridLayout.addWidget(QPushButton("R0-C1"), 0, 1) # Добавляем в макет экземпляр класса QPushButton
        self.gridLayout.addWidget(QPushButton("R2-C0"), 2, 0) # Добавляем в макет экземпляр класса QPushButton

        self.widget.setLayout(self.gridLayout) # Устанавливаем gridLayout в качестве макета родительского виджета с помощью метода setLayout()
        self.setCentralWidget(self.widget) # Устанавливаем widget в качестве главного виджета экземпляра класса QMainWindow


class QFormLayoutExample(QMainWindow):
    """
        Описание
            
            QFormLayoutExample представляет собой приложение с графическим интерфейсом
            на PySide6. В данном приложении мы рассмотрим принцип работы одного из базовых
            макетов — QFormLayout 
            
            QFormLayout — является одним из макетов доступных в рамках фреймворка
            PySide6. Как можно понять из названия представляет собой макет который
            рекомендуется к использованию при создании форм например для регистрации 
            или указания личных данных пользователя

        Пример использования данного макета, а также структура класса QHBoxLayoutExample
        представлены ниже



        Структура класса QFormLayoutExample
        |
        |————Конструктор(__init__(self))
             |
             |— Метод super().__init__() для инициализации
             |  родительского класса QMainWindow
             |
             |— Метод setWindowTitle(title: str) См.описание BasicWindow
             |  
             |— Метод setFixedSize(width: int, height: int) См.описание BasicWindow
             |
             |— Метод setWindowIcon(QIcon(icon_path: str)) См.описание BasicWindow
             |
             |— Метод addRow(title: str, widget: QWidget) экземпляра класса QHBoxLayout, служит
             |  добавления элемента вместе с его подписью в родительский макет
             |
             |— Метод addRow(title: str, widget: QWidget) экземпляра класса QHBoxLayout, служит
             |  добавления элемента, а также его подписи в родительский макет
             |
             |— Метод addRow(title: str, widget: QWidget) экземпляра класса QFormLayout, служит
             |  добавления элемента и его подписи в родительский макет
             |
             |— Метод addRow(title: str, widget: QWidget) экземпляра класса QFormLayout, служит
             |  добавления элемента и его подписи в родительский макет
             |
             |— Метод setLayout(layout: QHBoxLayout) класса QWidget. Используется для установки макета для
             |  и принимает в качестве значения обьект макета QFormLayout
             |
             |
             |— Метод setCentralWidget(widget: QWidget) класса QMainWindow. С помощью него мы имеем возможность
             |  установить главный (родительский) виджет нашего окна. В качестве параметров принимает
             |  объект QWidget

        """
    def __init__(self):
        super().__init__() # Инициализируем родительский класс QMainWindow
        self.setWindowTitle("QGridLayout Example") # Устанавливаем заголовок текущего окна
        self.setWindowIcon(QIcon("./qt.ico")) # Устанавливаем иконку текущего окна c помощью класса QIcon
        self.setFixedSize(500, 145) # Устанавливаем фиксированный размер текущего окна
        
        self.widget = QWidget() # Инициализируем объект QWidget
        self.formLayout = QFormLayout() # Инициализируем объект QFormLayout 

        self.formLayout.addRow("Кнопка 1", QPushButton("Click me")) # Добавляем в макет экземпляр класса QPushButton
        self.formLayout.addRow("Кнопка 2", QPushButton("Click me")) # Добавляем в макет экземпляр класса QPushButton
        self.formLayout.addRow("Кнопка 3", QPushButton("Click me")) # Добавляем в макет экземпляр класса QPushButton
        self.formLayout.addRow("Кнопка 4", QPushButton("Click me")) # Добавляем в макет экземпляр класса QPushButton
        
        self.widget.setLayout(self.formLayout) # Устанавливаем formLayout в качестве макета родительского виджета с помощью метода setLayout()
        self.setCentralWidget(self.widget) # Устанавливаем widget в качестве главного виджета экземпляра класса QMainWindow

class WidgetList(QMainWindow):
    def __init__(self):
        """
        Описание:
            WidgetList представляет собой приложение с графическим интерфейсом
            на PySide6, и служит для демонстрации основных виджетов из модуля
            QWidgets. Однако теперь тем, как приступить к использованию данных
            объектов стоит привести их краткое описание:
                
                Объект виджета — класс в составе модуля QtWidgets,
                который служит для отображения отдельно взятых элементов
                графического интерфейса, основывается на графическом API
                используемой операционной системы, в нашем случае на WinAPI.
                Как можно понять из вышенаписанного, основное достоинство
                PySide6 на фоне оригинальных графических API — Кроссплатформенность

                Модуль QtWidgets — является частью фреймворка PySide6, служит для
                структурированного хранения совокупности обьектов виджетов, таких
                как QLabel, QLineEdit, QPushButton и т.д. По праву считается одной
                из важнейших частей графического фреймворка PySide6
            
        Ниже будет рассмотрена структура класса WidgetList:
        
        Структура класса WidgetList
        |
        |————Конструктор(__init__(self))    
        |            
        |— Метод super().__init__() для инициализации 
        |  родительского класса QMainWindow
        |
        |— Метод setWindowTitle(title: str) См.описание BasicWindow 
        |  
        |— Метод resize(width: int, height: int) См.описание BasicWindow
        |
        |— Метод setWindowIcon(QIcon(icon_path: str)) См.описание BasicWindow   
        |
        |— Атрибут widget служит для обьявления класса QWidget, что будет выступать
        |  в качестве главного виджета данного окна, и хранит в себе совокупность
        |  прочих дочерних обьектов приложения
        |
        |— Атрибут layout используется для обьявления класса QVBoxLayout, что выступает
        |  в качестве макета графического интерфейса, и помогает структурировать виджеты
        |  в рамках окна, или отдельной его области
        |
        |— Список widgets служит для хранения совокупности объектов модуля QWidgets,
        |  служит для дальнейшего добавления в макет layout с помощью цикла for 
        |
        |— Однострочный цикл for, иначе называемый генератором списков. Как было
        |  написанно ранее, служит для добавления в макет обьектов виджетов из
        |  списка widgets с помощью метода класса QVBoxLayout — addWidget()
        |
        |— Метод setLayout() класса QWidget. Используется для установки макета для
        |  и принимает в качестве значения обьект ранее упомянутого макета, в нашем
        |  случае QVBoxLayout
        |
        |— Метод setCentralWidget() класса QMainWindow. С помощью него мы имеем возможность
        |  установить главный (родительский) виджет нашего окна. В качестве параметров принимает
        |  объект QWidget  
        """
        super().__init__() # Инициализируем родительский класс QMainWindow
        self.setWindowTitle("QtWidgets list") # Устанавливаем заголовок окна
        self.setWindowIcon(QIcon("./qt.ico")) # Устанавливаем иконку текущего окна c помощью класса QIcon
        self.widget = QWidget() # Инициализируем объект QWidget
        self.layout = QVBoxLayout() # Инициализируем объект QVBoxLayout
        self.widgets = [QCheckBox,  # Инициализируем список виджетов
                        QPushButton,
                        QComboBox,
                        QDateEdit,
                        QDateTimeEdit,
                        QDial,
                        QDoubleSpinBox,
                        QFontComboBox,
                        QLabel,
                        QProgressBar,
                        QLCDNumber,
                        QLineEdit,
                        QRadioButton,
                        QSlider,
                        QSpinBox,
                        QTimeEdit]
        [self.layout.addWidget(i()) for i in self.widgets] # Добавляем обьекты виджетов в макет с помощью метода addWidget()
        self.widget.setLayout(self.layout) # Устанавливаем layout в качестве макета родительского виджета с помощью метода setLayout()
        self.setCentralWidget(self.widget) # Устанавливаем widget в качестве главного виджета экземпляра класса QMainWindow


class QLabelWidget(QMainWindow):
    """
    Описание
        QLabelWidget представляет собой приложение с графическим интерфейсом
        на PySide6, служит для демонстрации базового функционала класса QLabel,
        из модуля QWidgets. Вышеупомянутый класс QLabel, является одним из
        базовых виджетов в модуле QWidgets, предоставляет функционал вывода
        информации в текстовом виде, и ее стилизации, посредством изменения
        шрифта, размера или цвета надписи. Также стоит упомянуть что QLabel
        поддерживает вывод изображений, однако пока что мы опустим данную
        возможность, и на примере структуры класса QLabelWidget рассмотрим
        базовый пример использования данного виджета

        Структура класса QLabelWidget
        |
        |————Конструктор(__init__(self))
             |
             |— Метод super().__init__() для инициализации
             |  родительского класса QMainWindow
             |
             |— Метод setWindowTitle(title: str) См.описание BasicWindow
             |  
             |— Метод setFixedSize(width: int, height: int) См.описание BasicWindow
             |
             |— Метод setWindowIcon(QIcon(icon_path: str)) См.описание BasicWindow
             |
             |— Атрибут text экземпляра класса QLabel, что будет хранить
             |  демонстрационную надпись
             |
             |— Метод setFont(font: QFont) экземпляра класса QLabel. Служит для установки
             |  шрифта и размера надписи внутри экземпляра класса QLabel. В качестве параметра
             |  принимает экземпляр класса QFont(font: str, textSize: int) в параметрах которого
             |  мы имеем возможность выставить необходимые настройки
             |
             |— Метод setStyleSheet(style: str) экземпляра класса QLabel. Данный метод может вызвать
             |  особенный интерес у людей что имеют опыт в frontend разработке. Причина проста — данный
             |  метод предоставляет возможность стилизации виджетов использованием языка стилизации CSS,
             |  что может быть весьма полезно при создании современных интерфейсов, соотвествующих 
             |  эстетическим стандартам нашего времени. В нашем примере мы лишь изменим цвет виджета
             |  QLabel, однако стоит помнить, что метод setStyleSheet крайне мощный инструмент стилизации,
             |  и доступен не только в экземплярах класса QLabel
             |
             |— Метод setAlignment(flag: AlignmentFlag) экземпляра класса QLabel. Используется для
             |  выравнивания QLabel внутри родительского виджета, в качестве параметра принимает
             |  значение констант из подкласса AlignmentFlag, либо же, как в нашем случае, результат
             |  побитовой операции OR, операндами в которой являются значения констант подкласса AlignmentFlag
             |
             |— Метод setCentralWidget(widget: QWidget) См.описание WidgetList


    """
    def __init__(self):
        super().__init__() # Инициализируем родительский класс QMainWindow
        self.setWindowTitle("QLabel Widget") # Устанавливаем заголовок окна
        self.setFixedSize(800, 700) # Устанавливаем фиксированный размер текущего окна
        self.setWindowIcon(QIcon("./qt.ico")) # Устанавливаем иконку текущего окна
        
        self.text = QLabel("Пример использования QLabel") # Инициализируем экземпляр класса QLabel
        
        self.text.setFont(QFont("Direct", 20)) # Устанавливаем шрифт и размер надписи QLabel

        self.text.setStyleSheet("color: green;") # Устанавливаем цвет надписи QLabel
        
        self.text.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter) # Реализуем выравнивание экземпляра класса QLabel по центру родительского виджета
        
        self.setCentralWidget(self.text) # Устанавливаем родительский виджет
        

class QToolTipExample(QMainWindow):
    """
    Описание
        QToolTipExample представляет собой приложение с графическим интерфейсом
        на PySide6. Служит для демонстрации возможностей метода setToolTip. Однако
        перед тем, как переходить к структуре класса QToolTipExample, стоит
        рассмотреть что из себя представляет ToolTip в парадигме фреймворка PySide6.
        
        ToolTip — всплывающее окно небольшого размера, что всплывает при наведении
        на виджет, и содержит в себе строку с кратким описанием данного виджета. По
        праву считается важным инструментом при построении user-friendly графических
        интерфейсов


    Структура класса QToolTipExample:
    |
    |————Конструктор
         |
         |— Метод super().__init__() для инициализации
         |  родительского класса QMainWindow
         |
         |— Метод setWindowTitle(title: str) См.описание BasicWindow
         |  
         |— Метод setFixedSize(width: int, height: int) См.описание BasicWindow
         |
         |— Метод setWindowIcon(QIcon(icon_path: str)) См.описание BasicWindow
         |
         |— Атрибут widget См.описание WidgetList
         |
         |— Атрибут layout См.описание WidgetList
         |
         |— Атрибут title хранит экземпляр класса QLabel, с надписью 'Take me'
         |
         |— Атрибут pushButton хранит экземпляр класса QPushButton, с текстом 'Take me'
         |
         |— Метод setToolTip(text: str) экземпляра класса QLabel. Устанавливает подпись с описанием виджета что
         |  всплывает при наведении
         |
         |— Метод setToolTip(text: str) экземпляра класса QPushButton. Устанавливает подпись с описанием виджета что
         |  всплывает при наведении
         |
         |— Метод addWidget(widget: QWidget) экземпляра класса QVBoxLayout. См.описание WidgetList
         |
         |— Метод addWidget(widget: QWidget) экземпляра класса QVBoxLayout. См.описание WidgetList
         |
         |— Метод setLayout(layout: QVBoxLayout) экземпляра класса QWidget. См.описание WidgetList
         |
         |— Метод setCentralWidget(widget: QWidget) экземпляра класса QMainWindow. См.описание WidgetList
    """
    def __init__(self):
        super().__init__() # Инициализируем родительский класс QMainWindow
        self.setWindowTitle("QToolTip Demonstration") # Устанавливаем заголовок окна
        self.setFixedSize(300, 70) # Устанавливаем фиксированный размер текущего окна
        self.setWindowIcon(QIcon("./qt.ico")) # Устанавливаем иконку текущего окна
        self.widget = QWidget() # Инициализируем экземпляр класса QWidget
        self.layout = QVBoxLayout() # Инициализируем экземпляр класса QVBoxLayout
        self.textLabel = QLabel("Take me") # Инициализируем экземпляр класса QLabel
        self.pushButton = QPushButton("Take me") # Инициализируем экземпляр класса QLabel
        self.textLabel.setToolTip("Элемент QLabel") # Устанавливаем ToolTip экземпляра класса QLabel
        self.pushButton.setToolTip("Элемент QPushButton") # Устанавливаем ToolTip экземпляра класса QPushButton
        self.layout.addWidget(self.textLabel) # Добавляем атрибут textLabel в макет QVBoxLayout
        self.layout.addWidget(self.pushButton) # Добавляем атрибут pushButton в макет QVBoxLayout
        self.widget.setLayout(self.layout) # Устанавливаем layout в качестве макета родительского виджета
        self.setCentralWidget(self.widget) # Устанавливаем родительский виджет



class QLineEditWidget(QMainWindow):
    """
    Описание
        QLineEditWidget представляет собой приложение с графическим интерфейсом
        на PySide6, и служит для демонстрации базовых возможностей класса QLineEdit
        из модуля фрейморка PySide6 — QWidgets. Перед тем как продемонстрировать
        функционал данного объекта, стоит ввести ряд определений, который представлен
        ниже:
            
            QLineEdit — класс из модуля QWidgets, представляет собой однострочное поле
            ввода, с которым, без сомнений, множество раз встречался каждый пользователь
            компьютера. Идеально подходит для получения от пользователя таких значений как
            имя, пароль, адрес электронной почты, и прочих подобных им значений.

            
            EchoMode — в парадигме модуля QWidgets в общем, и класса QLineEdit частности,
            представляет собой атрибут хранящий значение одной из констант подкласса
            EchoMode. По данному значению определяет тип отображения введенных пользователем
            значений. Всего типов отображения введенных значений 4, и их краткое описание
            приложено ниже:
                
                Normal — тип отображения введенных значений, что установлен по умолчанию.
                Отображает данные в том виде, в котором они были введены, и не проводит
                над ними никаких метаморфоз

                NoEcho — весьма редкий тип отображения введенных значений, как можно
                понять из названия, поля с данным типов отображения не показывают введенных
                значений вовсе, что может быть весьма полезно при вводе критических данных,
                когда даже компрометация длины введенных данных недопустима

                Password — что очевидно из названия, данный тип отображения используется
                для создания полей ввода конфиденциальной информации, такой как пароли, 
                токены и т.д. Скрывает значения за точками или знаками звездочек по мере
                их ввода

                PasswordEchoOnEdit — тип отображения значений, что комбинирует в себе
                черты таких типов как Normal и Password. При вводе информации отображает
                значения как обвчное поле с типом Normal, однако после снятия фокуса с виджета
                QLineEdit, тип отображения сразу становится идентичен типу отображения Password

        Структура класса QLineEditWidget:
        |
        |————Конструктор (__init__(self))
        |    |
        |    |— Метод super().__init__() Инициализируем родительский класс
        |    |
        |    |— Метод setWindowTitle(title: str) См.описание BasicWindow
        |    |
        |    |— Метод setWindowIcon(icon: QIcon) См.описание BasicWindow
        |    |
        |    |— setFixedSize(width: int, height: int) См.описание BasicWindow
        |    |
        |    |— Атрибут widget См.описание WidgetList
        |    |
        |    |— Атрибут layout См.описание WidgetList
        |    |               
        |    |— Атрибут title Экземпляр класса QLabel, хранит в себе заголовок к полям ввода что расположены ниже
        |    |
        |    |— Атрибут lineEditNormal Экзепляр класса QLineEdit, используется для отображения поля ввода с стандарным типом
        |    |  отображения введенных значений
        |    |
        |    |— Метод setPlaceholderText(placeholder: str), экземпляра класса QLineEdit. Используется установки значения
        |    |  placeholder, другими словами текста, что отображается в пустом поле ввода в качестве подсказки для пользователя
        |    |  
        |    |— Метод setEchoMode(EchoMode: QLineEdit.EchoMode), экземпляра класса QLineEdit. Используется для установки типа
        |    |  отображения введенных в виджет QLineEdit значений. В качестве параметра принимает значение одной из констант 
        |    |  подкласса EchoMode
        |    |
        |    |— Атрибут lineEditNoEcho Экзепляр класса QLineEdit, используется для отображения поля ввода с скрытым типом
        |    |  отображения введенных значений
        |    |
        |    |— Метод setPlaceholderText(placeholder: str), экземпляра класса QLineEdit. Используется установки значения
        |    |  placeholder, другими словами текста, что отображается в пустом поле ввода в качестве подсказки для пользователя
        |    |  
        |    |— Метод setEchoMode(EchoMode: QLineEdit.EchoMode), экземпляра класса QLineEdit. Используется для установки типа
        |    |  отображения введенных в виджет QLineEdit значений. В качестве параметра принимает значение одной из констант 
        |    |  подкласса EchoMode
        |    |
        |    |— Атрибут lineEditPassword Экзепляр класса QLineEdit, используется для отображения поля ввода что предназначено
        |    |  для введения паролей
        |    |
        |    |— Метод setPlaceholderText(placeholder: str), экземпляра класса QLineEdit. Используется установки значения
        |    |  placeholder, другими словами текста, что отображается в пустом поле ввода в качестве подсказки для пользователя
        |    |  
        |    |— Метод setEchoMode(EchoMode: QLineEdit.EchoMode), экземпляра класса QLineEdit. Используется для установки типа
        |    |  отображения введенных в виджет QLineEdit значений. В качестве параметра принимает значение одной из констант 
        |    |  подкласса EchoMode
        |    |
        |    |— Атрибут lineEditPasswordEchoOnEdit Экзепляр класса QLineEdit, используется для отображения поля ввода с типом
        |    |  отображения введенных значений PasswordEchoOnEdit
        |    |
        |    |— Метод setPlaceholderText(placeholder: str), экземпляра класса QLineEdit. Используется установки значения
        |    |  placeholder, другими словами текста, что отображается в пустом поле ввода в качестве подсказки для пользователя
        |    |  
        |    |— Метод setEchoMode(EchoMode: QLineEdit.EchoMode), экземпляра класса QLineEdit. Используется для установки типа
        |    |  отображения введенных в виджет QLineEdit значений. В качестве параметра принимает значение одной из констант 
        |    |  подкласса EchoMode
        |    |
        |    |— Атрибут text Экземпляр класса QLabel, в парадигме данного приложения используется для отображения данных, что
        |    |  были введены через виджеты QLineEdit
        |    |
        |    |— Сигнал textChanged атрибута lineEditNormal. Устанавливает связь между атрибутом lineEditNormal, и методом
        |    |  setText(text: str) атрибута text
        |    |
        |    |— Сигнал textChanged атрибута lineEditNoEcho. Устанавливает связь между атрибутом lineEditNoEcho, и методом
        |    |  setText(text: str) атрибута text
        |    |
        |    |— Сигнал textChanged атрибута lineEditPassword. Устанавливает связь между атрибутом lineEditPassword, и методом
        |    |  setText(text: str) атрибута text
        |    |
        |    |— Сигнал textChanged атрибута lineEditPasswordEchoOnEdit. Устанавливает связь между атрибутом lineEditPasswordEchoOnEdit,
        |    |  и методом setText(text: str) атрибута text
        |    |
        |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
        |    |
        |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
        |    |
        |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
        |    |
        |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
        |    |
        |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
        |    |
        |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
        |    |
        |    |— Метод setLayout(layout: QVBoxLayout) См.описание WidgetList
        |    |
        |    |— Метод setCentralWidget(widget: QWidget) См.описание WidgetList
    """
    def __init__(self):
        super().__init__() # Инициализируем родительский класс QMainWindow
        self.setWindowTitle("QLineEdit Widget") # Устанавливаем заголовок текущего окна
        self.setWindowIcon(QIcon("./qt.ico")) # Устанавливаем иконку текущего окна
        self.setFixedSize(400, 200) # Задаем фиксированный размер текущего окна
        self.widget = QWidget() # Инициализируем экземпляр класса QWidget
        self.layout = QVBoxLayout() # Инициализируем экземпляр класса QVBoxLayout
        
        self.title = QLabel("Echo mode:") # Инициализируем экземпляр класса QLabel
        
        self.lineEditNormal = QLineEdit() # Инициализируем экземпляр класса QLineEdit
        self.lineEditNormal.setPlaceholderText("Normal") # Устанавливаем на экземпляр класса QLineEdit placeholder
        self.lineEditNormal.setEchoMode(QLineEdit.EchoMode.Normal) # Устанавливаем тип отображения значений на экземпляр класса QLineEdit
        
        self.lineEditNoEcho = QLineEdit() # Инициализируем экземпляр класса QLineEdit 
        self.lineEditNoEcho.setPlaceholderText("NoEcho") # Устанавливаем на экземпляр класса QLineEdit placeholder  
        self.lineEditNoEcho.setEchoMode(QLineEdit.EchoMode.NoEcho) # Устанавливаем тип отображения значений на экземпляр класса QLineEdit
        
        self.lineEditPassword = QLineEdit() # Инициализируем экземпляр класса QLineEdit 
        self.lineEditPassword.setPlaceholderText("Password") # Устанавливаем на экземпляр класса QLineEdit placeholder 
        self.lineEditPassword.setEchoMode(QLineEdit.EchoMode.Password) # Устанавливаем тип отображения значений на экземпляр класса QLineEdit
        
        self.lineEditPasswordEchoOnEdit = QLineEdit() 
        self.lineEditPasswordEchoOnEdit.setPlaceholderText("PasswordEchoOnEdit") # Устанавливаем на экземпляр класса QLineEdit placeholder
        self.lineEditPasswordEchoOnEdit.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit) # Устанавливаем тип отображения значений на экземпляр класса QLineEdit
        
        self.text = QLabel("") # Инициализируем экземпляр класса QLabel, который будет использоватся для вывода значений

        self.lineEditNormal.textChanged.connect(self.text.setText) # Устанавливаем связь между атрибутом lineEditNormal, и методом setText(text: str) атрибута text 
        self.lineEditNoEcho.textChanged.connect(self.text.setText) # Устанавливаем связь между атрибутом lineEditNormal, и методом setText(text: str) атрибута text
        self.lineEditPassword.textChanged.connect(self.text.setText) # Устанавливаем связь между атрибутом lineEditNormal, и методом setText(text: str) атрибута text
        self.lineEditPasswordEchoOnEdit.textChanged.connect(self.text.setText) # Устанавливаем связь между атрибутом lineEditNormal, и методом setText(text: str) атрибута text
        
        self.layout.addWidget(self.title) # Добавляем атрибут title в макет QVBoxLayout
        self.layout.addWidget(self.lineEditNormal) # Добавляем атрибут lineEditNormal в макет QVBoxLayout
        self.layout.addWidget(self.lineEditNoEcho) # Добавляем атрибут lineEditNoEcho в макет QVBoxLayout
        self.layout.addWidget(self.lineEditPassword) # Добавляем атрибут lineEditPassword в макет QVBoxLayout
        self.layout.addWidget(self.lineEditPasswordEchoOnEdit) # Добавляем атрибут lineEditPasswordEchoOnEdit в макет QVBoxLayout
        self.layout.addWidget(self.text) # Добавляем атрибут text в макет QVBoxLayout
        self.widget.setLayout(self.layout) # Устанавливаем layout в качестве макета родительского виджета
        self.setCentralWidget(self.widget) # Устанавливаем widget в качестве родительского виджета приложения


class QPushButtonWidget(QMainWindow):
    """
    Описание
    
        QPushButtonWidget представляет собой приложение с графическим интерфейсом
        на PySide6, служит для демонстрации базового функционала виджета QPushButton.
        Однако перед тем как переходить к структуре класса QPushButtonWidget стоит
        дать краткое определение виджету QPushButton.

        QPushButton — класс из модуля фреймворка PySide6, QWidgets. Служит для
        добавления, стилизации и масштабирования, пожалуй одного из наиболее
        фундаментальных элемента — кнопки. Несмотря на свою простоту весьма
        сложно представить без данного виджета даже самые простые приложения
        имеющие графический интерфейс. Структура класса QPushButtonWidget 
        будет рассмотрена ниже

    Структура класса QPushButtonWidget:
    |
    |————Конструктор (__init__(self))
    |    |
    |    |— Метод super().__init__() Инициализируем родительский класс
    |    |
    |    |— Метод setWindowTitle(title: str) См.описание BasicWindow
    |    |  в парадигме приложения QPushButtonWidget используется для
    |    |  вывода информации о количестве кликов
    |    |
    |    |— Метод setWindowIcon(icon: QIcon) См.описание BasicWindow
    |    |
    |    |— setFixedSize(width: int, height: int) См.описание BasicWindow
    |    |
    |    |— Атрибут btn экземпяр класса QPushButton, служит для демонстрации
    |    |  базовых возможней виджета QPushButton
    |    |
    |    |— Сигнал clicked атрибута btn. Устанавливает связь между атрибутом
    |    |  btn и методом addIteration(self) 
    |    |
    |    |— Метод setCentralWidget(widget: QWidget) См.описание WidgetList
    

    """
    def __init__(self):
        super().__init__() # Инициализируем родительский класс QMainWindow
        self.number = 0 # Инициализируем атрибут счетчика кликов
        self.setWindowTitle("QPushButton Widget | Click count: 0") # Устанавливаем заголовок окна
        self.setWindowIcon(QIcon("./qt.ico")) # Устанавливаем иконку текущего окна c помощью класса QIcon
        self.setFixedSize(700, 700) # Устанавливаем фиксированный размер текущего окна
        self.btn = QPushButton("Click") # Инициализируем экземпляр класса QPushButton
        self.btn.clicked.connect(self.add_iteration) # Устанавливает сигнал clicked на атрибут btn
        self.setCentralWidget(self.btn) # Устанавливаем widget в качестве главного виджета экземпляра класса QMainWindow   

    def addIteration(self):
        self.number += 1 # Увеличиваем зачение счетчика на единицу
        self.setWindowTitle(f"Button click: {self.number}") # Устанавливаем новое значение счетчика


class QSpinBoxWidget(QMainWindow):
    def __init__(self):
        """
    Описание
    
    QSpinBoxWidget представляет собой приложение с графическим интерфейсом
    на PySide6, служит для демонстрации базового функционала виджета QSpinBox.
    Перед тем как переходить к примерам использования данного виджета, который
    без сомнений встречается не реже предыдущего, стоит дать ему краткое опреде-
    ление

    QSpinBox — объект из модуля QWidgets фреймворка PySide6. Сам виджет
    представляет собой поле ввода предназначенное для установки целочисленных
    значений. В отличие от стандартного поля ввода QLineEdit, снабжен двумя
    небольшими кнопками с правой стороны виджета для увеличения или уменьшения
    введенного значения на один шаг. Ниже будет рассмотрена структура QSpinBoxWidget
    что демонстрирует базовый пример использования вышупомянутого виджета



    Структура класса QSpinBoxWidget:
    |
    |————Конструктор (__init__(self))
    |    |
    |    |— Метод super().__init__() Инициализируем родительский класс
    |    |
    |    |— Метод setWindowTitle(title: str) См.описание BasicWindow
    |    |
    |    |— Метод setWindowIcon(icon: QIcon) См.описание BasicWindow
    |    |
    |    |— setFixedSize(width: int, height: int) См.описание BasicWindow
    |    |
    |    |— Атрибут widget См.описание WidgetList
    |    |
    |    |— Атрибут layout См.описание WidgetList
    |    |
    |    |— Атрибут text хранит экземпяр класса QLabel, используется для
    |    |  вывода значений из виджета QSpinBox
    |    |
    |    |— Атрибут spinBox содержит в себе экземпяр класса QComboBox,
    |    |  служит для демонстрации базовых возможностей данного виджета
    |    |
    |    |— Метод setMinimum(value: int) экземпляра класса QComboBox,
    |    |  служит для установки минимального значения виджета QComboBox
    |    |
    |    |— Метод setMaximum(value: int) экземпляра класса QComboBox,
    |    |  служит для установки максимального значения виджета QComboBox
    |    |
    |    |— Сигнал valueChanged атрибута spinBox. Устанавливает связь между атрибутом
    |    |  spin_box и методом setValue(self)
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
    |    |
    |    |— Метод setLayout(layout: QVBoxLayout) См.описание WidgetList
    |    |
    |    |— Метод setCentralWidget(widget: QWidget) См.описание WidgetList 
    |    |
    |
    |————Метод setValue(self)
         |
         |— Метод setText(text: str) атрибута text, в парадигме приложения QSpinBoxWidget
         |  служит для установки в виджете QLabel значения взятого из виджета QSpinBox
         |
    """
        super().__init__() # Инициализируем родительский класс QMainWindow
        self.setWindowTitle("QSpinBox Widget") # Устанавливаем заголовок окна
        self.setWindowIcon(QIcon("./qt.ico")) # Устанавливаем иконку текущего окна c помощью класса QIcon
        self.setFixedSize(300, 70) # Устанавливаем фиксированный размер текущего окна
        self.widget = QWidget() # Инициализируем экземпляр класса QWidget
        self.layout = QVBoxLayout() # Инициализируем экземпляр класса QVBoxLayout
        self.text = QLabel("Текущее значение: 0") # Инициализируем экземпляр класса QLabel
        self.spinBox = QSpinBox() # Инициализируем экземпляр класса QSpinBox
        self.spinBox.setMinimum(0) # Устанавливаем минимальное значение что может хранить экземпляр класса QSpinBox
        self.spinBox.setMaximum(150) # Устанавливаем максимальное значение что может хранить экземпляр класса QSpinBox
        self.spin_box.valueChanged.connect(self.setValue) # Устанавливает сигнал clicked на атрибут btn 
        self.layout.addWidget(self.text) # Добавляем атрибут text в макет QVBoxLayout
        self.layout.addWidget(self.spinBox) # Добавляем атрибут spin_box в макет QVBoxLayout
        self.widget.setLayout(self.layout) # Устанавливаем layout в качестве макета родительского виджета с помощью метода setLayout()
        self.setCentralWidget(self.widget) # Устанавливаем widget в качестве главного виджета экземпляра класса QMainWindow

    def setValue(self, value) -> None:
        self.text.setText(f"Текущее значение: {value}") # Устанавливаем значение экземпляра класса QSpinBox


class QDoubleSpinBoxWidget(QMainWindow):
    """
    Описание
    
        QSpinBoxWidget представляет собой приложение с графическим интерфейсом
        на PySide6, служит для демонстрации базового функционала виджета QSpinBox.
        В своей сути практически идентичен виджету QSpinBox, что был рассмотрен
        ранее. Единственное различие виджетов QSpinBox и QDoubleSpinBox, заключается
        в виде значений что хранит виджет. Если в QSpinBox представлены лишь целочисленные
        значения, то в QDoubleSpinBox хранятся значения ввиде чисел с плавающей точкой,
        с двумя знаками после запятой. Ниже будет представлена демонстрация работы вышупомянутого
        виджета


    Структура класса QDoubleSpinBoxWidget:
    |
    |————Конструктор (__init__(self))
    |    |
    |    |— Метод super().__init__() Инициализируем родительский класс
    |    |
    |    |— Метод setWindowTitle(title: str) См.описание BasicWindow
    |    |
    |    |— Метод setWindowIcon(icon: QIcon) См.описание BasicWindow
    |    |
    |    |— setFixedSize(width: int, height: int) См.описание BasicWindow
    |    |
    |    |— Атрибут widget См.описание WidgetList
    |    |
    |    |— Атрибут layout См.описание WidgetList
    |    |
    |    |— Атрибут text хранит экземпяр класса QLabel, используется для
    |    |  вывода значений из виджета QSpinBox
    |    |
    |    |— Атрибут spin_box содержит в себе экземпяр класса QDoubleComboBox,
    |    |  служит для демонстрации базовых возможностей данного виджета
    |    |
    |    |— Метод setMinimum(value: int) экземпляра класса QDoubleSpinBox,
    |    |  служит для установки минимального значения виджета QDoubleSpinBox
    |    |
    |    |— Метод setMaximum(value: int) экземпляра класса QDoubleSpinBox,
    |    |  служит для установки максимального значения виджета QDoubleSpinBox
    |    |
    |    |— Сигнал valueChanged атрибута spin_box. Устанавливает связь между атрибутом
    |    |  spin_box и методом setValue(self)
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
    |    |
    |    |— Метод setLayout(layout: QVBoxLayout) См.описание WidgetList
    |    |
    |    |— Метод setCentralWidget(widget: QWidget) См.описание WidgetList 
    |    |
    |
    |————Метод setValue(self)
         |
         |— Метод setText(text: str) атрибута text, в парадигме приложения QDoubleSpinBoxWidget
         |  служит для установки в виджете QLabel значения взятого из виджета QDoubleSpinBox
         |
    """
    def __init__(self):
        super().__init__() # Инициализируем родительский класс QMainWindow
        self.setWindowTitle("QSpinBox Widget") # Устанавливаем заголовок окна
        self.setWindowIcon(QIcon("./qt.ico")) # Устанавливаем иконку текущего окна c помощью класса QIcon
        self.setFixedSize(300, 70) # Устанавливаем фиксированный размер текущего окна
        self.widget = QWidget() # Инициализируем экземпляр класса QWidget
        self.layout = QVBoxLayout() # Инициализируем экземпляр класса QVBoxLayout
        self.text = QLabel("Текущее значение: 0") # Инициализируем экземпляр класса QLabel
        self.spinBox = QDoubleSpinBox() # Инициализируем экземпляр класса QDoubleSpinBox
        self.spinBox.setMinimum(0) # Устанавливаем минимальное значение что может хранить экземпляр класса QDoubleSpinBox
        self.spinBox.setMaximum(150) # Устанавливаем максимальное значение что может хранить экземпляр класса QDoubleSpinBox
        self.spinBox.valueChanged.connect(self.setValue) # Устанавливает сигнал valueChanged на атрибут spinBox
        self.layout.addWidget(self.text) # Добавляем атрибут text в макет QVBoxLayout
        self.layout.addWidget(self.spinBox) # Добавляем атрибут spinBox в макет QVBoxLayout
        self.widget.setLayout(self.layout) # Устанавливаем layout в качестве макета родительского виджета с помощью метода setLayout()
        self.setCentralWidget(self.widget) # Устанавливаем widget в качестве главного виджета экземпляра класса QMainWindow

    def setValue(self, value) -> None:
        self.text.setText(f"Текущее значение: {value}") # Устанавливаем значение экземпляра класса QDoubleSpinBox


class QCheckBoxWidget(QMainWindow):
    """
    Описание

        QCheckBoxWidget представляет собой приложение с графическим интерфейсом
        на PySide6, служит для демонстрации основных функций виджета QCheckBox.
        Перед тем как переходить к демонстрации возможностей данного виджета
        на реальном примере, стоит дать ему краткое определение

        QCheckBox — класс из модуля QWidgets фреймворка PySide6. Представляет
        собой виджет что может возвращать лишь два значения — True или False.
        В плане внешнего вида является обычной 'галочкой', которую можно отметить,
        либо же убрать отметку. Весьма непллохой выбор если необходимо получить
        значение в формате типа данных bool. Ниже будет рассмотрена структура класса
        QCheckBoxWidget, что показывает базовые возможности данного виджета

    Структура класса QCheckBoxWidget:
    
    |
    |————Конструктор (__init__(self))
    |    |
    |    |— Метод super().__init__() Инициализируем родительский класс
    |    |
    |    |— Метод setWindowTitle(title: str) См.описание BasicWindow
    |    |
    |    |— Метод setWindowIcon(icon: QIcon) См.описание BasicWindow
    |    |
    |    |— setFixedSize(width: int, height: int) См.описание BasicWindow
    |    |
    |    |— Атрибут widget См.описание WidgetList
    |    |
    |    |— Атрибут layout См.описание WidgetList
    |    |
    |    |— Атрибут checkBox хранит экземпяр класса QCheckBox, служит
    |    |  демонстрации базового функционала виджета QCheckBox
    |    |
    |    |— Метод setChecked(value: bool) экземпляра класса QCheckBox
    |    |  Используется для установки отметки на виджете QCheckBox
    |    |
    |    |— Сигнал stateChanged атрибута checkBox. Устанавливает связь между атрибутом
    |    |  checkBox и методом switchCheckBox(self, state)
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
    |    |
    |    |— Метод setLayout(layout: QVBoxLayout) См.описание WidgetList
    |    |
    |    |— Метод setCentralWidget(widget: QWidget) См.описание WidgetList
    |
    |
    |————Метод setValue(self, value)
         |
         |— Метод setText(text: str) атрибута checkBox, в парадигме приложения QCheckBoxWidget
         |  служит для установки в виджете QCheckBox статуса его выделения
         |

    """
    def __init__(self):
        super().__init__() # Инициализируем родительский класс QMainWindow
        self.setWindowTitle("QCheckBox Widget") # Устанавливаем заголовок окна
        self.setWindowIcon(QIcon("./qt.ico")) # Устанавливаем иконку текущего окна c помощью класса QIcon
        self.setFixedSize(300, 70) # Устанавливаем фиксированный размер текущего окна
        self.widget = QWidget() # Инициализируем экземпляр класса QWidget
        self.layout = QVBoxLayout() # Инициализируем экземпляр класса QVBoxLayout 
        self.checkBox = QCheckBox("CheckBox enable") # Инициализируем экземпляр класса QSpinBox
        self.checkBox.setChecked(True) # Устанавливаем отметку на виджет QCheckBox
        self.checkbox.stateChanged.connect(self.switchCheckBox) # Устанавливает сигнал stateChanged на атрибут checkBox
        self.layout.addWidget(self.checkBox) # Добавляем атрибут check_box в макет QVBoxLayout
        self.widget.setLayout(self.layout) # Устанавливаем layout в качестве макета родительского виджета с помощью метода setLayout()
        self.setCentralWidget(self.widget) # Устанавливаем widget в качестве главного виджета экземпляра класса QMainWindow

    def switchCheckBox(self, state) -> None:
        self.checkBox.setText("CheckBox disable") if not self.check_box.isChecked() else self.check_box.setText("CheckBox enable") # Устанавливаем новое значение экземпляра класса QCheckBox в зависимости от предыдущего 


class QRadioButtonWidget(QMainWindow):
    """
    Описание
    
        QRadioButtonWidget представляет собой приложение с графическим интерфейсом
        на PySide6, служит для демонстрации основных функций виджета QRadioButton.
        В своей сути данный виджет мало отличен от предыдущего расммотренного
        виджета QCheckBox. Однако в отличие от QCheckBox, QRadioButton в основном
        служит для выбора значения из небольшой совокупности элементов, например
        при выборе в акнете половой принадлежности или семейного положения. Пример
        использования данного виджета, а также структура класса QRadioButtonWidget
        будет представлена ниже
    
    
    Структура класса QRadioButtonWidget:
    |
    |————Конструктор (__init__(self))
    |    |
    |    |— Метод super().__init__() Инициализируем родительский класс
    |    |
    |    |— Метод setWindowTitle(title: str) См.описание BasicWindow
    |    |
    |    |— Метод setWindowIcon(icon: QIcon) См.описание BasicWindow
    |    |
    |    |— setFixedSize(width: int, height: int) См.описание BasicWindow
    |    |
    |    |— Атрибут widget См.описание WidgetList
    |    |
    |    |— Атрибут layout См.описание WidgetList
    |    |
    |    |— Атрибут text хранит экземпяр класса QLabel, служит
    |    |  отображения опции, выбранной в данный момент
    |    |
    |    |— Атрибут radioBtn1 экземпяр класса QRadioButton, является
    |    |  первой опцией
    |    |  
    |    |— Атрибут radioBtn2 экземпяр класса QRadioButton, является
    |    |  второй опцией
    |    |
    |    |— Атрибут radioBtn3 экземпяр класса QRadioButton, является
    |    |  третий опцией
    |    |
    |    |— Сигнал clicked атрибута radioBtn1. Устанавливает связь между атрибутом
    |    |  radioBtn1 и методом switchCheckBox(self, state)
    |    |
    |    |— Сигнал clicked атрибута radioBtn2. Устанавливает связь между атрибутом
    |    |  radioBtn2 и методом switchCheckBox(self, state)
    |    |
    |    |— Сигнал clicked атрибута radioBtn3. Устанавливает связь между атрибутом
    |    |  radioBtn3 и методом switchCheckBox(self, state)
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList 
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList 
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList 
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList 
    |    |
    |    |— Метод setLayout(layout: QVBoxLayout) См.описание WidgetList
    |    |
    |    |— Метод setCentralWidget(widget: QWidget) См.описание WidgetList
    |
    |————Метод setStatus(self)
         |
         |— Метод setText(text: str) экземпляра класса QLabel, используeтся
         |  для установки названия опции выбранной в данный момент 
         |
    """
    def __init__(self):
        super().__init__() # Инициализируем родительский класс QMainWindow
        self.setWindowTitle("QRadioButton Widget") # Устанавливаем заголовок окна
        self.setWindowIcon(QIcon("./qt.ico")) # Устанавливаем иконку текущего окна c помощью класса QIcon
        self.setFixedSize(300, 200) # Устанавливаем фиксированный размер текущего окна

        self.widget = QWidget() # Инициализируем экземпляр класса QWidget
        self.layout = QVBoxLayout() # Инициализируем экземпляр класса QVBoxLayout

        self.text = QLabel("Опция не выбрана") # Инициализируем экземпляр класса QLabel

        self.radioBtn1 = QRadioButton("Первая опция") # Инициализируем экземпляр класса QRadioButton
        self.radioBtn2 = QRadioButton("Вторая опция") # Инициализируем экземпляр класса QRadioButton
        self.radioBtn3 = QRadioButton("Третья опция") # Инициализируем экземпляр класса QRadioButton

        self.radioBtn1.clicked.connect(lambda: self.set_status(self.radioBtn1)) # Устанавливает сигнал clicked на атрибут radioBtn1
        self.radioBtn2.clicked.connect(lambda: self.set_status(self.radioBtn2)) # Устанавливает сигнал clicked на атрибут radioBtn2
        self.radioBtn3.clicked.connect(lambda: self.set_status(self.radioBtn3)) # Устанавливает сигнал clicked на атрибут radioBtn3
 
        self.layout.addWidget(self.text) # Добавляем атрибут text в макет QVBoxLayout
        self.layout.addWidget(self.radioBtn1) # Добавляем атрибут radioBtn1 в макет QVBoxLayout
        self.layout.addWidget(self.radioBtn2) # Добавляем атрибут radioBtn2 в макет QVBoxLayout
        self.layout.addWidget(self.radioBtn3) # Добавляем атрибут radioBtn3 в макет QVBoxLayout
        
        self.widget.setLayout(self.layout) # Устанавливаем layout в качестве макета родительского виджета с помощью метода setLayout()
        self.setCentralWidget(self.widget) # Устанавливаем widget в качестве главного виджета экземпляра класса QMainWindow

    def setStatus(self, button) -> None:
        self.text.setText(button.text()) # Устанавливаем новое значение экземпляра класса QLabel


class QListWidgetExample(QMainWindow):
    """
    Описание
    
        QListWidgetExample представляет собой приложение с графическим интерфейсом
        на PySide6, служит для демонстрации основных функций виджета QListWidget.
        Как вы уже могли догадаться из названия данного виджета, QListWidget
        представляет собой список хранящий в себе некую совокупность инкапсулированных
        в него элементов. Виджет QListWidget стоит использовать для хранения совокупности
        неизменяемых элементов небольшой длины, например дистрибутивов операционной системы
        Linux, как в нашем примере. Структура класса QListWidgetExample, и пример использования
        виджета QListWidget приложены ниже

    Структура класса QListWidget:
    |
    |————Конструктор (__init__(self))
    |    |
    |    |— Метод super().__init__() Инициализируем родительский класс
    |    |
    |    |— Метод setWindowTitle(title: str) См.описание BasicWindow
    |    |
    |    |— Метод setWindowIcon(icon: QIcon) См.описание BasicWindow
    |    |
    |    |— setFixedSize(width: int, height: int) См.описание BasicWindow
    |    |
    |    |— Атрибут widget См.описание WidgetList
    |    |
    |    |— Атрибут layout См.описание WidgetList
    |    |
    |    |— Атрибут text хранит экземпяр класса QLabel, служит
    |    |  отображения опции, выбранной в данный момент
    |    |
    |    |— Атрибут listWidget содержит экземпяр класса QListWidget, выполняет
    |    |  функцию хранения элементов
    |    |
    |    |— Метод addItems экземпляра класса QListWidget, в качестве параметров принимает
    |    |  список содержащий инкапсулируемые значения, и добавляет их в экземпляр
    |    |  класса QListWidget
    |    |  
    |    |— Сигнал currentItemChanged атрибута listWidget. Устанавливает связь между атрибутом
    |    |  listWidget и методом setValue(self, state)
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList 
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList 
    |    |
    |    |— Метод setLayout(layout: QVBoxLayout) См.описание WidgetList
    |    |
    |    |— Метод setCentralWidget(widget: QWidget) См.описание WidgetList
    |
    |————Метод setValue(self, item)
         |
         |— Метод setText(text: str) экземпляра класса QLabel, используeтся
         |  для установки в виджет QLabel элемента выбранного в QListWidget 
         |
    """
    def __init__(self):
        super().__init__() # Инициализируем родительский класс QMainWindow
        self.setWindowTitle("QListWidget") # Устанавливаем заголовок окна
        self.setWindowIcon(QIcon("./qt.ico")) # Устанавливаем иконку текущего окна c помощью класса QIcon
        self.setFixedSize(500, 150) # Устанавливаем фиксированный размер текущего окна
        self.widget = QWidget() # Инициализируем экземпляр класса QWidget
        self.layout = QVBoxLayout() # Инициализируем экземпляр класса QVBoxLayout
        self.text = QLabel("Текущий элемент:") # Инициализируем экземпляр класса QLabel
        self.listWidget = QListWidget() # Инициализируем экземпляр класса QListWidget
        self.listWidget.addItems(["Ubuntu", "Debian", "Fedora", "Arch", "NixOS", "ParrotOS", "Gentoo"]) # Инкапсулируем значения в экземпляр класса QListWidget
        self.listWidget.currentItemChanged.connect(self.setValue) # Устанавливает сигнал currentItemChanged на атрибут listWidget
        self.layout.addWidget(self.text) # Добавляем атрибут text в макет QVBoxLayout
        self.layout.addWidget(self.listWidget) # Добавляем атрибут listWidget в макет QVBoxLayout
        self.widget.setLayout(self.layout) # Устанавливаем layout в качестве макета родительского виджета с помощью метода setLayout()
        self.setCentralWidget(self.widget) # Устанавливаем widget в качестве главного виджета экземпляра класса QMainWindow

    def setValue(self, item) -> None:
        self.text.setText(f"Текущий элемент: {item.text()}")


class QScrollBarWidget(QMainWindow):
    """
    Описание
        QScrollBarWidget представляет собой приложение с графическим интерфейсом
        на PySide6, служит для демонстрации основных функций виджета QScrollBar.
        Как вы уже могли догадаться из названия — класс QScrollBar предоставляет
        нам независимый от прочих виджет скроллбара. Помимо возможности кастомизации
        и масштабирования внутри родительского окна, вышеупомянутый виджет также может
        связываться с виджетами которые не имеют скроллбара по умолчанию, например
        QListWidget, как в нашем примере. Ниже будет продемонстрировано, как можно
        связать скроллбар, с другим виджетом, а также структура класса QScrollBarWidget

    Структура класса QScrollBarWidget:
    |
    |————Конструктор (__init__(self))
    |    |
    |    |— Метод super().__init__() Инициализируем родительский класс
    |    |
    |    |— Метод setWindowTitle(title: str) См.описание BasicWindow
    |    |
    |    |— Метод setWindowIcon(icon: QIcon) См.описание BasicWindow
    |    |
    |    |— setFixedSize(width: int, height: int) См.описание BasicWindow
    |    |
    |    |— Атрибут widget См.описание WidgetList
    |    |
    |    |— Атрибут layout См.описание WidgetList
    |    |
    |    |— Атрибут listWidget хранит экземпляр класса QListWidget
    |    |
    |    |— Метод setHorizontalScrollBarPolicy(flag: ScrollBarPolicy) экземпляра класса QListWidget
    |    |  служит для отключения горизонтального скроллбара вышеупомянутого родительского класса
    |    |
    |    |— Метод setVerticalScrollBarPolicy(flag: ScrollBarPolicy) экземпляра класса QListWidget
    |    |  служит для отключения вертикального скроллбара вышеупомянутого родительского класса
    |    |
    |    |— Наполняющий виджет QListWidget пронумерованными элементами генератор списков. Итерируется
    |    |  диапазоне целочисленных значений сгенерированных методом range(start: int, end: int)
    |    |
    |    |— Атрибут scrollBar хранит экземпляр класса QScrollBar,
    |    |  служит для демонстрации базового функционала виджета QScrollBar
    |    |
    |    |— Метод setRange(start: int, end: int) экземпляра класса QScrollBar
    |    |  используется для установки допустимого диапазона значений виджета QScrollBar
    |    |
    |    |— Метод setOrientation(flag: Orientation) экземпляра класса QScrollBar
    |    |  используется для установки ориентации виджета QScrollBar
    |    |
    |    |— Сигнал valueChanged атрибута scrollBar. Устанавливает связь между атрибутом
    |    |  scrollBar и методом setScrollValue(self, i)    
    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
    |    |
    |    |— Метод setLayout(layout: QVBoxLayout) См.описание WidgetList
    |    |
    |    |— Метод setCentralWidget(widget: QWidget) См.описание WidgetList
    |
    |
    |————Метод setScrollValue(self, i)
         |
         |— Метод setValue(step: int) метода verticalScrollBar(). В контексте приложения QScrollBarWidget 
         |  используется для установки значения внешнего скроллбара, внутреннему скроллбару 
    """    
    def __init__(self):
        super().__init__() # Инициализируем родительский класс QMainWindow
        self.setWindowTitle(f"QScrollBar Widget") # Устанавливаем заголовок окна
        self.setWindowIcon(QIcon("./qt.ico")) # Устанавливаем иконку текущего окна c помощью класса QIcon
        self.setFixedSize(500, 300) # Устанавливаем фиксированный размер текущего окна
        
        self.widget = QWidget() # Инициализируем экземпляр класса QWidget
        self.layout = QHBoxLayout() # Инициализируем экземпляр класса QVBoxLayout
        
        self.listWidget = QListWidget() # Инициализируем экземпляр класса QListWidget
        
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff) # Скрываем горизонтальный скроллбар виджета QListWidget
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff) # Скрываем вертикальный скроллбар виджета QListWidget
        
        [self.listWidget.addItem(f"Item {i}") for i in range(1, 30)] # Наполняем значениями виджет QListWidget через генератор списков
        
        self.scrollBar = QScrollBar(self) # Инициализируем экземпляр класса QScrollBar
        self.scrollBar.setRange(0, self.listWidget.count()) # Устанавливаем допустимый диапазон значений виджета QScrollBar
        self.scrollBar.setOrientation(Qt.Orientation.Vertical) # Устанавливаем ориентацию виджета QScrollBar
        self.scrollBar.valueChanged.connect(self.setScrollValue) # Устанавливает сигнал valueChanged на атрибут scrollBar
        
        self.layout.addWidget(self.listWidget) # Добавляем атрибут textArea в макет QVBoxLayout
        self.layout.addWidget(self.scrollBar) # Добавляем атрибут scrollBar в макет QVBoxLayout
        
        self.widget.setLayout(self.layout) # Устанавливаем layout в качестве макета родительского виджета с помощью метода setLayout()
        self.setCentralWidget(self.widget) # Устанавливаем widget в качестве главного виджета экземпляра класса QMainWindow
    
    def setScrollValue(self, i) -> None:
        self.listWidget.verticalScrollBar().setValue(i) # Устанавливаем значение скроллбара виджета QListWidget взятого из виджета QScrollBar


class QComboBoxWidget(QMainWindow):
    """
    Описание
    
        QComboBoxWidget представляет собой приложение с графическим интерфейсом
        на PySide6, служит для демонстрации основных функций виджета QComboBox.
        Виджет QComboBox практичен идентичен виджетy QListWidget по своему
        функционалу и внешнего виду, единственное различие между вышеперечисленными
        виджетами — вид представления списка. Если QListWidget хранит значения в открытом
        виде, то QComboBox является так называемым выпадающим списком, т.е в закрытом виде
        он демонстрирует только первое значение, но при нажатии 'выпадает' демонстрируя
        прочие хрянящиеся в нем значения. Структуру класса QComboBoxWidget, а также пример
        использования разобранного ранее виджета вы можете наблюдать ниже

    Структура класса QComboBoxWidget:
    |
    |————Конструктор (__init__(self))
    |    |
    |    |— Метод super().__init__() Инициализируем родительский класс
    |    |
    |    |— Метод setWindowTitle(title: str) См.описание BasicWindow
    |    |
    |    |— Метод setWindowIcon(icon: QIcon) См.описание BasicWindow
    |    |
    |    |— setFixedSize(width: int, height: int) См.описание BasicWindow
    |    |
    |    |— Атрибут widget См.описание WidgetList
    |    |
    |    |— Атрибут layout См.описание WidgetList
    |    |
    |    |— Атрибут text хранит экземпяр класса QLabel, служит
    |    |  отображения элемента, выбранного в данный момент
    |    |
    |    |— Атрибут comboBox содержит экземпяр класса QComboBox, выполняет
    |    |  функцию хранения элементов в выпадающем списке
    |    |
    |    |— Метод addItems экземпляра класса QComboBox, в качестве параметров принимает
    |    |  список значений, что должны быть добавлены в экземпляр класса QComboBox
    |    |  
    |    |— Сигнал currentItemChanged атрибута comboBox. Устанавливает связь между атрибутом
    |    |  comboBox и методом showOption(self, state)
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList 
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList 
    |    |
    |    |— Метод setLayout(layout: QVBoxLayout) См.описание WidgetList
    |    |
    |    |— Метод setCentralWidget(widget: QWidget) См.описание WidgetList
    |
    |————Метод showOption(self, item)
         |
         |— Метод setText(text: str) экземпляра класса QLabel, используeтся
         |  для установки в виджет QLabel элемента выбранного в QComboBox
         |
    """
    def __init__(self):
        super().__init__() # Инициализируем родительский класс QMainWindow
        self.setWindowTitle("QComboBox Widget") # Устанавливаем заголовок окна
        self.setWindowIcon(QIcon("./qt.ico")) # Устанавливаем иконку текущего окна c помощью класса QIcon
        self.setFixedSize(500, 70) # Устанавливаем фиксированный размер текущего окна

        self.widget = QWidget() # Инициализируем экземпляр класса QWidget
        self.layout = QVBoxLayout() # Инициализируем экземпляр класса QVBoxLayout
        
        self.text = QLabel("Текущее значение: Ubuntu") # Инициализируем экземпляр класса QLabel
        
        self.comboBox = QComboBox() # Инициализируем экземпляр класса QComboBox
        self.comboBox.addItems(["Ubuntu", "Debian", "Fedora", "Gentoo"]) # Добавляем значения в экземпляр класса QComboBox
        self.comboBox.currentIndexChanged.connect(self.showOption) # Устанавливает сигнал currentIndexChanged на атрибут comboBox
        
        self.layout.addWidget(self.text) # Добавляем атрибут text в макет QVBoxLayout
        self.layout.addWidget(self.comboBox) # Добавляем атрибут comboBox в макет QVBoxLayout
        
        self.widget.setLayout(self.layout) # Устанавливаем layout в качестве макета родительского виджета с помощью метода setLayout()
        self.setCentralWidget(self.widget) # Устанавливаем widget в качестве главного виджета экземпляра класса QMainWindow

    def showOption(self) -> None:
        self.text.setText(f"Текущее значение: {self.comboBox.currentText()}")


class QSliderWidget(QMainWindow):
    """
    Описание

        QSliderWidget представляет собой приложение с графическим интерфейсом
        на PySide6, служит для демонстрации основных функций виджета QSlider.
        Вышеупомянутый виджет также наверняка хорошо знаком любому пользователю
        ПК, представляет собой так называемый 'ползунок', если быть точнее вертикальную
        или горизонтальную линию с отметкой, которая при передвижении по виджету позволяет
        выбрать определенное значение из диапазона, как правильно целочисленное, в диапазоне
        от 0 до 100. Часто используется в программном обеспечении для работы со звуком или видео,
        однако находит свое применение и в прочих областях разработки программного обеспечения. 
        Структура класса QSliderWidget, а также пример использования виджета QSlider представлены
        ниже


    Структура класса QSliderWidget:
    |
    |————Конструктор (__init__(self))
    |    |
    |    |— Метод super().__init__() Инициализируем родительский класс
    |    |
    |    |— Метод setWindowTitle(title: str) См.описание BasicWindow
    |    |
    |    |— Метод setWindowIcon(icon: QIcon) См.описание BasicWindow
    |    |
    |    |— setFixedSize(width: int, height: int) См.описание BasicWindow
    |    |
    |    |— Атрибут widget См.описание WidgetList
    |    |
    |    |— Атрибут layout См.описание WidgetList
    |    |
    |    |— Атрибут text хранит экземпяр класса QLabel, отображает текущее
    |    |  значение экземпляра класса QSlider
    |    |
    |    |— Атрибут slider содержит экземпяр класса QSlider
    |    |
    |    |— Метод setRange(min: int, max: int) экземпляра класса QSlider,
    |    |  служит для установки допустимого диапазона значений виджета QSlider
    |    |
    |    |— Метод setSingleStep(step: int) экземпляра класса QSlider,
    |    |  устанавливает размер шага виджета QSlider
    |    |
    |    |— Метод setPageeStep(step: int) экземпляра класса QSlider,
    |    |  устанавливает размер шага ячейки виджета QSlider
    |    |
    |    |— Метод setTickPosition(step: int) экземпляра класса QSlider,
    |    |  устанавливает стиль виджета QSlider, в качестве значения
    |    |  принимает значения констант из подкласса TickPosition
    |    |
    |    |— Сигнал valueChanged атрибута slider. Устанавливает связь между атрибутом
    |    |  slider и методом setValue(self)
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
    |    |
    |    |— Метод setLayout(layout: QVBoxLayout) См.описание WidgetList
    |    |
    |    |— Метод setCentralWidget(widget: QWidget) См.описание WidgetList
    |
    |————Метод setValue(self)
         |
         |— Метод setText(text: str) экземпляра класса QLabel, используeтся
         |  для установки в виджет QLabel текущего значения экземпляра класса
         |  QSlider

    """
    def __init__(self):
        super().__init__() # Инициализируем родительский класс QMainWindow
        self.setWindowTitle("QSliderWidget") # Устанавливаем заголовок окна
        self.setWindowIcon(QIcon("./qt.ico")) # Устанавливаем иконку текущего окна c помощью класса QIcon
        self.setFixedSize(500, 100) # Устанавливаем фиксированный размер текущего окна
        
        self.widget = QWidget() # Инициализируем экземпляр класса QWidget
        self.layout = QVBoxLayout() # Инициализируем экземпляр класса QVBoxLayout 
        
        self.text = QLabel("Текущее значение: 0") # Инициализируем экземпляр класса QLabel
        
        self.slider = QSlider(Qt.Orientation.Horizontal) # Устанавливаем горизонтальную ориентацию виджета QSlider
        self.slider.setRange(0, 200) # Устанавливаем виджету QSlider диапазон допустимых значений
        self.slider.setSingleStep(1) # Устанавливаем длину шага виджета QSlider
        self.slider.setPageStep(5) # Устанавливаем длину крупного шага виджета QSlider
        
        self.slider.setTickPosition(QSlider.TickPosition.TicksBothSides) # Устанавливаем стиль виджета QSlider
        self.slider.valueChanged.connect(self.setValue) # Устанавливает сигнал valueChanged на атрибут slider
        
        self.layout.addWidget(self.slider) # Добавляем атрибут slider в макет QVBoxLayout
        self.layout.addWidget(self.text) # Добавляем атрибут text в макет QVBoxLayout
        
        self.widget.setLayout(self.layout) # Устанавливаем layout в качестве макета родительского виджета с помощью метода setLayout()
        self.setCentralWidget(self.widget) # Устанавливаем widget в качестве главного виджета экземпляра класса QMainWindow

    def setValue(self) -> None:
        self.text.setText(f"Текущее значение: {self.slider.value()}") # Устанавливаем новое значение экземпляру класса QLabel
        

class QTimeEditWidget(QMainWindow):
    """
    Описание
    
        QTimeEditWidget представляет собой приложение с графическим интерфейсом
        на PySide6, служит для демонстрации основных функций виджета QTimeEdit.
        Перед непосредственной демонстрацией использования данного виджета стоит
        дать краткое определение объекту, что за него отвечает

        QTimeEdit — класс модуля QWidgets, фреймворка PySide6. В контексте
        пользовательского интерфейса окна представляет собой поле ввода
        предназначенное для указания времени в привычном нам формате.
        При выделении отдельных частей, таких как часы или минуты, 
        позволяет с помощью стрелок быстро устанавливать нужное значение

    Теперь мы можем перейти к структуре класса QTimeEditWidget, а также
    демонстрации функционала виджета QTimeEdit


    Структура класса QTimeEditWidget:
    |
    |————Конструктор (__init__(self))
    |    |
    |    |— Метод super().__init__() Инициализируем родительский класс
    |    |
    |    |— Метод setWindowTitle(title: str) См.описание BasicWindow
    |    |
    |    |— Метод setWindowIcon(icon: QIcon) См.описание BasicWindow
    |    |
    |    |— setFixedSize(width: int, height: int) См.описание BasicWindow
    |    |
    |    |— Атрибут widget См.описание WidgetList
    |    |
    |    |— Атрибут layout См.описание WidgetList
    |    |
    |    |— Атрибут text хранит экземпяр класса QLabel, служит для отображения
    |    |  времени выбранного с помощью экземпляра класса QTimeEdit
    |    |
    |    |— Атрибут time содержит экземпяр класса QTimeEdit
    |    |
    |    |— Сигнал editingFinished атрибута time. Устанавливает связь между атрибутом
    |    |  time и методом setTime(self)
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
    |    |
    |    |— Метод setLayout(layout: QVBoxLayout) См.описание WidgetList
    |    |
    |    |— Метод setCentralWidget(widget: QWidget) См.описание WidgetList
    |
    |————Метод setTime(self)
         |
         |— Метод setText(text: str) экземпляра класса QLabel, используeтся
         |  для установки в виджет QLabel текущего времени что было взято из 
         |  экземпляра класса QTimeEdit

    """
    def __init__(self):
        super().__init__() # Инициализируем родительский класс QMainWindow
        self.setWindowTitle("QTimeEdit Widget") # Устанавливаем заголовок окна
        self.setWindowIcon(QIcon("./qt.ico")) # Устанавливаем иконку текущего окна c помощью класса QIcon
        self.setFixedSize(500, 70) # Устанавливаем фиксированный размер текущего окна
        
        self.widget = QWidget() # Инициализируем экземпляр класса QWidget
        self.layout = QVBoxLayout() # Инициализируем экземпляр класса QVBoxLayout
        
        self.text = QLabel("Выбранное время: 12:00:00") # Инициализируем экземпляр класса QLabel
        
        self.time = QTimeEdit() # Инициализируем экземпляр класса QTimeEdit
        self.time.editingFinished.connect(self.setTime) # Устанавливает сигнал editingFinished на атрибут time
        
        self.layout.addWidget(self.time) # Добавляем атрибут time в макет QVBoxLayout
        self.layout.addWidget(self.text) # Добавляем атрибут text в макет QVBoxLayout
        
        self.widget.setLayout(self.layout) # Устанавливаем layout в качестве макета родительского виджета с помощью метода setLayout()
        self.setCentralWidget(self.widget) # Устанавливаем widget в качестве главного виджета экземпляра класса QMainWindow

    def setTime(self) -> None:
        self.text.setText(f"Выбранное время: {str(self.time.time().toPyTime())}") # Устанавливаем новое значение экземпляру класса QLabel


class QDateEditWidget(QMainWindow):
    """
    Описание
    
        QDateEditWidget представляет собой приложение с графическим интерфейсом
        на PySide6, служит для демонстрации основных функций виджета QTimeEdit.
        Перед демонстрацией использования данного виджета стоит дать краткое
        определение классу что непосредственно связан с ним

            QDateEdit — класс модуля QWidgets, фреймворка PySide6. В контексте
            пользовательского интерфейса окна представляет собой поле ввода
            предназначенное для указания даты т.е года, месяца и дня. Может
            быть полезен для получения даты рождения от пользователя, или
            любой другой информации связанной с указанием точной даты.
    
        Структуру класса QDateEditWidget, а также демонстрацию базовых
        возможностей виджета QDateEdit вы можете наблюдать ниже
    
    Структура класса QDateEditWidget:
    |
    |————Конструктор (__init__(self))
    |    |
    |    |— Метод super().__init__() Инициализируем родительский класс
    |    |
    |    |— Метод setWindowTitle(title: str) См.описание BasicWindow
    |    |
    |    |— Метод setWindowIcon(icon: QIcon) См.описание BasicWindow
    |    |
    |    |— setFixedSize(width: int, height: int) См.описание BasicWindow
    |    |
    |    |— Атрибут widget См.описание WidgetList
    |    |
    |    |— Атрибут layout См.описание WidgetList
    |    |
    |    |— Атрибут text хранит экземпяр класса QLabel, служит для отображения
    |    |  времени выбранного с помощью экземпляра класса QDateEdit
    |    |
    |    |— Атрибут date содержит экземпяр класса QDateEdit
    |    |
    |    |— Сигнал editingFinished атрибута date. Устанавливает связь между атрибутом
    |    |  date и методом setDate(self)
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
    |    |
    |    |— Метод setLayout(layout: QVBoxLayout) См.описание WidgetList
    |    |
    |    |— Метод setCentralWidget(widget: QWidget) См.описание WidgetList
    |
    |————Метод setDate(self)
         |
         |— Метод setText(text: str) экземпляра класса QLabel, используeтся
         |  для установки в виджет QLabel текущей даты взятой из экземпляра 
         |  класса QTimeEdit

    """
    def __init__(self):
        super().__init__() # Инициализируем родительский класс QMainWindow
        self.setWindowTitle("QDateEdit Widget") # Устанавливаем заголовок окна
        self.setWindowIcon(QIcon("./qt.ico")) # Устанавливаем иконку текущего окна c помощью класса QIcon
        self.setFixedSize(500, 70) # Устанавливаем фиксированный размер текущего окна
        
        self.widget = QWidget() # Инициализируем экземпляр класса QWidget
        self.layout = QVBoxLayout() # Инициализируем экземпляр класса QVBoxLayout
        
        self.text = QLabel("Выбранная дата: 1970-01-01") # Инициализируем экземпляр класса QLabel
        
        self.date = QDateEdit() # Инициализируем экземпляр класса QDateEdit
        self.date.editingFinished.connect(self.setDate) # Устанавливает сигнал editingFinished на атрибут date
        
        self.layout.addWidget(self.date) # Добавляем атрибут date в макет QVBoxLayout
        self.layout.addWidget(self.text) # Добавляем атрибут text в макет QVBoxLayout
        
        self.widget.setLayout(self.layout) # Устанавливаем layout в качестве макета родительского виджета с помощью метода setLayout()
        self.setCentralWidget(self.widget) # Устанавливаем widget в качестве главного виджета экземпляра класса QMainWindow

    def setDate(self) -> None:
        self.text.setText(f"Выбранная дата: {str(self.date.date().toPyDate())}") # Устанавливаем новое значение экземпляру класса QLabel

class QDateTimeEditWidget(QMainWindow):
    """
    Описание
    
        QDateTimeEditWidget представляет собой приложение с графическим интерфейсом
        на PySide6, служит для демонстрации основных функций виджета QTimeEdit.
        Перед демонстрацией примера использования данного виджета стоит
        дать краткое определение отвечающему за него объекту

        QDateTimeEdit — класс модуля QWidgets, фреймворка PySide6. В контексте
        пользовательского интерфейса является полем ввода, что служит для 
        указания даты и времени в привычном всем нам формате. При выделении 
        отдельных частей, таких как месяцы или часы, позволяет с помощью стрелок 
        быстро устанавливать данным частям нужные значения

        Теперь мы можем перейти к структуре класса QDateTimeEditWidget, а также
        демонстрации функционала виджета QDateTimeEdit

    Структура класса QDateTimeEditWidget:
    |
    |————Конструктор (__init__(self))
    |    |
    |    |— Метод super().__init__() Инициализируем родительский класс
    |    |
    |    |— Метод setWindowTitle(title: str) См.описание BasicWindow
    |    |
    |    |— Метод setWindowIcon(icon: QIcon) См.описание BasicWindow
    |    |
    |    |— setFixedSize(width: int, height: int) См.описание BasicWindow
    |    |
    |    |— Атрибут widget См.описание WidgetList
    |    |
    |    |— Атрибут layout См.описание WidgetList
    |    |
    |    |— Атрибут text хранит экземпяр класса QLabel, служит для отображения
    |    |  даты и времени выбранного с помощью экземпляра класса QDateTimeEdit
    |    |
    |    |— Атрибут dateTime содержит экземпяр класса QDateTimeEdit
    |    |
    |    |— Сигнал dateTimeChanged атрибута dateTime. Устанавливает связь между атрибутом
    |    |  dateTime и методом setDateTime(self)
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
    |    |
    |    |— Метод setLayout(layout: QVBoxLayout) См.описание WidgetList
    |    |
    |    |— Метод setCentralWidget(widget: QWidget) См.описание WidgetList
    |
    |————Метод setDateTime(self)
         |
         |— Метод setText(text: str) экземпляра класса QLabel, используeтся
         |  для установки в виджет QLabel даты и времени которые были выбраны
         |  с помощью виджета QDateTimeEdit
         |

    """
    def __init__(self):
        super().__init__() # Инициализируем родительский класс QMainWindow
        self.setWindowTitle("QDateTimeEdit Widget") # Устанавливаем заголовок окна
        self.setWindowIcon(QIcon("./qt.ico")) # Устанавливаем иконку текущего окна c помощью класса QIcon
        self.setFixedSize(500, 70) # Устанавливаем фиксированный размер текущего окна
        self.widget = QWidget() # Инициализируем экземпляр класса QWidget
        self.layout = QVBoxLayout() # Инициализируем экземпляр класса QVBoxLayout
        
        self.text = QLabel("Текущие дата и время:") # Инициализируем экземпляр класса QLabel 
        
        self.dateTime = QDateTimeEdit(calendarPopup=False) # Инициализируем экземпляр класса QDateTimeEdit
        self.dateTime.dateTimeChanged.connect(self.setDateTime) # Устанавливает сигнал editingFinished на атрибут datetime
        
        self.layout.addWidget(self.dateTime) # Добавляем атрибут dateTime в макет QVBoxLayout
        self.layout.addWidget(self.text) # Добавляем атрибут text в макет QVBoxLayout
        
        self.widget.setLayout(self.layout) # Устанавливаем layout в качестве макета родительского виджета с помощью метода setLayout()
        self.setCentralWidget(self.widget) # Устанавливаем widget в качестве главного виджета экземпляра класса QMainWindow

    def setDateTime(self) -> None:
        self.text.setText(f"Текущие дата и время: {self.dateTime.dateTime().toString('dd-MM-yyyy HH:mm')}") # Устанавливаем новое значение экземпляру класса QLabel
        



class QCalendarWidgetExample(QMainWindow):
    """
    Описание
    
        QCalendarWidgetExample представляет собой приложение с графическим интерфейсом
        на PySide6, служит для демонстрации основных функций виджета QCalendarWidget.
        По субьективному мнению вашего покорного слуги, виджет QCalendarWidget 
        является одним из самых концептуально интересных виджетов модуля QWidgets.
        Как можно догадаться из названия, данный виджет представляет собой календарь,
        в котором мы имеет возможность выбрать такие параметры как год, месяц, и день.
        Имеет много сходств с рассмотренным ранее виджетом QDateEdit, однако возвращаемые
        значения несколько отличны.

        Структура класса QCalendarWidgetExample, а также демонстрация виджета QCalendarWidget
        представлена ниже

    Структура класса QCalendarWidgetExample:
    |
    |————Конструктор (__init__(self))
    |    |
    |    |— Метод super().__init__() Инициализируем родительский класс
    |    |
    |    |— Метод setWindowTitle(title: str) См.описание BasicWindow
    |    |
    |    |— Метод setWindowIcon(icon: QIcon) См.описание BasicWindow
    |    |
    |    |— setFixedSize(width: int, height: int) См.описание BasicWindow
    |    |
    |    |— Атрибут widget См.описание WidgetList
    |    |
    |    |— Атрибут layout См.описание WidgetList
    |    |
    |    |— Атрибут text хранит экземпяр класса QLabel, служит для отображения
    |    |  времени выбранного с помощью экземпляра класса QCalendarWidget,
    |    |
    |    |— Атрибут calendar хранит экземпляр класса QCalendarWidget,
    |    |  используется для выбора даты
    |    |
    |    |— Метод setGridVisible(value: bool) устанавливает значение
    |    |  видимости сетки виджета QCalendarWidget
    |    |
    |    |— Сигнал clicked[QDate] атрибута calendar. Устанавливает связь между атрибутом
    |    |  dateTime и методом setCalendarDate(self)
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
    |    |
    |    |— Метод setLayout(layout: QVBoxLayout) См.описание WidgetList
    |    |
    |    |— Метод setCentralWidget(widget: QWidget) См.описание WidgetList 
    |
    |————Метод setCalendarDate(self)
         |
         |— Метод setText(text: str) экземпляра класса QLabel, используeтся
         |  для установки в виджет QLabel даты которые были выбраны
         |  с помощью виджета QCalendarWidget
         |
    """
    def __init__(self):
        super().__init__() # Инициализируем родительский класс QMainWindow
        self.setWindowTitle("QCalendar Widget") # Устанавливаем заголовок окна
        self.setWindowIcon(QIcon("./qt.ico")) # Устанавливаем иконку текущего окна c помощью класса QIcon
        self.setFixedSize(800, 300) # Устанавливаем фиксированный размер текущего окна
        
        self.widget = QWidget() # Инициализируем экземпляр класса QWidget
        self.layout = QVBoxLayout() # Инициализируем экземпляр класса QVBoxLayout
        
        self.text = QLabel(f"Выбранная дата: Thu Jan 1 1970") # Инициализируем экземпляр класса QLabel
        
        self.calendar = QCalendarWidget()# Инициализируем экземпляр класса QCalendarWidget 
        self.calendar.setGridVisible(True) # Устанавливаем видимость сетки
        self.calendar.clicked[QDate].connect(self.setCalendarDate) # Устанавливает сигнал editingFinished на атрибут calendar
        
        self.layout.addWidget(self.calendar) # Добавляем атрибут calendar в макет QVBoxLayout
        self.layout.addWidget(self.text) # Добавляем атрибут text в макет QVBoxLayout
        
        self.widget.setLayout(self.layout) # Устанавливаем layout в качестве макета родительского виджета с помощью метода setLayout()
        self.setCentralWidget(self.widget) # Устанавливаем widget в качестве главного виджета экземпляра класса QMainWindow

    def setCalendarDate(self) -> None:
        self.text.setText(f"Выбранная дата: {str(self.calendar.selectedDate().toString())}") # Устанавливаем новое значение экземпляру класса QLabel


class QProgressBarWidget(QMainWindow):
    """
    Описание
        
        QProgressBarWidget представляет собой приложение с графическим интерфейсом
        на PySide6, служит для демонстрации основных функций виджета QProgressBarWidget.
        Как вы наверняка догадались из названия, QProgressBar является виджетом, который
        демонстрирует пользователю степень выполнения той или иной операции. Внешнее
        представляет собой пустую шкалу, что заполняется по мере выполнения той или иной
        операции.
        
        Структуру класса QProgressBarWidget, а также демонстрацию базовых возможностей виджета
        QProgressBar вы можете наблюдать ниже
    

    Структура класса QProgressBarWidget:
    |
    |————Конструктор (__init__(self))
    |    |
    |    |— Метод super().__init__() Инициализируем родительский класс
    |    |
    |    |— Метод setWindowTitle(title: str) См.описание BasicWindow
    |    |
    |    |— Метод setWindowIcon(icon: QIcon) См.описание BasicWindow
    |    |
    |    |— setFixedSize(width: int, height: int) См.описание BasicWindow
    |    |
    |    |— Атрибут widget См.описание WidgetList
    |    |
    |    |— Атрибут layout См.описание WidgetList
    |    |
    |    |— Атрибут progressBar хранит экземпляр класса QProgressBar,
    |    |  служит для демонстрации базового функционала виджета QProgressBar
    |    |
    |    |— Атрибут startButton хранит экземпляр класса QPushButton,
    |    |
    |    |— Метод setFixedSize(width: int, height: int) экземпляра класса QPushButton
    |    |  Устанавливает фиксированный размер виджета QPushButton
    |    |
    |    |— Сигнал clicked атрибута startButton. Устанавливает связь между атрибутом
    |    |  startButton и методом showLoading(self)
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
    |    |
    |    |— Метод setLayout(layout: QVBoxLayout) См.описание WidgetList
    |    |
    |    |— Метод setCentralWidget(widget: QWidget) См.описание WidgetList 
    |
    |————Метод showLoading(self)
         |
         |——Цикл for итерирующийся по диапазону значений сгенерированных
         |  методом range(start: int, end: int)
         |   |
         |   |— Метод sleep(delay: float) встроенного модуля time. Используется
         |   |  для инициации задержки на указанное в параметрах функции время
         |   |
         |   |— Метод setValue(value: int) экземпляра класса QProgressBar, используeтся
         |   |  для установки текущей позиции виджета QProgressBar
         |   |
         |
         |— Метод setValue(value: int) экземпляра класса QProgressBar, в парадигме метода
         |  showLoading(self) обнуляет значение виджета QProgressBar, после задержки
"""
    def __init__(self):
        super().__init__() # Инициализируем родительский класс QMainWindow
        self.setWindowTitle("QProgressBar Widget") # Устанавливаем заголовок окна
        self.setWindowIcon(QIcon("./qt.ico")) # Устанавливаем иконку текущего окна c помощью класса QIcon
        self.setFixedSize(500, 100) # Устанавливаем фиксированный размер текущего окна
        
        self.widget = QWidget() # Инициализируем экземпляр класса QWidget
        self.layout = QVBoxLayout() # Инициализируем экземпляр класса QVBoxLayout
        
        self.progressBar = QProgressBar() # Инициализируем экземпляр класса QProgressBar
        
        self.startButton = QPushButton("Start") # Инициализируем экземпляр класса QPushButton
        self.startButton.setFixedSize(480, 40) # Устанавливаем фиксированный размер виджета QPushButton
        self.startButton.clicked.connect(self.showLoading) # Устанавливает сигнал clicked на атрибут startButton 
        
        self.layout.addWidget(self.progressBar) # Добавляем атрибут progressBar в макет QVBoxLayout
        self.layout.addWidget(self.startButton) # Добавляем атрибут startButton в макет QVBoxLayout
        
        self.widget.setLayout(self.layout) # Устанавливаем layout в качестве макета родительского виджета с помощью метода setLayout()
        self.setCentralWidget(self.widget) # Устанавливаем widget в качестве главного виджета экземпляра класса QMainWindow
        
    def showLoading(self) -> None:
        for i in range(0, 250):
            sleep(0.01) # Устанавливаем задержку в 0.01s
            self.progressBar.setValue(i) # Устанавливаем значение виджета QProgressBar
        
        self.progressBar.setValue(0) # Обнуляем значение виджета QProgressBar


class QFontComboBoxWidget(QMainWindow):
    """
    Описание
        
        QFontComboBoxWidget представляет собой приложение с графическим интерфейсом
        на PySide6, служит для демонстрации основных функций виджета QFontComboBox.
        Как вы уже могли догадаться виджет QFontComboBox практичен идентичен ранее 
        рассмотренному виджетy QComboBox по своему функционалу и внешнего виду, 
        единственное различие между вышеперечисленными виджетами заключается в функционале.
        Если QComboBox дает разработчику возможность инкапсуляции собственных значений,
        то QFontComboBox служит для выбора пользователем шрифта. Рекомендуется к использованию
        в рамках программного обеспечения для редактирования документов или дизайна интерфейсов.

        Структура класса QFontComboBoxWidget, а также пример использовая вышеразобранного виджета
        представлены ниже

    Структура класса QFontComboBoxWidget:
    |
    |————Конструктор (__init__(self))
    |    |
    |    |— Метод super().__init__() Инициализируем родительский класс
    |    |
    |    |— Метод setWindowTitle(title: str) См.описание BasicWindow
    |    |
    |    |— Метод setWindowIcon(icon: QIcon) См.описание BasicWindow
    |    |
    |    |— setFixedSize(width: int, height: int) См.описание BasicWindow
    |    |
    |    |— Атрибут widget См.описание WidgetList
    |    |
    |    |— Атрибут layout См.описание WidgetList
    |    |
    |    |— Атрибут text хранит экземпяр класса QLabel, служит
    |    |  отображения названия шрифта, что был выбран с помощью виджета QFontComboBox
    |    |
    |    |— Атрибут fontComboBox содержит экземпяр класса QFontComboBox, используется
    |    |  для выбора шрифта 
    |    |
    |    |— Сигнал currentFontChanged атрибута fontComboBox. Устанавливает связь между атрибутом
    |    |  fontComboBox и методом updateLabel(self, state)
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList 
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList 
    |    |
    |    |— Метод setLayout(layout: QVBoxLayout) См.описание WidgetList
    |    |
    |    |— Метод setCentralWidget(widget: QWidget) См.описание WidgetList
    |
    |————Метод updateLabel(self, font)
         |
         |— Метод setText(text: str) экземпляра класса QLabel, используeтся
         |  для установки в виджет QLabel названия шрифта выбранного в QFontComboBox
         |
         |— Метод setFont(font: QFont) экземпляра класса QLabel, используeтся
         |  для установки выбранного в виджете QFontComboBox шрифта в качестве
         |  основного шрифта надписи атрибута text
    """
    def __init__(self):
        super().__init__() # Инициализируем родительский класс QMainWindow
        self.setWindowTitle("QFontComboBox Widget") # Устанавливаем заголовок окна
        self.setWindowIcon(QIcon("./qt.ico")) # Устанавливаем иконку текущего окна c помощью класса QIcon
        self.setFixedSize(500, 70) # Устанавливаем фиксированный размер текущего окна
        
        self.widget = QWidget() # Инициализируем экземпляр класса QWidget
        self.layout = QVBoxLayout() # Инициализируем экземпляр класса QVBoxLayout
        
        self.text = QLabel("Текущий шрифт: ") # Инициализируем экземпляр класса QLabel
        
        self.fontComboBox = QFontComboBox() # Инициализируем экземпляр класса QFontComboBox
        self.fontComboBox.currentFontChanged.connect(self.updateLabel) # Устанавливает сигнал currentFontChanged на атрибут fontComboBox
        
        self.layout.addWidget(self.text) # Добавляем атрибут text в макет QVBoxLayout
        self.layout.addWidget(self.fontComboBox) # Добавляем атрибут fontComboBox в макет QVBoxLayout
        
        self.widget.setLayout(self.layout) # Устанавливаем layout в качестве макета родительского виджета с помощью метода setLayout()
        self.setCentralWidget(self.widget) # Устанавливаем widget в качестве главного виджета экземпляра класса QMainWindow
    
    def updateLabel(self, font) -> None:
        self.text.setText(f"Текущий шрифт: {font.family()}")
        self.text.setFont(font)


class QTextEditWidget(QMainWindow):
    def __init__(self):
        """
    Описание
        
        QTextEditWidget представляет собой приложение с графическим интерфейсом
        на PySide6, служит для демонстрации основных функций виджета QTextEdit.
        Перед тем как перейти к демонстрации функционала данного виджета
        стоит дать ему определение

        QTextEdit — класс модуля QWidgets фреймворка PySide6. В рамках пользовательского
        интерфейса представляет собой текстовое поле с возможностью редактирования и
        масштабирования. Как правило использует в рамках программного обеспечения
        для редактирования документов, однако успешно применяется в прочем ПО, где
        требуется возможность вставки и редактирования больших объемом текста

        Структура класса QTextEditWidget, а также демонстрация базового функционала
        виджета QTextEdit представлена ниже


    Структура класса QTextEditWidget:
    |
    |————Конструктор (__init__(self))
    |    |
    |    |— Метод super().__init__() Инициализируем родительский класс
    |    |
    |    |— Метод setWindowTitle(title: str) См.описание BasicWindow
    |    |
    |    |— Метод setWindowIcon(icon: QIcon) См.описание BasicWindow
    |    |
    |    |— setFixedSize(width: int, height: int) См.описание BasicWindow
    |    |
    |    |— Атрибут widget См.описание WidgetList
    |    |
    |    |— Атрибут layout См.описание WidgetList
    |    |
    |    |— Атрибут textEdit хранит экземпяр класса QTextEdit, предназначен для
    |    |  демонстрации базового функционала виджета QTextEdit
    |    |
    |    |— Метод insertPlainText(text: str) экземпляра класса QTextEdit.
    |    |  Служит для вставки в виджет QTextEdit совокупности строк.
    |    |  В подавляющем большинстве случаев используется для предустановки
    |    |  текстового значения
    |    |
    |    |— Сигнал textChanged атрибута textEdit. Устанавливает связь между атрибутом
    |    |  textEdit и методом setCount(self)
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList 
    |    |
    |    |— Метод setLayout(layout: QVBoxLayout) См.описание WidgetList
    |    |
    |    |— Метод setCentralWidget(widget: QWidget) См.описание WidgetList
    |
    |
    |————Метод setCount(self)
         |
         |— Метод setWindowTitle(text: str) экземпляра класса QMainWindow, в парадигме
         |  метода setCount(self) служит для обновления счетчика символов в заголовке
"""
        super().__init__() # Инициализируем родительский класс QMainWindow
        self.setWindowTitle("QTextEdit Widget | Symbol count: 13") # Устанавливаем заголовок окна
        self.setWindowIcon(QIcon("./qt.ico")) # Устанавливаем иконку текущего окна c помощью класса QIcon
        self.setFixedSize(700, 400) # Устанавливаем фиксированный размер текущего окна
        
        self.widget = QWidget() # Инициализируем экземпляр класса QWidget
        self.layout = QVBoxLayout() # Инициализируем экземпляр класса QVBoxLayout
        
        self.textEdit = QTextEdit() # Инициализируем экземпляр класса QTextEdit
        self.textEdit.insertPlainText("Введите текст") # Устанавливаем значение виджета QPlainTextEdit
        self.textEdit.textChanged.connect(self.setCount) # Устанавливает сигнал textChanged на атрибут textEdit
        
        self.layout.addWidget(self.textEdit) # Добавляем атрибут textEdit в макет QVBoxLayout
        
        self.widget.setLayout(self.layout) # Устанавливаем layout в качестве макета родительского виджета с помощью метода setLayout()
        self.setCentralWidget(self.widget) # Устанавливаем widget в качестве главного виджета экземпляра класса QMainWindow
    
    def setCount(self) -> None:
        self.setWindowTitle(f"QTextEdit Widget | Symbol count: {len(self.textEdit.toPlainText())}")


class QPlainTextEditWidget(QMainWindow):
    """
    Описание
        
        QPlainTextEditWidget представляет собой приложение с графическим интерфейсом
        на PySide6, служит для демонстрации основных функций виджета QPlainTextEdit.
        Виджет QPlainTextEdit мало чем отличен от ранее рассмотренного виджета QTextEdit,
        однако имеет ряд отличий что перечисленны ниже

            QPlainTextEdit
                
                Наличие встроенного скроллбара

                Высокая скорость работы поля ввода, что обеспечена благодаря
                встроенной оптимизации виджета 
            
            QPlainTextEdit
                
                Отсутствие встроенного скроллбара

                Обычная скорость работы поля ввода, встроенная оптимизация
                отсутствует
    
        
        Структура класса QPlainTextEditWidget и демонстрация функционала виджета QPlainTextEdit
        представлены ниже


    Структура класса QPlainTextEditWidget:
    |
    |————Конструктор (__init__(self))
    |    |
    |    |— Метод super().__init__() Инициализируем родительский класс
    |    |
    |    |— Метод setWindowTitle(title: str) См.описание BasicWindow
    |    |
    |    |— Метод setWindowIcon(icon: QIcon) См.описание BasicWindow
    |    |
    |    |— setFixedSize(width: int, height: int) См.описание BasicWindow
    |    |
    |    |— Атрибут widget См.описание WidgetList
    |    |
    |    |— Атрибут layout См.описание WidgetList
    |    |
    |    |— Атрибут plainEdit хранит экземпяр класса QPlainTextEdit, предназначен для
    |    |  демонстрации базового функционала виджета QPlainTextEdit
    |    |
    |    |— Метод insertPlainText(text: str) экземпляра класса QPlainTextEdit.
    |    |  Служит для вставки в виджет QPlainTextEdit некого набора символов.
    |    |  Идентична по своему функционалу аналогичному методу в классе QTextEdit
    |    |
    |    |
    |    |— Сигнал textChanged атрибута plainText. Устанавливает связь между атрибутом
    |    |  plainText и методом setCount(self)
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList 
    |    |
    |    |— Метод setLayout(layout: QVBoxLayout) См.описание WidgetList
    |    |
    |    |— Метод setCentralWidget(widget: QWidget) См.описание WidgetList
    |
    |
    |————Метод setCount(self)
         |
         |— Метод setWindowTitle(text: str) экземпляра класса QMainWindow, в парадигме
         |  метода setCount(self) служит для обновления информации о количестве символов в заголовке
"""
    def __init__(self):
        super().__init__() # Инициализируем родительский класс QMainWindow
        self.setWindowTitle("QPlainTextEdit Widget | Symbol count: 13") # Устанавливаем заголовок окна
        self.setWindowIcon(QIcon("./qt.ico")) # Устанавливаем иконку текущего окна c помощью класса QIcon
        self.setFixedSize(700, 400) # Устанавливаем фиксированный размер текущего окна
        
        self.widget = QWidget() # Инициализируем экземпляр класса QWidget
        self.layout = QVBoxLayout() # Инициализируем экземпляр класса QVBoxLayout
        
        self.plainText = QPlainTextEdit() # Инициализируем экземпляр класса QPlainTextEdit
        self.plainText.insertPlainText("Введите текст") # Устанавливаем начальное значение виджета QPlainTextEdit
        self.plainText.textChanged.connect(self.setCount) # Устанавливает сигнал textChanged на атрибут plainText
        
        self.layout.addWidget(self.plainText) # Добавляем атрибут plainText в макет QVBoxLayout
        
        self.widget.setLayout(self.layout) # Устанавливаем layout в качестве макета родительского виджета с помощью метода setLayout()
        self.setCentralWidget(self.widget) # Устанавливаем widget в качестве главного виджета экземпляра класса QMainWindow
    
    def setCount(self) -> None:
        self.setWindowTitle(f"QPlainTextEdit Widget | Symbol count: {len(self.plainText.toPlainText())}") 


class QTextBrowserWidget(QMainWindow):
    """
    Описание
        
        QTextBrowserWidget представляет собой приложение с графическим интерфейсом
        на PySide6, служит для демонстрации основных функций виджета QTextBrowser.
        Последний 'текстовый' виджет что будет нами рассмотрен. В контексте 
        пользовательского интерфейса мало отличны от виджетов QTextEdit и QPlainTextEdit,
        однако функционал несколько отличается. QTextBrowser не предусматривает редактирование
        его содержания в базовой реализации, однако имеет заметное преимущество среди подобных
        ему виджетов наличичием поддержки гипертекстовой разметки.

        Демонстрация базового функционала виджета QTextBrowser, а также структура класса
        QTextBrowserWidget представлены ниже

    Структура класса QTextBrowserWidget:
    |
    |————Конструктор (__init__(self))
    |    |
    |    |— Метод super().__init__() Инициализируем родительский класс
    |    |
    |    |— Метод setWindowTitle(title: str) См.описание BasicWindow
    |    |
    |    |— Метод setWindowIcon(icon: QIcon) См.описание BasicWindow
    |    |
    |    |— setFixedSize(width: int, height: int) См.описание BasicWindow
    |    |
    |    |— Атрибут widget См.описание WidgetList
    |    |
    |    |— Атрибут layout См.описание WidgetList
    |    |
    |    |— Атрибут textBrowser хранит экземпляр класса textBrowserEdit, предназначен для
    |    |  демонстрации базового функционала виджета QTextBrowserEdit
    |    |
    |    |— Метод insertPlainText(text: str) экземпляра класса QTextBrowserEdit.
    |    |  Служит для вставки в виджет QTextBrowserEdit некого набора символов.
    |    |  Идентична по своему функционалу аналогичным методам в классах QTextEdit и QPlainTextEdit
    |    |
    |    |
    |    |— Сигнал textChanged атрибута textBrowser. Устанавливает связь между атрибутом
    |    |  textBrowser и методом setCount(self)
    |    |
    |    |— Атрибут inputText хранит экземпляр класса QLineEdit, предназначен для
    |    |  ввода значений в виджет QTextBrowser
    |    |
    |    |— Сигнал textChanged атрибута inputText. Устанавливает связь между атрибутом
    |    |  inputText и методом insertPlainText(self) экземпляра класса QTextBrowser
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList 
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList 
    |    |
    |    |— Метод setLayout(layout: QVBoxLayout) См.описание WidgetList
    |    |
    |    |— Метод setCentralWidget(widget: QWidget) См.описание WidgetList
    |
    |
    |————Метод setCount(self)
         |
         |— Метод setWindowTitle(text: str) экземпляра класса QMainWindow, в парадигме
         |  метода setCount(self) служит для обновления информации о количестве символов в заголовке
"""
    def __init__(self):
        super().__init__() # Инициализируем родительский класс QMainWindow
        self.setWindowTitle("QTextBrowser Widget | Symbol count: 13") # Устанавливаем заголовок окна
        self.setWindowIcon(QIcon("./qt.ico")) # Устанавливаем иконку текущего окна c помощью класса QIcon
        self.setFixedSize(700, 400) # Устанавливаем фиксированный размер текущего окна
        
        self.widget = QWidget() # Инициализируем экземпляр класса QWidget
        self.layout = QVBoxLayout() # Инициализируем экземпляр класса QVBoxLayout 
        
        self.textBrowser = QTextBrowser() # Инициализируем экземпляр класса QTextBrowser
        self.textBrowser.textChanged.connect(self.set_count)
        
        self.inputText = QLineEdit() # Инициализируем экземпляр класса QLineEdit
        self.inputText.setPlaceholderText("Введите текст") # Устанавливаем значение виджета QLineEdit
        self.inputText.textChanged.connect(self.textBrowser.insertPlainText) # Устанавливает сигнал textChanged на атрибут inputText
        
        self.layout.addWidget(self.inputText) # Добавляем атрибут inputText в макет QVBoxLayout
        self.layout.addWidget(self.textBrowser) # Добавляем атрибут textBrowser в макет QVBoxLayout
        
        self.widget.setLayout(self.layout) # Устанавливаем layout в качестве макета родительского виджета с помощью метода setLayout()
        self.setCentralWidget(self.widget) # Устанавливаем widget в качестве главного виджета экземпляра класса QMainWindow
    
    def set_count(self) -> None:
        self.setWindowTitle(f"QTextBrowser Widget | Symbol count: {len(self.textBrowser.toPlainText())}") # Устанавливаем новое значение счетчика символов

class QStatusBarWidget(QMainWindow):
    """
    Описание
        
        QStatusBarWidget представляет собой приложение с графическим интерфейсом
        на PySide6, служит для демонстрации основных функций виджета QStatusBar.
        Название виджета QStatusBar наверняка известно небольшую числу обычных
        пользователей ПК, однако следы его применения заметны в широком спектре
        программного обеспечения. Особенно часто данный виджет можно встретить
        в текстовых редакторах, что не удивительно ведь изначально он создавался
        именно для применения в них. В рамках пользовательского интерфейса виджет
        QStatusBar представляет собой полоску в нижней части родительского окна.
        Может содержать в себе информацию вроде названия редактируемого документа,
        количества строк или символов, а также выводить короткие сообщения что
        отображают действия пользователя
     
        Структура класса QTextBrowserWidget а также демонстрация базового функционала
        виджета QStatusBarWidget представлены ниже
    

    Структура класса QStatusBarWidget:
    |
    |————Конструктор (__init__(self))
    |    |
    |    |— Метод super().__init__() Инициализируем родительский класс
    |    |
    |    |— Метод setWindowTitle(title: str) См.описание BasicWindow
    |    |
    |    |— Метод setWindowIcon(icon: QIcon) См.описание BasicWindow
    |    |
    |    |— setFixedSize(width: int, height: int) См.описание BasicWindow
    |    |
    |    |— Атрибут statusBar хранит в себе метод statusBar() экземпляра класса
    |    |  QMainWindow, является родительским объектом виджета QStatusBar 
    |    |
    |    |— Метод addPermanentWidget(status: QLabel) экземпляра объекта statusBar.
    |    |  Предназначен для установки значения статуса в формате виджета QLabel
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание QWidgetList
    |    |
    |    |  
    |    |— Атрибут textEditor хранит экземпляр класса QTextEdit, служит 
    |    |  родительским виджетом приложения QStatusBarWidget
    |    |
    |    |— Сигнал textChanged атрибута textEditor. Устанавливает связь между атрибутом
    |    |  textEditor и методом showInfo(self)
    |    |
    |    |— Метод setCentralWidget(widget: QWidget) См.описание WidgetList
    |
    |————Метод showInfo(self)
         |
         |— Метод setWindowTitle(title: str) экземпляра класса QMainWindow
         |  служит для обновления информации о количестве символов внутри виджета QTextEdit
         |
         |— Метод showMessage(message: str, timeoutMs: int) экземпляра объекта statusBar().
         |  Принимает в качестве параметров строку, что выводится в качестве сообщения при
         |  вызове метода, а также значение с типом данных int, которое устанавливает сколько
         |  данное сообщение будет нахожится в пределах родительского виджета
         |
    """
    def __init__(self):
        super().__init__() # Инициализируем родительский класс QMainWindow
        self.setWindowTitle("QStatusBar Widget | Количество символов: 0") # Устанавливаем заголовок окна
        self.setWindowIcon(QIcon("./qt.ico")) # Устанавливаем иконку текущего окна c помощью класса QIcon
        self.setFixedSize(700, 400) # Устанавливаем фиксированный размер текущего окна

        self.statusBar = self.statusBar() # Инициализируем атрибут statusBar содержащий в себе метод statusBar() экземпляра класса QMainWindow
        
        self.statusBar.addPermanentWidget(QLabel("Untitled")) # Добавляем 'название' текущего документа
        
        self.statusBar.addWidget(QLabel("Режим чтения")) # Добавляем отметку режима чтения

        self.textEditor = QTextEdit() # Инициализируем экземпляр класса QLabel
        self.textEditor.textChanged.connect(self.showInfo) # Устанавливает сигнал textChanged на атрибут textEditor

        self.setCentralWidget(self.textEditor) # Устанавливаем widget в качестве главного виджета экземпляра класса QMainWindow

    def showInfo(self) -> None:
        self.setWindowTitle(f"QStatusBar Widget | Количество символов: {len(self.textEditor.toPlainText())}") # Обновляем значение счетчика
        self.statusBar.showMessage("Текст редактируется..", 350) # Выводим сообщение о редактировании


class QMultiDocumentApplication(QMainWindow):
    """    
    Описание
        
        QMultiDocumentApplication представляет собой приложение с графическим интерфейсом
        на PySide6, служит для демонстрации базового функционала виджета QMdiArea. Виджет
        QMdiArea является родительским виджетом для дочерним виджетов QMdiSubWindow,
        по сути являясь лишь областью для их размещения. Следы использования данного виджета
        обычный пользователь встречает весьма редко, однако данный виджет хорошо себя показывает
        в программном обеспечении которое предназначена для задач по типу удаленного администрирования
        других компьютеров, либо же управление системой видеонаблюдения

        Структура класса QMultiDocumentApplication и пример использования виджета
        QMdiArea представлены ниже

        
    Структура класса QMultiDocumentApplication:
    |
    |————Конструктор (__init__(self))
    |    |
    |    |— Метод super().__init__() Инициализируем родительский класс
    |    |
    |    |— Метод setWindowTitle(title: str) См.описание BasicWindow
    |    |
    |    |— Метод setWindowIcon(icon: QIcon) См.описание BasicWindow
    |    |
    |    |— setFixedSize(width: int, height: int) См.описание BasicWindow
    |    |
    |    |— Атрибут count. Используется для хранения значения счетчика окон
    |    |
    |    |— Атрибут menuBar хранит экземпяр объекта menuBar(), является
    |    |  родительским классом меню текущего окна
    |    |
    |    |— Атрибут fileMenu содержит метод addMenu(menu: str), служит
    |    |  для добавления пункта меню в родительский виджет QMenuBar
    |    |
    |    |— Метод addAction(action: QAction) атрибута fileMenu. Cлужит для 
    |    |  добавления действия New в fileMenu
    |    |
    |    |— Метод addAction(action: QAction) атрибута fileMenu. Cлужит для 
    |    |  добавления действия Exit в fileMenu
    |    |
    |    |— Сигнал triggered атрибута fileMenu. Устанавливает связь между атрибутом
    |    |  fileMenu и методом openSubWindow(self, command). Используется для обработки
    |    |  команд поступающих из атрибута menuBar
    |    |
    |    |— Атрибут mdi экземпяра класса QMdiArea, служит для хранения дочерних окон
    |    |
    |    |— Метод setCentralWidget(widget: QWidget) См.описание WidgetList
    |    |
    |
    |    
    |
    |————Метод openDialog(self)
         |
         |— Конструкция match:case принимающая в качестве параметра название
         |  действия выбранного с помощью виджета QmenuBar
         |  |
         |  |
         |  |— Ветвление 'New'
         |  |  |
         |  |  |— Атрибут win экземпяра класса QMdiSubWindow
         |  |  |
         |  |  |— Метод setWindowTitle(title: str) См.описание BasicWindow
         |  |  |
         |  |  |— Метод setWidget(widget: QWidget) экземпляра класса QMdiSubWindow.
         |  |  |  Служит для добавления виджета в родительский виджет QMdiSubWindow
         |  |  |
         |  |  |— Метод addSubWindow(widget: QWidget) экземпляра класса QMdiArea
         |  |  |  Добавляет дочернее окно в родительский виджет QMdiArea
         |  |  |
         |  |  |— Метод show() экземпляра класса QMdiSubWindow. Отображает дочернее
         |  |  |  окно в рамках родительского виджета QMdiArea
         |  |  |  
         |  |
         |  |— Ветвление 'Exit'
         |  |  |
         |  |  |— Метод close() экземпляра родительского класса QMainWindow
         |  |  |         
"""
    def __init__(self):
        super().__init__() # Инициализируем родительский класс QMainWindow
        self.setWindowTitle("QMultiDocument Widget") # Устанавливаем заголовок окна
        self.setWindowIcon(QIcon("./qt.ico")) # Устанавливаем иконку текущего окна c помощью класса QIcon
        self.setFixedSize(1200, 720) # Устанавливаем фиксированный размер текущего окна
        
        self.count = 0 # Инициализируем атрибут счетчика окон
        
        menuBar = self.menuBar() # # Инициализируем атрибут menuBar 
        
        fileMenu = menuBar.addMenu("File") # Добавляем пункт меню File
        fileMenu.addAction("New") # Добавляем подпункт меню New
        fileMenu.addAction("Exit") # Добавляем подпункт меню Exit
        fileMenu.triggered[QAction].connect(self.openSubWindow) # Устанавливаем сигнал triggered на атрибут fileMenu
        
        self.mdi = QMdiArea() # Инициализируем экземпляр класса QMdiArea
        
        self.setCentralWidget(self.mdi) # Устанавливаем widget в качестве главного виджета экземпляра класса QMainWindow

    def openSubWindow(self, command) -> None:
        match command.text():
            case "New":
                self.count += 1 # Увеличиваем значение счетчика
                win = QMdiSubWindow() # Инициализируем экземпляр класса QMdiSubWindow
                win.setWindowTitle(f"Дочернее окно {self.count}") # Уставливает заголовок окна с порядковым номером
                win.setWidget(QTextEdit()) # Устанавливаем центральный виджет атрибута win
                self.mdi.addSubWindow(win) # Добавляем дочернее окно в экземпляр класса QMdiArea
                win.show() # Отображаем добавленное окно
                
            case "Exit": self.close() # Закрываем родительское окно QMainWindow


class QDockWidgetDemonstration(QMainWindow):
    """
    Описание
    
        QDockWidgetDemonstration представляет собой приложение с графическим интерфейсом
        на PySide6, служит для демонстрации базового функционала виджета QDockWidget.
        Данный виджет служит для вынесения отдельных элементов логики пользовательского
        интерфейса (в нашем случае QListWidget) в дочернее окно родительского виджета
        QMainWindow.

        Пример использования выше разобранного виджета, а также структура класса
        QDockWidgetDemonstration представлены ниже


    Структура класса QDockWidgetDemonstration:
    |
    |————Конструктор (__init__(self))
    |    |
    |    |— Метод super().__init__() Инициализируем родительский класс
    |    |
    |    |— Метод setWindowTitle(title: str) См.описание BasicWindow
    |    |
    |    |— Метод setWindowIcon(icon: QIcon) См.описание BasicWindow
    |    |
    |    |— setFixedSize(width: int, height: int) См.описание BasicWindow
    |    |
    |    |— Атрибут widget См.описание WidgetList
    |    |
    |    |— Атрибут layout См.описание WidgetList
    |    |
    |    |— Атрибут items хранит экземпляр класса QDockWidget, предназначен для
    |    |  демонстрации базового функционала виджета QDockWidget
    |    |
    |    |— Атрибут itemList хранит экземпляр класса QListWidget. В парадигме приложения
    |    |  QDockWidgetDemonstration служит для инкапсуляции в виджет QDockWidget
    |    |
    |    |— Метод addItems(items: list) принимает в качестве агрумента список пронумерованных
    |    |  элементов
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
    |    |
    |    |— Метод setWidget(widget: QWidget) экземпляра класса QMdiSubWindow.
    |    |  Служит для добавления экземпляра класса QListWidget в родительский виджет QDockWidge
    |    |
    |    |— Метод addDockWidget(flag: DockWidgetArea, dockWidget: QDockWidget) экземпляра класса QMainWindow. 
    |    |  В качестве агрументов принимает значения констант подкласса DockWidgetArea, а также экземпляр класса
    |    |  QDockWidget, в контексте приложения QDockWidgetDemonstration, атрибут items
    |    |
    |    |— Метод setCentralWidget(widget: QWidget) См.описание WidgetList
    |    |
    """
    def __init__(self):
        super().__init__() # Инициализируем родительский класс QMainWindow
        self.setWindowTitle("QDockWidget Demonstration") # Устанавливаем заголовок окна
        self.setWindowIcon(QIcon("./qt.ico")) # Устанавливаем иконку текущего окна c помощью класса QIcon
        self.setFixedSize(700, 500) # Устанавливаем фиксированный размер текущего окна
        
        self.widget = QWidget() # Инициализируем экземпляр класса QWidget
        self.layout = QVBoxLayout() # Инициализируем экземпляр класса QVBoxLayout
        
        self.items = QDockWidget("Items") # Инициализируем экземпляр класса QDockWidget
        
        self.itemList = QListWidget() # Инициализируем экземпляр класса QListWidget
        self.itemList.addItems([ "Items 1", "Items 2", "Items 3", "Items 4", "Items 5"]) # Инкапсулируем значения в экземпляр класса QListWidget
        
        self.layout.addWidget(QTextEdit()) # Добавляем экземпляр класса QTextEdit в макет QVBoxLayout
        self.items.setWidget(self.itemList) # Добавляем центральный виджет атрибуту items
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.items) # Позиционируем экземпляр класса QDockWidget внутри родительского окна
        self.setCentralWidget(self.widget) # Устанавливаем widget в качестве главного виджета экземпляра класса QMainWindow


class QToolBoxWidget(QMainWindow):
    """
    Описание
        
        QToolBoxWidget представляет собой приложение с графическим интерфейсом
        на PySide6, служит для демонстрации базового функционала виджета QToolBox.
        Сам виджет QToolBox имеет ряд сходств с виджетами QTabWidget и QTabBar,
        и в сути своей является выпадающей вкладкой. Хорошо себя показывает в 
        программном обеспечении для редактирования документов, но также может быть
        применен в прочих пользовательских интерфейсах

        Структура класса QToolBoxWidget, а также демонстрация базового функционала
        виджета QToolBox представлены ниже

    Структура класса QToolBoxWidget:
    |
    |————Конструктор (__init__(self))
    |    |
    |    |— Метод super().__init__() Инициализируем родительский класс
    |    |
    |    |— Метод setWindowTitle(title: str) См.описание BasicWindow
    |    |
    |    |— Метод setWindowIcon(icon: QIcon) См.описание BasicWindow
    |    |
    |    |— setFixedSize(width: int, height: int) См.описание BasicWindow
    |    |
    |    |— Атрибут widget См.описание WidgetList
    |    |
    |    |— Атрибут layout См.описание WidgetList
    |    |
    |    |— Атрибут toolBox хранит экземпляр класса QToolBox, предназначен для
    |    |  демонстрации базового функционала виджета QToolBox
    |    |
    |    |— Метод addItem(widget: QWidget, title: str) экземпляра класса QToolBox.
    |    |  Предназначен для добавления дочернего виджета с заголовком, в экземпляр
    |    |  класса QToolBox
    |    |
    |    |— Метод addItem(widget: QWidget, title: str) См.описание QToolBoxWidget
    |    |
    |    |— Метод addItem(widget: QWidget, title: str) См.описание QToolBoxWidget
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
    |    |
    |    |— Метод setLayout(layout: QVBoxLayout) См.описание WidgetList
    |    |
    |    |— Метод setCentralWidget(widget: QWidget) См.описание WidgetList
"""
    def __init__(self):
        super().__init__() # Инициализируем родительский класс QMainWindow
        self.setWindowTitle("QToolBox Widget") # Устанавливаем заголовок окна
        self.setWindowIcon(QIcon("./qt.ico")) # Устанавливаем иконку текущего окна c помощью класса QIcon
        self.setFixedSize(700, 500) # Устанавливаем фиксированный размер текущего окна
        
        self.widget = QWidget() # Инициализируем экземпляр класса QWidget
        self.layout = QVBoxLayout() # Инициализируем экземпляр класса QVBoxLayout
        
        self.toolBox = QToolBox() # Инициализируем экземпляр класса QToolBox
        self.toolBox.addItem(QTextEdit(), "Документ 1") # Добавляем экземпяр класса QTextEdit в атрибут toolBox
        self.toolBox.addItem(QTextEdit(), "Документ 2") # Добавляем экземпяр класса QTextEdit в атрибут toolBox
        self.toolBox.addItem(QTextEdit(), "Документ 3") # Добавляем экземпяр класса QTextEdit в атрибут toolBox
        
        self.layout.addWidget(self.toolBox) # Добавляем атрибут toolBox в макет QVBoxLayout
        
        self.widget.setLayout(self.layout) # Устанавливаем layout в качестве макета родительского виджета с помощью метода setLayout()
        self.setCentralWidget(self.widget) # Устанавливаем widget в качестве главного виджета экземпляра класса QMainWindow


class QLCDNumberWidget(QMainWindow):  
    """
    Описание
        QLCDNumberWidget представляет собой приложение с графическим интерфейсом
        на PySide6, служит для демонстрации базового функционала виджета QLCDNumber.
        Является сколь концептуально любопытным, столь и бесполезным в разработке
        ПО виджетом, представляет собой крупную надпись хранящую целочисленные значения.
        В рамках практического применения может пригодится лишь в небольшом программном
        обеспечении, цель которого — демонстрация текущего времени
    
        Структура класса QLCDNumberWidget, а также пример использования виджета
        QLCDNumber представлены ниже

    Структура класса QLCDNumberWidget:
        |
        |————Конструктор (__init__(self))
        |    |
        |    |— Метод super().__init__() Инициализируем родительский класс
        |    |
        |    |— Метод setWindowTitle(title: str) См.описание BasicWindow
        |    |
        |    |— Метод setWindowIcon(icon: QIcon) См.описание BasicWindow
        |    |
        |    |— setFixedSize(width: int, height: int) См.описание BasicWindow
        |    |
        |    |— Атрибут widget См.описание WidgetList
        |    |
        |    |— Атрибут layout См.описание WidgetList
        |    |
        |    |— Атрибут lcd хранит экземпляр класса QLCDNumber, который
        |    |  предназначен для демонстрации базовых возможностей виджета QLCDNumber
        |    |
        |    |— Метод display(value: int) экземпляра класса QLCDNumber
        |    |  Устанавливает значение виджета QLCDNumber
        |    |
        |    |— Атрибут inputNumber хранит экземпляр класса QLineEdit,
        |    |  служит для получения от пользователя значений для ввода
        |    |  в виджет QLCDNumber
        |    |
        |    |— Метод setPlaceholderText(placeholder: str), экземпляра класса QLineEdit. См.описание QLineEditWidget
        |    |
        |    |— Сигнал textChanged атрибута inputNumber. Устанавливает связь между атрибутом inputNumber, и методом
        |    |  setValue(self)
        |    |
        |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
        |    |
        |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
        |    |
        |    |— Метод setLayout(layout: QVBoxLayout) См.описание WidgetList
        |    |
        |    |— Метод setCentralWidget(widget: QWidget) См.описание WidgetList
        |
        |————Метод setValue(self)
             |
             |— Ветвление 'if self.inputNumber.text().isdigit() and len(self.inputNumber.text()) <= 4'
             |  |
             |  |— Метод display(value: int) экземпляра класса QLCDNumber. См.описание QLCDNumberWidget
             |
             |——Ответвление
             |  |
             |  |— Метод setText экземпляра класса QLineEdit. В парадигме атрибута inputNumber обнуляет
             |  |  значение последнего
    """
    def __init__(self):
        super().__init__() # Инициализируем родительский класс QMainWindow
        self.setWindowTitle("QLCDNumber Widget") # Устанавливаем заголовок окна 
        self.setWindowIcon(QIcon("./qt.ico")) # Устанавливаем иконку текущего окна c помощью класса QIcon
        self.setFixedSize(700, 700) # Устанавливаем фиксированный размер текущего окна
        
        self.widget = QWidget() # Инициализируем экземпляр класса QWidget
        self.layout = QVBoxLayout() # Инициализируем экземпляр класса QVBoxLayout
        
        self.lcd = QLCDNumber(4) # Инициализируем экземпляр класса QLCDNumber
        self.lcd.display(1234) # Устанавливаем 4-х разрядное число в качестве начального значения
        
        self.inputNumber = QLineEdit() # Инициализируем экземпляр класса QLineEdit
        self.inputNumber.setPlaceholderText("Введите значение") # Устанавливаем placeholder виджета QLineEdit
        self.inputNumber.textChanged.connect(self.setValue) # Добавляем сигнал к атрибуту inputNumber
        
        self.layout.addWidget(self.lcd) # Добавляем атрибут lcd в макет QVBoxLayout
        self.layout.addWidget(self.inputNumber) # Добавляем атрибут inputNumber в макет QVBoxLayout

        self.widget.setLayout(self.layout) # Устанавливаем layout в качестве макета родительского виджета с помощью метода setLayout()
        self.setCentralWidget(self.widget) # Устанавливаем widget в качестве главного виджета экземпляра класса QMainWindow
        
    def setValue(self) -> None:
        # Реализуем простейшую валидацию данных, в случае если длина значения атрибута inputNumber меньше или равна 4, а также все
        # символы данного значения являются цифрами, присваиваем его атрибуту lcd
        if self.inputNumber.text().isdigit() and len(self.inputNumber.text()) <= 4: self.lcd.display(int(self.inputNumber.text())) 
        else: self.inputNumber.setText("") # В ином случае случае обнуляем значение атрибута inputNumber


class QDialWidget(QMainWindow):
    """
    Описание
        QDialWidget представляет собой приложение с графическим интерфейсом
        на PySide6, служит для демонстрации базового функционала виджета QDial.
        Наверняка хорошо знакомы пользователям ПО для обработки аудио или видео
        контента. В рамках пользовательского интерфейса является переключателем
        округлой формы, имеет функциональные сходства с виджетом QSlider,
        используется для выбора значения из предустановленного разработчиком 
        диапазона

        Структура класса QDialWidget, и пример использования виджета QDial
        представлены ниже

    Структура класса QDialWidget:
    |
    |————Конструктор (__init__(self))
    |    |
    |    |— Метод super().__init__() Инициализируем родительский класс
    |    |
    |    |— Метод setWindowTitle(title: str) См.описание BasicWindow
    |    |
    |    |— Метод setWindowIcon(icon: QIcon) См.описание BasicWindow
    |    |
    |    |— setFixedSize(width: int, height: int) См.описание BasicWindow
    |    |
    |    |— Атрибут widget См.описание WidgetList
    |    |
    |    |— Атрибут layout См.описание WidgetList
    |    |
    |    |— Атрибут text хранит экземпяр класса QLabel, служит
    |    |  для визуализации значения экземпляра класса QDial
    |    |
    |    |— Метод setFont(font: QFont) экземпляра класса QLabel. См.описание QLabelWidget
    |    |
    |    |— Метод setAlignment(flag: AlignmentFlag) экземпляра класса QLabel. См.описание QLabelWidget
    |    |
    |    |— Атрибут dial хранит экземпяр класса QDial, служит для демонстрации
    |    |  базовых возможностей виджета QDial
    |    |
    |    |— Метод setRange(min: int, max: int) экземпляра класса QDial,
    |    |  служит для установки диапазона допустимых значений виджета QDial
    |    |
    |    |— Метод setSingleStep(step: int) экземпляра класса QDial,
    |    |  устанавливает размер шага виджета QDial
    |    |
    |    |— Сигнал valueChanged атрибута dial. Устанавливает связь между атрибутом
    |    |  dial и методом setValue(self)
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
    |    |
    |    |— Метод setLayout(layout: QVBoxLayout) См.описание WidgetList
    |    |
    |    |— Метод setCentralWidget(widget: QWidget) См.описание WidgetList
    |
    |
    |————Метод setValue(self, value)
         |
         |— Метод setText(text: str) Устанавливаем текущее значение виджета QDial, в экземпляре класса QLabel
"""
    def __init__(self):
        super().__init__() # Инициализируем родительский класс QMainWindow
        self.setWindowTitle("QDial Widget") # Устанавливаем заголовок окна
        self.setWindowIcon(QIcon("./qt.ico")) # Устанавливаем иконку текущего окна c помощью класса QIcon
        self.setFixedSize(250, 250) # Устанавливаем фиксированный размер текущего окна
        
        self.widget = QWidget() # Инициализируем экземпляр класса QWidget
        self.layout = QVBoxLayout() # Инициализируем экземпляр класса QVBoxLayout
        
        self.text = QLabel("0") # Инициализируем экземпляр класса QLabel 
        self.text.setFont(QFont("Arial", 35)) # Устанавливаем параметры шрифта экземпляра класса QLabel
        self.text.setAlignment(Qt.AlignmentFlag.AlignHCenter) # Устанавливает тип выравнивания экземпляра класса QLabel
        
        self.dial = QDial() # Инициализируем экземпляр класса QDial
        self.dial.setRange(0, 200) # Устанавливаем диапазон допустимых значений
        self.dial.setSingleStep(1) # Устанавливаем длину шага виджета QDial
        self.dial.valueChanged.connect(self.setValue) # Устанавливаем сигнал valueChanged на атрибут dial
        
        self.layout.addWidget(self.dial) # Добавляем атрибут dial в макет QVBoxLayout
        self.layout.addWidget(self.text) # Добавляем атрибут text в макет QVBoxLayout
        
        self.widget.setLayout(self.layout) # Устанавливаем layout в качестве макета родительского виджета с помощью метода setLayout()
        self.setCentralWidget(self.widget) # Устанавливаем widget в качестве главного виджета экземпляра класса QMainWindow
    
    def setValue(self, value) -> None:
        self.text.setText(str(value)) # Устанавливаем значение экземпляра класса QLabel


class QMenuBarExample(QMainWindow):
    """
    Описание
        
        QMenuBarExample представляет собой приложение с графическим интерфейсом
        на PySide6, служит для демонстрации базового функционала виджета QMenuBar.
        QmenuBar является хорошо знакомым любом пользователю ПК меню, которое
        расположено в верхней части родительского окна. Может хранить в себе
        подменю содержащие команды на подобии открытия документа или перехода
        в настройки программы

        Структура класса QMenuBarExample, а также пример использования виджета
        QMenuBar представлены ниже

    Структура класса QMenuBarExample:
    |
    |————Конструктор (__init__(self))
    |    |
    |    |— Метод super().__init__() Инициализируем родительский класс
    |    |
    |    |— Метод setWindowTitle(title: str) См.описание BasicWindow
    |    |
    |    |— Метод setWindowIcon(icon: QIcon) См.описание BasicWindow
    |    |
    |    |— setFixedSize(width: int, height: int) См.описание BasicWindow
    |    |
    |    |— Атрибут menuBar хранит экземпяр объекта menuBar(), является
    |    |  родительским классом меню текущего окна
    |    |
    |    |— Атрибут fileMenu содержит метод addMenu(menu: str), служит
    |    |  для добавления пункта меню в родительский виджет QMenuBar
    |    |
    |    |— Атрибут aboutMenu содержит метод addMenu(menu: str), служит
    |    |  для добавления пункта меню в родительский виджет QMenuBar
    |    |
    |    |— Атрибут exitAction содержит экземпляр класса QAction(action: str, self), 
    |    |  служит для обьявления опции меню
    |    |
    |    |— Атрибут aboutAction содержит экземпляр класса QAction(action: str, self), 
    |    |  служит для обьявления опции меню
    |    |
    |    |— Сигнал triggered атрибута exitAction. Устанавливает связь между атрибутом
    |    |  exitAction и методом close() экземпляра класса QMainWindow. Используется для закрытия
    |    |  приложения
    |    |
    |    |— Метод addAction(action: QAction) служит для добавления подпунктов в пункты меню menuBar
    |    |
    |    |— Метод addAction(action: QAction) служит для добавления подпунктов в пункты меню menuBar
    |
    |
    |————Метод showAboutWindow(self)
         |
         |— Атрибут window экземпяра класса QMessageBoxWindow, в рамках метода showAboutWindow
         |  представляет собой информационное уведомление
         |
         |— Метод exec() Отображает информационное уведомление
    """
    def __init__(self):
        super().__init__() # Инициализируем родительский класс QMainWindow
        self.setWindowTitle("QMenuBar Widget") # Устанавливаем заголовок окна
        self.setWindowIcon(QIcon("./qt.ico")) # Устанавливаем иконку текущего окна c помощью класса QIcon
        self.setFixedSize(500, 300) # Устанавливаем фиксированный размер текущего окна
        
        menuBar = self.menuBar() # Инициализируем объект menuBar
        fileMenu = menuBar.addMenu("File") # Добавляем пункт меню File
        aboutMenu = menuBar.addMenu("About") # Добавляем пункт меню About
        exitAction = QAction("Exit", self) # Добавляем подпункт меню Exit
        aboutAction = QAction("About", self) # Добавляем подпункт меню About
        
        exitAction.triggered.connect(self.close) # Устанавливаем сигнал triggered на атрибут exitAction
        aboutAction.triggered.connect(self.showAboutWindow) # Устанавливаем сигнал triggered на атрибут aboutAction
        
        fileMenu.addAction(exitAction) # Добавляем подпункт меню в пункт меню fileMenu
        aboutMenu.addAction(aboutAction) # Добавляем подпункт меню в пункт меню aboutMenu

    def showAboutWindow(self) -> None:
        window = QMessageBoxWindow(title="Описание", icon=QMessageBox.Icon.Information, text="Описание программы") # Инициализируем экземпляр класса QMessageBoxWindow
        window.exec() # Отображаем информационное уведомление


class QDialogWidgets(QMainWindow):
    """
    Описание

    QDialogWidget — представляет собой приложение с графическим интерфейсом
    на PySide6. Служит для демонстрации возможностей классов QFileDialog, 
    QInputDialog, QFontDialog. Ранее перечисленные классы можно концептуально
    обьединить в единую группу под названием 'диалоговые' классы. Для лучшего
    понимания данной концепции стоит разобраться что из себя представляют сами
    диалоговые окна

        Диалоговые окна — в парадигме графических API современных операционных систем 
        в общем, и модуля QWidgets фреймворка PySide6 в частности представляют собой
        классифицированную по типам совокупность всплывающих дочерних главному окну
        окон, обычно выполняющих одну небольшую функцию, например извещение пользователя
        о некотором событии, получение единичного значения, выбор шрифта и т.д

    Существует великое множество диалоговых окон, однако в рамках приложения 
    QDialogWidgets мы рассмотрим лишь основные виды диалоговых окон
    
    
    Структура класса QDialogWidgets:
        |
        |————Конструктор (__init__(self))
        |    |
        |    |— Метод super().__init__() Инициализируем родительский класс
        |    |
        |    |— Метод setWindowTitle(title: str) См.описание BasicWindow
        |    |
        |    |— Метод setWindowIcon(icon: QIcon) См.описание BasicWindow
        |    |
        |    |— setFixedSize(width: int, height: int) См.описание BasicWindow
        |    |
        |    |— Атрибут widget См.описание WidgetList
        |    |
        |    |— Атрибут layout См.описание WidgetList
        |    |
        |    |— Атрибут text Используется для хранения экземпляра класса QLabel(text: str)
        |    |  Используется для отображения заголовка виджета QComboBox
        |    |
        |    |— Атрибут messageType экземпяр класса QComboBox, служит для хранения
        |    |  данных о типе диалогового окна
        |    |
        |    |— Метод addItems(items:list) принимает в качестве агрумента список
        |    |  содержащий данные о типах диалогового окна с типом данных 'str'
        |    |
        |    |— Атрибут openDialogButton хранит в себе экземпляр класса QPushButton,
        |    |  используется для открытия диалогового окна типа, что был выбран в QComboBox
        |    |
        |    |— Сигнал clicked атрибута openDialogButton. Устанавливает связь между атрибутом
        |    |  openDialogButton и методом openDialog(self)
        |    |
        |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
        |    |
        |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
        |    |
        |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
        |    |
        |    |— Метод setLayout(layout: QVBoxLayout) См.описание WidgetList
        |    |
        |    |— Метод setCentralWidget(widget: QWidget) См.описание WidgetList
        |
        |————Метод openDialog(self)
             |
             |— Конструкция match:case принимает в качестве параметра тип диалогового
             |   окна который возвращает метод currentText() принадлежащий экземпляру
             |   класса QComboBox из атрибута dialogType
             |  |
             |  |
             |  |— Ветвление 'QFileDialog'
             |  |  |
             |  |  |— Атрибут fileDialog хранит в себе экземпляр класса QFileDialog
             |  |  |
             |  |  |— Метод setWindowTitle(title: str) Используется для установки заголовка
             |  |  |  диалогового окна
             |  |  |
             |  |  |— Метод setFileMode(fileMode: FileMode) предназначен для установки
             |  |  |  ограничения на тип выбираемого файла или директории. В качестве
             |  |  |  параметра принимает значения констант из подкласса FileMode
             |  |  |
             |  |  |— Метод setViewMode Используется для выбора вида отображения
             |  |  |  диалогового окна QFileDialog. В качестве параметра принимает
             |  |  |  значения констант из подкласса FileMode
             |  |  |
             |  |  |— Ветвление 'if fileDialog.exec()'
             |  |  |  |
             |  |  |  |— Метод exec() экземпляра класса QFileDialog, используется для
             |  |  |  |  инициации отображения диалогового окна QFileDialog
             |  |  |  |
             |  |  |  |— Метод selectedFiles экземпляра класса QFileDialog. В случае 
             |  |  |  |  успешного отображения диалогового окна QFileDialog и как следствие
             |  |  |  |  выбора пользователем файлов, или директорий, возвращает их названия
             |  |  |  |  внутри списка с типом данных 'list[str]' для проведения дальнейших 
             |  |  |  |  операций
             |  |  |  |
             |  |  |  |— Метод setWindowTitle(title: str) в контексте приложения QDialogWidgets
             |  |  |  |  используется для вывода в заголовке текущего окна значений которые были
             |  |  |  |  получены от диалогового окна
             |  |
             |  |— Ветвление 'QInputDialog'
             |  |  |
             |  |  |— Атрибуты value и ok
             |  |  |  |
             |  |  |  |— Атрибут value Хранит в себе строку, что была получена из поля ввода
             |  |  |  |  диалогового окна QInputDialog
             |  |  |  |
             |  |  |  |— Атрибут ok с типом данных 'bool'. Хранит в себе результат проверки
             |  |  |  |  наличия некого значения в поле ввода диалогового окна QInputDialog
             |  |  |  |  В случае если поле ввода остается пустым, хранит в себе False
             |  |  |  |
             |  |  |  |— Ветвление 'if ok'
             |  |  |  |  |
             |  |  |  |  Метод setWindowTitle(title: str) в контексте приложения QDialogWidgets
             |  |  |  |  используется для вывода в заголовке текущего окна значений полученных
             |  |  |  |  от диалогового окна QInputDialog
             |  |  |
             |  |  |
             |  |
             |  |— Ветвление 'QFontDialog'
             |  |  |
             |  |  |— Атрибуты value и ok
             |  |  |  |
             |  |  |  |— Атрибут font Хранит в себе экземпляр класса с параметрами что были 
             |  |  |  |  получены из диалогового окна QFontDialog
             |  |  |  |
             |  |  |  |— Атрибут ok с типом данных 'bool'. Хранит в себе результат проверки
             |  |  |  |  наличия параметров шрифта полученных от диалогового окна QFontDialog
             |  |  |  |  В случае если шрифт не был выбран хранит в себе False
             |  |  |  |
             |  |  |  |— Ветвление 'if ok'
             |  |  |  |  |
             |  |  |  |  Метод setWindowTitle(title: str) в контексте приложения QDialogWidgets
             |  |  |  |  используется для вывода в заголовке окна названия шрифта что было получено
             |  |  |  |  от диалогового окна QFontDialog
             |  |  |
    """
    def __init__(self):
        super().__init__() # Инициализируем родительский класс QMainWindow
        self.setWindowTitle("QInputDialog Widget") # Устанавливаем заголовок окна
        self.setWindowIcon(QIcon("./qt.ico")) # Устанавливаем иконку текущего окна c помощью класса QIcon
        self.setFixedSize(400, 100) # Устанавливаем фиксированный размер текущего окна 
        
        self.widget = QWidget() # Инициализируем экземпляр класса QWidget
        self.layout = QVBoxLayout() # Инициализируем экземпляр класса QVBoxLayout
        
        self.text = QLabel("Выберите тип диалогового окна:") # Инициализируем экземпляр класса QLabel
        
        self.dialogType = QComboBox() # Инициализируем экземпляр класса QComboBox
        self.dialogType.addItems(["QInputDialog", "QFontDialog", "QFileDialog"])
        
        self.openDialogButton = QPushButton("Открыть") # Инициализируем экземпляр класса QPushButton
        self.openDialogButton.clicked.connect(self.openDialog)
        
        self.layout.addWidget(self.dialogType) # Добавляем dialogType в макет QVBoxLayout
        self.layout.addWidget(self.openDialogButton) # Добавляем атрибут openDialogButton в макет QVBoxLayout 
        
        self.widget.setLayout(self.layout) # Устанавливаем layout в качестве макета родительского виджета с помощью метода setLayout()
        self.setCentralWidget(self.widget) # Устанавливаем widget в качестве главного виджета экземпляра класса QMainWindow
    
    def openDialog(self) -> None:
        match self.dialogType.currentText():
            case "QFileDialog":
                fileDialog = QFileDialog() # Инициализируем экземпляр класса QFileDialog
                fileDialog.setWindowTitle("Open file") # Устанавливаем заголовок диалогового окна QFileDialog
                fileDialog.setFileMode(QFileDialog.FileMode.ExistingFile) # Устанавливаем допустимый для отображения тип файла
                fileDialog.setViewMode(QFileDialog.ViewMode.Detail) # Устанавливаем допустимый режим отображения файлов и директорий
                if fileDialog.exec():
                    filename = fileDialog.selectedFiles()[0].split('/') # Получаем имя выбранного файла его пути
                    self.setWindowTitle(f"QFileDialog Widget | Filename: {filename[len(filename)-1]}") # Отображаем значение полученное из диалогового окна QFileDialog
            
            case "QInputDialog":
                value, ok = QInputDialog().getText(self, "QInputDialog", "Введите значение") # Инициализируем экземпляр класса QInputDialog, а также его статус
                if ok: self.setWindowTitle(f"QInputDialog Widget | Value: {value}") # Отображаем значение полученное из диалогового окна QInputDialog

            case "QFontDialog":
                font, ok = QFontDialog().getFont(QFont("Arial", 25)) # Инициализируем экземпляр класса QFontDialog, а также его статус
                if ok: self.setWindowTitle(f"QFontDialog Widget | Font: {font.toString().split(',')[0]}") # Отображаем значение полученное из диалогового окна QFontDialog


class QMessageBoxWindow(QMessageBox):
    def __init__(self, title: str, icon: QIcon, text: str, choose=False):
        super().__init__() # Инициализируем родительский класс QMainWindow
        self.setWindowTitle(title) # Устанавливаем заголовок окна
        self.setIcon(icon) # Устанавливаем эквивалентную типу иконку диалогового окна
        self.setText(text) # Устанавливаем текст диалогового окна
        self.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No if choose else QMessageBox.StandardButton.Ok) # Устанавливаем кнопки диалогового окна
        self.exec() # Отображаем диалоговое окно


class QMessageBoxWidget(QMainWindow):
    """
    Описание:
        QMessageBoxWidget — представляет собой приложение с графическим интерфейсом
        на PySide6. Служит для демонстрации возможностей класса QMessageBox, и отлично
        от большинства предыдущих примеров наличием дополнительного класса QMessageBoxWindow,
        использование которого позволяет повысить читаемость кода, а также облегчить его
        поддержку и использование в других проектах. С прочими использованными виджетами
        вы наверняка уже знакомы из предыдущих примеров, однако мы в любом случае подробно
        рассмотрим структуру обоих классов

    Структура класса QMessageBoxWindow:
    |    
    |————Конструктор (__init__(self))
         |
         |— Метод super().__init__() Инициализируем родительский класс
         |
         |— Метод setWindowTitle(title: str) Устанавливаем заголовок окна уведомления
         |
         |— Метод setIcon(icon: Icon) Устанавливаем иконку из подкласса Icon которая 
         |  соответствует типу уведомления
         |
         |— Метод setText(text: str) Устанавливаем текст уведомления
         |
         |— Метод setStandardButtons При необходимости устанавливаем кнопки из подкласса StandardButton
         |  Как можно заметить, у нас есть возможность комбинировать кнопки из данного набора, передавая
         |  в качестве параметра функции результаты побитовой операции OR
         |
         |— Метод exec() Запускаем окно через базовый метод отображения окна

    Структура класса QMessageBoxWidget:
    |
    |————Конструктор (__init__(self))
    |    |
    |    |— Метод super().__init__() Инициализируем родительский класс
    |    |
    |    |— Метод setWindowTitle(title: str) См.описание BasicWindow
    |    |
    |    |— Метод setWindowIcon(icon: QIcon) См.описание BasicWindow
    |    |
    |    |— setFixedSize(width: int, height: int) См.описание BasicWindow
    |    |
    |    |— Атрибут widget См.описание WidgetList
    |    |
    |    |— Атрибут layout См.описание WidgetList
    |    |
    |    |— Атрибут text Используется для хранения экземпляра класса QLabel(text: str)
    |    |  Используется для отображения заголовка виджета QComboBox
    |    |
    |    |— Атрибут messageType экземпяр класса QComboBox, служит для хранения
    |    |  информации о типах уведомлений QMessageBox
    |    |
    |    |— Метод addItems(items: list) принимает в качестве агрумента список
    |    |  содержащий данные о типах уведомлений в типе данных 'str'
    |    |
    |    |— Атрибут openMessageBox хранит в себе экземпляр класса QPushButton,
    |    |  используется для открытия уведомления с типом, что был выбран в QComboBox
    |    |
    |    |— Сигнал clicked атрибута openMessageBox. Устанавливает связь между атрибутом
    |    |  openMessageBox и методом openWindow(self) при нажатии на вышеуказанный атрибут
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
    |    |
    |    |— Метод setLayout(layout: QVBoxLayout) См.описание WidgetList
    |    |
    |    |— Метод setCentralWidget(widget: QWidget) См.описание WidgetList
    |
    |————Метод openWindow(self)
         |
         |— Конструкция match:case принимающая в качестве параметра тип уведомления
         |  который возвращает метод currentText() принадлежащий экземпляру класса
         |  QComboBox из атрибута messageType
         |  |
         |  |
         |  |— Ветвление 'Information'
         |  |  |
         |  |  |— Инициализирует экземпляр класса QMessageBoxWindow с параметрами
         |  |  |  информационного окна
         |  |  
         |  |
         |  |— Ветвление 'Question'
         |  |  |
         |  |  |— Инициализирует экземпляр класса QMessageBoxWindow с параметрами
         |  |  |  окна подтверждения операции
         |  |
         |  |
         |  |— Ветвление 'Warning'
         |  |  |
         |  |  |— Инициализирует экземпляр класса QMessageBoxWindow с параметрами
         |  |  |  окна предупреждения
         |  |
         |  |
         |  |— Ветвление 'Critical'
         |  |  |
         |  |  |— Инициализирует экземпляр класса QMessageBoxWindow с параметрами
         |  |  |  окна ошибки
    """
    def __init__(self):
        super().__init__() # Инициализируем родительский класс QMainWindow
        self.setWindowTitle("QMessageBox Widget") # Устанавливаем заголовок окна
        self.setWindowIcon(QIcon("./qt.ico")) # Устанавливаем иконку текущего окна c помощью класса QIcon
        self.setFixedSize(300, 100) # Устанавливаем фиксированный размер текущего окна
        
        self.widget = QWidget() # Инициализируем экземпляр класса QWidget
        self.layout = QVBoxLayout() # Инициализируем экземпляр класса QVBoxLayout
        
        self.text = QLabel("Выберите тип уведомления:") # Инициализируем экземпляр класса QLabel
        
        self.messageType = QComboBox() # Инициализируем экземпляр класса QComboBox
        self.messageType.addItems(["Information", "Question", "Warning", "Critical"]) # Инкапсулируем значения в экземпляр класса QComboBox 
        
        self.openMessageBox = QPushButton("Открыть") # Инициализируем экземпляр класса QPushButton
        self.openMessageBox.clicked.connect(self.openWindow) # Устанавливает сигнал clicked на атрибут openMessageBox
        
        self.layout.addWidget(self.text) # Добавляем атрибут text в макет QVBoxLayout
        self.layout.addWidget(self.messageType) # Добавляем атрибут messageType в макет QVBoxLayout
        self.layout.addWidget(self.openMessageBox) # Добавляем атрибут openMessageBox в макет QVBoxLayout
        
        self.widget.setLayout(self.layout) # Устанавливаем layout в качестве макета родительского виджета с помощью метода setLayout()
        self.setCentralWidget(self.widget) # Устанавливаем widget в качестве главного виджета экземпляра класса QMainWindow

    def openWindow(self) -> None:
        match self.messageType.currentText():
            case "Information": QMessageBoxWindow(title="Information", icon=QMessageBox.Icon.Information, text="Информационное сообщение") # Отображаем информационное диалоговое окно
            case "Question": QMessageBoxWindow(title="Question", icon=QMessageBox.Icon.Question, text="Подтверждение действия", choose=True) # Отображаем диалоговое окно подтверждения
            case "Warning": QMessageBoxWindow(title="Warning", icon=QMessageBox.Icon.Warning, text="Предупреждение") # Отображаем предупреждающее диалоговое окно
            case "Critical": QMessageBoxWindow(title="Critical", icon=QMessageBox.Icon.Critical, text="Сообщение об ошибке") # Отображаем диалоговое окно сообщающее об ошибке


class QSplitterWidget(QMainWindow):
    """
    Описание

    QSplitterWidget представляет собой приложение с графическим интерфейсом
    на PySide6. Служит для демонстрации возможностей класса QSplitter. Сам
    виджет QSplitter является не совсем стандартным виджетом в совокупности
    виджетов что были рассмотрены ранее. QSplitter можно описать как невидимый
    контейнер, который может хранить в сeбе некую совокупность виджетов, и 
    предоставлять пользователю возможность их масштабирования т.е изменение
    размера внутри родительского контейнера

    Структура классса QSplitterWidget и демонстрация базовых возможностей
    виджета QSplitter представлены ниже
    

    Структура класса QSplitterWidget:
    |
    |————Конструктор (__init__(self))
    |    |
    |    |— Метод super().__init__() Инициализируем родительский класс
    |    |
    |    |— Метод setWindowTitle(title: str) См.описание BasicWindow
    |    |
    |    |— Метод setWindowIcon(icon: QIcon) См.описание BasicWindow
    |    |
    |    |— setFixedSize(width: int, height: int) См.описание BasicWindow
    |    |
    |    |— Атрибут widget См.описание WidgetList
    |    |
    |    |— Атрибут layout См.описание WidgetList
    |    |
    |    |— Атрибут splitter содержит экземпяр класса QSplitter.
    |    |  Используется для демонстрации базового функционала виджета QSplitter
    |    |
    |    |— Атрибут textEdit1 содержит экземпяр класса QTextEdit.
    |    |  Выступает в качестве дочернего виджета экземпляра класса QSplitter
    |    |  
    |    |— Атрибут textEdit2 содержит экземпяр класса QTextEdit.
    |    |  Дочерний виджет экземпляра класса QSplitter   
    |    |
    |    |— Атрибут textEdit3 содержит экземпяр класса QTextEdit.
    |    |  Является дочерним виджетом экземпляра класса QSplitter
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
    |    |
    |    |— Метод setLayout(layout: QVBoxLayout) См.описание WidgetList
    |    |
    |    |— Метод setCentralWidget(widget: QWidget) См.описание WidgetList
   """
    def __init__(self):
        super().__init__() # Инициализируем родительский класс QMainWindow
        self.setWindowTitle("QSplitter Widget") # Устанавливаем заголовок окна
        self.setWindowIcon(QIcon("./qt.ico")) # Устанавливаем иконку текущего окна c помощью класса QIcon
        self.setFixedSize(500, 500) # Устанавливаем фиксированный размер текущего окна
        
        self.widget = QWidget() # Инициализируем экземпляр класса QWidget 
        self.layout = QVBoxLayout() # Инициализируем экземпляр класса QVBoxLayout
        
        self.splitter = QSplitter(Qt.Orientation.Vertical) # Инициализируем экземпляр класса QLabel с вертикальной ориентацией
        
        self.textEdit1 = QTextEdit() # Инициализируем экземпляр класса QTextEdit
        self.textEdit2 = QTextEdit() # Инициализируем экземпляр класса QTextEdit
        self.textEdit3 = QTextEdit() # Инициализируем экземпляр класса QTextEdit
        
        self.splitter.addWidget(self.textEdit1) # Добавляем атрибут textEdit1 в макет QVBoxLayout
        self.splitter.addWidget(self.textEdit2) # Добавляем атрибут textEdit2 в макет QVBoxLayout
        self.splitter.addWidget(self.textEdit3) # Добавляем атрибут textEdit3 в макет QVBoxLayout         
        self.layout.addWidget(self.splitter) # Добавляем атрибут splitter в макет QVBoxLayout

        self.widget.setLayout(self.layout) # Устанавливаем layout в качестве макета родительского виджета с помощью метода setLayout()
        self.setCentralWidget(self.widget) # Устанавливаем widget в качестве главного виджета экземпляра класса QMainWindow


class QTabWidgetDemonstration(QTabWidget):
    """
    Описание

        QTabWidgetDemonstration представляет собой приложение с графическим
        интерфейсом на PySide6. Служит для демонстрации возможностей виджета
        QTabWidget. Данный виджет предоставляет разработчику возможность
        умещать интерфейсы содержащие большое количество внутренней логики
        внутри одного окна фиксированного размера. Переключение между частями
        подобного интерфейса происходит посредством взаимодействия с знакомым
        каждому пользователю ПК виджета — вкладок
        
        Структура класса QTabWidgetDemonstration, а также демонстрация базового
        функционала виджета QTabWidget представлены ниже

    Структура класса QTabWidgetDemonstration:
        |
        |————Конструктор (__init__(self))
        |    |
        |    |— Метод super().__init__() Инициализируем родительский класс
        |    |
        |    |— Метод setWindowTitle(title: str) См.описание BasicWindow
        |    |
        |    |— Метод setWindowIcon(icon: QIcon) См.описание BasicWindow
        |    |
        |    |— Атрибут tab1 экземпяр класса QWidget. Инициализирует объект
        |    |  вкладки
        |    |
        |    |— Атрибут tab1 экземпяр класса QWidget. Инициализирует объект
        |    |  вкладки
        |    |
        |    |— Атрибут tab2 экземпяр класса QWidget. Инициализирует объект
        |    |  вкладки
        |    |
        |    |— Атрибут tab3 экземпяр класса QWidget. Инициализирует объект
        |    |  вкладки
        |    |
        |    |— Метод addTab(tab: QWidget, name: str) экземпляра класса QTabWidget, используется для
        |    |  добавления вкладки в родительский виджет
        |    |
        |    |— Метод addTab(tab: QWidget, name: str) экземпляра класса QTabWidget, используется для
        |    |  добавления вкладки в родительский виджет
        |    |
        |    |— Метод addTab(tab: QWidget, name: str) экземпляра класса QTabWidget, используется для
        |    |  добавления вкладки в родительский виджет
        |    |
        |    |— Метод setTabText(index: int title: str) экземпляра класса QTabWidget, служит для
        |    |  установки заголовка вкладки по ее индексу
        |    |
        |    |— Метод setTabText(index: int title: str) экземпляра класса QTabWidget, служит для
        |    |  установки заголовка вкладки по ее индексу
        |    |
        |    |— Метод setTabText(index: int title: str) экземпляра класса QTabWidget, служит для
        |    |  установки заголовка вкладки по ее индексу
        |    | 
        |    |— Метод showNameForm(self) служит для инициализации вкладки Personal
        |    |
        |    |— Метод showBornForm(self) служит для инициализации вкладки Born
        |    |
        |    |— Метод showAddressForm(self) служит для инициализации вкладки Address
        |
        |
        |————Метод showNameForm(self)
        |    |
        |    |— Атрибут nameTabLayout См.описание WidgetList
        |    |
        |    |— Атрибут surnameInput экземпляр класса QLineEdit, служит для 
        |    |  получения от пользователя информации о его фамилии 
        |    |
        |    |— Метод setPlaceholderText(placeholder: str), экземпляра класса QLineEdit. См описание QLineEditWidget
        |    |
        |    |— Атрибут surnameInput экземпляр класса QLineEdit, служит для 
        |    |  получения от пользователя информации о его имени
        |    |
        |    |— Метод setPlaceholderText(placeholder: str), экземпляра класса QLineEdit. См описание QLineEditWidget
        |    |
        |    |— Метод addRow(widget: QWidget) См.описание QFormLayout
        |    |
        |    |— Метод addRow(widget: QWidget) См.описание QFormLayout
        |    |
        |    |— Метод setLayout(layout: QVBoxLayout) См.описание WidgetList 
        |
        |
        |————Метод showBornForm(self)
        |    |
        |    |— Атрибут bornTabLayout См.описание WidgetList
        |    |
        |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
        |    |
        |    |— Метод setLayout(layout: QVBoxLayout) См.описание WidgetList        
        |    
        |
        |————Метод showAddressForm(self)
             |
             |— Атрибут addressTabLayout См.описание WidgetList
             |
             |— Атрибут cityInput экземпляр класса QLineEdit, служит для 
             |  получения от пользователя информации о городе в котором он проживает
             |
             |— Метод setPlaceholderText(placeholder: str), экземпляра класса QLineEdit. См описание QLineEditWidget
             |
             |— Атрибут streetInput экземпляр класса QLineEdit, служит для 
             |  получения от пользователя информации об улице на которой он проживает 
             |
             |— Метод setPlaceholderText(placeholder: str), экземпляра класса QLineEdit. См описание QLineEditWidget
             |
             |— Метод addRow(widget: QWidget) См.описание QFormLayout
             |
             |— Метод addRow(widget: QWidget) См.описание QFormLayout
             |
             |— Метод setLayout(layout: QVBoxLayout) См.описание WidgetList
    """
    def __init__(self):
        super().__init__() # Инициализируем родительский класс QMainWindow
        self.setWindowTitle("QTabBar Widget") # Устанавливаем заголовок окна
        self.setWindowIcon(QIcon("./qt.ico")) # Устанавливаем иконку текущего окна c помощью класса QIcon
        
        self.tab1 = QWidget() # Инициализируем экземпляр класса QWidget
        self.tab2 = QWidget() # Инициализируем экземпляр класса QWidget
        self.tab3 = QWidget() # Инициализируем экземпляр класса QWidget
        
        self.addTab(self.tab1, "Tab 1") # Добавляем вкладку экземпляру класса QTabWidget
        self.addTab(self.tab2, "Tab 2") # Добавляем вкладку экземпляру класса QTabWidget
        self.addTab(self.tab3, "Tab 3") # Добавляем вкладку экземпляру класса QTabWidget
        
        self.setTabText(0, "Personal") # Устанавливаем название вкладки
        self.setTabText(1, "Born") # Устанавливаем название вкладки
        self.setTabText(2, "Address") # Устанавливаем название вкладки
        
        self.showNameForm() # Инициализируем вкладку showNameForm
        self.showBornForm() # Инициализируем вкладку showBornForm
        self.showAddressForm() # Инициализируем вкладку showAddressForm


    def showNameForm(self) -> None:
        self.nameTabLayout = QFormLayout() # Инициализируем экземпляр класса макета QFormLayout
        self.surnameInput = QLineEdit() # Инициализируем экземпляр класса QLineEdit
        self.surnameInput.setPlaceholderText("Фамилия") # Устанавливаем placeholder виджета QLineEdit
        self.nameInput = QLineEdit() # Инициализируем экземпляр класса QLineEdit
        self.nameInput.setPlaceholderText("Имя") # Устанавливаем placeholder виджета QLineEdit 
        self.nameTabLayout.addRow("Фамилия", self.surnameInput) # Добавляем атрибут textEdit1 в макет QFormLayout
        self.nameTabLayout.addRow("Имя", self.nameInput) # Добавляем атрибут textEdit1 в макет QFormLayout
        self.tab1.setLayout(self.nameTabLayout) # Устанавливаем layout в качестве макета родительского виджета с помощью метода setLayout()
        
    def showBornForm(self) -> None:
        self.bornTabLayout = QVBoxLayout() # Инициализируем экземпляр класса макета QVBoxLayout
        self.bornTabLayout.addWidget(QDateEdit()) # Добавляем жкземпляр класса QDateEdit в родительский макет
        self.tab2.setLayout(self.bornTabLayout) # Устанавливаем layout в качестве макета родительского виджета с помощью метода setLayout()
    
    def showAddressForm(self) -> None:
        self.addressTabLayout = QFormLayout() # Инициализируем экземпляр класса макета QFormLayout
        self.cityInput = QLineEdit() # Инициализируем экземпляр класса QLineEdit
        self.cityInput.setPlaceholderText("Город") # Устанавливаем placeholder виджета QLineEdit
        self.streetInput = QLineEdit() # Инициализируем экземпляр класса QLineEdit
        self.streetInput.setPlaceholderText("Улица") # Устанавливаем placeholder виджета QLineEdit
        self.addressTabLayout.addRow( "Город", self.cityInput) # Добавляем атрибут textEdit1 в макет QFormLayout
        self.addressTabLayout.addRow("Улица", self.streetInput) # Добавляем атрибут textEdit1 в макет QFormLayout
        self.tab3.setLayout(self.addressTabLayout) # Устанавливаем layout в качестве макета родительского виджета с помощью метода setLayout()
    
class QTabBarWidget(QMainWindow):
    """
    Описание

        QTabBarWidget представляет собой приложение с графическим
        интерфейсом на PySide6. Служит для демонстрации возможностей виджета
        QTabBar. Данный виджет мало чем отличен рассмотренного ранее виджета
        QTabWidget, данный виджет также предоставляет возможность разделения
        логики крупных интерфейсов на отдельные части с помощью вкладков,
        поэтому будет лишен чрезчур подробного описания

        Структура класса QTabBarWidget, а также пример использования
        данного виджета представлены ниже


    Структура класса QTabBarWidget
    |
    |————Конструктор(__init__(self))
    |    |
    |    |— Метод super().__init__() для инициализации
    |    |  родительского класса QMainWindow
    |    |
    |    |— Метод setWindowTitle(title: str) См.описание BasicWindow
    |    |  
    |    |— Метод setFixedSize(width: int, height: int) См.описание BasicWindow
    |    |
    |    |— Метод setWindowIcon(QIcon(icon_path: str)) См.описание BasicWindow
    |    |
    |    |— Атрибут text экземпляр класса QLabel, служит для демонстрации номера
    |    |  выбранного подменю
    |    |
    |    |— Метод setFont(QFont(font: str, textSize: int)) См.описание QLabelWidget  
    |    |
    |    |— Метод setAlignment(QFont(flag: AlignmentFlag) См.описание QLabelWidget  
    |    |
    |    |— Атрибут tabBar хранит экземпляр класса QTabBar, используется для демонстрации
    |    |  базового функционала виджета QTabBar
    |    |
    |    |— Метод addTab(title: str) служит для добавления вкладки к экземпляру класса QTabBar 
    |    |
    |    |— Метод addTab(title: str) См.описание QTabBarWidget
    |    |
    |    |— Метод addTab(title: str) См.описание QTabBarWidget
    |    |
    |    |— Сигнал currentChanged атрибута tabBar. Устанавливает связь между атрибутом
    |    |  tabBar и методом setValue(self, value)
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
    |    |
    |    |— Метод setLayout(layout: QVBoxLayout) См.описание WidgetList
    |    |
    |    |— Метод setCentralWidget(widget: QWidget) См.описание WidgetList
    |
    |————Метод setValue(self, value)
         |
         |— Метод setText(text: str) атрибута text, в парадигме приложения QTabBarWidget,
         |  служит для изменения значения текущей вкладки
         |
    """
    def __init__(self):
        super().__init__() # Инициализируем родительский класс QMainWindow
        self.setWindowTitle("QTabBar Widget") # Устанавливаем заголовок окна 
        self.setWindowIcon(QIcon("./qt.ico")) # Устанавливаем иконку текущего окна c помощью класса QIcon
        self.setFixedSize(500, 500) # Устанавливаем фиксированный размер текущего окна
        
        self.widget = QWidget() # Инициализируем экземпляр класса QWidget
        self.layout = QVBoxLayout() # Инициализируем экземпляр класса QVBoxLayout
        
        self.text = QLabel("Вкладка 1") # Инициализируем экземпляр класса QLabel
        self.text.setFont(QFont("Arial", 30)) # Устанавливаем размер и шрифт экземпляра класса QLabel
        self.text.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter) # Позиционируем экземпляр класса QLabel
        
        self.tabBar = QTabBar() # Инициализируем экземпляр класса QTabBar
        self.tabBar.addTab("Tab 1") # Добавляем вкладку в экземпляр класса QTabBar
        self.tabBar.addTab("Tab 2") # Добавляем вкладку в экземпляр класса QTabBar
        self.tabBar.addTab("Tab 3") # Добавляем вкладку в экземпляр класса QTabBar
        self.tabBar.currentChanged.connect(self.setValue) # Устанавливает сигнал currentChanged на атрибут tabBar
        
        self.layout.addWidget(self.tabBar) # Добавляем атрибут tabBar в макет QVBoxLayout
        self.layout.addWidget(self.text) # Добавляем атрибут text в макет QVBoxLayout
        
        self.widget.setLayout(self.layout) # Устанавливаем layout в качестве макета родительского виджета с помощью метода setLayout()
        self.setCentralWidget(self.widget) # Устанавливаем widget в качестве главного виджета экземпляра класса QMainWindow

    def setValue(self, value) -> None:
        self.text.setText(f"Вкладка {value + 1}") # Устанавливаем новое значение вкладки


class QDragAndDropWidget(QMainWindow):
    """
    Описание
    
        QDragAndDropWidget представляет собой приложение с графическим
        интерфейсом на PySide6. Служит для демонстрации возможностей
        функции Drag&Drop. В отличии рассмотренных ранее виджетов,
        считать Drag&Drop виджетом, было некорректно. DraG&Drop
        можно охаракетеризовать как дочернюю функцию виджетов из
        модуля QWidgets, которая предоставляет возможность их
        перетаскивание в рамках родительского виджета

        Пример использования функции Drag&Drop, а также структура
        класса QDragAndDropWidget будет представлена ниже
    
    Структура класса QDragAndDropWidget:
    |
    |————Конструктор (__init__(self))
    |    |
    |    |— Метод super().__init__() Инициализируем родительский класс
    |    |
    |    |— Метод setWindowTitle(title: str) См.описание BasicWindow
    |    |
    |    |— Метод setWindowIcon(icon: QIcon) См.описание BasicWindow
    |    |
    |    |— setFixedSize(width: int, height: int) См.описание BasicWindow
    |    |
    |    |— Атрибут widget См.описание WidgetList
    |    |
    |    |— Атрибут layout См.описание WidgetList
    |    |
    |    |— Атрибут firstList содержит экземпяр класса QListWidget,
    |    |  используется для демонстрации возможностей функции QDrag&Drop
    |    |
    |    |— Атрибут secondList содержит экземпяр класса QListWidget,
    |    |  используется для демонстрации возможностей функции QDrag&Drop
    |    |
    |    |— Метод addItems экземпляра класса QListWidget. См.описание QListWidgetExample
    |    |
    |    |— Метод addItems экземпляра класса QListWidget. См.описание QListWidgetExample
    |    |
    |    |——Цикл for итерирующийся по списку содержащему атрибуты firstList и secondList 
    |    |  |
    |    |  |— Метод setDragEnabled(value: bool) экземпляра класса QListWidget.
    |    |  |  Разрешает изьятие элемента из родительского списка
    |    |  |
    |    |  |— Метод setAcceptDrops(value: bool) экземпляра класса QListWidget.
    |    |  |  Разрешает добавление элементов извне в родительский список
    |    |  |
    |    |  |— Метод setDropIndicatorShown(value: bool) экземпляра класса QListWidget.
    |    |  |  Включает индикацию элементов при перетаскивании
    |    |  |
    |    |  |— Метод setDragDropMode(flag: DragDropMode) экземпляра класса QListWidget.
    |    |  |  Позволяет выбрать режим работы QDrag&Drop 
    |    |  |
    |    |  |— Метод setDefaultDropAction(flag: DropAction) экземпляра класса QListWidget.
    |    |  |  в контексте приложения QDragAndDropWidget был выбран режим перемещения элементов, 
    |    |  |  а не копирования, что установлен по умолчанию
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
    |    |
    |    |— Метод setLayout(layout: QVBoxLayout) См.описание WidgetList
    |    |
    |    |— Метод setCentralWidget(widget: QWidget) См.описание WidgetList
    """
    def __init__(self):
        super().__init__() # Инициализируем родительский класс QMainWindow
        self.setWindowTitle("QDrag&Drop Widget") # Устанавливаем заголовок окна
        self.setWindowIcon(QIcon("./qt.ico")) # Устанавливаем иконку текущего окна c помощью класса QIcon
        self.setFixedSize(500, 500) # Устанавливаем фиксированный размер текущего окна
        
        self.widget = QWidget() # Инициализируем экземпляр класса QWidget
        self.layout = QHBoxLayout() # Инициализируем экземпляр класса QVBoxLayout
        
        self.firstList = QListWidget() # Инициализируем экземпляр класса QListWidget
        self.secondList = QListWidget() # Инициализируем экземпляр класса QListWidget
        
        self.firstList.addItems(["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]) # Добавляем элементы в атрибут firstList
        self.secondList.addItems(["Item 6", "Item 7", "Item 8"]) # Добавляем элементы в атрибут secondList

        for itemList in [self.firstList, self.secondList]:
            itemList.setDragEnabled(True) # Разрешаем взятие элементов из итерируемого экземпляра класса QListWidget
            itemList.setAcceptDrops(True) # Разрешаем добавление элементов в итерируемый экземпляр класса QListWidget
            itemList.setDropIndicatorShown(True) # Включаем отображение индикатора при пeретаскивании
            itemList.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop) # Устанавливаем режим работы QDrag&Drop
            itemList.setDefaultDropAction(Qt.DropAction.MoveAction) # Устанавливаем режим перемещения элементов

        self.layout.addWidget(self.firstList) # Добавляем атрибут firstList в макет QVBoxLayout
        self.layout.addWidget(self.secondList) # Добавляем атрибут secondList в макет QVBoxLayout

        self.widget.setLayout(self.layout) # Устанавливаем layout в качестве макета родительского виджета с помощью метода setLayout()
        self.setCentralWidget(self.widget) # Устанавливаем widget в качестве главного виджета экземпляра класса QMainWindow


class QTableViewWidget(QMainWindow):
    """
    
        QTableViewWidget представляет собой приложение с графическим
        интерфейсом на PySide6. Служит для демонстрации функционала виджета
        QTableView. Сам же виджет QTableView, в рамках пользовательского
        интерфейса является обыкновенной таблицей содержащей заголовки, 
        ячейки, столбцы и строки. Следы использования данного виджета вы
        наверняка можно наблюдать в программном обеcпечении для работы
        с таблицами, или реляционными базами данных на подобии SQL

        Структура класса QTableViewWidget, а также демонстрация возможностей
        виджета QTableView представлены ниже

    Структура класса QTableViewWidget:
    |
    |————Конструктор (__init__(self))
    |    |
    |    |— Метод super().__init__() Инициализируем родительский класс
    |    |
    |    |— Метод setWindowTitle(title: str) См.описание BasicWindow
    |    |
    |    |— Метод setWindowIcon(icon: QIcon) См.описание BasicWindow
    |    |
    |    |— setFixedSize(width: int, height: int) См.описание BasicWindow
    |    |
    |    |— Атрибут widget См.описание WidgetList
    |    |
    |    |— Атрибут layout См.описание WidgetList
    |    |
    |    |— Атрибут title экземпляра класса QLabel, содержит в себе заголовок
    |    |  приложения QTableViewWidget
    |    |
    |    |— Метод setAlignment(flag: AlignmentFlag) экземпляра класса QLabel. См.описание QLabelWidget
    |    |
    |    |— Атрибут model экземпляра класса QStandardItemModel, содержит модель данных
    |    |  для дальнейшей инкапсуляции в экземпляр класса QTableView
    |    |
    |    |— Метод setHorizontalHeaderLabels(titles: list) экземпляра класса QStandardItemModel
    |    |  Служит для установки заголовков таблицы с горизонтальной ориентацией
    |    |
    |    |— Двумерный список rows:list[list[QStandardItem]]. Содержит в себе совокупность списков
    |    |  хранящий в себе экземпляры класса QStandardItem с значениями типа данных 'str', а также
    |    |  предназначен для дальнейшей инкапсуляции в экземпляр класса QStandardItemModel
    |    |
    |    |— Вложенный цикл for итерирующийся по двумерному списку экземпляров класса QStandardItem
    |    |  |
    |    |  |— Метод setTextAlignment(flag: AlignmentFlag) экземпляра класса QStandardItem. Служит для
    |    |  |  выравнивания значений что хранит экземпляр класса QStandardItem
    |    |  |
    |    |
    |    |— Генератор списков наполняющий атрибут model списками экзепляров класса QStandardItem 
    |    |
    |    |— Атрибут table экземпляра класса QTableView, представляет собой виджет который принято называть
    |    |  таблицой
    |    |
    |    |— Метод setModel(model: QStandardItemModel) экземпляра класса QTableView. Предназначен
    |    |  инкапсуляции модели данных в экземпляр класса QTableView
    |    |
    |    |— Метод resizeColumnsToContents() экземпляра класса QTableView.
    |    |  Служит для выравнивания ширины столбцов по размерам их содержимого
    |    |
    |    |— Метод setStretchLastSection(value: bool) экземпляра класса QTableView.
    |    |  Служит вытягивания последнего столбца до края таблицы
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
    |    |
    |    |— Метод addWidget(widget: QWidget) См.описание WidgetList
    |    |
    |    |— Метод setLayout(layout: QVBoxLayout) См.описание WidgetList
    |    |
    |    |— Метод setCentralWidget(widget: QWidget) См.описание WidgetList
"""
    def __init__(self):
        super().__init__() # Инициализируем родительский класс QMainWindow
        self.setWindowTitle("QTableView Widget") # Устанавливаем заголовок окна
        self.setWindowIcon(QIcon("./qt.ico")) # Устанавливаем иконку текущего окна c помощью класса QIcon
        self.setFixedSize(1000, 500) # Устанавливаем фиксированный размер текущего окна

        self.widget = QWidget() # Инициализируем экземпляр класса QWidget
        self.layout = QVBoxLayout() # Инициализируем экземпляр класса QVBoxLayout
        
        self.title = QLabel("Список популярных языков программирования") # Инициализируем экземпляр класса QLabel
        self.title.setAlignment(Qt.AlignmentFlag.AlignHCenter) # Позиционируем виджет QLabel
        
        self.model = QStandardItemModel() # Инициализируем экземпляр класса QStandardItemModel
        
        self.model.setHorizontalHeaderLabels(["Язык программирования", "Создатель", "Год создания", "Уровень сложности", "Парадигма",
        "Официальный сайт"]) # Устанавливаем горизонтальные заголовки столцов
        
        self.rows = [
                    [QStandardItem("Python"), QStandardItem("Гвидо ван Россум"), QStandardItem("1991"), 
                     QStandardItem("Легкий"), QStandardItem("Парадигма ООП"), QStandardItem("https://python.org/")],
                    [QStandardItem("Ruby"), QStandardItem("Деннис Ритчи"), QStandardItem("1993"), 
                     QStandardItem("Средний"), QStandardItem("Мульти-парадигмальный"), QStandardItem("https://www.ruby-lang.org/")],
                    [QStandardItem("С++"), QStandardItem("Бьерн Страуступ"), QStandardItem("1985"),
                     QStandardItem("Высокий"), QStandardItem("Мульти-парадигмальный"), QStandardItem("https://isocpp.org/")],
                    [QStandardItem("PHP"), QStandardItem("Расмус Лердорф"), QStandardItem("1994"),
                     QStandardItem("Средний"), QStandardItem("Парадигма ООП"), QStandardItem("https://php.net/")]
                    ] # Обьявляем двумерных список, хранящий значения для вставки в таблицу
        
        for row in self.rows:
            for item in row:
                item.setTextAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter) # Центрируем значение итерируемой ячейки

        [self.model.appendRow(row) for row in self.rows] # Добавляем строки в модель с помощью генератора списков
        
        self.table = QTableView() # Инициализируем экземпляр класса QTableView
        self.table.setModel(self.model) # Устанавливаем атрибут model, в качестве модели виджета QTableView
        
        self.table.resizeColumnsToContents() # Форматируем размер столбцов по размеру содержимого ячеек
        self.table.horizontalHeader().setStretchLastSection(True) # Растягиваем последний столбец по края таблицы
        
        self.layout.addWidget(self.title) # Добавляем атрибут title в макет QVBoxLayout
        self.layout.addWidget(self.table) # Добавляем атрибут table в макет QVBoxLayout 
        
        self.widget.setLayout(self.layout) # Устанавливаем layout в качестве макета родительского виджета с помощью метода setLayout()
        self.setCentralWidget(self.widget) # Устанавливаем widget в качестве главного виджета экземпляра класса QMainWindow



def main() -> None:
    app = QApplication(argv) # Инициализируем экземпляра класса QApplication 
    gui = BasicWindow() # Инициализируем экземпляр класса приложения
    gui.show() # Отображаем главное окно приложения
    app.exec() # Запускаем приложение

if __name__ == '__main__': main()
