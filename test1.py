from selenium import webdriver
import webbrowser
# driver = webdriver.Firefox(executable_path=r'/home/comp/Downloads/geckodriver')

#driver= webdriver.Chrome(executable_path=r'/home/comp/Desktop/chromedriver')
list1=['amazon','flipkart','myntra']
google = input('Google search:')
# item = input('Item search:')
yes=0

for x in list1:
    if google==x:
        yes+=1
            
if yes==1:
    item = input('Item search:')
    print("Valid")
    driver= webdriver.Chrome(executable_path=r'/usr/lib/chromium-browser/chromedriver')
    driver.get('https://www.'+google+'.com')
    if google=='amazon':
        element = driver.find_element_by_id("twotabsearchtextbox" )
        element.send_keys(item)
        element.submit()
    if google=='myntra':
        element = driver.find_element_by_xpath("//*[@id='desktop-header-cnt']/div[2]/div[3]/input")
        element.send_keys(item)
        element = driver.find_element_by_xpath("//*[@id='desktop-header-cnt']/div[2]/div[3]/a").click()

    if google=='flipkart':
        element = driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
        element = driver.find_element_by_xpath("//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input")
        element.send_keys(item)
        element = driver.find_element_by_xpath("//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/button").click()

else:
    print("invalid")
