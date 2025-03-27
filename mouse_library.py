import random
import pyautogui
import time
class MouseAutomation:

    def switch_screens(self) -> None:
        """
        Switches the active screen using Alt + Tab
        a random number of times.
        """
        max_switches = random.randint(1, 5)
        pyautogui.keyDown('alt') 
        
        for _ in range(1, max_switches):
            pyautogui.press('tab')     
        
        pyautogui.keyUp('alt')   


    def wiggle_mouse(self) -> None:
        """
        Wiggles the mouse between two coordinates.
        """
        max_wiggles = 1#random.randint(4, 9)

        for _ in range(0, max_wiggles):
            coords = self.get_random_coords()
            pyautogui.moveTo(
                x=coords[0], 
                y=coords[1],
                duration=5
            )
            time.sleep(10)
        

    def get_random_coords(self) -> []:
        """
        Returns a list of coordinates in the 
        format [x=1980, y=1080]
        """
        screen = pyautogui.size()
        width = screen[0]
        height = screen[1]
        
        return [
            random.randint(100, width - 200),
            random.randint(100, height - 200)
        ]