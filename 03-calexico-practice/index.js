// Global variables
const URL = "http://localhost:3000/menu";
let currentDish;

// DOM selectors
const menuItems = document.querySelector("#menu-items");
const dishImage = document.querySelector("#dish-image");
const dishName = document.querySelector("#dish-name");
const dishDescription = document.querySelector("#dish-description");
const dishPrice = document.querySelector("#dish-price");
const numInCart = document.querySelector("#number-in-cart");
const cartForm = document.querySelector("#cart-form");

// Fetch functions
function getAllDishes(url) {
  return fetch(url)
    .then((res) => res.json()); // ADVANCED:iterating data moved to initializers section 
}

function updateDish(url, dishObj) { // ADVANCED
  const config = { // 1st I compose the configuration object...
    method: "PATCH",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(dishObj),
  };
  return fetch(url + `/${dishObj.id}`, config) // then pass config as 2nd arg to fetch
    .then((res) => {
        if (res.ok) { // a little error handling. The Response has a boolean 'ok' property
        return res.json();
        } else {
        throw "Failed to update the cart!"; // throw this error message if the PATCH fails on the server
        }
    });
}

// Render functions
function renderMenu(dishObj) { // renders each dish name in span on left
  const dish = document.createElement("span");
  dish.textContent = dishObj.name;
  dish.addEventListener("click", () => renderDetails(dishObj));
  menuItems.append(dish);
}

function renderDetails(dishObj) { // renders a single dish obj in the detail section
  currentDish = dishObj; // sets a reference to the currently selected dish in the global scope
  dishImage.src = dishObj.image;
  dishName.textContent = dishObj.name;
  dishDescription.textContent = dishObj.description;
  dishPrice.textContent = `$${dishObj.price}`;
  numInCart.textContent = dishObj.number_in_bag;
}

function renderTotalOrderElements() { // ADVANCED: adds elements to display the total order price to DOM
  let hr = document.createElement("hr");
  const h3 = document.createElement("h3");
  h3.textContent = "Order total:";
  const span = document.createElement("span");
  span.id = "total-orders";
  h3.append(span);
  document.querySelector("#dish").append(hr, h3);
}

function displayTotal(dishArr) { // ADVANCED: calcs the current total order amount from the entire array and renders in DOM
  const span = document.querySelector("#total-orders");
  const currTotal = dishArr.reduce(
    (sum, dish) => sum + dish.price * dish.number_in_bag,
    0
  );
  span.textContent = ` $${currTotal}`;
}

// Event Listeners & Handlers

cartForm.addEventListener("submit", addToCart); // addEventListener implicitly passes the Event to the invoked handler callback function

function addToCart(e) {
  e.preventDefault();
  const numToAdd = Number(e.target.amount.value);
  //   const currNum = Number(numInCart.textContent); // grabs the current number in cart from DOM instead of reading from obj
  //   numInCart.textContent = currNum + numToAdd;
  currentDish.number_in_bag += numToAdd; // currentDish.number_in_bag = currentDish.number_in_bag + numToAdd
  // renderDetails(currentDish) // reuse render fn to update numInCart OR 
  // numInCart.textContent = currentDish.number_in_bag // update numInCart directly

  /* ADVANCED */
  updateDish(URL, currentDish) // calls our PATCH fetch function
    .then((updatedDish) => { // receives JSONified updated dishObj
      renderDetails(updatedDish); // updates DOM from the server response
      return getAllDishes(URL); // we need to re-fetch the updated dishes array 
    })
    .then(displayTotal); // to recalc the total order price

  e.target.reset();
}

// Initializers
renderTotalOrderElements(); // ADVANCED: adds new DOM elements for the total order
getAllDishes(URL)
    .then((dishArr) => {        // I had to move this .then() here instead of
        displayTotal(dishArr);  // leaving it in getAllDishes() in order for 
        dishArr.forEach((dishObj) => renderMenu(dishObj)); // the displayTotal() call following
        renderDetails(dishArr[0]);  // the updateDish() call to work
    });
