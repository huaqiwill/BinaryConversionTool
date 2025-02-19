from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
import sys
from app.view.main_window import MainWindow
from qfluentwidgets import FluentTranslator, setTheme, Theme

if __name__ == "__main__":
    # 启用高DPI支持
    # QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    # QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    
    app = QApplication(sys.argv)
    
    # 设置Fluent主题
    translator = FluentTranslator()
    app.installTranslator(translator)
    setTheme(Theme.AUTO)
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec())