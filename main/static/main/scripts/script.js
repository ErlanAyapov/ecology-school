function encodeImageFileAsURL(element, input_id) {
    const input_base64 = document.getElementById(input_id);
    var file = element.files[0];
    var reader = new FileReader();
    var base64;
    reader.onloadend = function() {
        input_base64.value = reader.result;
        $('#blah').attr('src', reader.result);
        $('#blah').attr('alt', 'таңдалды');
        $("#blah").css("display", 'block');
        $("#btn_upd").css("display", 'block');
    }
    reader.readAsDataURL(file);
    // reader.readAsDataURL(element.files[0]);        
}
function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#blah')
            .attr('src', e.target.result)
            };

            reader.readAsDataURL(input.files[0]);
        }
    }
