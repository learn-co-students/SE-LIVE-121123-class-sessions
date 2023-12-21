// Global variables
const URL = "http://localhost:3000/menu";

// DOM selectors
const menuItems = document.querySelector("#menu-items");
const dishImage = document.querySelector("#dish-image");
const dishName = document.querySelector("#dish-name");
const dishDescription = document.querySelector("#dish-description");
const dishPrice = document.querySelector("#dish-price");
const cartForm = document.querySelector("#cart-form")
const numInCart = document.querySelector("#number-in-cart")
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
  numInCart.textContent = dishObj.number_in_bag
}


// Event Listeners & Handlers

cartForm.addEventListener('submit', addToCart)

function addToCart(e){
    e.preventDefault()
    // console.log("🚀 ~ file: index.js:44 ~ addToCart ~ e:", e.target.amount.value)
    const numToAdd = Number(e.target.amount.value)
    console.log("🚀 ~ file: index.js:46 ~ addToCart ~ numToAdd:", numToAdd)
    const currNum = Number(numInCart.textContent)
    console.log("🚀 ~ file: index.js:49 ~ addToCart ~ currNum:", currNum)
    numInCart.textContent = currNum + numToAdd
    e.target.reset()
}

// Initializer
getAllDishes(URL);
