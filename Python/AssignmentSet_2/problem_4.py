def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    if food_type != "V" and food_type != "N":
        return -1
    elif distance_in_kms < 1:
        return -1
    elif quantity_ordered < 1:
        return -1


    if food_type == "V":
        bill_amount += 120 *quantity_ordered
    else:
        bill_amount += 150 *quantity_ordered

    if distance_in_kms > 6:
        bill_amount += 6 * (distance_in_kms - 6)
        distance_in_kms = 6

    if distance_in_kms > 3 and distance_in_kms <= 6:
        bill_amount += 3 * (distance_in_kms - 3)
    return bill_amount

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",2,7)
print(bill_amount)