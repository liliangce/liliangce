# /usr/bin/evn python
# coding:utf-8


"""
假设有5本组合一套，剩余的有3本组合一套，那么该种组合的方式需要转换为两种4本组合
"""
DISCOUNT_SELECTOR = {1: 1, 2: 0.95, 3: 0.9, 4: 0.80, 5: 0.75}


class TotalPrice(object):
    """价格计算器"""
    def __init__(self, book_one=0, book_two=0, book_three=0, book_four=0, book_five=0):
        self.buy_books = [book_one, book_two, book_three, book_four, book_five]

    def decomposition_books(self):
        """由多到少最大组合"""
        buy_books = self.buy_books
        book_type = len(buy_books)
        composition = {}
        for i in range(book_type):
            buy_books.sort(reverse=True)
            rest_book_type = len(buy_books)
            for j in range(rest_book_type):
                buy_books.sort(reverse=True)
                if buy_books[-1] == 0:
                    buy_books.pop()
            rest_book_type = len(buy_books)
            if rest_book_type:
                composition[rest_book_type] = buy_books[-1]
                for k in range(rest_book_type):
                    buy_books[k] -= buy_books[-1]
        return composition

    def compute_best_composition(self):
        """如果有五本组合和3本组合存在，则需要转换最优组合"""
        best_composition = self.decomposition_books()
        if 5 in best_composition.keys() and 3 in best_composition.keys():
            if best_composition[3] > best_composition[5]:
                if 4 not in best_composition.keys():
                    best_composition[4] = 0
                best_composition[4] += best_composition[5]*2
                best_composition[3] -= best_composition[5]
                best_composition.pop(5)
            else:
                if 4 not in best_composition.keys():
                    best_composition[4] = 0
                best_composition[4] += best_composition[3]*2
                best_composition[5] -= best_composition[3]
                best_composition.pop(3)
        print best_composition
        return best_composition

    def total_price(self):
        """计算最低价格"""
        best_composition = self.compute_best_composition()
        price = 0
        for i in best_composition.keys():
            price += best_composition[i]*i*8*DISCOUNT_SELECTOR[i]
        return price

if __name__ == "__main__":
    test = TotalPrice(2, 2, 2, 1, 1)
    print test.total_price()
