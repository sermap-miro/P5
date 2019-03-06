Facteur_Pont_Resistance_30V = 9.93
Facteur_Pont_Resistance_30V = 9.2

batterie_reg_a = 0.00815919327063187
batterie_reg_b = 2.61834435852431

# pour 20 V = > 10.21

def Batt_Mean(m, n=100):
    x=0
    for _ in range(n):
        x+=m.BATTERIE()
        #x+=self.BATTERIE()*1.1/1024
    #print('{}'.format(x/n))
    return (x/n)
#
# def Batt_Mean(n=10):
#     x=0
#     for _ in range(n):
#         x+=m.BATTERIE() * 34 * 1.1 / 4095
#         #x+=self.BATTERIE()*1.1/1024
#     print('{}'.format(x/n))
#
#
def Scan(n=120):
    for _ in range(n):
        Batt_Mean()
        time.sleep(0.5)

# f(x) = a * x + b

# a = (f(x_2) - f(x_1)) / (x_2 - x_1)
# b = (x_2 * f(x_1) - x_1 * f(x_2)) / (x_2 - x_1)

# a = (y_2 - y_1) / (x_2 - x_1)
# b = (x_2 * y_1 - x_1 * y_2) / (x_2 - x_1)

#def Regression(y_1=936, y_2=3352 ,x_1=10, x_2=30):
def Regression(x_1=904.7, x_2=3355.93 ,y_1=10, y_2=30):
    return ((y_2 - y_1) / (x_2 - x_1), (x_2 * y_1 - x_1 * y_2) / (x_2 - x_1))
    #return ((30 - 10) / (self.batterie_30_v - self.batterie_10_v), (self.batterie_30_v * 10 - self.batterie_10_v * 30) / (self.batterie_30_v - self.batterie_10_v))


#   print('{},{}'.format(m.batterie_10_v, m.batterie_30_v))
