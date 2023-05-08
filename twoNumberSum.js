const twoNumberSum = (numbers, targetSum) => {
    for(let i = 0; i < numbers.length; i++){
      for(let j = 1; j < numbers.length; j++){
        if(i !== j && numbers[i] + numbers[j] === targetSum) {
          return [numbers[i], numbers[j]]
        }
      }
    }
  
    return []
}