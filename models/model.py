from PySide6.QtCore import QObject, Signal

class Model(QObject):

    def __init__(self):
        super().__init__()
        self.left_value = 0
        self.right_value = 0
        self.answer = 0

    # Viewへ加算結果を通知するSignal
    answer_changed = Signal(float)

    @property
    def left_value(self):
        return self._left_value

    @left_value.setter
    def left_value(self, value: float):
        self._left_value = value

    @property
    def right_value(self):
        return self._right_value

    @right_value.setter
    def right_value(self, value: float):
        self._right_value = value

    @property
    def answer(self):
        return self._answer

    @answer.setter
    def answer(self, value: float):
        self._answer = value
        self.answer_changed.emit(value)

    def add(self):
        self.answer = self.left_value + self.right_value
