const list_project = document.querySelectorAll("#list");
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
}