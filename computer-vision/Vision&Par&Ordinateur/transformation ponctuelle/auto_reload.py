import os
import sys
import time
import subprocess
import signal

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

SCRIPT_TO_RUN = "main.py"

class AutoReloadHandler(FileSystemEventHandler):
    def __init__(self):
        self.process = None
        self.restart()

    def restart(self):
        if self.process:
            try:
                os.kill(self.process.pid, signal.SIGTERM)
                self.process.wait(timeout=3)
            except Exception as e:
                print(f"⚠️ Erreur de fermeture : {e}")
                self.process.kill()
        self.process = subprocess.Popen([sys.executable, SCRIPT_TO_RUN])

    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            print(f"Modification : {event.src_path}")
            self.restart()

if __name__ == "__main__":
    dossier = "."
    handler = AutoReloadHandler()
    observer = Observer()
    observer.schedule(handler, path=dossier, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Arrêt...")
        observer.stop()
        if handler.process:
            handler.process.terminate()
    observer.join()
