

function isEven(number){
    function cut(target){
        if (Math.abs(target) == 0){
            return true;
                                  }
        else if (Math.abs(target) == 1){
            return false;
                                       }
        else{
            return cut(Math.abs(target) - 2);
            }

    
                        }
    return cut(number);
                        }

// isEven(50)