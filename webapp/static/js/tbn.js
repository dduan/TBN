$(document).ready(function() {	
	var date = new Date();
	var docName = "Created On " + date.toDateString() + " " 
		+ date.toLocaleTimeString();	
	$("#doc_title").val(docName);
	var retrieveDocs = JSON.parse(localStorage.getItem("docs"));
	if (retrieveDocs) {
		var listMenu = $("#menu");
		$.each(retrieveDocs, function(name, body) {
			console.log(name + ' ' + body);
			listMenu.append('<li><a href="#" class="saved_doc">' 
				+ name + '</a></li>');
		});
	} else {
		retrieveDocs = {};
	}

	$(".saved_doc").click(function(e) {
		
		var title = $(e.target).text();
		var body = retrieveDocs[title];
		$("#doc_title").val(title);
		$('#formula_area').val(body);
	});

	$("#save_button").click(function(e) {
		var title = $("#doc_title").val();
		var body = $("#formula_area").val();
		retrieveDocs[title] = body;
		console.log(retrieveDocs);
		localStorage.setItem('docs', JSON.stringify(retrieveDocs));
	});

	$("#new_button").click(function(e) {
		console.log("mouse click");
	});

	$("#formula_area").keydown(function(e) {
		var value = $("#formula_area").val();
		$.getJSON("/api", {"input": value}, function(result) {
			$("#output").val(result.join("\n"));
		});
	});
});