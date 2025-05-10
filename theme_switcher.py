import os
import time
import datetime
import subprocess
import ctypes
import winreg
import sys
import logging
import json
from pathlib import Path

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

    LIGHT_WALLPAPER_ID = "1234567890"
    DARK_WALLPAPER_ID = "0987654321"

    WALLPAPER_ENGINE_PATH = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\wallpaper_engine\\wallpaper32.exe"
    WALLPAPER_CONFIG_PATH = os.path.join(os.environ["APPDATA"], "Wallpaper Engine")

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

def change_wallpaper_engine(use_dark):
    """Change wallpaper using Wallpaper Engine"""
    try:
        wallpaper_id = Config.DARK_WALLPAPER_ID if use_dark else Config.LIGHT_WALLPAPER_ID
        theme_name = "dark" if use_dark else "light"

        if not os.path.exists(Config.WALLPAPER_ENGINE_PATH):
            logging.error("Wallpaper Engine not found")
            return False

        try:
            subprocess.run(["taskkill", "/F", "/IM", "wallpaper32.exe", "/T"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            subprocess.run(["taskkill", "/F", "/IM", "wallpaper64.exe", "/T"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            time.sleep(1)

            workshop_url = f"steam://run/431960//args//-control openworkshop:{wallpaper_id}"
            subprocess.Popen(["start", "", workshop_url], shell=True)

            logging.info(f"Wallpaper switched to {theme_name} (ID: {wallpaper_id})")
            return True
        except Exception as e:
            logging.warning(f"Method 1 failed: {e}")

        try:
            general_config = os.path.join(Config.WALLPAPER_CONFIG_PATH, "general.json")
            if os.path.exists(general_config):
                with open(general_config, 'r') as f:
                    config = json.load(f)
                config["wallpaperWorkshopId"] = wallpaper_id
                with open(general_config, 'w') as f:
                    json.dump(config, f, indent=2)

                subprocess.run(["taskkill", "/F", "/IM", "wallpaper32.exe", "/T"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                subprocess.run(["taskkill", "/F", "/IM", "wallpaper64.exe", "/T"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                time.sleep(1)

                subprocess.Popen([Config.WALLPAPER_ENGINE_PATH])

                logging.info(f"Wallpaper changed to {theme_name} via config (ID: {wallpaper_id})")
                return True
        except Exception as e:
            logging.error(f"Method 2 failed: {e}")
            return False

    except Exception as e:
        logging.error(f"Unexpected error changing wallpaper: {e}")
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
        change_wallpaper_engine(use_dark)

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
