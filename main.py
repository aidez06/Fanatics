import time
import csv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import gspread
import time
from pprint import pprint
from oauth2client.service_account import ServiceAccountCredentials

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '\
           'AppleWebKit/537.36 (KHTML, like Gecko) '\
           'Chrome/75.0.3770.80 Safari/537.36'}



print(work_sheet.acell('B25').value)
each_products = [] #getting each product links


for page in range(1,6): # loop all pages from 1-5
    page_url = f'https://www.fanatics.com/?pageNumber={page}&pageSize=72&query=customizable%20jersey&sortOption=TopSellers'
    r = requests.get(page_url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    products = soup.find_all('div', {'class': 'product-image-container'}) # products
    for product in products:
        product_links =product.find('a')
        each_products.append(f"https://www.fanatics.com{product_links['href']}")

increment = 25
for each_product in each_products:
    r = requests.get(each_product,headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    product_wrapper = soup.find('div',{'class': 'layout-column large-4 medium-6 small-12'})
    product_name = product_wrapper.find('h1',{'data-talos':'labelPdpProductTitle'}).text

    #work_sheet.update(f'B{increment}',product_name)

    product_price = product_wrapper.find('span', {'class':'sr-only'}).text

    #work_sheet.update(f'G{increment}',product_price)

    product_size = product_wrapper.find('div', {'class': 'size-selector-list'})
    product_available_sizes = product_size.find_all('a', {'class': 'size-selector-button available'})




    print(product_name)
    print(product_price)
    for product_available_size in product_available_sizes:
        print(product_available_size.text) # this is all getting available sizes of products
        #work_sheet.update(f'G{increment}', product_available_size.text)


    product_images = soup.find('div', {'class': 'thumbnails text-center'})  # getting all the images on this loop
    try:
        image_products = []
        if product_images:
            for product_image in product_images:
                output_product = product_image.find('img')['src']
                print(f"https:{output_product[:-3] + '900'}")
                image_products.append(f"https:{output_product[:-3] + '900'}")
        print(image_products)
    except:
        pass

    


