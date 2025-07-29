# Touch-friendly launcher UI (simplified)
import os

def list_apps():
    apps = [f for f in os.listdir("../apps") if f.endswith(".py")]
    return apps

def launch_app(app_name):
    os.system(f"python3 ../apps/{app_name}")

if __name__ == "__main__":
    print("=== TapMind OS Launcher ===")
    apps = list_apps()
    for idx, app in enumerate(apps):
        print(f"{idx + 1}. {app}")
    choice = int(input("Select an app to launch: ")) - 1
    if 0 <= choice < len(apps):
        launch_app(apps[choice])
    else:
        print("Invalid choice.")
