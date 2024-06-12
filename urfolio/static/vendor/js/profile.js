/*const list_project = document.querySelectorAll("#list");
const list_button = document.querySelectorAll("#list-project");
const svg_userProdStatus = document.querySelectorAll("#list_userProject line")
const svg_likedProdStatus = document.querySelectorAll("#svg_status_liked line")
var status = {
    user: 'close',
    liked: 'close'
};

function openCloseList (i, status, list_project){
    console.log('work')
    if((i == 0 && status.user == 'close') || (i == 1 && status.liked == 'close')){
        if(i == 0){
            status.user = 'open';
            svg_userProdStatus[0].setAttribute('stroke-width', '0');
        } else {
            status.liked = 'open';
            svg_likedProdStatus[0].setAttribute('stroke-width', '0');
        }
        console.log(status)
        list_project[i].style.display = "block";
    }
    else{
        if(i == 0){
            status.user = 'close';
            svg_userProdStatus[0].setAttribute('stroke-width', '2');
        } else {
            status.liked = 'close';
            svg_likedProdStatus[0].setAttribute('stroke-width', '2');
        }
        list_project[i].style.display = "none";
    }
}

for(i = 0; i < list_button.length; i++){
    list_button[i].addEventListener('click', () =>{openCloseList(i, status, list_project)})
}*/

const button_user_progect = document.getElementById("button_user_project")
const button_liked_progect = document.getElementById("button_liked_project")
const list_project = document.querySelectorAll("#list_project")
const svg_status = document.querySelectorAll("#svg_list_status line")

function openCloseList(i){
    console.log("work", i)
    if (list_project[i].style.display === "none" || list_project[i].style.display === "") {
        list_project[i].style.display = "flex"
        if(i == 0){
            svg_status[0].setAttribute('stroke-width', '0');
        }
        else{
            svg_status[2].setAttribute('stroke-width', '0');
        }
    }
    else if(list_project[i].style.display === "flex") {
            list_project[i].style.display = "none"
            if(i == 0){
                svg_status[0].setAttribute('stroke-width', '2');
            }
            else{
                svg_status[2].setAttribute('stroke-width', '2');
            }
        }
}

button_user_progect.addEventListener('click', () =>{openCloseList(0)})
button_liked_progect.addEventListener('click', () =>{openCloseList(1)})

// Лента проектов

const userLeftBtn = document.getElementById('user_left_btn');
const userRightBtn = document.getElementById('user_right_btn');
const likedLeftBtn = document.getElementById('liked_left_btn');
const likedRightBtn = document.getElementById('liked_right_btn');
const userHorizonScroll = document.getElementById('list_user_project');
const likedHorizonScroll = document.getElementById('list_liked_project');

userRightBtn.addEventListener('click', ()=>{
    userHorizonScroll.style.scrollBehavior = "smooth";
    userHorizonScroll.scrollLeft += 466;
});

userLeftBtn.addEventListener('click', ()=>{
    userHorizonScroll.style.scrollBehavior = "smooth";
    userHorizonScroll.scrollLeft -= 466;
});

likedRightBtn.addEventListener('click', ()=>{
    likedHorizonScroll.style.scrollBehavior = "smooth";
    likedHorizonScroll.scrollLeft += 466;
});

likedLeftBtn.addEventListener('click', ()=>{
    likedHorizonScroll.style.scrollBehavior = "smooth";
    likedHorizonScroll.scrollLeft -= 466;
});
