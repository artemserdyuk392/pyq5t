# импорт необходимых библиотек
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QVBoxLayout, QPushButton, QComboBox
)

class AmortizationApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Расчет годовой амортизации")
        self.setGeometry(100, 100, 500, 400)

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
        self.button = QPushButton("Рассчитать амортизацию")
        self.button.clicked.connect(self.calculate)
        self.layout.addWidget(self.button)

        # Результат
        self.label4 = QLabel("Годовая амортизация, тыс. руб.")
        self.layout.addWidget(self.label4)

        self.lineedit_result = QLineEdit(self)
        self.layout.addWidget(self.lineedit_result)

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

# Запуск приложения
app = QApplication(sys.argv)
window = AmortizationApp()
window.show()
sys.exit(app.exec_())

