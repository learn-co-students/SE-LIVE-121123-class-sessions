// Global
const baseURL = "http://localhost:3000/movies"
let selectedMovie;
// let movieArray;

// Selectors
const movieList = document.querySelector("#movie-list")
const detailImage = document.querySelector("#detail-image")
console.log("🚀 ~ file: index.js:9 ~ detailImage:", detailImage)
const title = document.querySelector("#title")
const yearReleased = document.querySelector("#year-released")
const description = document.querySelector("#description")
const amount = document.querySelector("#amount")
const watched = document.querySelector("#watched")
const bloodForm = document.querySelector("#blood-form")

// Fetches

function getAllMovies(url){
    return fetch(url)
     .then(res => res.json())
     .then(moviesArr => {
        renderAllMovies(moviesArr)
        renderDetail(moviesArr[0])
    })
}

// Render functions
function renderAllMovies(moviesArr){
    // console.log("🚀 ~ file: index.js:17 ~ renderAllMovies ~ moviesArr:", moviesArr)
    moviesArr.forEach(movieObj => renderNav(movieObj))
}

function renderNav(movieObj){
    // console.log("🚀 ~ file: index.js:22 ~ renderNav ~ movieObj:", movieObj)
    const img = document.createElement('img')
    img.addEventListener('click', () => renderDetail(movieObj))
    // console.log("🚀 ~ file: index.js:25 ~ renderNav ~ img:", img)
    img.src = movieObj.image
    movieList.append(img)
}

function renderDetail(movieObj){
    selectedMovie = movieObj
    console.log("🚀 ~ file: index.js:36 ~ renderDetail ~ movieObj:", movieObj)
    detailImage.src = movieObj.image
    title.textContent = movieObj.title
    description.textContent = movieObj.description
    yearReleased.textContent = movieObj["release_year"]
    let watchVal = movieObj.watched ? "Watched" : "Unwatched"
    watched.textContent = watchVal
    amount.textContent = movieObj.blood_amount
}


// Event listeners and handlers
// watched.addEventListener('click', () => toggleWatched())
watched.addEventListener('click', toggleWatched)

function toggleWatched(){
    selectedMovie.watched = !selectedMovie.watched
    if (selectedMovie.watched) {
        watched.textContent = "Watched"
    } else {
        watched.textContent = "Unwatched"
    }
}

bloodForm.addEventListener('submit', (e) => handleBloodSubmit(e))

function handleBloodSubmit(e) {
    e.preventDefault()
    console.dir(e.target)
    const newBlood = parseInt(e.target["blood-amount"].value)
    console.log(newBlood)
    selectedMovie.blood_amount += newBlood
    console.log("🚀 ~ file: index.js:77 ~ handleBloodSubmit ~ selectedMovie.blood_amount:", selectedMovie.blood_amount)
    renderDetail(selectedMovie)
    bloodForm.reset()
}

// Initalizers
getAllMovies(baseURL)