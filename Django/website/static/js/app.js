
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


// Design Edit Functions

var activeDesignId;
var draggability = 'disable';

function productChoiceButton(id,imageUrl,art_draggability,url,csrfToken,pageName){
  draggability =art_draggability;
  if (art_draggability=='enable'){
    $("#art_image_edit_controller_space").show()
  }else{
    $("#art_image_edit_controller_space").hide()
  }
  $("#save_button").hide()
  $( function() {
    $( ".crop_frame" ).draggable();
  } );
  $( function() {
    $( ".crop_frame" ).draggable(draggability);
  } );
  $( function() {
    $( "#art_image_edit" ).draggable();
  } );
  $( function() {
    $( "#art_image_edit" ).draggable(draggability);
  } );
  activeDesignId = id
  $.ajax({
    type: 'GET',
    url: url,
    data: {
      'designId':id,
      'csrfmiddlewaretoken': csrfToken,
    },
    dataType: 'json',
    success: function(data){
      var data = data
      $('.productChoiceButton').css({ 'border-bottom': 'solid 4px white'})
      $('#productChoiceButton_'+data['id']).css({ 'border-bottom': 'solid 4px #f76c6c'})
      art_top = parseInt(data['top'])
      art_left = parseInt(data['left'])
      art_height = data['height']
      width = data['width']
      frame_top = parseInt(data['frame_top'])
      frame_left = parseInt(data['frame_left'])
      frame_height = data['frame_height']
      frame_width = data['frame_width']
      frame_border_radius = data['frame_border_radius']
      rotation = data['rotation']
      $("#art_image_edit").css({ top: art_top, left: art_left, height: art_height, transform: rotation} );
      $(".crop_frame").css({ top: frame_top, left: frame_left, height: frame_height, width: frame_width, 'border-radius': frame_border_radius} );
      $("#height").val(art_height);
      $("#frame_height").val(frame_height);
      $("#frame_width").val(frame_width);
      $("#frame_border_radius").val(frame_border_radius);
      $(".imgbuttom").removeClass("border-success").addClass("border-dark")
      $("#product_".concat(activeDesignId)).removeClass("border-dark").addClass("border-success");
      document.getElementById("product_image_edit").src = imageUrl;
    }
  });
};

function saveCoordinate(url,csrfToken){

  var art_top = $( "#art_image_edit" ).css("top")
  var art_left = $( "#art_image_edit" ).css("left")
  var height = $( "#art_image_edit" ).css("height")
  var width = $( "#art_image_edit" ).css("width")
  var rotation = $( "#art_image_edit" ).css("transform")
  var frame_top = $( ".crop_frame" ).css("top")
  var frame_left = $( ".crop_frame" ).css("left")
  var frame_height = $( ".crop_frame" ).css("height")
  var frame_width = $( ".crop_frame" ).css("width")
  var frame_border_radius = $( ".crop_frame" ).css("border-top-left-radius")
  var designId = activeDesignId
  $.ajax({
    type: 'POST',
    url: url,
    data: {
      'csrfmiddlewaretoken': csrfToken,
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
    },
    success: alert,
    dataType: 'json'
  });
  function alert(data) {
    var data = data
    $("#save_button").hide()
    flashMessage("Your design is saved successfully")
  };
};

function designEditButtons(){
  $(".crop_frame").mousedown(function() {
    if(draggability=='enable'){
      $("#save_button").show()
      $("#art_image_edit_controller_space").show()
    }
  });

  $( function() {
    $( ".crop_frame" ).draggable();
  } );
  $( function() {
    $( ".crop_frame" ).draggable(draggability);
  } );
  $( function() {
    $( "#art_image_edit" ).draggable();
  } );
  $( function() {
    $( "#art_image_edit" ).draggable(draggability);
  } );

  if (draggability=='enable'){
    $("#art_image_edit_controller_space").show()
  }else{
    $("#art_image_edit_controller_space").hide()
  }

  $(".crop_frame").mouseover(function(){
    if(draggability=='enable'){
      $(".crop_frame").mouseover(function(){
        if(draggability=='enable'){
          $(".crop_frame").css({ 'backgroud-color': 'black', border: '5px solid rgba(250, 0, 0, .5)', 'cursor': 'move'})
        }
        else{
          $(".crop_frame").css({'cursor': 'auto'})
        }
      });
      $(".crop_frame").mouseout(function(){
        $(".crop_frame").css({ 'backgroud-color': 'black', border: '5px solid rgba(250, 0, 0, .0)'})
      });

      $( "#height" ).change(function(){
        $("#save_button").show()
        height = $("#height").val();
        $( "#art_image_edit" ).css({ height: height});
      });

      $( "#frame_height" ).change(function(){
        $("#save_button").show()
        height = $("#frame_height").val();
        $(".crop_frame").css({ 'backgroud-color': 'black', border: '5px solid rgba(250, 0, 0, .5)'})
        $( ".crop_frame" ).css({ height: height});
      });

      $( "#frame_width" ).change(function(){
        $("#save_button").show()
        width = $("#frame_width").val();
        $(".crop_frame").css({ 'backgroud-color': 'black', border: '5px solid rgba(250, 0, 0, .5)'})
        $( ".crop_frame" ).css({ width: width});
      });

      $("#frame_border_radius").change(function(){
        $("#save_button").show()
        value = $("#frame_border_radius").val();
        $( ".crop_frame" ).css({ 'border-radius': value+'px'});
      });
      $( "#rotation" ).change(function(){
        $("#save_button").show()
        value = $("#rotation").val();
        $( "#art_image_edit" ).css({'-webkit-transform': 'rotate(' + value + 'deg)',
        '-moz-transform': 'rotate(' + value + 'deg)',
        '-ms-transform': 'rotate(' + value + 'deg)',
        '-o-transform': 'rotate(' + value + 'deg)',
        'transform': 'rotate(' + value + 'deg)',});
      });
    }
  });
}
function flashMessage(message){
  $('.flashMessage').text(message)
  $('.flashMessage').slideDown(500).delay(2000).slideUp();
}

function deleteProductDesign(url,csrfToken){
  $( "#dialog-confirm" ).dialog({
    resizable: false,
    height: "auto",
    width: 400,
    modal: true,
    buttons: {
      "Yes I am sure": function() {
            $.post(url, {csrfmiddlewaretoken: csrfToken, action: "delete", pk: activeDesignId}, function(){
              window.location.reload();
            })
      },
      Cancel: function() {
        $( this ).dialog( "close" );
      }
    }
  });
}
