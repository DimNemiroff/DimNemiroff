base_rate = 40
price_per_km = 10
total_trip = 0          #trip counter
total_cash = 0          #driver's cash
total_distance = 0      #car mileage per shift in km
trip_cost = 0


def calculate_trip_price(distance_km):
    global total_trip
    price = float(base_rate + (distance_km*price_per_km))
    total_trip += 1
    #print(price)
    return price                  
        
while True:
    int(total_trip)
    try:
        distance_km = float(input('enter a disnance ')) 
    except ValueError:
        continue   
    trip_cost = calculate_trip_price(distance_km)
    total_cash = total_cash + trip_cost
    total_distance = total_distance + distance_km
    print(f'Це ваша {total_trip} поїздка',f'Дальність - {distance_km} км', f'Ціна поїздки - {trip_cost} грн.', f'Каса - {total_cash} грн.', f'Пробіг за зміну - {total_distance} км', sep='\n' ) 
    if input('Нове замовлення ') in ('N','n', 'Н' , 'н'):
        break
    


