let romanToInt = function(s) {
    const romanNumeralHash = {
        I: 1,
        V: 5,
        X: 10,
        L: 50,
        C: 100,
        D: 500,
        M: 1000
    }

let integer = 0
    sArray = s.split("")
    for(let i = 0; i < sArray.length; i++){
        if(sArray[i] === "I" && sArray[i+1] === "V") {
            integer += (romanNumeralHash[sArray[i+1]] - romanNumeralHash[sArray[i]])
            i++;
        } else if (sArray[i] === "I" && sArray[i+1] === "X") {
            integer += (romanNumeralHash[sArray[i+1]] - romanNumeralHash[sArray[i]]);
            i++; 
        } else if (sArray[i] === "X" && sArray[i+1] === "L") {
            integer += (romanNumeralHash[sArray[i+1]] - romanNumeralHash[sArray[i]]);
            i++; 
        } else if (sArray[i] === "X" && sArray[i+1] === "C") {
            integer += (romanNumeralHash[sArray[i+1]] - romanNumeralHash[sArray[i]]);
            i++; 
        } else if (sArray[i] === "C" && sArray[i+1] === "D") {
            integer += (romanNumeralHash[sArray[i+1]] - romanNumeralHash[sArray[i]]);
            i++; 
        } else if (sArray[i] === "C" && sArray[i+1] === "M") {
            integer += (romanNumeralHash[sArray[i+1]] - romanNumeralHash[sArray[i]]);
            i++; 
        } else {
            integer += romanNumeralHash[sArray[i]];
        }
    }

    return integer
}