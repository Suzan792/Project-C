function like_button(id){
  var post_url ="{% url 'home_page' %}"
  $.ajax({
    type: 'POST',
    url: post_url,
    data: {
      'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
      'id':id,
    },
    success: LikePost,
    dataType: 'html'
  });
  function LikePost(data, jqXHR) {
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
