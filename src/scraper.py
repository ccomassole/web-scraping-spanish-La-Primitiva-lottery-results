# Press CTRL + B to launch the Script from SublimeText
# Practice 1. Web Scraping from the website loteriasyapuestasdelestado.es
# NOTE: chromedriver.exe required and placed in the same folder than curent script


# Scraper Class Definition Module

import os  # path management
import time  # time control
from bs4 import BeautifulSoup  # scraping
import lxml  # Processing files with xml format
import numpy as np  # Advanced calculations (required by pandas library)
import pandas as pd  # Multidimensional data manipulation
from selenium import webdriver  # Automatic Browser management
from selenium.webdriver.chrome.options import Options  # Chrome Driver Options for Selenium
from selenium.webdriver.support.ui import Select  # Select class to control select html options with selenium
from fake_useragent import UserAgent  # Useragent faker.


class Scraper():

    def __init__(self, name):
        # Draws class definition
        draws = [
            'Classic',
            'ElGordo'
        ]
        subdomains = {
            'Classic': "/es/la-primitiva",
            'ElGordo': "/es/gordo-primitiva"
        }
        labels = {
            'Classic': "la Loteria Primitiva",
            'ElGordo': "el Gordo de la Primitiva"
        }

        if name in draws:
            self.tipo = name
            self.subdomain = subdomains[name]
            self.url = "https://www.loteriasyapuestas.es"
            self.label = labels[name]
        else:
            # Exception in case of error during the instantiation
            print("Oops! The requires Draw called as " + "'" + name + "'" + " does not exist.  Check the code of the main module...")
            exit()

    def __get_html(self, url, driver, waiting_time, date="nd"):
        # Downloads the page to scrap combining Selenium and Beautiful Soup

        if date == "nd":
            try:
                driver.get(url)
            except:
                print('Oops! Error accessing ' + url + '. Verify the url name or the network.')
                exit()
            time.sleep(waiting_time)
        else:
            try:
                select = Select(driver.find_element_by_id('day'))
            except:
                print("Oops! Html layout seems to be changed. Check it and re-code if necessary.")
                exit()
            select.select_by_visible_text(date)
            time.sleep(waiting_time)
        try:
            element = driver.find_element_by_id("idContainerLoteriaNacional")
        except:
            print("Oops! Html layout seems to be changed. Check it and re-code if necessary.")
            exit()
        return element.get_attribute('outerHTML')

    def __get_dates(self, html):
        # Scrapes the dates of the last draws and stores all of them in a list

        dates = []
        try:
            match = html.find('select', id='day')
            options = match.find_all('option')
        except:
            print("Oops! Html layout seems to be changed. Check it and re-code if necessary.")
            exit()
        for date in options:
            dates.append(date.text)
        return dates

    def __get_data(self, html, date):
        # get the data with BeautifulSoup

        combination = {}  # Dictionary that will store the winning numbers for a particular date

        # Asign basic values (draw type and date of the draw)
        combination['Lottery'] = self.tipo
        combination['Date'] = date

        # Scrape the winning numbers
        # Main winning numbers
        try:
            match = html.find('div', class_='cuerpoRegionIzq')
            match = match.find('ul')
            i = 1
            for winning_number in match.find_all('li'):
                winning_number = winning_number.text
                winning_number = winning_number.split(' ')
                combination['Winner_Num_' + str(i)] = winning_number[1]
                i = i + 1

            # Complementary and Refund winning numbers
            match = html.find('div', class_='cuerpoRegionDerecha')
            for winning_number in match.find_all('span'):
                winning_number = winning_number.text
                if i == 7:
                    combination['Complementary'] = winning_number  # Complementary Winning Number
                else:
                    combination['Refund'] = winning_number  # Refund Winning Number
                i = i + 1

            # Joker Sequence only for Classic Game
            if self.tipo == 'Classic':
                match = html.find('div', class_='joker')
                winning_number = match.find('span', class_='numero').text
                # Cleaning and refining the text
                winning_number = winning_number.replace(' ', '')
                winning_number = winning_number.replace('\r', '')
                winning_number = winning_number.replace('\n', '')
                winning_number = winning_number.replace('\t', '')
                combination['Joker'] = winning_number  # Joker Winning Number
        except:
            print("Oops! Html layout seems to be changed. Check it and re-code if necessary.")
            exit()
        return combination

    def scrape(self):
        # Self scrape process

        results = {}  # diccionary to store all lottery results
        draws_results = pd.DataFrame()  # dataframe to manage the stored results

        # Driver navigator configuration (browser: Chrome, library: Selenium)
        options = Options()
        ua = UserAgent()
        options.add_argument(f'user-agent={ua.random}')  # random user-agent generator (to reduce the risk to be blocked)
        waiting_period = 2  # 2 seconds waiting time before scraping the pages

        # Launch Chrome browser
        try:
            os.chdir("../drivers")
        except:
            print("Oops! Can find ../drivers folder")
            exit()
        try:
            scriptpath = os.getcwd()
            driverpath = scriptpath + "\chromedriver.exe"
            driver = webdriver.Chrome(options=options, executable_path=driverpath)
        except:
            print("Oops! Can not execute webdriver. Check if "'"chromedriver.exe"'" is properly installed in " + driverpath)
            exit()
        driver.set_window_position(-10000, 0)  # hide the browser from view

        # Download HTML element
        html_block = self.__get_html(self.url + self.subdomain, driver, waiting_period)
        bs = BeautifulSoup(html_block, 'lxml')

        # Get dates of the different draws
        draws_dates = self.__get_dates(bs)

        # For each date, get and safe the winning numbers in the dictionary
        i = 0
        for date in draws_dates:
            html_block = self.__get_html(self.url + self.subdomain, driver, waiting_period, date)
            bs = BeautifulSoup(html_block, 'lxml')
            results[i] = self.__get_data(bs, date)
            i = i + 1

        # Closing the driver
        driver.quit()

        # Transforming Dictionary into a Dataframe for final processing
        draws_results = pd.DataFrame(results).T

        # Showing and returning the results
        print("Ultimas Combinaciones Ganadoras de los sorteos de " + self.label + " de " + "'" + self.url + "'...\n")
        print(draws_results)
        return draws_results
