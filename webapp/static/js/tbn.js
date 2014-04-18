$(document).ready(function() {

	var TBNWebClient;

	TBNWebClient = (function() {
	  function TBNWebClient() {
			// click on listed doc name
			var _this = this;

			this.createDocument();
			this.updateDocumentList();



			$("#save_button").click(function(e) {
				_this.saveDocument();
				_this.updateDocumentList();
			});

			$("#new_button").click(function(e) {_this.createDocument();});

	  }

		TBNWebClient.prototype.allDocuments = function() {
			return JSON.parse(localStorage.getItem("docs")) || {};
		}

	  TBNWebClient.prototype.createDocument = function() {
			var date = new Date();
			var docName = "Created On " + date.toDateString() + " "
				+ date.toLocaleTimeString();
			$("#doc_title").val(docName);
			$("#formula_area").val("");
			$("#result_area").val("");
		};

	  TBNWebClient.prototype.updateDocumentList = function() {
			var retrieveDocs = this.allDocuments();
			var _this = this;
			$('.saved_doc').remove();
			if (retrieveDocs) {
				var listMenu = $("#menu");
				$.each(retrieveDocs, function(name, body) {
					listMenu.append('<li><a href="#" class="saved_doc">'
						+ name + '</a></li>');
				});
				$(".saved_doc").click(function(e) {
					_this.openDocument($(e.target).text());
				});
			}
		};

	  TBNWebClient.prototype.saveDocument = function() {
			var title = $("#doc_title").val();
			var body = $("#formula_area").val();
			var docs = this.allDocuments();
			docs[title] = body;
			localStorage.setItem('docs', JSON.stringify(docs));
		};

		TBNWebClient.prototype.openDocument = function(name) {
			var body = this.allDocuments()[name];
			console.log(body);
			$("#doc_title").val(name);
			$('#formula_area').val(body);
		}

		TBNWebClient.prototype.evaluateDocument = function() {
			var value = $("#formula_area").val();
			$.getJSON("/api", {"input": value}, function(result) {
				$("#output").val(result.join("\n"));
			});
		}
	  return TBNWebClient;

	})();

	new TBNWebClient();
});
