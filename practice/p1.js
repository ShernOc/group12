//Find the Maximum number in an array 
const numbers= [2,34,5,6]

function number(num){
    let max = Math.max(...num)
    return max
}

console.log(number(numbers))

//Find the unique number a list 

const my_list = [1,3,4,5,6,6]

function life(num){
    return num.length === new Set (num).size
}

let unique = life(my_list)
console.log(unique)

// // Are not that bad: 
// // Practice programming: 
// // What is the difference between, Js and Python. 
// // 