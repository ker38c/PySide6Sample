from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Slot
from models.model import Model
from controllers.controller import Controller
from views.Ui_Addition import Ui_MainWindow

class View(QMainWindow):
    def __init__(self, model :Model, controller :Controller):
        super().__init__()
        self._model = model
        self._controller = controller
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        # UiMainViewのtextEdit編集終了通知Signalを、ViewのSlotに接続
        self._ui.lineEdit_left_value.editingFinished.connect(self.change_left_value)
        self._ui.lineEdit_right_value.editingFinished.connect(self.change_right_value)

        # UiMainViewの加算ボタンクリック通知Signalを、ControllerのSlotに接続
        self._ui.button_add.clicked.connect(self._controller.add)

        # Modelの加算結果の更新通知Signalを、ViewのSlotに接続
        self._model.answer_changed.connect(self.answer_changed)

        # Controllerの不正な入力値通知Signalを、ViewのSlotに接続
        self._controller.invalid_left_value.connect(self.invalid_left_value)
        self._controller.invalid_right_value.connect(self.invalid_left_value)

    # Modelの加算結果の更新通知を受信
    @Slot(float)
    def answer_changed(self, value: float):
        self._ui.label_answer.setText(str(value))

    # UiのtextEditの編集終了通知を受信
    @Slot()
    def change_left_value(self):
        self._controller.change_left_value(self._ui.lineEdit_left_value.text())

    @Slot()
    def change_right_value(self):
        self._controller.change_right_value(self._ui.lineEdit_right_value.text())

    # Controllerの不正な入力値通知を受信
    @Slot()
    def invalid_left_value(self):
        self._ui.lineEdit_left_value.clear()

    @Slot()
    def invalid_left_value(self):
        self._ui.lineEdit_right_value.clear()