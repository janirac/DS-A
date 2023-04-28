let isPalindrome = function(x) {
    if(x < 1) return false
    if(x < 10) return true
    
    const reversed = 0
    let temp = x

    while (temp > 0) {
        const lastDigit = temp % 10
        reversed = reversed * 10 + lastDigit
        temp = Math.floor(temp / 10)
    }

    return reversed === x
}