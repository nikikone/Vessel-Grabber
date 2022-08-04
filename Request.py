

class Request(object):
    page = ""
    api = []

    def __init__(self, page, blocks):
        page_url = f'https://www.marinetraffic.com/ru/ais/home/centerx:{page["x"]}/centery:{page["y"]}/zoom:{page["z"]}'
        headers = {
            "Accept": "*/*",
            "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/64.0.3282.167 Safari/537.36",
            "x-requested-with": "XMLHttpRequest",
            "authority": "www.marinetraffic.com",
            "vessel-image": "00981b0123ffd63a011457d3a2c4de528a01"
        }
        self.page = {
            "url": page_url,
            "headers": headers
        }
        for block in blocks:
            api_url = f'https://www.marinetraffic.com/getData/get_data_json_4' \
                      f'/z:{block["z"]}/X:{block["x"]}/Y:{block["y"]}/station:0'
            self.api.append({
                "url": api_url,
                "headers": headers
            })
