from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt
from qfluentwidgets import (FluentWindow, LineEdit, ComboBox,
                            CardWidget, InfoBar, InfoBarPosition,
                            StrongBodyLabel, BodyLabel, SubtitleLabel,
                            FluentIcon, PrimaryPushButton,
                            TransparentToolButton, ToolTipFilter,
                            setTheme, Theme)
from ..common.converter import NumberConverter


class ConverterInterface(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setObjectName("ConverterInterface")
        self.converter = NumberConverter()
        self._init_ui()

    def _init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(6)

        # 创建输入区域
        input_card = CardWidget()
        input_layout = QVBoxLayout(input_card)
        input_layout.setSpacing(6)

        # 添加标题和说明
        header_layout = QHBoxLayout()
        title_label = SubtitleLabel("进制转换")
        help_button = TransparentToolButton(FluentIcon.QUESTION)
        help_button.installEventFilter(
            ToolTipFilter(help_button, "支持二进制、八进制、十进制和十六进制转换"))
        header_layout.addWidget(title_label)
        header_layout.addStretch(1)
        header_layout.addWidget(help_button)
        input_layout.addLayout(header_layout)

        # 输入控件
        input_controls = QHBoxLayout()
        input_controls.setSpacing(8)
        self.input_edit = LineEdit()
        self.input_edit.setPlaceholderText("请输入数值")
        self.input_base = ComboBox()
        self.input_base.addItems(["二进制", "八进制", "十进制", "十六进制"])
        self.input_base.setCurrentText("十进制")
        self.input_base.setMinimumWidth(120)

        input_controls.addWidget(BodyLabel("输入值:"))
        input_controls.addWidget(self.input_edit, 1)
        input_controls.addWidget(BodyLabel("进制:"))
        input_controls.addWidget(self.input_base)
        input_layout.addLayout(input_controls)

        layout.addWidget(input_card)

        # 创建输出区域
        output_card = CardWidget()
        output_layout = QVBoxLayout(output_card)
        output_layout.setSpacing(16)

        # 添加输出标题
        output_title = SubtitleLabel("转换结果")
        output_layout.addWidget(output_title)

        # 创建结果网格
        self.output_labels = {}
        bases = ["二进制", "八进制", "十进制", "十六进制"]
        for base in bases:
            result_card = CardWidget()
            result_card.setObjectName("ResultCard")
            result_layout = QHBoxLayout(result_card)

            label = BodyLabel(f"{base}:")
            result_label = BodyLabel()
            result_label.setTextInteractionFlags(Qt.TextSelectableByMouse)
            result_label.setObjectName("ResultLabel")

            result_layout.addWidget(label)
            result_layout.addWidget(result_label)
            output_layout.addWidget(result_card)
            self.output_labels[base] = result_label

        layout.addWidget(output_card)

        # 设置样式
        self.setStyleSheet("""
            QWidget#ResultCard {
                background-color: rgb(251, 251, 251);
                border-radius: 6px;
                padding: 12px;
            }
            QLabel#ResultLabel {
                color: rgb(51, 51, 51);
                font-size: 14px;
            }
        """)

        # 连接信号
        self.input_edit.textChanged.connect(self.on_input_changed)
        self.input_base.currentTextChanged.connect(self.on_input_changed)

    def on_input_changed(self):
        text = self.input_edit.text().strip()
        base_map = {
            "二进制": 2,
            "八进制": 8,
            "十进制": 10,
            "十六进制": 16
        }
        input_base = base_map[self.input_base.currentText()]

        # 获取转换结果
        results = self.converter.convert(text, input_base)

        # 更新显示
        if results:
            for base, value in results.items():
                self.output_labels[base].setText(value)
        else:
            if text:
                self.show_error("输入错误", "请检查输入的数值是否符合所选进制")
            self.clear_outputs()

    def clear_outputs(self):
        for label in self.output_labels.values():
            label.setText("")

    def show_error(self, title, content):
        InfoBar.error(
            title=title,
            content=content,
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=2000,
            parent=self
        )


class MainWindow(FluentWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("进制转换工具")
        self.resize(500, 400)

        # 设置主题
        setTheme(Theme.AUTO)

        # 创建并添加转换器界面
        self.converter_interface = ConverterInterface()
        self.addSubInterface(
            self.converter_interface,
            icon=FluentIcon.CARE_UP_SOLID,
            text="进制转换"
        )
