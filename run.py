# run.py
import os
import sys
import importlib

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("\nPress Enter to return to menu...")

def run_module(module_name):
    """Import and execute a module as if run with `python -m`."""
    try:
        module = importlib.import_module(module_name)
        if hasattr(module, "__main__"):
            module.__main__()
        elif hasattr(module, "main"):
            module.main()
        else:
            # If module runs on import (has a guard), just import is enough
            pass
    except SystemExit:
        pass
    except Exception as e:
        print(f"\n⚠️  Error running {module_name}: {e}")
    pause()

def show_menu():
    while True:
        clear_screen()
        print("╔════════════════════════════════════════╗")
        print("║        STORAGE SENTINEL MENU           ║")
        print("╠════════════════════════════════════════╣")
        print("║ 1. Take Snapshot                       ║")
        print("║ 2. Compare Latest Snapshots            ║")
        print("║ 3. Show Stats Report                   ║")
        print("║ 4. Exit                                ║")
        print("╚════════════════════════════════════════╝")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            print("\n🔍 Running snapshot module...\n")
            import core.snapshot
            pause()

        elif choice == "2":
            print("\n🔎 Running compare module...\n")
            import core.compare
            pause()

        elif choice == "3":
            print("\n📊 Generating stats report...\n")
            import core.stats
            pause()

        elif choice == "4":
            print("\n👋 Goodbye, Sentinel terminated.")
            break
        else:
            input("\n❌ Invalid choice. Press Enter to retry...")

if __name__ == "__main__":
    show_menu()
# run.py
import os
import sys
import importlib

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("\nPress Enter to return to menu...")

def run_module(module_name):
    """Import and execute a module as if run with `python -m`."""
    try:
        module = importlib.import_module(module_name)
        if hasattr(module, "__main__"):
            module.__main__()
        elif hasattr(module, "main"):
            module.main()
        else:
            # If module runs on import (has a guard), just import is enough
            pass
    except SystemExit:
        pass
    except Exception as e:
        print(f"\n⚠️  Error running {module_name}: {e}")
    pause()

def show_menu():
    while True:
        clear_screen()
        print("╔════════════════════════════════════════╗")
        print("║        STORAGE SENTINEL MENU           ║")
        print("╠════════════════════════════════════════╣")
        print("║ 1. Take Snapshot                       ║")
        print("║ 2. Compare Latest Snapshots            ║")
        print("║ 3. Show Stats Report                   ║")
        print("║ 4. Exit                                ║")
        print("╚════════════════════════════════════════╝")

        choice = input("Enter choice: ").strip()

elif choice == "1":
    print("\n🔍 Running snapshot module...\n")
    from core.snapshot import save_snapshot_to_db
    folder = input("Enter directory to snapshot (blank = current): ").strip() or "."
    save_snapshot_to_db(folder)
    pause()

elif choice == "2":
    print("\n🔎 Running compare module...\n")
    from core.compare import compare_snapshots
    # Here you can add a wrapper to pick the last two CSVs automatically.
    pause()


elif choice == "3":
    print("\n📊 Generating stats report...\n")
    from core.stats import query_db, print_report
    stats = query_db()
    print_report(stats)
    pause()

elif choice == "4":
    print("\n👋 Goodbye, Sentinel terminated.")
    break

else:
            input("\n❌ Invalid choice. Press Enter to retry...")
if __name__ == "__main__":
    show_menu()
