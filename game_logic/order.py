

class Order:
    def __init__(self, unit, order_type, target=None):
        self.unit = unit
        self.order_type = order_type  # 'move', 'hold', 'support', etc.
        self.target = target