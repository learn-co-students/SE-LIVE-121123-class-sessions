MANTRA
1. FETCH the data
2. SELECT `DOM` elements
3. CREATE new elements (as needed)
4. ATTACH event listeners (as needed)
5. ASSIGN data to element attributes
6. APPEND new elements to DOM

# Deliverables
As a user, I can:
1. View all movies in nav element on page load
- [x] Fetch all movie data
- [x] Select the nav element
- [x] Iterate over array of movies
- [x] Create <img> for each movie
- [x] Attach listeners to <img>s
- [x] Assign the src from movie obj
- [x] Append each <img> to nav element

2. View the 1st movie details on page load
- [] Fetch data for 1st movie? (if necessary)
- [x] Select the proper DOM elements   
- [x] set attributes of DOM elements with 1st movie properties
- [x] call render function and send it the 1st movie

3. Click a movie in the nav and see its details in the detail section 
  - [x] Add event listener to each <img> in nav
  - [x] use renderDetail fn from above

4. Click a 'watched' button which toggles the value; it persists, but only in DOM
- [x] attach listener to button
- [x] callback fn also flips value of watched for the detail movie obj
- [x] callback needs a conditional that sets button text

5. Enter a number of drops for each movie in the form and have it persist in the DOM
- [x] select the form
- [x] attach listener to form
- [x] preventDefault()
- [x] get input value from form
- [x] increment the `blood_amount` for detail movie with input value
- [x] upate the DOM

## Data shape
```json
{
    "id": 1,
    "title": "Friday the 13th",
    "release_year": 1980,
    "description": "Camp counselors are stalked and murdered by an unknown assailant while trying to reopen a summer camp that was the site of a child's drowning.",
    "image": "./assets/f13-1.jpeg",
    "watched": false,
    "blood_amount": 0
}
```