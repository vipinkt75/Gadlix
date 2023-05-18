$(document).ready(function () {
  $('#form').on('submit', function (event) {
    event.preventDefault(); // prevent the form from submitting normally

    $.ajax({
      type: 'POST',
      url: '/contact/', // the URL to which the form data will be submitted
      data: $(this).serialize(), // serialize the form data for submission
      dataType: 'json',
      success: function (response) {
        if (response.status === 'true') {
          // if the response indicates success, show the success message
          // $('.sb-success-result').addClass('sb-active');
          swal(
            'Success',
            'message successfully sent',
            'success')
          $('#form').trigger("reset");
        }
        else {
          // if the response indicates failure, show the error message
          
          $(document).on('click', '#ba', function(e) {
            swal(
              'Error!',
              'Form validation error!',
              'error'
            )
            $('#form').trigger("reset");
          });
        }
      },
      error: function (xhr, textStatus, errorThrown) {
        alert('An error occurred while submitting the form.');
      }
    });
  });
});



