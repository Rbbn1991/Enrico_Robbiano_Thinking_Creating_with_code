const textbox = document.getElementById('my_textbox');
const button = document.getElementById('my_button');
const parag = document.getElementById('text_space');

const textbox_red = document.getElementById('my_textbox_red');
const button_red = document.getElementById('my_button_red');

const content= document.getElementById('content')

const eraser=document.getElementById('eraser')

function remove(){
  const paragraphs= document.querySelectorAll(".red, .black");
  if (paragraphs.length>0) {
    var i=paragraphs.length-1;
    content.removeChild(paragraphs[i]);

  }


}


function add_text(){
    const new_parag=document.createElement("p");
    new_parag.className = 'black';
    new_parag.innerText=textbox.value;
    textbox.value='Write Here';
    content.appendChild(new_parag)

}

function add_text_red(){

    const new_parag=document.createElement("p");
    new_parag.className='red';
    new_parag.innerText=textbox_red.value;
    textbox_red.value='Write Here';
    content.appendChild(new_parag)


}

function clean_box(){
  textbox.value=""
}
function clean_box_red(){
  textbox_red.value=""
}

textbox.addEventListener('click',clean_box);
textbox_red.addEventListener('click',clean_box_red);

button.addEventListener('click',add_text);
button_red.addEventListener('click',add_text_red);
eraser.addEventListener('click',remove);
