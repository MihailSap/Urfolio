// Лайки постов
const like_button = document.querySelectorAll('#like-button');
const like_icon = document.querySelectorAll('#like-icon');
const sum_like = document.querySelectorAll('#like-number');
let amount_like = Array(like_button.length).fill({count: 0, liked: false}); // выгрузка с бэка

function likePost(i){
    if(!amount_like[i].liked){
        like_icon[i].src = "static/vendor/assets/img/red-likes.svg";
        sum_like[i].style.color = "#FF0000";
        amount_like[i].count += 1;
        amount_like[i].liked = true;
        sum_like[i].innerText = amount_like[i].count;
    } else{
        like_icon[i].src = "static/vendor/assets/img/Likes.png";
        sum_like[i].style.color = "#CAD1E1";
        amount_like[i].count -= 1;
        amount_like[i].liked = false;
        sum_like[i].innerText = amount_like[i].count;
    }
}

//Добавить отправку на бэк

for (let i = 0; i<like_button.length; i++){
    like_button[i].addEventListener('click', ()=>{likePost(i)})
};


// Сортировка ленты
const sort_type_button = document.querySelectorAll("#sorting-type");
var lines_time = document.querySelectorAll('#sort-type_time line');
var lines_rating = document.querySelectorAll('#sort-type_rating line');
var lines_title = document.querySelectorAll('#sort-type_title line');
let sortTypes = {
    timeSortType: "none",
    ratingSortType: "none",
    titleSortType: "none"
};


function sort(i, sortTypes){
    if(i == 0){
        if (sortTypes.timeSortType == 'none') {
            lines_time[0].setAttribute('x2', '12');
            lines_time[1].setAttribute('x2', '7');
            sortTypes.timeSortType = 'ascending';
            console.log( sortTypes.timeSortType, i);
        } else if ( sortTypes.timeSortType == 'ascending') {
            lines_time[0].setAttribute('x2', '2')
            lines_time[2].setAttribute('x2', '12');
            sortTypes.timeSortType = 'descending';
        }else{
            lines_time[1].setAttribute('x2', '2');
            lines_time[2].setAttribute('x2', '2');
            sortTypes.timeSortType = "none";
        }
        sendSortTypeToBackend(i, sortTypes.timeSortType);
    }
    if(i == 1){
        if (sortTypes.ratingSortType == 'none') {
            lines_rating[0].setAttribute('x2', '12');
            lines_rating[1].setAttribute('x2', '7');
            sortTypes.ratingSortType = 'ascending';
            console.log(sortTypes.ratingSortType, i);
        } else if (sortTypes.ratingSortType == 'ascending') {
            lines_rating[0].setAttribute('x2', '2')
            lines_rating[2].setAttribute('x2', '12');
            sortTypes.ratingSortType = 'descending';
        }else{
            lines_rating[1].setAttribute('x2', '2');
            lines_rating[2].setAttribute('x2', '2');
            sortTypes.ratingSortType = "none";
        }
        sendSortTypeToBackend(i,sortTypes.ratingSortType);
    }
    if(i == 2){
        if (sortTypes.titleSortType == 'none') {
            lines_title[0].setAttribute('x2', '12');
            lines_title[1].setAttribute('x2', '7');
            sortTypes.titleSortType = 'ascending';
            console.log(sortTypes.titleSortType, i);
        } else if (sortTypes.titleSortType == 'ascending') {
            lines_title[0].setAttribute('x2', '2')
            lines_title[2].setAttribute('x2', '12');
            sortTypes.titleSortType = 'descending';
        }else{
            lines_title[1].setAttribute('x2', '2');
            lines_title[2].setAttribute('x2', '2');
            sortTypes.titleSortType = "none";
        }
        sendSortTypeToBackend(i,sortTypes.titleSortType);
    }
}

function sendSortTypeToBackend(i,sortType){
    
    console.log("Sending sort type to backend: " + sortType);
}

for (let i = 0; i < sort_type_button.length; i++){
    sort_type_button[i].addEventListener('click', () => {sort(i, sortTypes);});
};


//Фильтр ленты
const type_filter = document.querySelectorAll("#filter-type");
const type_item = document.querySelectorAll("#type_item")
var type_project = document.querySelectorAll("#svg_project line");
var type_year = document.querySelectorAll("#svg_year line");
var type_course = document.querySelectorAll("#svg_course line");
var type_author = document.querySelectorAll("#svg_author line");
var statusFilter = {
    project: 'close',
    year: 'close',
    course: 'close',
    author: 'close'
};

// Открытие ленты
function openFilter(i,status){
        if(i == 0 && statusFilter.project == 'close'){
            type_project[0].setAttribute('stroke-width', '0');
            type_item[i].style.display = "flex"
            status.project = 'open';
        } else if(i == 0 && statusFilter.project == 'open') {
            type_project[0].setAttribute('stroke-width', '2');
            type_item[i].style.display = "none"
            status.project = 'close';
        }
        else if(i == 1 && statusFilter.year == 'close'){
            type_year[0].setAttribute('stroke-width', '0');
            type_item[i].style.display = "flex"
            status.year = 'open';
        } else if(i == 1 && statusFilter.year == 'open') {
            type_year[0].setAttribute('stroke-width', '2');
            type_item[i].style.display = "none"
            status.year = 'close';
        }
        else if(i == 2 && statusFilter.course == 'close'){
            type_course[0].setAttribute('stroke-width', '0');
            type_item[i].style.display = "flex"
            status.course = 'open';
        } else if(i == 2 && statusFilter.course == 'open') {
            type_course[0].setAttribute('stroke-width', '2');
            type_item[i].style.display = "none"
            status.course = 'close';
        }
        else if(i == 3 && statusFilter.author == 'close'){
            type_author[0].setAttribute('stroke-width', '0');
            type_item[i].style.display = "flex"
            status.author = 'open';
        } else if(i == 3 && statusFilter.author == 'open') {
            type_author[0].setAttribute('stroke-width', '2');
            type_item[i].style.display = "none"
            status.author = 'close';
        }
};

for(let i = 0; i < type_filter.length; i++){
    type_filter[i].addEventListener('click', () => {openFilter(i, statusFilter)})
};

//Применение фильтра
const novella = document.getElementById('#filter_novella');
const site = document.getElementById('#filter_site');
const year22 = document.getElementById('#filterYear_22');
const year23 = document.getElementById('#filterYear_23');
const course1 = document.getElementById('#filter_course1');
const course2 = document.getElementById('#filter_course2');
const author = document.getElementById('#nameAuthor');
const sendFilter = document.getElementById('#sendFilter');

//Функция отправки фильтра на бэк 

sendFilter.addEventListener('click', /*Название функции отправляющей на бэк*/)