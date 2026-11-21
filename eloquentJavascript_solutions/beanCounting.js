

function countBs(string){
    let total = 0

    for(char of string){
        if (char == "B"){
            total += 1
                        }  
                        }
    return total
                        

                        }

//countBs("There were Beans on the Floor, alonside Bananas. Beurk.")

function countChar(string, letter){
    let total = 0

    for(char of string){
        if (char.toLowerCase() == letter.toLowerCase()){
            total += 1
                                                       }  
                        }
    return total
                                   }
//countChar("Cacolac could be written with one k or two k, but I'm not sure.", "c")                