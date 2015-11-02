$(document).ready(function() {

//    var ad_first = $('.ad_zone .ad:first-child').html();
//    console.log(ad_first);

//儲存購買清單
    $('.purchase').on('click', function(){
        var newItem = {
            "id": $(this).val(),
            "Qtd": $(this).prev().val()
        };
        var storedItems = JSON.parse(localStorage.getItem("itemArray")) || [];
        for (i=0, j=storedItems.length; i<j; i++) {
            if (storedItems[i].id == newItem.id) {
                storedItems[i].Qtd = parseInt(storedItems[i].Qtd) + parseInt(newItem.Qtd);
            } else {
                storedItems.push(newItem);
            }
        }

        localStorage.setItem("itemArray", JSON.stringify(storedItems));
        b=JSON.parse(localStorage.getItem('itemArray'));
        console.log(b);
    });


});