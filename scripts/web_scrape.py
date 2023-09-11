import os
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options 
import pandas as pd 
from itertools import zip_longest

N_PAGES = range(26, 39)
PRICE_RANGE = [(510, 550)]
for price in PRICE_RANGE:
    lowest_price = price[0]
    highest_price = price[1]
    for page in N_PAGES:
        website = f"https://www.domain.com.au/rent/melbourne-region-vic/?ptype=apartment-unit-flat,block-of-units,development-site,duplex,free-standing,new-apartments,new-home-designs,new-house-land,new-land,pent-house,semi-detached,studio,terrace,town-house,vacant-land,villa&price={lowest_price}-{highest_price}&sort=price-asc&page={page}"
        chromedriver_path = 'chromedriver-mac-arm64/chromedriver.exe'

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

        # Zip data into columns with equal lengths
        zipped_data = list(zip_longest(address, prices, bedrooms, baths, parks, types, fillvalue=' '))

        # Extend the data dictionary with zipped_data
        for item in zipped_data:
            data['Address'].append(item[0])
            data['Prices'].append(item[1])
            data['Bedroom'].append(item[2])
            data['Bathroom'].append(item[3])
            data['Parking'].append(item[4])
            data['Type'].append(item[5])

        df = pd.DataFrame(data)
        df.to_csv(f'../data/raw/dataset/price_{lowest_price}_{highest_price}_page{page}.csv', index=False)
        print(f"Data written {page}.xlsx")

input("Press Enter to exit")
driver.quit()