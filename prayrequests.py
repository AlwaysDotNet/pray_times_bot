from requests import get, post

class PrayRequests:
    def __init__(self, reg:str) -> None:
        self.__reg_id = {"Toshkent":1,
                         "Andijon":17,
                         "Samarqand":47,
                         "Buxoro":34,
                         "Farg'ona":77,
                         "Xorazm":101,
                         "Namangan":149,
                         "Jizzax":107}
        self.__city = reg
        self.__content = ""
        self.__url = "https://praytime.uz/"
    def request(self):
        try:
            id = 1
            if self.__city in self.__reg_id.keys():
                id = self.__reg_id[self.__city]
            print(id)
            body = {
                "region_id":id
            }
            res = get(self.__url, params=body)
            if res.status_code == 200:
                self.__content = res.text
            else:
                raise Exception(f"Surov yuborishdan keyin xatolig javobi olindi: {res.status_code}")
        except Exception as e:
            print(e)
    @property
    def Content(self):
        return self.__content
if __name__ == "__main__":
    sl = PrayRequests("Farg'ona")
    sl.request()
    print(sl.Content)