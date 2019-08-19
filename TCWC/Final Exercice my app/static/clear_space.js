const task_input=document.getElementById("input_task");

function clear_text(){
task_input.value="";
}

task_input.addEventListener("click",clear_text);