def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0

    #Start writing your code here
    #Populate the variables: five_needed and one_needed

    five_needed = rupees_to_make // 5
    
    if five_needed > no_of_five:
      five_needed = no_of_five
      
    rupees_to_make -= 5 * five_needed
    
    one_needed = rupees_to_make
    
    if one_needed <= no_of_one:
      print("No. of Five needed :", five_needed)
      print("No. of One needed  :", one_needed)
    else:
      print(-1)
    
#Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
make_amount(28,8,5)