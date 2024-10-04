# screen_config.py
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QGuiApplication

class screen_config:
    def __init__(self):
        """Initialize screen scaling settings."""
        self._configure_scaling()

    def _configure_scaling(self):
        """Apply platform-specific screen scaling fixes."""
        # Enable high DPI scaling attribute (for scaling widgets)
        QGuiApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
        
        # Ensure proper handling of high DPI displays
        QGuiApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

        # Windows-specific scaling fixes
        if sys.platform == "win32":
            try:
                # Apply DPI awareness for Windows 10
                from ctypes import windll
                windll.shcore.SetProcessDpiAwareness(1)  # Set DPI awareness (Windows 8.1+)
            except Exception as e:
                print(f"Failed to set DPI awareness: {e}")

        # macOS-specific scaling fixes (optional)
        if sys.platform == "darwin":
            # macOS automatically handles scaling, but can customize if needed
            print("macOS detected, auto DPI scaling in effect.")

    def apply(self):
        """Apply scaling configuration (for any external application if needed)."""
        self._configure_scaling()

