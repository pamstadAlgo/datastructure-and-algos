

class BinarySearch:

    def __init__(self, ordered_list):
        self.list = ordered_list

    def search(self, target):
        found = False
        first = 0
        last = len(self.list)-1

        while first <= last and not found:
            #compute mid point
            mid = (first + last)//2

            #compare target to mid
            if target < self.list[mid]:
                #move last
                last = mid -1
            elif target > self.list[mid]:
                first = mid + 1
            else:
                found = True
                return mid
            


bs = BinarySearch([2,5,8,12,16,23,38,56,72,91])

print(bs.search(2))