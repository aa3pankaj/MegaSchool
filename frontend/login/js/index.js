$('.form').find('input, textarea').on('keyup blur focus', function (e) {
  
  var $this = $(this),
      label = $this.prev('label');

	  if (e.type === 'keyup') {
			if ($this.val() === '') {
          label.removeClass('active highlight');
        } else {
          label.addClass('active highlight');
        }
    } else if (e.type === 'blur') {
    	if( $this.val() === '' ) {
    		label.removeClass('active highlight'); 
			} else {
		    label.removeClass('highlight');   
			}   
    } else if (e.type === 'focus') {
      
      if( $this.val() === '' ) {
    		label.removeClass('highlight'); 
			} 
      else if( $this.val() !== '' ) {
		    label.addClass('highlight');
			}
    }

});
/*
$('#form' ).submit(function(e){
      e.preventDefault();

      $.ajax({
        type:'POST',
        url:'127.0.0.1:8000/',  // make sure , you are calling currect url
        data:$(this).serialize(),
        success:function(json){              
          alert(json.message); 
          if(json.status==200){
             var comment = json.comment;
             var user = json.user;
             /// set `comment` and `user` using jquery to some element
           }             
        },
        error:function(response){
          alert("some error occured. see console for detail");
        }
      });
     });
*/
$('.tab a').on('click', function (e) {
  
  e.preventDefault();
  
  $(this).parent().addClass('active');
  $(this).parent().siblings().removeClass('active');
  
  target = $(this).attr('href');

  $('.tab-content > div').not(target).hide();
  
  $(target).fadeIn(600);
  
});



$("#loginform").submit(function(event) {

        var data = {}
        data["username"] = $("#username").val();
        
        data["password"] = $("#password").val();
		data["csrfmiddlewaretoken"]="{{ csrf_token }}";
		
		  
        $.ajax({
                 type: "POST",
                 contentType: "application/json",
                 url: "http://127.0.0.1:8000/login/" ,
				 
                  data: JSON.stringify(data),
				 
                 dataType: 'json',
                 timeout: 600000,
				 
                 success: handleData,
                 error: function (e) {
                     console.log("ERROR: ", e);
					
                    
					 
                 }
        });


    });
	function handleData(data) {
    alert(data);
	 alert(json.message); 
                     if(json.status==200){
						 alert("ahhefe");
						    window.location.href = "../dash/index.html";
                      var comment = json.comment;
                      var user = json.user;
                        /// set `comment` and `user` using jquery to some element
                       }   
				  
                     console.log("DONE");
    //do some stuff
}
$("#form").submit(function(event) {

        var data = {}
        data["username"] = $("#username").val();
        data["first_name"] = $("#first_name").val();
        data["last_name"] = $("#last_name").val();
        data["password"] = $("#password").val();
		data["user_type"] = $("#user_type").val();
        data["email"]=$("#email").val();
        data["csrfmiddlewaretoken"]="{{ csrf_token }}";
		console.log(data);
		 /*data: { csrfmiddlewaretoken: "{{ csrf_token }}",   // < here 
            state:"inactive" 
          },*/
        $.ajax({
                 type: "POST",
                 contentType: "application/json",
                 url: "http://127.0.0.1:8000/signup/",
				 
                  data: JSON.stringify(data),
				 
                 dataType: 'json',
                 timeout: 600000,
                 success: function (data) {
					 alert("success")
                     console.log("DONE");
                 },
                 error: function (e) {
                     console.log("ERROR: ", e);
                     display(e);
                 }
        });


    });



