from sales import calc_shipping, calc_tax # Importing the functions from sales.py
import sales # Importing the module sales.py

#what is the difference between the two imports is that the first one imports the functions directly, so you can call them directly without the module name, while the second one imports the module, so you have to call the functions with the module name.

sales.calc_shipping() # This is the same as calc_shipping()
sales.calc_tax() # This is the same as calc_tax()



calc_shipping()

calc_tax()

# This is the same as:

# from sales import calc_shipping as shipping, calc_tax as tax

# shipping()
