var favDishes=["Pizza", 'Hamburgers', 'Focaccia'];

console.log(favDishes[0]);
console.log(favDishes[1]);
console.log(favDishes[2]);

console.log(favDishes.length);

favDishes.push('French Fries');

var dishcount= favDishes.length;

console.log("There are "+ dishcount.toString()+ " dishes");

favDishes.splice(1,1);

favDishes.sort();

console.log(favDishes);

console.log(favDishes.length);
