const likedLeftBtn = document.getElementById('liked_left_btn');
const likedRightBtn = document.getElementById('liked_right_btn');
const userHorizonScroll = document.getElementById('list_user_project');
const likedHorizonScroll = document.getElementById('list_liked_project');

likedRightBtn.addEventListener('click', ()=>{
    likedHorizonScroll.style.scrollBehavior = "smooth";
    likedHorizonScroll.scrollLeft += 466;
});

likedLeftBtn.addEventListener('click', ()=>{
    likedHorizonScroll.style.scrollBehavior = "smooth";
    likedHorizonScroll.scrollLeft -= 466;
});


var i = 0;
const check = document.querySelectorAll("#check")
var statusImage = {
    first: 'not',
    second: 'not',
    third: 'not',
    fourth: 'not'
};

const submitButton = document.getElementById("sumbit");
submitButton.disabled = true;

document.getElementById('first').addEventListener('change', function(){
    if( this.value ){
        console.log( "Оппа, выбрали файл!" );
        console.log( this.value );
        if (statusImage.first == 'not'){
            i += 1
            statusImage.first = 'add';
            check[0].style.display = 'block'
        };
    } else { // Если после выбранного тыкнули еще раз, но дальше cancel
        console.log( "Файл не выбран" );
    }
    if(i >= 4){
        submitButton.disabled = false;
    }
});

document.getElementById('second').addEventListener('change', function(){
    if( this.value ){
        console.log( "Оппа, выбрали файл!" );
        console.log( this.value );
        if (statusImage.second == 'not'){
            i += 1
            statusImage.second = 'add';
            check[1].style.display = 'block'
        };
    } else { // Если после выбранного тыкнули еще раз, но дальше cancel
        console.log( "Файл не выбран" );
    }
    if(i >= 4){
        submitButton.disabled = false;
    }
});

document.getElementById('third').addEventListener('change', function(){
    if( this.value ){
        console.log( "Оппа, выбрали файл!" );
        console.log( this.value );
        if (statusImage.third == 'not'){
            i += 1
            statusImage.third = 'add';
            check[2].style.display = 'block'
        };
    } else { // Если после выбранного тыкнули еще раз, но дальше cancel
        console.log( "Файл не выбран" );
    }
    if(i >= 4){
        submitButton.disabled = false;
    }
});

document.getElementById('fourth').addEventListener('change', function(){
    if( this.value ){
        console.log( "Оппа, выбрали файл!" );
        console.log( this.value );
        if (statusImage.fourth == 'not'){
            i += 1
            statusImage.fourth = 'add';
            check[3].style.display = 'block'
        };
    } else { // Если после выбранного тыкнули еще раз, но дальше cancel
        console.log( "Файл не выбран" );
    }
    if(i >= 4){
        submitButton.disabled = false;
    }
});
