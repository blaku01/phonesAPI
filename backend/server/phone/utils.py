from time import sleep
from bs4 import BeautifulSoup
import requests


def get_image(model_name):
    url = f"https://www.google.com/search?q={model_name}&sxsrf=ALiCzsbBKaJNxy7lY6tudbSNlAN569ZGiQ:1652964597118&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiBvoz9zOv3AhXlo4sKHfFcA7wQ_AUoAnoECAIQBA&biw=1396&bih=685&dpr=1.38&sfr=gws&gbv=1&sei=Az2GYqnFFdH_qgGDh424AQ"
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    items = doc.find("img", {"class":'yWs4tf'})
    sleep(0.2)
    return items['src']
