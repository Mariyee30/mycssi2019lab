const myButton = document.querySelector('#mybutton');
const myBox = document.querySelector('#box');
myButton.addEventListener('click', (event) => {
  // this code runs when the button is clicked
  console.log('Like button clicked!');
  myButton.innerHTML = 'Liked!';
  myButton.style.backgroundColor = 'lightgreen';
});

myButton.addEventListener('mousemove', (event) => {
  let red = Math.round(Math.random()*255);
  let green = Math.round(Math.random()*255);
  let blue = Math.round(Math.random()*255);
  myBox.style.backgroundColor = "rgb("+red+","+green+","+blue+")";
})
