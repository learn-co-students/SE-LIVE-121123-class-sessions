## Mantra
1. FETCH the data
2. SELECT the right DOM elements
3. CREATE new elements (as needed)
4. ATTACH event listeners (as needed)
5. ASSIGN data to DOM elements
6. APPEND new elements to the DOM

## Core Deliverables
As a user, I can:
1. View all menu items in a Menu section on page load
- [x] Fetch all dish data (and jsonify)
- [x] Select `menu-items`
- [x] Iterate over array objects
- [x] Create <span> for each obj
- [x] Assign dish name to <span>
- [x] Append <span> to `menu-items`
2. View the details of the first menu item in the Dish detail section on page load
- [x] Select DOM elements from dish section
- [x] Assign values of dish from data to DOM elements
- [x] Wrap this in a render function
- [x] Call the fn, passing the first dish as arg
3. Click a menu item and see it's details displayed in the dish detail section
- [x] Attach listeners to each menu item
- [x] Listener calls renderDetails with dishObj
4. Add menu items to  'my cart'. Cart only needs to increment when same dish is selected, but can reset when is selected (no persistence needed front or back)
- [x] select form, # in cart from DOM
- [x] attach listener to form and handle submit (preventDefault)
- [x] get form input either from selected DOM node OR from e.target
- [x] get current value of cart
- [x] calculate new value of cart
- [x] update DOM