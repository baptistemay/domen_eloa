
function minimum(array){

    if (array.length == 0) {
        return `This array is empty.`;
    }

    let result = array[0];
    
    for(item of array){

        if (item < result) {
            result = item;
        }
    }

    return result;
}

