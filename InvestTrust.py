import requests
import json
import os

def get_data(load_url):
    html = requests.get(load_url)
    a = html.text[html.text.find("bootstrappedData:"):]
    b = a[a.find("\"price\""):]
    c = b[:b.find("}")]
    data = "{" + c + "}"
    data = json.loads(data)
    data.update({"name":os.path.basename(load_url)})
    return data

def data_2_str(data, th1=1.0, th2=2.0):
    name = data["name"]
    priceDate = data["priceDate"]
    price = float(data["price"])
    unit  = data["issuedCurrency"]
    percentChange1Day = float(data["percentChange1Day"])

    star = ""
    if percentChange1Day > th1:
        star = "@ sell"
    if percentChange1Day < -th1:
        star = "* buy"
    if percentChange1Day > th2:
        star = "@@@ sell"
    if percentChange1Day < -th2:
        star = "*** buy"
    return "{0:15s} : {1:10.3f} {2} [{3:+.2f} %]         {4}".format(name, price, unit, percentChange1Day, star)

# Test
if __name__ == "__main__":
    load_urls = [
      "https://www.bloomberg.co.jp/quote/NYFANG:IND",
      "https://www.bloomberg.co.jp/quote/QQQ:US",
    ]
    for load_url in load_urls:
        data = get_data(load_url)
        print(data_2_str(data))
