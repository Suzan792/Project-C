
function like_button(id,url,csrfToken,authenticated){
  if (authenticated=='False'){
    flashMessage("You must be logged in to like an ArtWork","info")
  }else{
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
  }

};




function flashMessage(message,type){

  $('.flashMessage').css({'visibility': 'visible'})

  if(type=='info'){$('.flashMessage').css({'background-color': 'orange'});}
  if(type=='warning'){$('.flashMessage').css({'background-color': 'red'});}
  if(type=='success'){$('.flashMessage').css({'background-color': 'green'});}
  $('.flashMessage').text(message)
  $('.flashMessage').slideDown(500).delay(2000).slideUp();
}



function popUpDialog(url,csrfToken, id,dialogId,actionName){
  $( dialogId ).dialog({
    resizable: false,
    height: "auto",
    width: 400,
    modal: true,
    buttons: {
      "Yes I am sure": function() {
            $.post(url, {csrfmiddlewaretoken: csrfToken, action: actionName, pk: id}, function(){
              window.location.reload();
            })
      },
      Cancel: function() {
        $( this ).dialog( "close" );
      }
    }
  });
}


function saveDesignCoordinate(url,csrfToken,artId,frameClass,TextId,confirmationMessage,buttonTextId,buttonArtId,buttonFrameId){
  $(".crop_frame").css({ 'backgroud-color': 'black', border: '5px solid rgba(250, 0, 0, 0)'})
  window.scrollTo(0,0);
  html2canvas(document.querySelector("#imageEditSpace")).then(canvas => {

  var imageUri = canvas.toDataURL();
  var art_top = $( artId ).css("top");
  var art_left = $( artId ).css("left");
  var height = $( artId ).css("height");
  var width = $( artId ).css("width");
  var rotation = $(artId).css("transform");
  var frame_top = $( frameClass ).css("top");
  var frame_left = $( frameClass ).css("left");
  var frame_height = $( frameClass ).css("height");
  var frame_width = $( frameClass).css("width");
  var frame_border_radius = $( frameClass).css("border-top-left-radius");
  var designId = activeDesignId;
  // text
  var font = $( TextId ).css("font-family");
  var font_weight = $( TextId ).css("font-weight");
  var font_style = $( TextId ).css("font-style");
  var font_color = $( TextId ).css("color");
  var text_top = $( TextId ).css("top");
  var text_left = $( TextId ).css("left");
  var text = $( TextId).text();
  var text_size = $(TextId).css("font-size");
  $.ajax({
    type: 'POST',
    url: url,
    data: {
      'csrfmiddlewaretoken': csrfToken,
      'action':'save',
      'designId':designId,
      'left': art_left,
      'top':art_top,
      'height':height,
      'width':width,
      'frame_top':frame_top,
      'frame_left':frame_left,
      'frame_height':frame_height,
      'frame_width':frame_width,
      'frame_border_radius':frame_border_radius,
      'rotation':rotation,
      'font':font,
      'font_weight':font_weight,
      'font_style':font_style,
      'font_color':font_color,
      'text_top':text_top,
      'text_left':text_left,
      'text':text,
      'text_size':text_size,
      'image':imageUri
    },
    success: alert,
    dataType: 'json'
  });
  });
  function alert(data) {
    var data = data
    if (confirmationMessage=='true'){
      flashMessage("Your design is saved successfully","success")
    }
      console.log("hi--")
    var schale = 0.15
    var small_art_coordinate_top = parseInt(art_top)*schale
    var small_art_coordinate_left = parseInt(art_left)*schale
    var small_art_height = parseInt(height)*schale
    var small_frame_coordinate_top = parseInt(frame_top)*schale
    var small_frame_coordinate_left = parseInt(frame_left)*schale
    var small_frame_height = parseInt(frame_height)*schale
    var small_frame_width = parseInt(frame_width)*schale
    var small_frame_frame_border_radius = parseInt(frame_border_radius)*schale

    var small_text_top = parseInt(text_top)*schale
    var small_text_left =parseInt(text_left)*schale
    var small_font_size = parseInt(text_size)*schale
    var small_font_weight =parseInt(font_weight)*schale
    $(buttonTextId+activeDesignId+'').text(text)
    $( buttonTextId+activeDesignId+'').css({top:small_text_top,left:small_text_left,
    'font-family':font,'font-weight':small_font_weight+'px',
    'font-style':font_style,'color':font_color,
    'font-size':small_font_size})
    $(buttonArtId+activeDesignId+'').css({ top: small_art_coordinate_top, left: small_art_coordinate_left, height: small_art_height});
    $(buttonFrameId+activeDesignId+'').css({ top: small_frame_coordinate_top, left: small_frame_coordinate_left, height: small_frame_height, width:small_frame_width, 'border-radius': small_frame_frame_border_radius});
    saveDesign = false;
  };
};
