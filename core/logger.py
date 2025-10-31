# core/logger.py
import os
import datetime
from colorama import init, Fore, Style

init(autoreset=True)  # Enables color support on Windows automatically

LOG_PATH = os.path.join("data", "sentinel.log")

def log(message, level="INFO"):
    """Logs message with timestamp and optional color."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted = f"[{timestamp}] {level}: {message}"

    # Write to log file
    os.makedirs("data", exist_ok=True)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(formatted + "\n")

    # Print color-coded message to console
    if level == "INFO":
        print(Fore.CYAN + formatted + Style.RESET_ALL)
    elif level == "SUCCESS":
        print(Fore.GREEN + formatted + Style.RESET_ALL)
    elif level == "WARNING":
        print(Fore.YELLOW + formatted + Style.RESET_ALL)
    elif level == "ERROR":
        print(Fore.RED + formatted + Style.RESET_ALL)
    else:
        print(formatted)
