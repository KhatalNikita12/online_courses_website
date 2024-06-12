var element=document.querySelector("button")
function hello(){
   alert(`you want to send message`)
   
}


//show/hide  question
const faqs=document.querySelectorAll('.faq')
faqs.forEach(faq=>{
    faq.addEventListener('click',()=>{
        faq.classList.toggle('open');
    })
})