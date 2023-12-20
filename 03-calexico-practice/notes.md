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
- [] Assign values of dish from data to DOM elements
- [x] Wrap this in a render function
- [x] Call the fn, passing the first dish as arg