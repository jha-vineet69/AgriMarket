import requests
import json
from bs4 import BeautifulSoup as bs
import pandas as pd
from datetime import date, timedelta
from selenium import webdriver
from time import sleep
from urllib.parse import urlencode


def get_url(Commodity, CommodityHead):
    """Given a Commodity and a CommodityHead, returns the complete URL to be browsed"""
    base_url = 'https://agmarknet.gov.in/SearchCmmMkt.aspx'
    parameters = {
        "Tx_Commodity": Commodity,
        "Tx_State": "0",
        "Tx_District": 0,
        "Tx_Market": 0,
        "DateFrom": "01-Jan-2020",
        "DateTo": "31-Jan-2020",
        "Fr_Date": "01-Jan-2020",
        "To_Date": "31-Jan-2020",
        "Tx_Trend": 0,
        "Tx_CommodityHead": CommodityHead,
        "Tx_StateHead": "--Select--",
        "Tx_DistrictHead": "--Select--",
        "Tx_MarketHead": "--Select--",
    }
    query = urlencode(parameters)
    return "?".join([base_url, query])


def get_soup(driver):
    """Constructs and returns a soup using the HTML content of `url` passed"""

    source = driver.page_source
    # return the soup
    return bs(source, "html.parser")


def get_all_tables(soup):
    """Extracts and returns all tables in a soup object"""
    return soup.find_all("table")


def get_table_headers(table):
    """Given a table soup, returns all the headers"""
    headers = []
    for th in table.find("tr").find_all("th"):
        headers.append(th.text.strip())
    return headers


def get_table_rows(table):
    """Given a table, returns all its rows"""
    rows = []
    for tr in table.find_all("tr")[1:]:
        cells = []
        # grab all td tags in this table row
        tds = tr.find_all("td")
        for td in tds:
            cells.append(td.text.strip())
        rows.append(cells)
    return rows


def save_as_csv(soup, CommodityHead):
    """Extract data from soup and write it to Csv file"""
    # extract all the tables from the web page
    tables = get_all_tables(soup)

    # iterate over all tables
    for table in tables:
        # get the table headers
        headers = get_table_headers(table)
        # get all the rows of the table
        rows = get_table_rows(table)
        # save table as csv file
        try:
            with open(f"E:/Agri_Data/Agri_Data_{CommodityHead}_Jan_2020.csv", mode='ab') as f:
                pd.DataFrame(rows, columns=headers).to_csv(f, header=f.tell() == 0, index=False)

        except ValueError as ve:
            pass
    return


def main():
    driver = webdriver.Chrome(executable_path='chromedriver_win32/chromedriver')
    # read Commodity data from csv file
    df = pd.read_csv("CommodityAndCommodityHeads.csv")
    for row in df.itertuples(index=False):
        url = get_url(row.Commodity, row.CommodityHead)
        # driver.get('https://bit.ly/3h0JRse')
        driver.get(url)
        driver.maximize_window()
        sleep(10)

        # get the soup
        soup = get_soup(driver)
        save_as_csv(soup, row.CommodityHead)

        while True:
            try:
                driver.find_element_by_xpath("//input[contains(@alt, '>')]").click()
                sleep(5)
                soup = get_soup(driver)
                save_as_csv(soup, row.CommodityHead)

            except:
                print("No more pages left")
                break
        sleep(5)


if __name__ == "__main__":
    main()
