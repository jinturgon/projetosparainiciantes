import requests

class Translate:
    def __init__(self, TEXT:str):
        self.text = TEXT

    def yandex_translate (self) -> str:
        URL = "https://translate.yandex.net/api/v1.5/tr.json/translate"
        KEY = "< API KEY >"
        LANG = "en-pt"
        FORMAT = "plain"
        OPTIONS = "1"    

        try:
            self.text = self.text.replace("’","'")
        except:
            Exception
        try:
            self.text = self.text.replace("•","-")
        except:
            Exception

        # defining a params dict for the parameters to be sent to the API 
        PARAMS = {'key':KEY, 'text':self.text.encode("utf-8"), 'lang':LANG, 'format':FORMAT, 'options':OPTIONS}

        # sending get request and saving the response as response object 
        r = requests.post(url = URL, params = PARAMS, headers={"content-type":"application/json;charset=UTF-8"})
        data = r.json()
        newtext = data['text']

        return newtext[0]