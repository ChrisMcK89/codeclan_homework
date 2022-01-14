class Guest:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def check_wallet(self):
        return self.wallet

    def reduce_wallet_by_fee(self, fee):
        self.wallet -= fee
        return self.wallet
