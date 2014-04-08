(function($){
	tile = function(){			
		var retrieveDocs = JSON.parse(localStorage.getItem("docs"));
		$.each(retrieveDocs, function(name, body) {
			$("#list").append('<li>'+name+'</li>');
			console.log(name);
		});
				
		$("form").keydown(function(e) {
			var value = $(this).find("textarea").val();
			$.getJSON("http://localhost:5000", {"input": value}, function(result) {
				$("#output").val(result.join("\n"));
			});
		});

		$("#save").click(function(e) {
			var value = $("textarea").val();
			var timeStamp = new Date().toString();
			retrieveDocs[timeStamp] = value;
			localStorage.setItem("docs", JSON.stringify(retrieveDocs));
		});
	};
})(jQuery);
