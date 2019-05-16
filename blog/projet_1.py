import requests
import bs4


def get_last_price(isin, place):
    """
    Get last price from url
    :param isin: ISIN code of a stock
    :param place: quotation place of a stock
    :return: float value of the last price
    """
    url = rf'https://www.euronext.com/fr/nyx_eu_listings/real-time/quote?isin={isin}&mic={place}'
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    integer = soup.find('span', {'id': 'lastPriceint'}).text
    integer = integer[:-1]
    decimals = soup.find('sup', {'id': 'lastPricefract'}).text
    last_price = float(f"{integer}.{decimals}")
    return last_price


def get_name(isin, place):
    #
    # To get the name of each company
    #
    url = rf'https://www.euronext.com/fr/nyx_eu_listings/real-time/quote?isin={isin}&mic={place}'
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    name = soup.find('span', {'class': 'instrument-name'}).text
    return name


def get_change_since_close(isin, place):
    #
    # To get the last price of previous close
    #
    url = rf'https://www.euronext.com/fr/nyx_eu_listings/real-time/quote?isin={isin}&mic={place}'
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    change_close = soup.find('span', {'id': 'cnDiffRelvalue'}).text
    change_close = change_close[1:7]
    if change_close[0] == "+":
        change_close = change_close[1:]
    return change_close


def get_change_since_open(isin, place):
    #
    # To get the last price since open
    #
    url = rf'https://www.euronext.com/fr/nyx_eu_listings/real-time/quote?isin={isin}&mic={place}'
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    change_open = soup.find('span', {'id': 'cnOpenDiffRelvalue'}).text
    change_open = change_open[1:7]
    if change_open[0] == "+":
        change_open = change_open[1:]
    return change_open

    #
    # printing all the function used
    #

#isins = ['FR0003500008', 'FR0000036675', 'FR0013252186', 'FR0013283108', 'FR0013176526']
#place = 'XPAR'
# for isin in isins:
#     print(get_name(isin, place), " | Last Price = ", get_last_price(isin, place), " | Change since close =",
#     get_change_since_close(isin, place), " | Change since open = ", get_change_since_open(isin, place), "|", isin)


