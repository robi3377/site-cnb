let slide = document.querySelector("#slide");
let btnRight = document.querySelector("#btn-right");
let btnLeft = document.querySelector("#btn-left");
let k = 1;
let topOffset = window.pageYOffset
let width = screen.width
let contor = 1;
let isDesktop;
window.addEventListener('DOMContentLoaded', function() {});
///////////////////////////////////INDEX/////////////////////////////////////////////////
if (window.location.pathname=='/index.html' || window.location.pathname=='/' || window.location.pathname=='/public/index.html' || window.location.pathname=='/public/anunturi.html' || window.location.pathname=='/anunturi.html' || window.location.pathname=='/istoric' || window.location.pathname=='/istoric.html') { // "/public/index.html" trebuie folosit numai pe proiectul local
    setInterval(() => {
        autoSlideShow();
      }, "5000");

    if (window.location.pathname=='/index.html' || window.location.pathname=='/' || window.location.pathname=='/public/index.html'){
        document.querySelector("#vid").volume = 0.2;
    }
}

if(width > 1260) isDesktop = true;
else isDesktop =false

function openImagePhone(value){
    if(isDesktop == false)
    document.querySelector("#openImage").style.transform = "translateX(0px)";
    let bgImage = document.querySelector("#bgimage"+value).style.backgroundImage.slice(5,-2);
    document.querySelector("#openedImage").src = bgImage;
}

function openImage(value){
    document.querySelector("#openImage").style.transform = "translateX(0px)";
    let bgImage = document.querySelector("#bgimage"+value).style.backgroundImage.slice(5,-2);
    document.querySelector("#openedImage").src = bgImage;
}

function closeImage(){  
    document.querySelector("#openImage").style.transform = "translateX(100vw)";
}

function darken(value){
    if(isDesktop == true){
        document.querySelector("#container"+value).style.transform = "translateY(0px)";
    }
}

function lightup(value){
    if(isDesktop == true){
    let containerHeight = document.querySelector("#container"+value).offsetHeight;
    document.querySelector("#container"+value).style.transform = "translateY(" + containerHeight + "px)";
    }
}

function autoSlideShow(){
    let singleSlideWidth = document.querySelector("#singleSlide").clientWidth;
    let sliderWidth = document.querySelector("#slideShow").clientWidth;
    let Slider = document.querySelector("#slideShow");
    Slider.style.transform = "translateX("+ (contor - 1) * -singleSlideWidth +"px)";

    for( let i = 1 ; i <= 5 ; i++){
        if(i != contor){
            document.querySelector("#i"+i).style.opacity = "0.5";
            document.querySelector("#i"+i).style.height = "1.25rem";
            document.querySelector("#i"+i).style.width = "1.25rem";
        }
        else{
            document.querySelector("#i"+i).style.opacity = "0.8";
            document.querySelector("#i"+i).style.height = "1.5rem";
            document.querySelector("#i"+i).style.width = "1.5rem";
        }
    }
    if( contor === 5 ){
        setTimeout(function(){
            Slider.style.transform = "translateX(-"+ (sliderWidth - singleSlideWidth) +"px)";

        },4500)
        contor = 1;
    }
    else if( contor === 1 ){
        Slider.style.transitionDuration = "0s";
        contor++;
    }
    else if( contor != 5 && contor != 1){
        contor++;
        Slider.style.transitionDuration = "500ms";
    }
}

// function searchResults( searchText , searchURL ){
//     this.searchText = searchText;
//     this.searchURL = searchURL;
// }
let searchResults = [
    {   
        "textSearch":"olimpici",
        "url":"http://www.w3schools.com",
    },
    {   
        "textSearch":"Atlas",
        "url":"https://www.tutorialspoint.com/how-to-stop-refreshing-the-page-on-submit-in-javascript",
    },
]
searchResults.push()
function Search(){
    for( let i = 0 ; i < searchResults.length ; i++ )
        if(document.querySelector("#searchBar").value == searchResults[i].textSearch)
            window.location.href = searchResults[i].url;
}

function slideShow(value){
    let singleSlideWidth = document.querySelector("#singleSlide").clientWidth;
    document.querySelector("#slideShow").style.transform = "translateX("+ (value - 1) * -singleSlideWidth +"px)";

    for( let i = 1 ; i <= 5 ; i++){
        if(i != value){
            document.querySelector("#i"+i).style.opacity = "0.5";
            document.querySelector("#i"+i).style.height = "1.25rem";
            document.querySelector("#i"+i).style.width = "1.25rem";
        }
        else{
            document.querySelector("#i"+i).style.opacity = "0.8";
            document.querySelector("#i"+i).style.height = "1.5rem";
            document.querySelector("#i"+i).style.width = "1.5rem";
        }
    }
    contor = value;
    setTimeout(function(){

    },20000)
}

function scrollNavBar(){
    let top = window.pageYOffset;
    if( top === 0 ){
        document.querySelector("#nav").style.backgroundColor = "rgb(118 36 36 / 0)"
    }
    else{
        document.querySelector("#nav").style.backgroundColor = "rgb(118 36 36 / 0.9)"
    }
}

///////////////////////////////////ISTORIC/////////////////////////////////////////////////

var images = ["url('./assets/scan0003.jpg')",
"url('./assets/scan0003.jpg')",
"url('./assets/scan0004.jpg')",
"url('./assets/scan0006.jpg')",
"url('./assets/scan0003.jpg')",
"url('./assets/scan0004.jpg')",
"url('./assets/scan0006.jpg')"];
var index = 0;
var div = document.createElement('div');

function makeImage() {
    if(screen.width>700)
        {div.style.width="80vw";
        div.style.height="80vh";
        div.style.backgroundSize="contain";}
    else
        {div.style.width="100vw";
        div.style.height="60vh";
        div.style.backgroundSize="contain";}   
   div.style.margin="auto"
   div.style.backgroundImage=images[0];
   div.style.backgroundPosition="center center";
   div.style.backgroundRepeat="no-repeat";
   document.getElementById('content').appendChild(div);
}
if (window.location.pathname=='/istoric.html' || window.location.pathname=='/public/istoric.html') {
setInterval(() => {
    slideShowIstoric();
  }, "3000");
}
function slideShowIstoric(){
    index++;
    if(index == 7)
        index = 0;
    index = index % images.length;
    div.style.backgroundImage=images[index];
}

function moveRight(){
    var div = document.getElementById('content').getElementsByTagName('div')[2];
    div.style.position="center"
    if(index==7)
         index=0;
    index++;
    index = index % images.length;
    if(screen.width>700)
         {div.style.backgroundSize="contain";
         div.style.backgroundRepeat="no-repeat";}
     else
         div.style.backgroundSize="contain"; 
    div.style.backgroundImage="none";
    div.style.backgroundImage=images[index];
 }
 
 function moveLeft(){
     var div = document.getElementById('content').getElementsByTagName('div')[2];
     div.style.position="center"
     if(index==0)
         index=7;
     index--;
     index = index % images.length;
     if(screen.width>700)
         {div.style.backgroundSize="contain";
         div.style.backgroundRepeat="no-repeat";}
     else
         div.style.backgroundSize="contain";  
     div.style.backgroundImage="none";
     div.style.backgroundImage=images[index];
  }

///////////////////////////////////CATEDRE/////////////////////////////////////////////////

let boolCatedre = [];
for (let index = 1; index <= 16; index++) {
    boolCatedre[index] = true;
}
function dropCatedre(value){
    if(boolCatedre[value] === true){
        document.querySelector("#materie"+value).style.display = "flex";
        document.querySelector("#border"+value).style.borderBottom="thin solid rgb(27 27 27)";
    }
    else{
        document.querySelector("#materie"+value).style.display = "none";
        document.querySelector("#border"+value).style.borderBottom="none";
    }
    boolCatedre[value] = !boolCatedre[value]; 
}

///////////////////////////////////INFORMATII/////////////////////////////////////////////////
let boolInformatii = [];
for (let index = 1; index <= 6; index++) {
    boolInformatii[index] = true;
}
function dropInformatii(value){
    if(boolInformatii[value] === true){
        document.querySelector("#info"+value).style.display = "flex";
        document.querySelector("#arrow"+value).style.transform = "rotate(180deg)"
    }
    else{
        document.querySelector("#info"+value).style.display = "none";
        document.querySelector("#arrow"+value).style.transform = "rotate(0deg)"
    }
    boolInformatii[value] = !boolInformatii[value]; 
}

///////////////////////////////////CONTACT/////////////////////////////////////////////////
if (window.location.pathname=='/contact.html' || window.location.pathname=='/public/contact.html') {
    let inputs = document.querySelector("form").childNodes;
    for( let i  = 1 ; i <= inputs.length ; i = i + 2 ){
        inputs[i].style.outline = "none";
    }
    }

///////////////////////////////////CREARE PROIECT/////////////////////////////////////////////////
if (window.location.pathname=='/creare%20proiect.html' || window.location.pathname=='/public/creare%20proiect.html') {
    function previewBeforeUpload(id){
        document.querySelector("#"+id).addEventListener("change",function(e){
          if(e.target.files.length == 0){
            return;
          }
          let file = e.target.files[0];
          let url = URL.createObjectURL(file);
          document.querySelector("#preview-image").src = url;
        });
      }
      
      previewBeforeUpload("file");

      
}

///////////////////////////////////GENERAL/////////////////////////////////////////////////
let droped = false;
function dropDown(value){
    if( value == 0 ){
        document.querySelector("#dropDown").style.display = "block";
        setTimeout(() => {
            document.querySelector("#dropDown").style.opacity = "1";
        },100)
        droped = true;
    }
    else if (value == 1){
        if(droped == true){document.querySelector("#dropDown").style.opacity = "1";
        setTimeout(() => {
            document.querySelector("#dropDown").style.display = "block";
        },100)}
        makeDropedFalse();
    }

}
function dropFade(){
    document.querySelector("#dropDown").style.opacity = "0";
    setTimeout(() => {
        document.querySelector("#dropDown").style.display = "none";
    },100)

}
function makeDropedFalse(){
    droped = false;
}

let opened = false;
function secondaryMenu(){
    if(opened === false){
        document.querySelector("#secondaryMenu").style.transform = "translateX(0px)";
        opened = !opened;
    }
    else{
        document.querySelector("#secondaryMenu").style.transform = "translateX(250px)";
        opened = !opened;
    }
}

if(topOffset > 0){
    document.querySelector("#nav").style.backgroundColor = "rgb(118 36 36 / 0.9)"
}

function navmod(){
    let top = window.pageYOffset;
    if( top === 0 ){
        document.querySelector("#nav").style.backgroundColor = "rgb(118 36 36 / 0)"
    }
    else{
        document.querySelector("#nav").style.backgroundColor = "rgb(118 36 36 / 0.9)"
    }
}