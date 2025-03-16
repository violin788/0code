exec(open('util.py').read())
def intrinio(inp):

    #Import the libraries:

    import intrinio_sdk as intrinio
    import pandas as pd

    #Authenticate using your personal API key, and select the API:

    #intrinio.ApiClient().set_api_key("YOUR_KEY_HERE")
    intrinio.ApiClient().set_api_key("OjA1ZDkxNjNkZGJlODZlZGFlM2UxZTA2NWM1Y2Q5ODBj")
    security_api = intrinio.SecurityApi()

    #You need to replace YOUR_KEY_HERE with your own API key.

    #Request the data:

    r = security_api.get_security_stock_prices(
        identifier="AAPL", 
        start_date="2022-01-01",
        #end_date="2021-12-31",
        end_date="2023-12-31", 
        frequency="daily",
        #page_size=10000
        page_size=10
    )

    #Convert the results into a DataFrame:

    df = (
        pd.DataFrame(r.stock_prices_dict)
        .sort_values("date")
        .set_index("date")
    )

    #Inspect the data:

    print(f"Downloaded {df.shape[0]} rows of data.")
    df.head()

    #The output looks as follows:

inp = []
intrinio(inp)