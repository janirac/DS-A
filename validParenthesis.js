const validParenthesis = function(s) {
    const valid = {
        "(": ")",
        "{": "}",
        "[": "]"
    }
    let i = 0
    while(i < s.length) {
        if(!valid[s[i]] === s[i+1] ) {
            return false
        }

        i+2
    }

    return true
}

console.log(validParenthesis("()"))