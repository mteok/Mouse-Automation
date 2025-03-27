# -*- coding: utf-8 -*-
import pyautogui
import time
import tkinter as tk
from tkinter import messagebox
from mouse_library import MouseAutomation
import threading
pyautogui.FAILSAFE = False


class MouseAutomationGUI:

    def main(self, duration: int) -> None:
        """
        Runs the application for a specified duration in seconds.
        """
        start_time = time.time()
        end_time = start_time + duration
        mouse = MouseAutomation()
        if duration != 0:
            messagebox.showinfo("Info",f'Stop at {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_time))}')
            
        while self.running:
            mouse.switch_screens()
            mouse.wiggle_mouse()
            self.running = time.time() < end_time or duration == 0 if self.running else False
        messagebox.showinfo("Application Stopped", "The automation has been stopped.")



    def start_application(self):
        """
        Starts the application with the duration specified in the GUI.
        """
        try:
            duration_getted = duration_entry.get()
            duration = int(duration_getted) if duration_getted else 0
            if duration < 0:
                raise ValueError("Duration must be a positive integer. 0 to never stop.")
            if duration > 0:
                messagebox.showinfo("Application Started", f"Running for {duration} seconds.")
            # Run the main method in a separate thread
            self.thread = threading.Thread(target=self.main, args=(duration,))
            self.thread.daemon = True  # Daemon thread will close when the main program exits
            self.running = True
            self.thread.start()
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))

    def stop_application(self):
        """
        Stops the application by setting the running flag to False.
        """
        self.running = False  # Signal the thread to stop
        # if hasattr(self, 'thread') and self.thread.is_alive():
        #     self.thread.join()  # Wait for the thread to finish
        

MouseAutomationGUI = MouseAutomationGUI()
# Create the GUI
root = tk.Tk()
root.title("Mouse Automation")

# Duration input
tk.Label(root, text="Enter duration (seconds):").pack(pady=5)
duration_entry = tk.Entry(root)
duration_entry.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

start_button = tk.Button(button_frame, text="Start", command=MouseAutomationGUI.start_application)
stop_button = tk.Button(button_frame, text="Stop", command=MouseAutomationGUI.stop_application)

start_button.pack(side=tk.LEFT, padx=5)
stop_button.pack(side=tk.LEFT, padx=5)

# Run the GUI event loop
root.mainloop()