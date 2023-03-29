import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from shutil import which
import time

class ProductosSpider(scrapy.Spider):
    name = 'productos'

    def __init__(self, externalUrl=None, *args, **kwargs):
        super(ProductosSpider, self).__init__(*args, **kwargs)
        chrome_options=Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--headless")
        chrome_path=which("chromedriver_linux64/chromedriver")
        driver=webdriver.Chrome(executable_path=chrome_path,options=chrome_options)
        driver.set_window_size(1440,4440)
        driver.get(externalUrl)
        
        buttons=driver.find_elements_by_xpath('//ul[contains(@class,"vtex-slider-0-x-sliderFrame")]/li')
        
        i=2
        allElements=[]
        arrayElements=[]
        totalButtons=buttons
        # for btn in totalButtons:
        if len(totalButtons) < 1:
            btn=WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div[1]/div/div/div/a'))
            )
            allElements=self.browserInteraction(driver,btn,4.5,i,totalButtons)
        else:

            while i <= len(totalButtons) +1:

                if i > len(totalButtons):
                    btn=driver.find_element_by_xpath('//ul[contains(@class,"vtex-slider-0-x-sliderFrame")]/li['+str(i-2)+']/button')
                else:
                    btn=driver.find_element_by_xpath('//ul[contains(@class,"vtex-slider-0-x-sliderFrame")]/li['+str(i)+']/button')

                    
                if btn.is_displayed():
                    arrayElements.append(self.browserInteraction(driver,btn,4.5,i,totalButtons))

                i+=1
                


            for oneElement in arrayElements:
                for singleProduct in oneElement:
                    allElements.append(singleProduct)
            
        self.start_urls = [externalUrl]
        self.html=allElements

        driver.close()


    def browserInteraction(self,driver,btn,timeSleep,i,totalButtons):
        elements=[]
        
        driver.execute_script("window.scrollTo(0, - document.body.scrollHeight);")
        time.sleep(.1)
        driver.execute_script("const d=document.body.scrollHeight-window.innerHeight,s=66,p=d/s,e=()=>{t+=p,window.scrollTo(0,t),t<d&&requestAnimationFrame(e)};let t=0;requestAnimationFrame(e);")
        time.sleep(1)

        wait = WebDriverWait(driver, 30)
        if len(totalButtons) > 1:
            wait.until(EC.visibility_of_element_located((By.ID, 'active')))
            driver.execute_script("void(document.querySelector('button#active').scrollIntoView({block: 'end'}))")

        time.sleep(.5)

        # cargar elementos en una lista
        pageElements=driver.find_elements_by_xpath('//div[@id="gallery-layout-container"]/div/section')
        for element in pageElements:
            name=element.find_element_by_xpath('a//h3/span').text
            price=element.find_element_by_xpath('a//div[@id="items-price"]/div/div').text
            elementDict={
                "name":name,
                "price":price
            }
            elements.append(elementDict)

        
        if len(totalButtons) > 1:
            wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="gallery-layout-container"]/div['+str(len(pageElements))+']/section')))
            if i > len(totalButtons):
                btn=WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, '//ul[contains(@class,"vtex-slider-0-x-sliderFrame")]/li['+str(i-2)+']/button'))
                )
            else:
                btn=WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, '//ul[contains(@class,"vtex-slider-0-x-sliderFrame")]/li['+str(i)+']/button'))
                )
            driver.execute_script("void(document.querySelector('button#active').scrollIntoView({block: 'end'}))")
            btn.click()
        else:
            btn.click()
            
        time.sleep(timeSleep)

        return elements


        
    def parse(self, response):
        products=self.html
        yield{
            "link":self.start_urls,
            "products":products
        }