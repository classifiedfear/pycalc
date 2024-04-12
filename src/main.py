import sys

from src.evaluator import evaluateExpression
from src.py_calc_controller import PyCalc
from src.py_calc_window import PyCalcWindow
from PyQt6.QtWidgets import(QApplication)


def main():
    pycalcapp = QApplication([])
    pycalcWindow = PyCalcWindow()
    pycalcWindow.show()
    PyCalc(model=evaluateExpression, view=pycalcWindow)
    sys.exit(pycalcapp.exec())


if __name__ == '__main__':
    main()
