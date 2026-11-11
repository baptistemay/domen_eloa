


// Create two distincts lists with even / odd numbers
let firstList = [];
for(let x = 0; x < 100; x++){
    firstList.push(x)
}
console.log(firstList); // Check if firstList is correct (0 to 99)
let evenNumbers = firstList.filter(x => x % 2 == 0);
console.log(evenNumbers) // check if numbers are even
let oddNumbers = firstList.filter(x => x % 2 != 0)
console.log(oddNumbers) // check if numbers are odd


// Fisher-Yates function
function fisherYates(Array){
  for (let i = evenNumbers.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [Array[i], Array[j]] = [Array[j], Array[i]];
  }
  return evenNumbers;
}
fisherYates(evenNumbers);
console.log(evenNumbers);
fisherYates(oddNumbers);
console.log(oddNumbers); // check the randomness

let rows = evenNumbers.length 
let columns = oddNumbers.length
let result = []
for(line = 0; line < columns / rows; line++){
    for(position = 0; position < rows / columns; position++){
        result += oddNumbers[position] +","
    }
    result += "\n"
    result += evenNumbers[line]
    evenNumbers.splice(0,9)
    oddNumbers.splice(0,9) // retire les dix premiers index des deux listes

}

console.log(result) // Donne une paire Impair/Pair
