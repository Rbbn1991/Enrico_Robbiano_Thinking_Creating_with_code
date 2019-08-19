const login=document.getElementById("login");
const submit_login=document.getElementById("submit_login");

var x=localStorage.length;
console.log(x);

if(x){
    login.value=localStorage.getItem('login');
}

function collect_id(){

localStorage.setItem("login", login.value);
}

function clear_text(){
login.value=" ";
}

submit_login.addEventListener('click', collect_id);
login.addEventListener("click",clear_text);

