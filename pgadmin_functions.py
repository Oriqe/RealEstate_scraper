import psycopg2
from datetime import datetime


def get_new_search_number():
    connection = psycopg2.connect(database="real_estate", user="postgres", password="********",
                                  host="localhost")
    cursor = connection.cursor()
    cursor.execute(f"""SELECT MAX(search_number) FROM new_first_list;""")
    answer = cursor.fetchall()[0][0]
    answer += 1
    cursor.close()
    return answer


def insert_zillow(line_of_dicts):
    import psycopg2

    connection = psycopg2.connect(database="real_estate", user="postgres", password="*********",
                                  host="localhost")
    cursor = connection.cursor()

    for i in line_of_dicts:
        if i:

            cursor.execute(

                f"""INSERT INTO new_first_list VALUES ('{i["home_type"]}',
                                                '{i["street_address"]}',
                                                '{i["city"]}',
                                                '{i["state"]}',
                                                '{i["zipcode"]}',
                                                '{i["longitude"]}',
                                                '{i["latitude"]}',
                                                '{i["home_status"]}',
                                                '{i["days_on_zillow"] if i["days_on_zillow"] != None else "NaN"}',
                                                '{i["zestimate"] if i["zestimate"] != None else "NaN"}',
                                                '{i["living_space"] if i["living_space"] != None else "NaN"}',
                                                '{i["lot_size"] if i["lot_size"] != None else "NaN"}',
                                                '{i["year_built"] if i["year_built"] != None else "NaN"}',
                                                '{i["price"] if i["price"] != "None" else "NaN"}',
                                                '{i["bedrooms"] if i["bedrooms"] != None else "NaN"}',
                                                '{i["bathrooms"] if i["bathrooms"] != None else "NaN"}',
                                                '{i["url"]}',
                                                '{i["rent_zestimate"] if i["rent_zestimate"] != None else "NaN"}',
                                                '{i["is_preforclosure_auction"]}',
                                                '{i["tax_assessed_value"] if i["tax_assessed_value"] != None else "NaN"}',
                                                '{i["time_stamp"]}',
                                                '{i["parcel_id"]}',
                                                '{i["county"]}',
                                                '{i["living_space_units"]}',
                                                '{i["search_number"]}',
                                                '{i["fsbo"]}',
                                                '{i["foreclosure"]}',
                                                '{i["for_auction"]}',
                                                '{i["bank_owned"]}',
                                                '{i["zpid"]}');""")

            connection.commit()
            for k in i["price_history"]:
                cursor.execute(
                    f"""INSERT INTO new_price_list VALUES ('{i["zpid"]}',
                                                        '{i["time_stamp"]}',
                                                        '{i["search_number"]}',
                                                        '{k["time"]}',
                                                        '{k["price"] if k["price"] != None else "NaN"}',
                                                        '{k["event"]}');""")
                connection.commit()
    cursor.close()
    print("inserted")


def dict_arrange(new_dict, search_number):
    ans = {"home_type": new_dict["homeType"],
           "street_address": new_dict["abbreviatedAddress"],
           "city": new_dict["city"],
           "state": new_dict["state"],
           "zipcode": new_dict["zipcode"],
           "longitude": new_dict["longitude"],
           "latitude": new_dict["latitude"],
           "home_status": new_dict["homeStatus"],
           "days_on_zillow": new_dict["daysOnZillow"],
           "zestimate": new_dict["zestimate"],
           "living_space": new_dict["livingAreaValue"],
           "lot_size": new_dict["lotSize"],
           "year_built": new_dict["yearBuilt"],
           "price": new_dict["price"],
           "bedrooms": new_dict["bedrooms"],
           "bathrooms": new_dict["bathrooms"],
           "url": "http://www.zillow.com" + new_dict["hdpUrl"],
           "rent_zestimate": new_dict["rentZestimate"],
           "is_preforclosure_auction": new_dict["isPreforeclosureAuction"],
           "tax_assessed_value": new_dict["taxAssessedValue"],
           "time_stamp": datetime.now(),
           "parcel_id": new_dict["parcelId"],
           "county": new_dict["county"][:-7],
           "living_space_units": new_dict["livingAreaUnits"],
           "search_number": search_number,
           "fsbo": new_dict["listingSubType"]["isFSBO"],
           "foreclosure": new_dict["listingSubType"]["isForeclosure"],
           "for_auction": new_dict["listingSubType"]["isForAuction"],
           "bank_owned": new_dict["listingSubType"]["isBankOwned"],
           "zpid": new_dict["zpid"],
           "price_history": new_dict["priceHistory"]
           }
    return ans
