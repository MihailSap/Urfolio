
var i = 0;
const check = document.querySelectorAll("#check")
var statusImage = {
    first: 'not',
    second: 'not',
    third: 'not',
    fourth: 'not'
};

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
});
