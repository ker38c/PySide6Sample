from PySide6.QtCore import QObject, Signal, Slot
from models.model import Model

class Controller(QObject):
    # Viewへ入力値が不正であることを通知するSignal
    invalid_left_value = Signal()
    invalid_right_value = Signal()

    def __init__(self, model :Model):
        super().__init__()
        self._model = model

    def change_left_value(self, value: str):
        try:
            self._model.left_value = float(value)
        except:
            self._model.left_value = float(0)
            self.invalid_left_value.emit()

    def change_right_value(self, value: str):
        try:
            self._model.right_value = float(value)
        except:
            self._model.right_value = float(0)
            self.invalid_right_value.emit()

    # 加算ボタンクリック時に実行
    @Slot()
    def add(self):
        self._model.add()