def adding(x):
    def money(y):
        return x+y
 
    return money
 
pan = adding(15)
 
print(pan(10))