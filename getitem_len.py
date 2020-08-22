import collections

Card = collections.namedtuple("Card", ['rank', 'suit'])  # 构建一个简单的类来表示一张纸牌，自Python2.6开始，namedtuple就加入到python里


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')  # 循环所有有可能的牌
    suits = "spades diamonds clubs hearts".split()  # 四种不同花色

    def __init__(self):
        self._card = [Card(rank, suit) for suit in self.suits for rank in self.ranks]  # 循环四个花色，13张不同的牌

    def __len__(self):
        return len(self._card)

    def __getitem__(self, position):
        return self._card[position]


if __name__ == '__main__':
    for i in reversed(range(5)):
        print(i)
