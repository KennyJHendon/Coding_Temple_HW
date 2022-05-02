
# Ask the user for four bits of input: Do you want to : Show/Add/Delete or Quit?
cart = []

while True:

    answer = input('Do you want to: Show, Add, Delete, or Quit?  Type your choice into the field and hit enter').lower()
    if answer == "add":
        thing = input('enter the name of the thing you would like to add to your cart').lower()
        cart.append(thing)
        print(cart)
        
    elif answer == 'delete':
        item = input('enter the name of the item you would like to delete').lower()
        
        if item in cart:
            cart.remove(item)
           
        else: 
            print('that item is not in your cart')
                
    elif answer == 'show':
        print('here is the contents of your cart')
      
        print (cart)
    elif answer == 'quit':
    
        print ('here is what you have in your cart:')
        print(cart)
        print('Thanks for shopping!')
        break
   
    else:
        print('sorry, that is not an option')
           
        
