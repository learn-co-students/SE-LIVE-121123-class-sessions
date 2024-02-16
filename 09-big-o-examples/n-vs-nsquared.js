const testArr = Array.from(
  { length: 40000 },
  () => Math.floor(Math.random() * 40000) + 11
);

function Checker() {
  this.count = 0;
}

let nSquaredChecks = new Checker();
function smallestNumNsquared(arr) {
  for (let num of arr) {
    let smallest;
    nSquaredChecks.count += 1;
    for (let innerNum of arr) {
      smallest = true;
      nSquaredChecks.count += 1;
      if (num > innerNum) {
        smallest = false;
        break;
      }
    }
    if (smallest) return num;
  }
}

let linearChecks = new Checker();
function smallestNumberN(arr) {
  let smallest = Infinity;
  for (let num of arr) {
    linearChecks.count += 1;
    if (num < smallest) smallest = num;
  }
  return smallest;
}

let harderNSquared = new Checker();
function smallestNumSquaredHarderToTell(arr) {
  for (let num of arr) {
    harderNSquared.count += 1;
    if (
      arr.filter((numCheck) => {
        harderNSquared.count += 1;
        return numCheck < num;
      }).length == 0
    ) {
      return num;
    }
  }
}

console.log("O(n squared)");
console.log(smallestNumNsquared(testArr));
console.log("Count: ", nSquaredChecks.count);
console.log("O(n)");
console.log(smallestNumberN(testArr));
console.log("Count: ", linearChecks.count);
console.log("O(n^2) but harder to identify")
console.log(smallestNumSquaredHarderToTell(testArr))
console.log("Count: ", harderNSquared.count)
