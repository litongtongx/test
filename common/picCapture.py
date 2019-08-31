from datetime import datetime
import os


def capture_pic(driver):
    pt = datetime.now().strftime('%Y%m%m%H%M%S')
    base_path = os.path.dirname(os.getcwd())
    pic_name = os.path.join(base_path, 'picture', pt+'.png')
    driver.get_screenshot_as_file(pic_name)


