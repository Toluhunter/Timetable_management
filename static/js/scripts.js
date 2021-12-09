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

  // window.addEventListener('DOMContentLoaded', ()=> {
          
  //   const daysBtn = document.querySelector('.mobdaysbtn');
  //   const dropdays = document.querySelector('.mobdropdays');

  //   daysBtn.addEventListener('click', () =>{
  //     dropdays.classList.toggle('hidden');
  //     dropdays.classList.toggle('flex');
  //   })

   
  // })

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

function delete_drag(ev){
  deleted = document.createElement("span");
  deleted.innerHTML = "(Deleted)";
  deleted.id = "(Deleted)"
  deleted.hidden=true
  ev.target.appendChild(deleted)
  ev.dataTransfer.setData("text", deleted.id);
  }


function drop(ev) {
  ev.preventDefault();
  var data = ev.dataTransfer.getData("text");
  var nodeCopy = document.getElementById(data).cloneNode(true); 
 
  // ev.target.appendChild(nodeCopy); 
  // console.log(ev.targe.id)
  value = nodeCopy.innerHTML
  if (value != "(Deleted)"){
    ev.target.value = value;
    return
  }
  
  _id = ev.target.id
  values = ['course', 'lecturer', 'venue']
  field = _id.split("_")
 

  for(i=0; i<values.length; i++){
    field[2] = values[i]
    obj = document.getElementById(field.join("_"))
    obj.value = "(Deleted)"
  }
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


//show Table
function viewmonTable() {
  if (document.getElementById('view_monday').style.display === 'none') {
    document.getElementById("view_monday").style.display = 'block';
  }
  
  // document.getElementById("monday").style.display = '';
  // document.getElementById("monday").classList.toggle('hidden');
  document.getElementById("view_monday").style.display = 'block';

 
  document.getElementById("view_tuesday").style.display = 'none';
  document.getElementById("view_wednesday").style.display = 'none';
  document.getElementById("view_thursday").style.display = 'none';
  document.getElementById("view_friday").style.display = 'none';




}
function viewtueTable() {
  // document.getElementById('tuesday').style.display = 'block';
  if (document.getElementById('view_tuesday').style.display === 'none') {
    document.getElementById("view_tuesday").style.display = 'block';
    
  }
  
  // document.getElementById('tuesday').classList.toggle('hidden');
  // document.getElementById("tuesday").style.display = '';
  // document.querySelector('table#tuesday').classList.toggle('hidden');
  document.getElementById("view_tuesday").style.display = 'block';
  
  
  document.getElementById("view_monday").style.display = 'none';
  document.getElementById("view_wednesday").style.display = 'none';
  document.getElementById("view_thursday").style.display = 'none';
  document.getElementById("view_friday").style.display = 'none';

}
function viewwedTable() {

  if (document.getElementById('view_wednesday').style.display === 'none') {
    document.getElementById("view_wednesday").style.display = 'block';  
  }

  // document.getElementById("wednesday").classList.toggle('hidden');
  document.getElementById("view_wednesday").style.display = 'block';

  document.getElementById("view_monday").style.display = 'none';
  document.getElementById("view_tuesday").style.display = 'none';
  document.getElementById("view_thursday").style.display = 'none';
  document.getElementById("view_friday").style.display = 'none';

  

}

function viewthurTable() {
  if (document.getElementById('view_thursday').style.display === 'none'){
    document.getElementById("view_thursday").style.display = 'block';
  }
  
  // document.getElementById("thursday").classList.toggle('hidden');
  document.getElementById("view_thursday").style.display = 'block';

  document.getElementById("view_monday").style.display = 'none';
  document.getElementById("view_tuesday").style.display = 'none';
  document.getElementById("view_wednesday").style.display = 'none';
  document.getElementById("view_friday").style.display = 'none';

  
}

function viewfriTable() {
  if (document.getElementById('view_friday').style.display === 'none'){
    document.getElementById("view_friday").style.display = 'block';
  }
  // document.getElementById("friday").classList.toggle('hidden');
  document.getElementById("view_friday").style.display = 'block';

  document.getElementById("view_monday").style.display = 'none';
  document.getElementById("view_tuesday").style.display = 'none';
  document.getElementById("view_wednesday").style.display = 'none';
  document.getElementById("view_thursday").style.display = 'none';


}




