let size = parseInt(prompt("Please enter a size fo the chessboard")) + 1;
let filled = "#";
let blank = " ";
chessboard = [];
for(let row = 1; row < size; row++){
    for(let column = 1; column < size; column++){
     
        if((column + row) % 2 == 0){
            chessboard += blank;
        }
        else{
            chessboard += filled;
        }
    }
    chessboard += "\n";
}
console.log(chessboard);