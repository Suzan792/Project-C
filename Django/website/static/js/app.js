
function like_button(id,url,csrfToken){
  var post_url =url
  $.ajax({
    type: 'POST',
    url: post_url,
    data: {
      'csrfmiddlewaretoken': csrfToken,
      'id':id,
    },
    success: LikePost,
    dataType: 'html'
  });
  function LikePost(data) {
    var data = $.parseJSON(data)
    if (data['liked']) {
      $('#heart_sign_color_'+data['art_pk']).addClass('text-danger')
      $('#like_count_'+data['art_pk']).text(data['like_count'])
    }
    else
    {
      $('#heart_sign_color_'+data['art_pk']).removeClass('text-danger')
      $('#like_count_'+data['art_pk']).text(data['like_count'])
    }
  };
};




function flashMessage(message){
  $('.flashMessage').text(message)
  $('.flashMessage').slideDown(500).delay(2000).slideUp();
}



function deleteProductDesign(url,csrfToken, id){
  $( "#dialog-confirm" ).dialog({
    resizable: false,
    height: "auto",
    width: 400,
    modal: true,
    buttons: {
      "Yes I am sure": function() {
            $.post(url, {csrfmiddlewaretoken: csrfToken, action: "delete", pk: id}, function(){
              window.location.reload();
            })
      },
      Cancel: function() {
        $( this ).dialog( "close" );
      }
    }
  });
}
