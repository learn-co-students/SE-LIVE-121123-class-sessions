// Global variables
const URL = "http://localhost:3000/menu";

// DOM selectors
const menuItems = document.querySelector("#menu-items");
const dishImage = document.querySelector("#dish-image");
const dishName = document.querySelector("#dish-name");
const dishDescription = document.querySelector("#dish-description");
const dishPrice = document.querySelector("#dish-price");
// console.log("🚀 ~ file: index.js:10 ~ dishPrice:", dishPrice)

// Fetch functions
function getAllDishes(url) {
  fetch(url)
    .then((res) => res.json())
    .then((dishArr) => {
      dishArr.forEach((dishObj) => renderMenu(dishObj));
      renderDetails(dishArr[0]);
    });
}

// Render functions
function renderMenu(dishObj) {
  const dish = document.createElement("span");
  dish.textContent = dishObj.name;
  dish.addEventListener('click', () => renderDetails(dishObj))
  menuItems.append(dish);
}

function renderDetails(dishObj) {
  console.log("🚀 ~ file: index.js:30 ~ renderDetails ~ dishObj:", dishObj);
  dishImage.src = dishObj.image
  dishName.textContent = dishObj.name
  dishDescription.textContent = dishObj.description
  dishPrice.textContent = `$${dishObj.price}`
}


// Event Listeners & Handlers

// Initializer
getAllDishes(URL);
