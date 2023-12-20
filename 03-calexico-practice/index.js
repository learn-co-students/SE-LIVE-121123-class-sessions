// Global variables
const URL = "http://localhost:3000/menu"

// DOM selectors
const menuItems = document.querySelector("#menu-items")

// Fetch functions
function getAllDishes(url){
    fetch(url)
      .then(res => res.json())
      .then(dishArr => {
        dishArr.forEach(dishObj => renderMenu(dishObj));
      })
}

// Render functions
function renderMenu(dishObj){
    const dish = document.createElement("span")
    dish.textContent = dishObj.name
    console.log("🚀 ~ file: index.js:20 ~ renderMenu ~ dish:", dish)
    menuItems.append(dish)
}


// Event Listeners & Handlers

// Initializer
getAllDishes(URL)