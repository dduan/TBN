(function($) {
	window.initClient = function() {			
		var retrieveDocs = JSON.parse(localStorage.getItem("docs"));
		if (retrieveDocs) {
			$.each(retrieveDocs, function(name, body) {
				$("#list").append('<li>'+name+'</li>');
			});
		}
		
				
		$("#formula_area").keydown(function(e) {
			var value = $("#formula_area").val();
			console.log('requesting');
			$.getJSON("/api", {"input": value}, function(result) {
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

