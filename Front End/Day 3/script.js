let guess=Math.floor(Math.random()*100)+1;
let input=document.getElementById('guess');
let dialog=document.getElementById('result');
let chancesLeft=document.getElementById('chances');
let chances=5;

function checkGuess(){
    if(guess===input.value){
        dialog.innerHTML='Victory 🎉 You guessed the right number!';
    }
    else if(input.value>100 || input.value<1){
        dialog.innerHTML='Please enter a number between 1 to 100 😡';
    }
    else if(guess>input.value){
        dialog.innerHTML='Try a higher number 😢';
        chances--;
       
        chancesLeft.innerHTML=chances;
    }
    else if(guess<input.value){
        dialog.innerHTML='Try a lower number 😢';
        chances--;
        chancesLeft.innerHTML=chances;
    }
    else{
        dialog.innerHTML='Please enter a valid number!';
    }
    if(chances===0){
        dialog.innerHTML=`You lost 💔 The number was ${guess}`;
    }
}
function playAgain(){
    dialog.innerHTML='';
    input.value='';
    chances=5;
    chancesLeft.innerHTML=chances;
}