const task_zone=document.getElementById('task_zone');
const text_box=document.getElementById('my_textbox');
const add_button=document.getElementById('add_button');
const remove=document.getElementById('remove_last_item');
const clear=document.getElementById('clear_all');


var saved = localStorage.getItem('item_list0');
var x = localStorage.length;

// If there are any saved items, update our list
if (x) {

  var k=0;
  while (k<x) {
  var lastname = localStorage.getItem('item_list'+k);
  k=k+1;

  const new_parag=document.createElement("p");
  const list=document.getElementsByClassName('new_item');
  new_parag.className="new_item";
  new_parag.innerText=lastname;
  task_zone.appendChild(new_parag);


  }

  }



function add_task(){
  const new_parag=document.createElement("p");
  const list=document.getElementsByClassName('new_item');
  new_parag.className="new_item";
  new_parag.innerText=text_box.value;
  text_box.value="";
  var z=list.length;
  task_zone.appendChild(new_parag);
  localStorage.setItem('item_list'+z, new_parag.innerHTML);


}

function remove_last(){
  const list=document.getElementsByClassName('new_item');
  if (list.length>0) {
    var i=list.length-1;
    task_zone.removeChild(list[i]);
    var z=list.length;
    localStorage.removeItem('item_list'+z);
  }
}

function clear_list(){
  const list=document.getElementsByClassName('new_item');
  var tot_len=list.length-1;
  while(list.length>0){
    var i=list.length-1;
    task_zone.removeChild(list[i]);
    var z=list.length;
    localStorage.removeItem('item_list'+z);
  }

}

add_button.addEventListener('click',add_task);
remove.addEventListener('click',remove_last);
clear.addEventListener('click',clear_list);
