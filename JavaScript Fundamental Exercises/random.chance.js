
function randomChance(num) {
    while (num > 0) {
        var randomNum = Math.floor(Math.random() * 100);
        if (randomNum == 1) {
            var prize = Math.floor(Math.random() * 50) + 50;
            num+=prize; 
            return num;
        }
        num--;
    }
    return 0;
}
console.log(randomChance(20));