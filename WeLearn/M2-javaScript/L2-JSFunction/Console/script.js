console.log("scrpit running!");

let name = 'Charlie';
console.log('Hello' + name + '!');
let age = 15;
console.log('You are ' + age + ' years old!');

if (age >= 16) {
  console.log('I can drive.');
} else {
  console.log("I can't drive.");
}

const greetPeople = (name1, name2) => {
  console.log('Hello, ' + name1 + ' and ' + name2 + '!');
}

const getFullName = (firstName, lastName) => {
  return firstName + ' ' + lastName;
}

let radius = 10
let area = Math.PI * radius * radius;
radius = radius * 2;
let width = Math.round(Math.random() * 100);
let height = Math.round(Math.random() * 50);
let circumference = width * 2 + height * 2;

let n = 1;

const increaseNumber = () => {
  n = n + 1;
  console.log(n);
}
setInterval(increaseNumber, 10);
