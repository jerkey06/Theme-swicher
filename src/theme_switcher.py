import os
import time
import datetime
import ctypes
import winreg
import sys
import logging

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("theme_switcher.log"),
        logging.StreamHandler()
    ]
)

class Config:
    LIGHT_THEME_START = 7   # 7:00 AM
    DARK_THEME_START = 19   # 7:00 PM

def is_dark_theme_active():
    """Check if dark mode is currently active"""
    try:
        registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
        key = winreg.OpenKey(registry, r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize")
        value, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
        return value == 0
    except Exception as e:
        logging.error(f"Error checking current theme: {e}")
        return None

def set_windows_theme(use_dark):
    """Set Windows theme to dark or light"""
    theme_value = 0 if use_dark else 1
    theme_name = "dark" if use_dark else "light"
    try:
        registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
        key = winreg.OpenKey(registry, r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "AppsUseLightTheme", 0, winreg.REG_DWORD, theme_value)
        winreg.SetValueEx(key, "SystemUsesLightTheme", 0, winreg.REG_DWORD, theme_value)
        logging.info(f"Theme set to {theme_name}")
        return True
    except Exception as e:
        logging.error(f"Error setting theme: {e}")
        return False

def get_appropriate_theme():
    """Determine appropriate theme based on current hour"""
    current_hour = datetime.datetime.now().hour
    return current_hour < Config.LIGHT_THEME_START or current_hour >= Config.DARK_THEME_START

def check_and_update():
    """Check and update theme and wallpaper"""
    use_dark = get_appropriate_theme()
    current_theme = is_dark_theme_active()
    if current_theme != use_dark:
        theme_name = "dark" if use_dark else "light"
        logging.info(f"Switching to {theme_name} theme ({datetime.datetime.now().strftime('%H:%M')})")
        set_windows_theme(use_dark)

def create_startup_shortcut():
    """Create a shortcut to run the script on Windows startup"""
    try:
        import win32com.client
        script_path = os.path.abspath(sys.argv[0])
        startup_folder = os.path.join(os.environ["APPDATA"], "Microsoft", "Windows", "Start Menu", "Programs", "Startup")

        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(os.path.join(startup_folder, "ThemeSwitcher.lnk"))
        shortcut.Targetpath = sys.executable
        shortcut.Arguments = f'"{script_path}"'
        shortcut.WorkingDirectory = os.path.dirname(script_path)
        shortcut.save()

        logging.info("Startup shortcut created")
        return True
    except Exception as e:
        logging.error(f"Error creating startup shortcut: {e}")
        return False

def main():
    logging.info("Starting Theme Switcher")

    if "--install" in sys.argv:
        create_startup_shortcut()
        return

    try:
        check_and_update()
        while True:
            now = datetime.datetime.now()
            sleep_seconds = 60 - now.second
            time.sleep(sleep_seconds)
            check_and_update()
    except KeyboardInterrupt:
        logging.info("Program interrupted by user")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
