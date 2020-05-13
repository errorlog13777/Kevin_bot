from selenium import webdriver

# https://ithelp.ithome.com.tw/articles/10222029
# https://medium.com/@yanweiliu/%E4%BD%BF%E7%94%A8python%E9%80%B2%E8%A1%8C%E7%B6%B2%E9%A0%81%E7%9A%84%E6%95%B4%E9%A0%81%E6%88%AA%E5%9C%96-e62ec2ac6e73

driverPath = r"C:\Program Files\Mozilla Firefox"
browser = webdriver.Firefox(driverPath)
browser.set_window_size(899, 699)
browser.get('https://t1.hbl917070.nctu.me/img/show?img=sbob_15&imgw=900&size=40&tc=ffffffff&tbt=6&tb=000000ff&tbac=00000000&y=50&txt=%E5%A5%BD%E6%A3%92%EF%BD%9B%E6%99%82%EF%BD%9D%E9%BB%9E%EF%BD%9B%E5%88%86%EF%BD%9D%E5%88%86%E4%BA%86#.jpg')
browser.save_screenshot('time.png')
browser.close()