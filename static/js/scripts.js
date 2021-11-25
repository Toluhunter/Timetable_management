//Drop down menu 

window.addEventListener('DOMContentLoaded', ()=> {
          
    const menuBtn = document.querySelector('.menubtn');
    const dropdown = document.querySelector('.dropdown');

    menuBtn.addEventListener('click', () =>{
      dropdown.classList.toggle('hidden');
      dropdown.classList.toggle('flex');
    })

   
  })

//Responsive mobile menu

  const btn = document.querySelector('button.toggle-mobile-menu')
        const menu = document.querySelector('.mobile-menu')

        btn.addEventListener('click', () => {
            menu.classList.toggle("hidden")
        })

//Drag 'n' drop
function allowDrop(ev) {
  ev.preventDefault();
}

function drag(ev) {
  ev.dataTransfer.setData("text", ev.target.id);
  //ev.effectAllowed = "copyMove"; 
}

function drop(ev) {
  ev.preventDefault();
  var data = ev.dataTransfer.getData("text");
  var nodeCopy = document.getElementById(data).cloneNode(true); 
 
  ev.target.appendChild(nodeCopy); 
  ev.target.value=nodeCopy.innerHTML
  //ev.target.appendChild(document.getElementById(data));
}

//show Table
function monTable(){
	document.getElementById("monday").classList.toggle('hidden');
  
}
function tueTable(){
	document.getElementById("tuesday").classList.toggle('hidden');
  
}
function wedTable(){
	document.getElementById("wednesday").classList.toggle('hidden');
  
}
function thurTable(){
	document.getElementById("thursday").classList.toggle('hidden');
 
}
function friTable(){
	document.getElementById("friday").classList.toggle('hidden');
  
}