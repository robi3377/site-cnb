$(document).ready(function() {
  // Store selected images
  var selectedImages = [];

  // Display selected images in the preview container
  function displaySelectedImages() {
    var imagePreviewContainer = $('#image-preview-container');
    imagePreviewContainer.empty();

    // Read and display each selected image
    selectedImages.forEach(function(file) {
      var reader = new FileReader();
      reader.onload = function(e) {
        var image = $('<img>').addClass('w-[30vh] h-[30vh]').attr('src', e.target.result);
        imagePreviewContainer.append(image);
      }
      reader.readAsDataURL(file);
    });
  }

  // Add selected images to the array
  $('#files').change(function() {
    selectedImages = Array.from(this.files);
    displaySelectedImages();
  });

  // Browse button click event
  $('#browse-button').click(function(e) {
    e.preventDefault();
    $('#files').click();
  });

  // Rest of your code
});

$(document).ready(function() {
  // Display selected image in the designated area
  $('#file').change(function() {
    var file = this.files[0];
    if (file) {
      var reader = new FileReader();
      reader.onload = function(e) {
        $('#preview-image').attr('src', e.target.result);
      }
      reader.readAsDataURL(file);
    }
  });
});


$(document).ready(function() {
    // Add new paragraph and subtitle inputs
    $('#add-input-button').click(function() {
      var paragraphInput = '<div class="paragraph-input">' +
                              '<input type="text" name="subtitlu[]" class="p-4 border-2 rounded-3xl" placeholder="Adaugă subtitlu">' +
                              '<input type="text" name="paragraf[]" class="p-4 border-2 rounded-3xl" placeholder="Adaugă paragraf">' +
                          '</div>';
      $('#paragraphs-container').append(paragraphInput);
    });
  });

////////////////////////////////////////////////////////

function openImage(value){
  document.querySelector("#openImage").style.transform = "translateX(0px)";
  let bgImage = document.querySelector("#bgimage"+value).style.backgroundImage.slice(5,-2);
  document.querySelector("#openedImage").src = bgImage;
}
function closeImage(){  
  document.querySelector("#openImage").style.transform = "translateX(100vw)";
}

function darken(value){
  if(isDesktop == true){
      document.querySelector("#container"+value).style.transform = "translateY(0px)";
  }
}

function lightup(value){
  if(isDesktop == true){
  let containerHeight = document.querySelector("#container"+value).offsetHeight;
  document.querySelector("#container"+value).style.transform = "translateY(" + containerHeight + "px)";
  }
}