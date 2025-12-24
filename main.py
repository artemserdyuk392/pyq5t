# импорт необходимых библиотек
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QVBoxLayout, QPushButton, QComboBox
)
import matplotlib.pyplot as plt


class AmortizationApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Расчет годовой амортизации")
        self.setGeometry(100, 100, 500, 450)

        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        # Заголовок
        self.label0 = QLabel("Расчет годовой амортизации")
        self.layout.addWidget(self.label0)

        # Тип основного средства
        self.label1 = QLabel("Тип основного средства")
        self.layout.addWidget(self.label1)

        self.combo = QComboBox(self)
        self.combo.addItems(["Комбайн", "Трактор", "Плуг"])
        self.combo.currentTextChanged.connect(self.update_life_time)
        self.layout.addWidget(self.combo)

        # Срок эксплуатации
        self.label2 = QLabel("Срок эксплуатации (лет)")
        self.layout.addWidget(self.label2)

        self.lineedit_life = QLineEdit(self)
        self.lineedit_life.setReadOnly(True)
        self.layout.addWidget(self.lineedit_life)

        # Балансовая стоимость
        self.label3 = QLabel("Балансовая стоимость, тыс. руб.")
        self.layout.addWidget(self.label3)

        self.lineedit_cost = QLineEdit(self)
        self.layout.addWidget(self.lineedit_cost)

        # Кнопка расчета
        self.button_calc = QPushButton("Рассчитать амортизацию")
        self.button_calc.clicked.connect(self.calculate)
        self.layout.addWidget(self.button_calc)

        # Фактическая амортизация
        self.label4 = QLabel("Фактическая амортизация, тыс. руб.")
        self.layout.addWidget(self.label4)

        self.lineedit_result = QLineEdit(self)
        self.lineedit_result.setReadOnly(True)
        self.layout.addWidget(self.lineedit_result)

        # Плановая амортизация (НОВОЕ)
        self.label5 = QLabel("Плановая амортизация, тыс. руб.")
        self.layout.addWidget(self.label5)

        self.lineedit_plan = QLineEdit(self)
        self.layout.addWidget(self.lineedit_plan)

        # Кнопка гистограммы
        self.button_chart = QPushButton("Амортизация (гистограмма)")
        self.button_chart.clicked.connect(self.show_chart)
        self.layout.addWidget(self.button_chart)

        # Установка начального срока
        self.update_life_time()

    def update_life_time(self):
        life_times = {
            "Комбайн": 25,
            "Трактор": 20,
            "Плуг": 15
        }
        current_type = self.combo.currentText()
        self.lineedit_life.setText(str(life_times[current_type]))

    def calculate(self):
        try:
            cost = float(self.lineedit_cost.text())
            life = int(self.lineedit_life.text())
            amortization = cost / life
            self.lineedit_result.setText(str(round(amortization, 2)))
        except ValueError:
            self.lineedit_result.setText("Ошибка ввода")

    def show_chart(self):
        try:
            fact = float(self.lineedit_result.text())
            plan = float(self.lineedit_plan.text())

            values = [fact, plan]
            labels = ["Фактическая", "Плановая"]

            plt.figure(figsize=(6, 4))
            plt.bar(labels, values)
            plt.title("Сравнение годовой амортизации")
            plt.ylabel("тыс. руб.")
            plt.grid(axis="y")
            plt.show()

        except ValueError:
            pass


# Запуск приложения
app = QApplication(sys.argv)
window = AmortizationApp()
window.show()
sys.exit(app.exec_())
