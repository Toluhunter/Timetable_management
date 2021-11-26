//Drop down menu 

window.addEventListener('DOMContentLoaded', ()=> {
          
    const menuBtn = document.querySelector('.menubtn');
    const dropdown = document.querySelector('.dropdown');

    menuBtn.addEventListener('click', () =>{
      dropdown.classList.toggle('hidden');
      dropdown.classList.toggle('flex');
    })

   
  })

  window.addEventListener('DOMContentLoaded', ()=> {
          
    const daysBtn = document.querySelector('.daysbtn');
    const dropdays = document.querySelector('.dropdays');

    daysBtn.addEventListener('click', () =>{
      dropdays.classList.toggle('hidden');
      dropdays.classList.toggle('flex');
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
function monTable() {
  if (document.getElementById('monday').style.display === 'none') {
    document.getElementById("monday").style.display = 'block';
  }
  
  // document.getElementById("monday").style.display = '';
  // document.getElementById("monday").classList.toggle('hidden');
  document.getElementById("monday").style.display = 'block';

 
  document.getElementById("tuesday").style.display = 'none';
  document.getElementById("wednesday").style.display = 'none';
  document.getElementById("thursday").style.display = 'none';
  document.getElementById("friday").style.display = 'none';




}
function tueTable() {
  // document.getElementById('tuesday').style.display = 'block';
  if (document.getElementById('tuesday').style.display === 'none') {
    document.getElementById("tuesday").style.display = 'block';
    
  }
  
  // document.getElementById('tuesday').classList.toggle('hidden');
  // document.getElementById("tuesday").style.display = '';
  // document.querySelector('table#tuesday').classList.toggle('hidden');
  document.getElementById("tuesday").style.display = 'block';
  
  
  document.getElementById("monday").style.display = 'none';
  document.getElementById("wednesday").style.display = 'none';
  document.getElementById("thursday").style.display = 'none';
  document.getElementById("friday").style.display = 'none';

}
function wedTable() {

  if (document.getElementById('wednesday').style.display === 'none') {
    document.getElementById("wednesday").style.display = 'block';  
  }

  // document.getElementById("wednesday").classList.toggle('hidden');
  document.getElementById("wednesday").style.display = 'block';

  document.getElementById("monday").style.display = 'none';
  document.getElementById("tuesday").style.display = 'none';
  document.getElementById("thursday").style.display = 'none';
  document.getElementById("friday").style.display = 'none';

  

}

function thurTable() {
  if (document.getElementById('thursday').style.display === 'none'){
    document.getElementById("thursday").style.display = 'block';
  }
  
  // document.getElementById("thursday").classList.toggle('hidden');
  document.getElementById("thursday").style.display = 'block';

  document.getElementById("monday").style.display = 'none';
  document.getElementById("tuesday").style.display = 'none';
  document.getElementById("wednesday").style.display = 'none';
  document.getElementById("friday").style.display = 'none';

  
}

function friTable() {
  if (document.getElementById('friday').style.display === 'none'){
    document.getElementById("friday").style.display = 'block';
  }
  // document.getElementById("friday").classList.toggle('hidden');
  document.getElementById("friday").style.display = 'block';

  document.getElementById("monday").style.display = 'none';
  document.getElementById("tuesday").style.display = 'none';
  document.getElementById("wednesday").style.display = 'none';
  document.getElementById("thursday").style.display = 'none';


}

