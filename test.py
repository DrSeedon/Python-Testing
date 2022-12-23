import json
import requests


def get_data():
    cookies = {
        '_ym_uid': '1668400941802674885',
        '_ym_d': '1668400941',
        '__lhash_': '57e0d9e778853852d41b70d29a4df52c',
        'MVID_AB_PDP_CHAR': '2',
        'MVID_AB_SERVICES_DESCRIPTION': 'var4',
        'MVID_ACTOR_API_AVAILABILITY': 'true',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CART_AVAILABILITY': 'true',
        'MVID_CATALOG_STATE': '1',
        'MVID_CITY_ID': 'CityCZ_1854',
        'MVID_CREDIT_AVAILABILITY': 'true',
        'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GIFT_KIT': 'true',
        'MVID_GLC': 'true',
        'MVID_GLP': 'true',
        'MVID_GTM_ENABLED': '011',
        'MVID_IMG_RESIZE': 'true',
        'MVID_INIT_DATA_OFF': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '2400000100000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_HANDOVER': '1',
        'MVID_LP_SOLD_VARIANTS': '3',
        'MVID_MCLICK': 'true',
        'MVID_MINDBOX_DYNAMICALLY': 'true',
        'MVID_MINI_PDP': 'true',
        'MVID_MOBILE_FILTERS': 'true',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_DESKTOP_FILTERS': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_PROMO_CATALOG_ON': 'true',
        'MVID_REGION_ID': '52',
        'MVID_REGION_SHOP': 'S913',
        'MVID_SERVICES': '111',
        'MVID_SERVICES_MINI_BLOCK': 'var2',
        'MVID_TIMEZONE_OFFSET': '7',
        'MVID_WEBP_ENABLED': 'true',
        'MVID_WEB_SBP': 'true',
        'SENTRY_ERRORS_RATE': '0.1',
        'SENTRY_TRANSACTIONS_RATE': '0.5',
        '_gid': 'GA1.2.931511672.1671791388',
        '_sp_ses.d61c': '*',
        '_ym_isad': '1',
        '__SourceTracker': 'google__organic',
        'admitad_deduplication_cookie': 'google__organic',
        'SMSError': '',
        'authError': '',
        'uxs_uid': 'bb6a3900-82ac-11ed-a0d8-a94fcd7cdf5b',
        'advcake_track_id': 'fb5b2436-a074-cafa-7ea6-2b16aec5fc1e',
        'advcake_session_id': 'cc3f0e44-8892-a461-4b7e-90330f140f86',
        'tmr_lvid': 'd3c822b9425e300c6b82e0e120488375',
        'tmr_lvidTS': '1671791391048',
        'flocktory-uuid': '8215e61b-ebbb-4e93-827b-c3278d671e6b-8',
        'afUserId': 'c53847ab-69ec-4c66-924c-b65f4ef6171f-p',
        'AF_SYNC': '1671791392095',
        'flacktory': 'no',
        'BIGipServeratg-ps-prod_tcp80': '2449792010.20480.0000',
        'bIPs': '-1707567431',
        'MVID_GUEST_ID': '22078633996',
        'MVID_VIEWED_PRODUCTS': '',
        'wurfl_device_id': 'generic_web_browser',
        'JSESSIONID': 'ZQLkjlDDgjy2lqCTF0JvqJjfvd481hRP3TQXWK2JVJmN2nXJmpZj!87393423',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'true',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'MVID_CART_MULTI_DELETE': 'true',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'false',
        'HINTS_FIO_COOKIE_NAME': '1',
        'searchType2': '2',
        'COMPARISON_INDICATOR': 'false',
        'MVID_NEW_OLD': 'eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9',
        'MVID_OLD_NEW': 'eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==',
        'BIGipServeratg-ps-prod_tcp80_clone': '2449792010.20480.0000',
        'MVID_GTM_BROWSER_THEME': '1',
        'deviceType': 'desktop',
        'CACHE_INDICATOR': 'true',
        '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VTXAlYIQttM3oXHnthWiQjCSNpTUx1d3c7Ly1DZlUJZ1xDZH10HCczNxkwQVFFM3V6CR81GkNsIGhKXSFGRk5/LBoYCGwmWAwUXj4zaWVpcC9gIBIlEU0hF0ZaFXtDLGAMcRVcQ0huejI8aR5fR10iP0ccOmlRJD4yXhA8dWUJCzowJS0xZid8Syk1HREyXldVNDtnQVRYigkgWA==',
        '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VTXAlYIQttM3oXHnthWiQjCSNpTUx1d3c7Ly1DZlUJZ1xDZH10HCczNxkwQVFFM3V6CR81GkNsIGhKXSFGRk5/LBoYCGwmWAwUXj4zaWVpcC9gIBIlEU0hF0ZaFXtDLGAMcRVcQ0huejI8aR5fR10iP0ccOmlRJD4yXhA8dWUJCzowJS0xZid8Syk1HREyXldVNDtnQVRYigkgWA==',
        'cfidsgib-w-mvideo': 'RSLW3SHaNKCtMaI9Rfdr9WkSW+q/9SfY6BtUj39E+tQeQ8lChlfn89YZNqTRqXI36Y1nV8MHCvhauP0rT0BXEMczk37qQAcvItjYYIrHWdRsfNSHsWMjYux9SQaS/VQe4TXgGyTdnv9xZB5Xa0qXksqNDr4jrBX6KRXv',
        'cfidsgib-w-mvideo': 'RSLW3SHaNKCtMaI9Rfdr9WkSW+q/9SfY6BtUj39E+tQeQ8lChlfn89YZNqTRqXI36Y1nV8MHCvhauP0rT0BXEMczk37qQAcvItjYYIrHWdRsfNSHsWMjYux9SQaS/VQe4TXgGyTdnv9xZB5Xa0qXksqNDr4jrBX6KRXv',
        'gsscgib-w-mvideo': 'Hek4KZuudVaM4j2ba/UKcK8Quqn8vAcoSFgeoJ7kTPZMQ+CDF16fIlNqaIt+mhbGSHpO+Be2bqAcqLwHoC1hfoq2T77aMpPYVUXPNH8C5nHXAoHKQoDgtymKE5ZBUNO1uW5/OIinJlx5NUwI+wAiIMMyU4ofMyIoJGcRhsJuqqhfRH/mF5FbqseNBLbj+t+bz5+L/OSNtPGnJ1R6yG/U+aHDT0i5Kj7Yk6BnUW1B3/GqDxbl2B0NnEjXfIXAxA==',
        'gsscgib-w-mvideo': 'Hek4KZuudVaM4j2ba/UKcK8Quqn8vAcoSFgeoJ7kTPZMQ+CDF16fIlNqaIt+mhbGSHpO+Be2bqAcqLwHoC1hfoq2T77aMpPYVUXPNH8C5nHXAoHKQoDgtymKE5ZBUNO1uW5/OIinJlx5NUwI+wAiIMMyU4ofMyIoJGcRhsJuqqhfRH/mF5FbqseNBLbj+t+bz5+L/OSNtPGnJ1R6yG/U+aHDT0i5Kj7Yk6BnUW1B3/GqDxbl2B0NnEjXfIXAxA==',
        'fgsscgib-w-mvideo': 'cp0M44e5eb8c0e2d7ebe80aa55997bbff5424333',
        'fgsscgib-w-mvideo': 'cp0M44e5eb8c0e2d7ebe80aa55997bbff5424333',
        'cfidsgib-w-mvideo': 'zGfpTansjBSxjdGP4DblpaXuVviS1qEtOkaVYFqkokno9c0TGJjdEdrTcyzFCZG06R6QkZfQI21c6UshuH14/l8V0YuRCHbB2S/t861/Q59xtKra9xIjRFigvf/rGGr/k7EFCWrctR13hNmHlCKsu4M5uGrTgo7xSsap',
        '_ga': 'GA1.2.1563689430.1671791388',
        'tmr_detect': '1%7C1671791421191',
        '_dc_gtm_UA-1873769-1': '1',
        '_dc_gtm_UA-1873769-37': '1',
        '_sp_id.d61c': '9641e5b5-2575-4589-bda0-757d44c67755.1668400942.3.1671791490.1668587631.443c5de6-5b58-465a-8887-345bfba06646.4c0ba6a4-f9c9-4efc-83a9-af142c7ab05c.997e2516-4752-44b8-832e-3c6b20e0108b.1671791387875.45',
        '_ga_CFMZTSS5FM': 'GS1.1.1671791387.1.1.1671791537.0.0.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1671791387.1.1.1671791537.11.0.0',
        'MVID_ENVCLOUD': 'prod1',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
        'baggage': 'sentry-transaction=%2F,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=4fe586207c0e48709ccca10521d9e322,sentry-sample_rate=0.5',
        'cache-control': 'no-cache',
        # 'cookie': '_ym_uid=1668400941802674885; _ym_d=1668400941; __lhash_=57e0d9e778853852d41b70d29a4df52c; MVID_AB_PDP_CHAR=2; MVID_AB_SERVICES_DESCRIPTION=var4; MVID_ACTOR_API_AVAILABILITY=true; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CART_AVAILABILITY=true; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityCZ_1854; MVID_CREDIT_AVAILABILITY=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GIFT_KIT=true; MVID_GLC=true; MVID_GLP=true; MVID_GTM_ENABLED=011; MVID_IMG_RESIZE=true; MVID_INIT_DATA_OFF=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=2400000100000; MVID_LAYOUT_TYPE=1; MVID_LP_HANDOVER=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_MOBILE_FILTERS=true; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_REGION_ID=52; MVID_REGION_SHOP=S913; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_TIMEZONE_OFFSET=7; MVID_WEBP_ENABLED=true; MVID_WEB_SBP=true; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; _gid=GA1.2.931511672.1671791388; _sp_ses.d61c=*; _ym_isad=1; __SourceTracker=google__organic; admitad_deduplication_cookie=google__organic; SMSError=; authError=; uxs_uid=bb6a3900-82ac-11ed-a0d8-a94fcd7cdf5b; advcake_track_id=fb5b2436-a074-cafa-7ea6-2b16aec5fc1e; advcake_session_id=cc3f0e44-8892-a461-4b7e-90330f140f86; tmr_lvid=d3c822b9425e300c6b82e0e120488375; tmr_lvidTS=1671791391048; flocktory-uuid=8215e61b-ebbb-4e93-827b-c3278d671e6b-8; afUserId=c53847ab-69ec-4c66-924c-b65f4ef6171f-p; AF_SYNC=1671791392095; flacktory=no; BIGipServeratg-ps-prod_tcp80=2449792010.20480.0000; bIPs=-1707567431; MVID_GUEST_ID=22078633996; MVID_VIEWED_PRODUCTS=; wurfl_device_id=generic_web_browser; JSESSIONID=ZQLkjlDDgjy2lqCTF0JvqJjfvd481hRP3TQXWK2JVJmN2nXJmpZj!87393423; MVID_CALC_BONUS_RUBLES_PROFIT=true; NEED_REQUIRE_APPLY_DISCOUNT=true; MVID_CART_MULTI_DELETE=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; MVID_GET_LOCATION_BY_DADATA=DaData; PRESELECT_COURIER_DELIVERY_FOR_KBT=false; HINTS_FIO_COOKIE_NAME=1; searchType2=2; COMPARISON_INDICATOR=false; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; BIGipServeratg-ps-prod_tcp80_clone=2449792010.20480.0000; MVID_GTM_BROWSER_THEME=1; deviceType=desktop; CACHE_INDICATOR=true; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VTXAlYIQttM3oXHnthWiQjCSNpTUx1d3c7Ly1DZlUJZ1xDZH10HCczNxkwQVFFM3V6CR81GkNsIGhKXSFGRk5/LBoYCGwmWAwUXj4zaWVpcC9gIBIlEU0hF0ZaFXtDLGAMcRVcQ0huejI8aR5fR10iP0ccOmlRJD4yXhA8dWUJCzowJS0xZid8Syk1HREyXldVNDtnQVRYigkgWA==; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VTXAlYIQttM3oXHnthWiQjCSNpTUx1d3c7Ly1DZlUJZ1xDZH10HCczNxkwQVFFM3V6CR81GkNsIGhKXSFGRk5/LBoYCGwmWAwUXj4zaWVpcC9gIBIlEU0hF0ZaFXtDLGAMcRVcQ0huejI8aR5fR10iP0ccOmlRJD4yXhA8dWUJCzowJS0xZid8Syk1HREyXldVNDtnQVRYigkgWA==; cfidsgib-w-mvideo=RSLW3SHaNKCtMaI9Rfdr9WkSW+q/9SfY6BtUj39E+tQeQ8lChlfn89YZNqTRqXI36Y1nV8MHCvhauP0rT0BXEMczk37qQAcvItjYYIrHWdRsfNSHsWMjYux9SQaS/VQe4TXgGyTdnv9xZB5Xa0qXksqNDr4jrBX6KRXv; cfidsgib-w-mvideo=RSLW3SHaNKCtMaI9Rfdr9WkSW+q/9SfY6BtUj39E+tQeQ8lChlfn89YZNqTRqXI36Y1nV8MHCvhauP0rT0BXEMczk37qQAcvItjYYIrHWdRsfNSHsWMjYux9SQaS/VQe4TXgGyTdnv9xZB5Xa0qXksqNDr4jrBX6KRXv; gsscgib-w-mvideo=Hek4KZuudVaM4j2ba/UKcK8Quqn8vAcoSFgeoJ7kTPZMQ+CDF16fIlNqaIt+mhbGSHpO+Be2bqAcqLwHoC1hfoq2T77aMpPYVUXPNH8C5nHXAoHKQoDgtymKE5ZBUNO1uW5/OIinJlx5NUwI+wAiIMMyU4ofMyIoJGcRhsJuqqhfRH/mF5FbqseNBLbj+t+bz5+L/OSNtPGnJ1R6yG/U+aHDT0i5Kj7Yk6BnUW1B3/GqDxbl2B0NnEjXfIXAxA==; gsscgib-w-mvideo=Hek4KZuudVaM4j2ba/UKcK8Quqn8vAcoSFgeoJ7kTPZMQ+CDF16fIlNqaIt+mhbGSHpO+Be2bqAcqLwHoC1hfoq2T77aMpPYVUXPNH8C5nHXAoHKQoDgtymKE5ZBUNO1uW5/OIinJlx5NUwI+wAiIMMyU4ofMyIoJGcRhsJuqqhfRH/mF5FbqseNBLbj+t+bz5+L/OSNtPGnJ1R6yG/U+aHDT0i5Kj7Yk6BnUW1B3/GqDxbl2B0NnEjXfIXAxA==; fgsscgib-w-mvideo=cp0M44e5eb8c0e2d7ebe80aa55997bbff5424333; fgsscgib-w-mvideo=cp0M44e5eb8c0e2d7ebe80aa55997bbff5424333; cfidsgib-w-mvideo=zGfpTansjBSxjdGP4DblpaXuVviS1qEtOkaVYFqkokno9c0TGJjdEdrTcyzFCZG06R6QkZfQI21c6UshuH14/l8V0YuRCHbB2S/t861/Q59xtKra9xIjRFigvf/rGGr/k7EFCWrctR13hNmHlCKsu4M5uGrTgo7xSsap; _ga=GA1.2.1563689430.1671791388; tmr_detect=1%7C1671791421191; _dc_gtm_UA-1873769-1=1; _dc_gtm_UA-1873769-37=1; _sp_id.d61c=9641e5b5-2575-4589-bda0-757d44c67755.1668400942.3.1671791490.1668587631.443c5de6-5b58-465a-8887-345bfba06646.4c0ba6a4-f9c9-4efc-83a9-af142c7ab05c.997e2516-4752-44b8-832e-3c6b20e0108b.1671791387875.45; _ga_CFMZTSS5FM=GS1.1.1671791387.1.1.1671791537.0.0.0; _ga_BNX5WPP3YK=GS1.1.1671791387.1.1.1671791537.11.0.0; MVID_ENVCLOUD=prod1',
        'dnt': '1',
        'pragma': 'no-cache',
        'referer': 'https://www.mvideo.ru/komputernye-komplektuushhie-5427/videokarty-5429/f/tolko-v-nalichii=da',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': '4fe586207c0e48709ccca10521d9e322-ac4af03b8d821346-1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54',
        'x-set-application-id': 'b33b94b2-9bc8-433c-b5eb-599a3103b290',
    }

    params = {
        'categoryId': '5429',
        'offset': '0',
        'limit': '24',
        'filterParams': 'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
        'doTranslit': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing',
                            params=params, cookies=cookies, headers=headers).json()

    products_ids = response.get('body').get('products')

    with open('1_products_ids.json', 'w') as file:
        json.dump(products_ids, file, indent=4, ensure_ascii=False)

    # print(products_ids)

    json_data = {
        'productIds': products_ids,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list',
                             cookies=cookies, headers=headers, json=json_data).json()
    with open('2_items.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    # print(len(response.get('body').get('products')))

    products_ids_str = ','.join(products_ids)

    params = {
        'productIds': products_ids_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices',
                            params=params, cookies=cookies, headers=headers).json()

    with open('3_prices.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    items_prices = {}

    material_prices = response.get('body').get('materialPrices')

    for item in material_prices:
        item_id = item.get('price').get('productId')
        item_base_price = item.get('price').get('basePrice')
        item_sale_price = item.get('price').get('salePrice')
        item_bonus = item.get('bonusRubles').get('total')

        items_prices[item_id] = {
            'item_basePrice': item_base_price,
            'item_salePrice': item_sale_price,
            'item_bonus': item_bonus
        }

    with open('4_items_prices.json', 'w') as file:
        json.dump(items_prices, file, indent=4, ensure_ascii=False)


def get_result():
    with open('2_items.json') as file:
        product_data = json.load(file)

    with open('4_items_prices.json') as file:
        product_prices = json.load(file)

    product_data = product_data.get('body').get('products')

    for item in product_data:
        product_id = item.get('productId')

        if product_id in product_prices:
            prices = product_prices[product_id]

        item['item_basePrice'] = prices.get('item_basePrice')
        item['item_salePrice'] = prices.get('item_salePrice')
        item['item_bonus'] = prices.get('item_bonus')

    with open('5_result.json', 'w') as file:
        json.dump(product_data, file, indent=4, ensure_ascii=False)


def main():
    get_data()
    get_result()


if __name__ == '__main__':
    main()
