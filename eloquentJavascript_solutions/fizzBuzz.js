
for(let count = 1; count < 101; count++){
    if(count % 5 == 0 && count % 3 == 0){
        console.log("FizzBuzz");
    }
    else if(count % 5 == 0){
        console.log("Buzz");
    }
    else if(count % 3 == 0){
        console.log("Fizz");
    }
    else{
        console.log(count);
    }
}