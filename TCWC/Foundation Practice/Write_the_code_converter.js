// Func: Eurs to CHF //
// euros=1.13 chf //

function eurosToCHF(euros){
    return euros*1.13;
}


// Func: Celsius to Farhenit //
// celsius *9/5 32 //

function celsiusToFarenheit(celsius){
    return (celsius*9/5)+32;
}

// Liters to gallons //
// liters/ 3.785 //

function LitersToGallons(liters){
    return liters/3.785;
}



// Func: ask if users wants to convert something //

function askContinue(){
    var answer= window.prompt("Do you want to convert a value? (yes/no)");
    if( answer == 'yes'){
        return true;
    } else{
        return false;
    }
}

// Ask which conversion the user wants to do?//

function askConversion(){
    var answer= window.prompt('Which conversion you want to do? (euros/celsius/liters');
    return answer;
}

// ask the value to convert //

function askValue(){
    var answer= window.prompt('Enter a value:');
    return answer;   
}

// Main Program//

while(askContinue()){

    var ConversionType=askConversion();
    var ConversionValue= askValue();
    var resultMessage= 'The result is: ';
    var result=0;

    if(ConversionType=='euros'){
        resultMessage +=eurosToCHF(Number((ConversionValue))).toString();
    }   else if( ConversionType=='celsius'){
        resultMessage += celsiusToFarenheit(Number(ConversionValue)).toString();
    }

        else if(ConversionType=='liters'){
        resultMessage += LitersToGallons(Number((ConversionValue)).toString());
    }
        else {
            resultMessage="Sorry.I can't to this conversion"
        }
    
    console.log(resultMessage);
}

console.log('Thanks for using our service');