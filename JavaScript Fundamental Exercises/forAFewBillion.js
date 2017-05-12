
function money(days) {
    var sum = .01;
    for (var i = 1; i <= days; i++) {
      console.log(sum);
      sum *= 2;
    }
}
money(30);
