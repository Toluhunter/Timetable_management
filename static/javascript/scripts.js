//Drop down menu 

window.addEventListener('DOMContentLoaded', ()=> {
          
    const menuBtn = document.querySelector('.menubtn');
    const dropdown = document.querySelector('.dropdown');

    menuBtn.addEventListener('mouseover', () =>{
      dropdown.classList.toggle('hidden');
      dropdown.classList.toggle('flex');
    })
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