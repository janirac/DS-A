// Write a function, maxValue, that takes in array of numbers as an argument. The function should return the largest number in the array.

// Solve this without using any built-in array methods.

// You can assume that the array is non-empty. 

const maxValue = (numbers) => {
    let largestNum = numbers[0]
    numbers.forEach((number) => {
        if(number > largestNum){
            largestNum = number
        }
    })

    return largestNum
}