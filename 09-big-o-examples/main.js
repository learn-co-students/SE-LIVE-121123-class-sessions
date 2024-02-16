function generateArr(n) {
  const nums = new Set();
  while (nums.size !== n) {
    nums.add(Math.floor(Math.random() * n) + 1);
  }
  return [...nums];
}

// function getRandom(arr, n) {
//   var result = new Array(n),
//       len = arr.length,
//       taken = new Array(len);
//   if (n > len)
//       throw new RangeError("getRandom: more elements taken than available");
//   while (n--) {
//       var x = Math.floor(Math.random() * len);
//       result[n] = arr[x in taken ? taken[x] : x];
//       taken[x] = --len in taken ? taken[len] : len;
//   }
//   return result;
// }

function getRandom(arr, n) {
  let result = new Set(),
    len = arr.length;
  if (n > len)
    throw new RangeError("getRandom: more elements taken than available");

  function generateRandomInt(mult) {
    return Math.floor(Math.random() * mult);
  }

  while (n--) {
    let x = generateRandomInt(len);
    while (result.has(arr[x])) {
      x = generateRandomInt(len);
    }
    result.add(arr[x]);
  }
  return [...result];
}

const numArr = generateArr(300);
console.log("🚀 ~ numArr:", numArr);

let i = 50;
while (i--) {
  console.log(getRandom(numArr, 25));
}
