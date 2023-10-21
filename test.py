from utils.stock_id_list import Stock_symbol_data_centre
from utils.data_reader import Baseutils

if __name__ == "__main__":
    data_centre = Stock_symbol_data_centre()
    base_utils = Baseutils()
    sp500_list = data_centre.Get_data(1) #from wiki 
    #prices = base_utils.fetch_prices(sp500_list[0])
    prices = base_utils.fetch_DataFrame(sp500_list[0])
    print(sp500_list)
    print(prices)