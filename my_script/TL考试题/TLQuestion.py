# /usr/bin/evn python
# coding:utf-8

DISCOUNT_SELECTOR = {1: 1, 2: 0.95, 3: 0.9, 4: 0.80, 5: 0.75}


class TLQuestion(object):
    """价格计算器"""
    def __init__(self, book_one=0, book_two=0, book_three=0, book_four=0, book_five=0):
        self.buy_modle = [book_one, book_two, book_three, book_four, book_five]

    def lowest_price(self):
        """计算最低价格"""
        buy_modle = self.buy_modle
        price = 0
        book_type = len(buy_modle)
        for i in range(book_type):
            buy_modle.sort(reverse=True)
            rest_book_type = len(buy_modle)
            for j in range(rest_book_type):
                buy_modle.sort(reverse=True)
                if buy_modle[-1] == 0:
                    buy_modle.pop()
            rest_book_type = len(buy_modle)
            if rest_book_type:
                min_num = buy_modle[-1]
                price += min_num * (rest_book_type * 8.0 * DISCOUNT_SELECTOR.get(rest_book_type))
                for k in range(rest_book_type):
                    buy_modle[k] -= min_num
        return price

if __name__ == "__main__":
    test = TLQuestion(3,2,1)
    print test.lowest_price()
