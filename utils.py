from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
import time
import logging
from instant_data_scraper import InstantDataScraper

    
# def find_next_page_button(driver, timeout=5):
#     next_page_xpaths = [
#         "//a[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'next')]",
#         "//a[contains(@class, 'next')]",
#         "//a[contains(@rel, 'next')]",
#         "//a[contains(@aria-label, 'Next')]",
#         "//button[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'next')]",
#         "//li[contains(@class, 'next')]/a",
#         # "//a[.//img[contains(@alt, 'Next')]]",
#         "//a[contains(text(), '→') or contains(text(), '▶') or contains(text(), '»')]",
#         "//button[contains(text(), '→') or contains(text(), '▶') or contains(text(), '»')]",
#         "//span[contains(text(), '→') or contains(text(), '▶') or contains(text(), '»')]",
#         "//i[contains(@class, 'arrow') or contains(@class, 'chevron-right')]",
#     ]

#     for xpath in next_page_xpaths:
#         try:
#             next_link = WebDriverWait(driver, timeout).until(
#                 EC.element_to_be_clickable((By.XPATH, xpath)))
#             logging.info(f"next page button detected")
#             return next_link
#         except TimeoutException:
#             logging.error(f"Timeout error while finding next button")
#             return None
#         except NoSuchElementException:
#             logging.error(f"Next button was not found in the DOM.")
#             return None
#         except WebDriverException as e:
#             logging.error(f"WebDriverException occurred: {e}")
#             return None
#         except Exception as e:
#             logging.error(f"An unexpected error occurred: {e}")
#             return None
        
        
def check_captcha(driver): 
    ''' check for captcha. if persents or encounters and error, return True meaning there is captcha. otherwise, Fasle'''
    try:
        # Check for common CAPTCHA indicators (e.g., iframe or div with CAPTCHA classes)
        captcha_element = driver.find_element(By.XPATH, "//iframe[contains(@src, 'recaptcha')]")
        logging.info("CAPTCHA detected!")
        return bool(captcha_element)
    except NoSuchElementException:
        logging.info("No CAPTCHA detected!")
        return False
    except Exception as e:
        logging.error(f'error occured while finding captcha: {e}')
        return True
    


def webpage_scraper(url, chromedriver_path, instant_data_scraper_path, timeout=5):
    service = Service(chromedriver_path,)
    chrome_options = Options()
    chrome_options.add_extension(instant_data_scraper_path)
    chrome_options.add_argument('start-maximized')
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    url_loaded = False

    try:
        driver.get(url)
        element = WebDriverWait(driver, timeout).until(
                    EC.presence_of_element_located((By.ID, "main")))
        url_loaded = True
        logging.info(f"Successfully accessed the URL: {url}")
    except Exception as e:
        logging.error(f"An error occurred while accessing {url}: {str(e)}")


    if url_loaded:
        captcha_present = check_captcha(driver=driver)
        if captcha_present:
            print('skip webpage since it contains captcha')
            return None
        elif bool(find_next_page_button(driver)):
            print('skip webpage since it contains url')
            return None
        else:
            try:
                extension = InstantDataScraper()
                extension.activate_extension()
                extension.download_add_exit_extension()
                driver.quit()
                print('scraped successfull.')
            except Exception as e:
                logging.error(f'error while handling extension: {str(e)}')
    