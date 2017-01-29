// sum the input of a number to one digit ie 21 = 3 untill it is less than 10
// so 2568 ==> 3

function sumDigits(number) {
    var remainder = number % 10;
    var sum = remainder;
    if(number >= 10) {
        var rest = Math.floor(number / 10);
        sum += sumDigits(rest);
    }
    return sum;
}
console.log(sumDigits(25))
