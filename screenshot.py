from selenium import webdriver
from time import sleep

filepath = 'demo.txt'
with open(filepath) as fp:
    line = fp.readline()
    inc = 1
    while line:
        hey = line.strip()
        line = fp.readline()
        browser = webdriver.Chrome()
        browser.get(hey)
        sleep(1)
        browser.get_screenshot_as_file("E:\py tools/screenshots/%d.png" % inc)
        inc += 1
        browser.quit()
