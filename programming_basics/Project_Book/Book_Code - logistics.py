contracts = int(input())

minibus_transport = 0
truck_transport = 0
train_transport = 0

for contract in range(0, contracts):
    cargo_weight = int(input())
    if cargo_weight <= 3:
        minibus_transport += cargo_weight
    elif 3 < cargo_weight <= 11:
        truck_transport += cargo_weight
    else:
        train_transport += cargo_weight

#  всичко товари
gross_weight = minibus_transport + truck_transport + train_transport
weight = gross_weight

#  цена всички товари
minibus_price = 200 * minibus_transport
truck_price = 175 * truck_transport
train_price = 120 * train_transport

gross_price = minibus_price + truck_price + train_price
avg_price = gross_price / gross_weight

print(f"{avg_price:.2f}")
print("{0:.2f}%".format(minibus_transport / gross_weight * 100))
print("{0:.2f}%".format(truck_transport / gross_weight * 100))
print("{0:.2f}%".format(train_transport / gross_weight * 100))
