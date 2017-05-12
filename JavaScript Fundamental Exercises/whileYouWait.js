function whileYouWait(days) {
  
  for (var i = days; i >= 0; i--) {
    if (i > 30) {
      console.log(i + " days until my birthday. Such a long time..");
    }
    else if (i > 5) {
      console.log(i + " DAYS UNTIL MY BIRTHDAY!!");
    }
    else if (i > 0) {
      console.log(i + " days until my birthday. Getting closer!");
    }
    else {
      console.log("ITS MY BDAY");
    }
  }
}
whileYouWait(20);