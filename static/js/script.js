
// functionality for the delete modal
$('#delete-button').click(function () {
    let blog_id = this.href;
    let href = blog_id;
    $('#delete-confirm').attr('href', href);
    
    return;
});

 // Shows loader and hides page content until everything is loaded

$(document).ready(function() {
    hideLoading();
});

 // Displays loader

function showLoading() {
    $("#loader").css("visibility", "visible");
    return;
}

// Hides loader
 
function hideLoading() {
    $("#loader").css("visibility", "hidden");
    return;
}