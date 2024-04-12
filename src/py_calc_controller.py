from functools import partial

from src.evaluator import evaluateExpression, ERROR_MSG
from src.py_calc_window import PyCalcWindow


class PyCalc:
    """PyCals's controller class"""

    def __init__(self, model: evaluateExpression, view: PyCalcWindow) -> None:
        self._evaluate = model
        self._view = view
        self._connectSignalsAndSlots()

    def _calculateResult(self):
        result = self._evaluate(expression=self._view.displayText)
        self._view.setDisplayText(result)

    def _buildExpression(self, subExpression):
        if self._view.displayText == ERROR_MSG:
            self._view.clearDisplay()
        expression = self._view.displayText + subExpression
        self._view.setDisplayText(expression)

    def _connectSignalsAndSlots(self):
        for keySymbol, button in self._view.buttonMap.items():
            if keySymbol not in {"=", "C"}:
                button.clicked.connect(
                    partial(self._buildExpression, keySymbol)
                )

        self._view.buttonMap['='].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttonMap['C'].clicked.connect(self._view.clearDisplay)