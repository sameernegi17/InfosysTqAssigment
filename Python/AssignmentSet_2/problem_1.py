def find_product(num1,num2,num3):
    product=0
    if num3 == 7:
      return -1
    elif num2 == 7:
      return num3
    elif num1 == 7:
      return num3 * num2
    else:
      return num1 * num2 * num3
    return product

#Provide different values for num1, num2, num3 and test your program
product=find_product(7,6,2)
print(product)