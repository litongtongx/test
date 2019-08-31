from common import readconfig
from selenium import webdriver
from common import picCapture
from common.logGen import LogGen

logger = LogGen(logger=__name__).get_log()
# 想加入try
def browser_start():
    browser_name = readconfig.get_browser("BrowserName")
    url = readconfig.get_url()
    if browser_name == 'chrome':
        logger.info("启动Chrome浏览器")
        driver = webdriver.Chrome()
        driver.get(url)
    elif browser_name == 'ie':
        logger.info("启动IE浏览器")
        driver = webdriver.Ie()
        driver.get(url)
    else:
        #打印log
        print("Please config conrect browser in config file")
    picCapture.capture_pic(driver)



if __name__ == '__main__':
    browser_start()