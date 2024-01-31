import json
import pickle


class car:
    def __init__(self,color,body,power):
        self.color = color
        self. body = body
        self. power = power
    def bodys (self):
        print(f"Тип кузова - {self.body}")
    def powers (self):
        print(f"Мощность - {self.power}")
    def colors (self):
        print(f"Ваша машина {self.color} цвета")
    def pickle_car(self):
        return pickle.dumps(car)
    def json_car(self):
        with open('car.json','w',encoding='utf-8') as f:
            f.write(json.dumps(self.__dict__,indent=2))



x = car("красный", "седан", 200)
print(x.pickle_car())
# x.json_car()



class Books:
    def __init__(self,author, count_paged):
        self.author = author
        self.count_paged=count_paged
    def get_autgor(self):
        return f'Автор книги - {self.author}'
    def count(self):
        return f'Количество страниц - {self.count_paged}'

    def pickle_book(self):
        return pickle.dumps(Books)

    def json_Books(self):
        with open('book.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(self.__dict__,indent=4))


book = Books('Пушкин', 500)
print(book.pickle_book())
book.json_Books()


class Stadium:
    def __init__(self, capacity):
        self.capacity = capacity
    def fans(self):
        return f'колличество мест -{self.capacity}'

    def pickle_stadium(self):
        return pickle.dumps(Stadium)




    def json_stadium(self):
        with open('stadium.json','w',encoding='utf-8') as f:
            f.write(json.dumps(self.__dict__,indent=4))


stadi = Stadium("Wembley")
print(stadi.pickle_stadium())
stadi.json_stadium()