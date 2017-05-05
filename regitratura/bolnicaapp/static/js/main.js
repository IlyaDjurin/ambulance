



//function getCookie(name) {
//          var cookieValue = null;
//          if (document.cookie && document.cookie != '') {
//                var cookies = document.cookie.split(';');
//         for (var i = 0; i < cookies.length; i++) {
//              var cookie = jQuery.trim(cookies[i]);
//         // Does this cookie string begin with the name we want?
//         if (cookie.substring(0, name.length + 1) == (name + '=')) {
//           cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//             break;
//             }
//         }
//      }
// return cookieValue;
//}
//
//function csrfSafeMethod(method) {
//    // these HTTP methods do not require CSRF protection
//    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
//}
//$.ajaxSetup({
//    beforeSend: function(xhr, settings) {
//        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
//            xhr.setRequestHeader("X-CSRFToken", csrftoken);
//        }
//    }
//});

$('#suggestion').keyup(function(){
//var csrftoken = getCookie('csrftoken');
var query = $(this).val();
$.ajax({
        url : /suggest_category/,
        type : "GET",
        data : { //csrfmiddlewaretoken : csrftoken//, suggestion: query},
        success: function(data){
        $('#cats').html(data);
        }
       });
   });

   //Работающий код с методом GET, но не работающий с  var csrftoken = getCookie('csrftoken');
//   $('#suggestion').keyup(function(){
//        var query = $(this).val();
//        $.post('/suggest_category/', {suggestion: query}, function(data){
//         $('#cats').html(data);
//        });
//    });
//
