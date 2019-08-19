var random;
random=Math.floor((Math.random()*100)+1);

var answer;
var answer_num;
var i=0;
var alfa=0;




function guessNumber(){
    var answer= window.prompt('Try to guess the number (between 1 and 100)');
    var answer_num=parseInt(answer);
    
    return answer_num;
    
}



while(alfa==0){

    var number_input=guessNumber(); 

    i=i+1;
   
    if(isNaN(number_input)){
        console.log('The value is not a number. you lost!');
        alfa=1;
    }else{

        if(number_input>random){
            console.log('Guess less');
            
        } else if( number_input<random){
            console.log('Guess more');
            
        
        } else{
            console.log('Congratulation, your guess is correct!!');
            console.log('Congratulations! you won in '+ i+ 'Moves');
            alfa=1;
        }
    }
    }
    




