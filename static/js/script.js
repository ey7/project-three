
// functionality for the delete modal
$('#delete-button').click(function () {
    let blog_id = this.href;
    let href = blog_id;
    $('#delete-confirm').attr('href', href);
    
    return;
});
