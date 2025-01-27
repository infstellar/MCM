import math
def f_income(x):
    return -(232 * x * (1 - x / 100000))

def f_life_pressure(x):
    return (x / 100000 * x + 0.1 * x / 100000)

def f_2(x):
    return 1778594.35*(0.946)**(x/0.048)
def f_3(x):
    return 1670000*0.946**(10*x-48)

def func_1(x):
    x/=10 #gg
    if x <= 420000:
        r = x*2.408037064506496884000038528593e-4
    else:
        r = math.log(((x-1)/4000)+3, 1.01)-370
    if r > 200:
        r = 200
    return r

def func_2(x):
    if x <= 0:
        return -100
    else:

        if x<=135000:
            r = math.log(((x/12)+6500)/480000, 5)+2.25
        else:
            r = math.log((x+400000)/480000, 10)+0.152

        r *= (100/0.4)

        return r



def pop2spend(x):
    return x*(232+50)

def spend2income(x, TAX_RATE=0.13):
    return x*(1-TAX_RATE)

def spend2tax(x, TAX_RATE=0.13):
    return x*TAX_RATE

def pop2infrastructure(x):
    return -(8*x**1.05)

def infrast2tour_sat(x):
    return func_1(x)-100

def pop2tour_sat(x):
    r = x/1500 + 1
    r = -(r**2)+2*r+100
    # r = -(x**1.001+25000)/250
    # print(f'pop: {x}; pop2tour_sat: {r}')
    return r

def infrast2local_sat(x):
    r = func_1(x)-100
    return r

def income2local_sat(x):
    x = (x*(365/10000))
    r = (func_2(x))
    # print(f'income pre house: {x}; income2local_sat: {r}')
    return r

def tax2infrast(x):
    if x <= 546000:
        r = (x - 150000) * 1
    else:
        r = (x/1.2) * (25/(math.log(100*x, 1.4))) + 183000
    # print(f'tax: {x}; tax2infrast: {r}')
    return r

def get_infrastructure_value(pop, tax_rate=0.13):
    # print(f'pop: {pop}; infrast: {pop2infrastructure(pop)} + {tax2infrast(spend2tax(pop2spend(pop)))}')
    return pop2infrastructure(pop) + tax2infrast(spend2tax(pop2spend(pop), tax_rate))

def local_satisfy_function(pop, tax_rate=0.13):
    r = income2local_sat(spend2income(pop2spend(pop), tax_rate))*0.5 + infrast2local_sat(get_infrastructure_value(pop, tax_rate))*0.5
    # print(f'pop: {pop}; local_satisfy_function={income2local_sat(spend2income(pop2spend(pop)))} + {infrast2local_sat(get_infrastructure_value(pop))*0.5}')
    return r

def tourism_satisfy_function(pop, tax_rate=0.13):
    r1 = infrast2tour_sat(get_infrastructure_value(pop, tax_rate))*0.98
    r2 = pop2tour_sat(pop)*0.02
    r = r1 + r2
    return r

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import numpy as np
    figure = plt.figure()


    models_pop = [
        {
            'name': 'local_satisfy_function',
            'func': local_satisfy_function
        },
        {
            'name': 'tourism_satisfy_function',
            'func': tourism_satisfy_function
        },
        {
            'name': 'get_infrastructure_value',
            'func': get_infrastructure_value
        },
        {
            'name': 'pop2tour_sat',
            'func': pop2tour_sat
        },
        {
            'name': 'infrast2tour_sat(get_infrastructure_value(pop))',
            'func': lambda xx : infrast2tour_sat(get_infrastructure_value(xx))
        },
        {
            'name': 'tax2infrast(spend2tax(pop2spend(pop)))',
            'func': lambda xxx : tax2infrast(spend2tax(pop2spend(xxx)))
        }
    ]

    models_doller = [
        {
            'name': 'income2local_sat',
            'func': income2local_sat
        },
        {
            'name': 'infrast2local_sat',
            'func': infrast2local_sat
        }
    ]

    for index, model in enumerate(models_pop):
        X = np.arange(0, 20000,100)
        ax = figure.add_subplot(4,2,index+1)
        ax.set_title(model['name'])
        y = []
        for x in X:
            y.append(model['func'](x))
        ax.plot(X,y)
    for index, model in enumerate(models_doller):
        X = np.arange(0, 20000*450, 10000)
        ax = figure.add_subplot(4,2,index+1+6)
        ax.set_title(model['name'])
        y = []
        for x in X:
            y.append(model['func'](x))
        ax.plot(X,y)
    plt.show()

