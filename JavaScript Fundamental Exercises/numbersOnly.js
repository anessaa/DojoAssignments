function numbersOnly (arr) {
    var newArr = [];
    for(var i = 0; i < arr.length; i++) {
        if (typeof arr[i] === "number") {
            newArr.push(arr[i]);
        }
    }
    return newArr;
}

var hi = [1, "apple", -3, "orange", 0.5];
var bye = [2, "grapes", 30, "burger", 100];
console.log(numbersOnly(hi));