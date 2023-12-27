
List1 = [5.2,4.8,5.1,2.7,3.5,2.9,4.6]
List2 = []



def split_list(grade):
    higrade, lowgrade = [],[]
    quantity = 0
    sum = 0.0
    if grade != []:
        for i in grade:
            sum += i
            quantity += 1
        average = sum/quantity
        for i in grade:
            if i > average: 
                higrade.append(i)
            else:
                lowgrade.append(i)
    return (lowgrade, higrade)


print(split_list(List2))

