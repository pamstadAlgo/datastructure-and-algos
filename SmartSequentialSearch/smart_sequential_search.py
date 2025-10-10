

class SmartSequentialSearch:

    def __init__(self, ordered_list):
        self.list = ordered_list

    def search(self,target):
        done = False
        loc = 0

        while loc < len(self.list) and not done:
            print(f'loc: {loc}, target: {target}, list[loc]: {self.list[loc]}')
            if target <= self.list[loc]:
                return loc
            else:
                loc += 1

sss = SmartSequentialSearch([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7])
print(sss.search(0.8))