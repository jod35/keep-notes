const formModal=document.querySelector('.note-modal');
const modalOpenButton=document.querySelector('.add-btn');

modalOpenButton.addEventListener('click',()=>{
    console.log("Hello")
    formModal.style.display="block"
})


const closeSection=(id)=>{
    const element=document.getElementById(id);

    element.style.display="none";
}
