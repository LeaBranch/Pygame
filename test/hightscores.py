from effects import printText

class Hightscore:
    def __init__(self, table):
        self.hs_table = table
        
    def update(self, name, scores):
        self.hs_table[name] = scores
                        
    def print_1(self, x, y):
        step_x = 250
        step_y = 30

        for name, scores in self.hs_table.items():
            printText(name, x, y)
            x += step_x
            printText(str(scores), x, y)
            x -= step_x
            y += step_y
