import pyautogui
import time
from pyautogui import FailSafeException
import logging
from selenium.common.exceptions import NoSuchWindowException


class InstantDataScraper():
    chrome_extension_button = (1762, 94)
    extension_activate_button = (1460, 302)
    locate_next_button = (418, 205)
    start_crawling_button = (403, 284)
    download_csv_button = (1003, 153)
    extension_close_button = (1883, 14)

    @staticmethod
    def activate_extension():
        try:
            pyautogui.click(InstantDataScraper.chrome_extension_button[0], InstantDataScraper.chrome_extension_button[1]) 
            time.sleep(1)
            pyautogui.click(InstantDataScraper.extension_activate_button[0], InstantDataScraper.extension_activate_button[1]) 
            time.sleep(4)
        except FailSafeException as e:
            logging.error(f"PyAutoGUI failed while activating extension: {str(e)}")
        except Exception as e:
            logging.error(f"An error occurred while activating extension: {str(e)}")


    # @staticmethod
    # def handle_next_on_extension(next_button, driver):
    #     # get the open windows; it should be two windows
    #     window_handles = driver.window_handles
    #     chrome_window = window_handles[0]
    #     extension_window = window_handles[1]
    #     pyautogui.click(InstantDataScraper.locate_next_button[0], InstantDataScraper.locate_next_button[1]) 
    #     # switch to chrome window
    #     time.sleep(2)
    #     driver.switch_to.window(chrome_window)
    #     # get the center of next button in the webpage
    #     # todo: next button location is not correct
    #     center_x = next_button.location['x'] + next_button.rect['width'] // 2
    #     center_y = next_button.location['y'] + next_button.rect['height'] // 2
    #     pyautogui.click(center_x, center_y) 
    #     # switch window 
    #     driver.switch_to.window(extension_window)
    #     time.sleep(1)
    #     pyautogui.click(InstantDataScraper.start_crawling_button[0], InstantDataScraper.start_crawling_button[1])
    #     time.sleep(3)

    @staticmethod
    def download_add_exit_extension():
        try:
            pyautogui.click(InstantDataScraper.download_csv_button[0], InstantDataScraper.download_csv_button[1]) 
            time.sleep(1)
            pyautogui.click(InstantDataScraper.extension_close_button[0], InstantDataScraper.extension_close_button[1]) 
            time.sleep(1)
        except FailSafeException as e:
            logging.error(f"PyAutoGUI failed while downloading and exiting extension: {str(e)}")
        except Exception as e:
            logging.error(f"An error occurred while downloading or closing extension: {str(e)}")