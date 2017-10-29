# /usr/bin/evn python
# coding:utf-8

class TLQuestion(object):

    def __init__(self):
        pass
    @staticmethod
    def lowest_price():
        buy_modle = [1, 1, 2, 2, 2]
        discount = {1:1,2:0.95,3:0.9,4:0.80,5:0.75}
        price = 0
        book_type = len(buy_modle)
        for i in range(book_type):
            buy_modle.sort(reverse=True)
            rest_book_type = len(buy_modle)
            for j in range(rest_book_type):
                buy_modle.sort(reverse=True)
                if buy_modle[-1]==0:
                    buy_modle.pop()
            rest_type = len(buy_modle)
            if rest_type:
                min_num = buy_modle[-1]
                price += min_num*(rest_type*8.0*discount.get(rest_type))
                for k in range(rest_type):
                    buy_modle[k]-=min_num
        return price

if __name__=="__main__":
    test = TLQuestion()
    print test.lowest_price()
