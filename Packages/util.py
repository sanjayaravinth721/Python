class max():
    def findMax(self):
        a = [3, 5, 7, 9, 2]
        max=a[0]
        for num in a:
            if(num>max):
              max=num
        return max