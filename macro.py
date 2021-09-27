from pynput import mouse
import pyautogui
import time


class Macro:
    """
    Macro gaming
    """
    def on_click(x, y, button, pressed):
        if button == mouse.Button.left: # if click on the mouse, do:
            time.sleep(0.1)  # delay because its very faster for the game
            pyautogui.press('q')  # press qq for change weapon

    # Collect events until released
with mouse.Listener(on_click=Macro.on_click) as listener:
    try:
        listener.join()
    except Macro as e:
        pass