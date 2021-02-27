sal_func = float(input())
sal_min = float(input())

reajuste = 0

def check_sal(sal):
    if sal < sal_min*1.5:
        return sal_min*1.5
    elif sal > sal_min*20:
        return sal_min*20
    return sal


if sal_func/sal_min <= 3:
    reajuste = sal_func*0.2
    sal = sal_func + reajuste
    sal = check_sal(sal)
    print(sal)
elif 3 < sal_func/sal_min <= 5:
    reajuste = sal_func*0.15
    sal = sal_func + reajuste
    sal = check_sal(sal)
    print(sal)
else:
    reajuste = sal_func*0.1
    sal = sal_func + reajuste
    sal = check_sal(sal)
    print(sal)
