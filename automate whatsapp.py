from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def connect():
    """
        Simulate the chrome driver and go to the whatsapp web page.
        Make sure to scan the QR code to login to your whatsapp account.
    """

    driver = webdriver.Chrome(driver_exe)       # Run the simulated chrome driver
    driver.get(url)     # go to the whatsapp web page
    driver.implicitly_wait(10)      # wait a little to make sure the page loads
    return driver


def send(person, message):
    """
        person: name in your contacts
        message: text to be sent
    """
    
    driver = connect()
    # Search for the person in the contacts
    driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys(person,Keys.ENTER)
    # Writes and sends a message to that person
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message ,Keys.ENTER)


url = "https://web.whatsapp.com"    # whatsapp web url
driver_exe = "C:/chromedriver/chromedriver.exe"     # chrome driver path

# provide the names of the contacts you want to send the message to
names= ['Jack', 'Blake', 'Pablo',
         'Julie', 'Cameron', 'Peter',
         'Mike', 'John', 'Kendal', 'James']

message = "Hello, I am making a party tonight. Do you want to join?"

# send the message to all the specified names
for name in names:
    send(name, message)


