from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging
import time
CHROMEDRIVER_PATH = '/home/ups/chromedriver'
WINDOW_SIZE = "1920,1080"
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                          chrome_options=chrome_options
                         )
logging.basicConfig(filename='/home/ups/UPS221.log', filemode='a', format='%(created)f %(message)s', level=logging.INFO)
driver.get("http://10.116.2.221/PSummary.html")
x=0
while (x==0):
    for num in range(30):
        try:
        #Get temp
            xPathOfTemp = '/html/body/font/center/form/table/tbody/tr[12]/td[3]/table/tbody/tr/td/b'
            Temp = (driver.find_element("xpath",xPathOfTemp).text)
            temperature_f = float(Temp) * (9.0/5.0) + 32.0
            if Temp == "":
                break
        except:
            time.sleep(1)
    #Get humidity
    xPathOfHumidity = '/html/body/font/center/form/table/tbody/tr[13]/td[3]/table/tbody/tr/td/b'
    Hum = (driver.find_element("xpath",xPathOfHumidity).text)
    Humidity = float(Hum)
    #Get RunTime
    xPathOfRunTime = '/html/body/font/center/form/table/tbody/tr[14]/td[3]/table/tbody/tr/td/b'
    Time = (driver.find_element("xpath",xPathOfRunTime).text)
    runTime = float(Time)
    #Get Voltage
    xPathOfVoltage = '/html/body/font/center/form/table/tbody/tr[19]/td[3]/table/tbody/tr/td[1]/b'
    Volt = (driver.find_element("xpath",xPathOfVoltage).text)
    Voltage = float(Volt)
    #Get Current
    xPathOfCurrent = '/html/body/font/center/form/table/tbody/tr[20]/td[3]/table/tbody/tr/td[1]/b'
    Amps = (driver.find_element("xpath",xPathOfCurrent).text)
    Current = float(Amps)
    #Get BatteryLoad
    xPathOfLoad = '/html/body/font/center/form/table/tbody/tr[30]/td[3]/table/tbody/tr/td[1]/b'
    Load = (driver.find_element("xpath",xPathOfLoad).text)
    batteryLoad = float(Load)
    #Get Bypass Status
    xPathOfBypass = '/html/body/font/center/form/table/tbody/tr[32]/td[3]/table/tbody/tr/td/b'
    bypassStatus = (driver.find_element("xpath",xPathOfBypass).text)
    #Get Battery Status
    xPathOfBattery = '/html/body/font/center/form/table/tbody/tr[36]/td[3]/table/tbody/tr/td/b'
    batteryStatus = (driver.find_element("xpath",xPathOfBattery).text)
    #Get Up Time
    xPathOfUpTime = '/html/body/font/center/form/table/tbody/tr[42]/td[3]/table/tbody/tr/td/b'
    UpTime = (driver.find_element("xpath",xPathOfUpTime).text)
        logging.info('Temp={0:0.1f} F and Humidity={1:0.1f} % and runTime={2:0.1f} minutes and Voltage={3:0.1f} Volts and Current={4:0.1f} and BatteryLoad={5:0.1f} % and BypassStatus={6} and BatteryStatus={7} and UpTime={8}'.format(temperature_f,Humidity,runTime,Voltage,Current,batteryLoad,bypassStatus,batteryStatus,UpTime))
    driver.refresh()
