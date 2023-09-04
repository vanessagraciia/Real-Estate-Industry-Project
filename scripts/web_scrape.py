import os
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options 
import pandas as pd 

website = 'https://www.domain.com.au/rent/melbourne-region-vic/?page=25'
chromedriver_path = '../chromedriver-mac-arm64/chromedriver.exe'

os.environ['webdriver.chrome.driver'] = chromedriver_path
driver = webdriver.Chrome()
driver.get(website)

address_name = driver.find_elements(By.XPATH, "//h2[contains(@class, 'css-bqbbuf')]")
address = []
try:
    for name in address_name:
        address.append(name.text)
   
except:
    address.append(' ')

print(address)


prices_list = driver.find_elements(By.XPATH, "//p[contains(@class, 'css-mgq8yx')]")
prices = []
try:
    for price in prices_list:
        prices.append(price.text)
   
except:
    prices.append(' ')

print(prices)

property_feature_elements = driver.find_elements(By.XPATH, "//span[contains(@data-testid, 'property-features-feature')][1]")
bedrooms = []
try:
    # Loop through each property feature element and extract the bedroom number
    for feature_element in property_feature_elements:
        feature_text = feature_element.text.strip()
        # Check if the feature text contains "Beds"
        if "Bed" in feature_text:
            bedroom_number = feature_text.split()[0]  # Extract the number before "Beds"
            bedrooms.append(bedroom_number)
        else:
            bedrooms.append(' ')
except:
    bedrooms.append(' ')

# Print the extracted bedroom numbers
for bedroom in bedrooms:
    print(bedroom)

property_feature_elements2 = driver.find_elements(By.XPATH, "//span[contains(@data-testid, 'property-features-feature')][2]")
baths = []
try:
    # Loop through each property feature element and extract the bedroom number
    for feature_element2 in property_feature_elements2:
        feature_text2 = feature_element2.text.strip()

        # Check if the feature text contains "Bath"
        if "Bath" in feature_text2:
            bath_number = feature_text2.split()[0]  # Extract the number before "Bath"
            baths.append(bath_number)
        else:
            baths.append(' ')
except:
    baths.append(' ')  # Append empty space if the XPATH location is not found

# Print the extracted bedroom numbers
for bath in baths:
    print(bath)

property_feature_elements3 = driver.find_elements(By.XPATH, "//span[contains(@data-testid, 'property-features-feature')][3]")
parks = []

try:
    # Loop through each property feature element and extract the bedroom number
    for feature_element3 in property_feature_elements3:
        feature_text3 = feature_element3.text.strip()
        
        # Check if the feature text contains "Beds"
        if "Parking" in feature_text3:
            park_number = feature_text3.split()[0]  # Extract the number before "Beds"
            parks.append(park_number)
        else:
            parks.append(' ')
except:
    parks.append(' ')

# Print the extracted bedroom numbers
for park in parks:
    print(bedroom)


house_type = driver.find_elements(By.XPATH, "//span[contains(@class, 'css-69')]")
types = []
try:
  
    for type in house_type:
        types.append(type.text)
    
except:
    types.append(' ')

print(types)


data = {'Address': [], 'Prices': [], 'Bedroom': [], 'Bathroom': [], 'Parking' : [], 'Type': []} 

max_length = max(len(address), len(prices))
bedroom = bedrooms + [''] * (max_length - len(bedrooms))

data['Address'].extend(address)
data['Prices'].extend(prices)
data['Bedroom'].extend(bedrooms)
data['Bathroom'].extend(baths)
data['Parking'].extend(parks)
data['Type'].extend(types)

current_page = 25
df = pd.DataFrame(data)
df.to_excel(f'../data/landing/rental{current_page}.xlsx', index=False)
print(f"Data written to rental{current_page}.xlsx")

input("Press Enter to exit")
driver.quit()