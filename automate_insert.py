import pyautogui
from time import sleep
import clipboard
import sys



def slp():
    sleep(0.25)


def copy():
    pyautogui.hotkey("ctrl", "c")


def paste():
    pyautogui.hotkey("ctrl", "v")


def docard(which):
    TAB_POS = None
    URL_POS = None
    SET_POS = None
    NUM = None

    if which == 1:
        TAB_POS = TAB_ONE_POS
        URL_POS = FIRST_CHOICE_URL
        SET_POS = FIRST_SET_NAME
        NUM = FIRST_CARD_NUM

    elif which == 2:
        TAB_POS = TAB_TWO_POS
        URL_POS = SECOND_CHOICE_URL
        SET_POS = SECOND_SET_NAME
        NUM = SECOND_CARD_NUM

    elif which == 3:
        TAB_POS = TAB_THREE_POS
        URL_POS = THIRD_CHOICE_URL
        SET_POS = THIRD_SET_NAME
        NUM = THIRD_CARD_NUM

    elif which == 4:
        TAB_POS = TAB_FOUR_POS
        URL_POS = FOURTH_CHOICE_URL
        SET_POS = FOURTH_SET_NAME
        NUM = FOURTH_CARD_NUM

    # Open tab 1
    pyautogui.click(TAB_POS)
    slp()

    # Triple click the set name and copy it
    pyautogui.click(SET_NAME_NUM, button='left', clicks=3, interval=0.25)
    copy()

    parseme = clipboard.paste()

    pkmn_name, rest = parseme.split(" · ")

    try:
        set_name, rest = rest.split(" (")
        rest, card_num = rest.split("#")
    except Exception:
        # We don't have a set code meaning its a promo set
        set_name, card_num = rest.split(" #")

    pyautogui.click(CARD_IMG_POS, button="right")
    slp()
    pyautogui.click(COPY_IMG_LINK)
    slp()

    pyautogui.click(URL_POS)
    slp()
    paste()
    slp()
    pyautogui.click(SET_POS)
    slp()
    clipboard.copy(set_name)
    paste()
    slp()
    pyautogui.click(NUM)
    clipboard.copy(card_num)
    paste()
    slp()


SEARCH_TAB_POS = (153, 26)
TAB_ONE_POS = (427, 32)
TAB_TWO_POS = (601, 30)
TAB_THREE_POS = (832, 25)
TAB_FOUR_POS = (1066, 23)
SET_NAME_NUM = (559, 335)

CARD_IMG_POS = (315, 524)
COPY_IMG_LINK = (434, 872)

FIRST_CHOICE_URL = (1468, 228)
FIRST_SET_NAME = (1726, 224)
FIRST_CARD_NUM = (1993, 221)

SECOND_CHOICE_URL = (1468, 247)
SECOND_SET_NAME = (1736, 254)
SECOND_CARD_NUM = (2017, 257)

THIRD_CHOICE_URL = (1481, 268)
THIRD_SET_NAME = (1730, 276)
THIRD_CARD_NUM = (2015, 277)

FOURTH_CHOICE_URL = (1507, 307)
FOURTH_SET_NAME = (1753, 300)
FOURTH_CARD_NUM = (2013, 298)

SAVE_BUTTON_ONE = (1319, 707)
SAVE_BUTTON_TWO = (1313, 737)
SAVE_BUTTON_THREE_PLUS = (1314, 747)

if len(sys.argv) > 1:
    try:
        card_count = int(sys.argv[1])
    except Exception as e:
        print(f"Invalid preferred card amount: {sys.argv[1]}")
        exit(1)

    if card_count > 4 or  card_count < 1:
        print("You must have between 1 and 4 preferred cards")
        exit(1)
else:
    # Default to four
    card_count = 4


for x in range(1, card_count + 1):
    docard(x)


if card_count == 1:
    pyautogui.click(SAVE_BUTTON_ONE)
elif card_count == 2:
    pyautogui.click(SAVE_BUTTON_TWO)
else:
    pyautogui.click(SAVE_BUTTON_THREE_PLUS)


# Close the tabs
if card_count >= 4:
    pyautogui.click(TAB_FOUR_POS, button="middle")
    slp()
if card_count >= 3:
    pyautogui.click(TAB_THREE_POS, button="middle")
    slp()
if card_count >= 2:
    pyautogui.click(TAB_TWO_POS, button="middle")
    slp()

pyautogui.click(TAB_ONE_POS, button="middle")
slp()


# Confirm the alert
sleep(3)
pyautogui.click((1919, 374))
slp()
pyautogui.hotkey("enter")
