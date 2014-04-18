$(document).ready(function() {

    var TBNWebClient;

    TBNWebClient = (function() {
      function TBNWebClient() {
            // click on listed doc name
            var _this = this;

            this.createDocument();
            this.updateDocumentList();

      $('#formula_area').keyup(function() {
            clearTimeout($.data(this, 'timer'));
            var wait = setTimeout(_this.evaluateDocument, 333);
            $(this).data('timer', wait);
            });

            $("#save_button").click(function(e) {
                _this.saveDocument();
                _this.updateDocumentList();
                _this.updateUiByState();
            });

            $("#new_button").click(function(e) {
                _this.createDocument();
                _this.updateUiByState();
            });

            $("#delete_button").click(function(e) {
                _this.displayDeleteWarning();
            });

            $("#confirm-delete").click(function(e) {
                $("#delete-warning").hide();
                _this.replaceEditingDocument();
                _this.createDocument();
                _this.updateDocumentList();
                _this.updateUiByState();
            });

            $("#cancel-delete").click(function(e) {
                $("#delete-warning").hide();
            });

            $(".alert .close").click(function(e) {
                $("#delete-warning").hide();
            });

            $("#download_button").click(function(e){
                _this.downloadFile();
            });
            this.editingDocument = '';
            this.updateUiByState();
      }

        TBNWebClient.prototype.allDocuments = function() {
            return JSON.parse(localStorage.getItem("docs")) || {};
        }

      TBNWebClient.prototype.createDocument = function() {
            var date = new Date();
            var docName = "Created On " + date.toDateString() + " "
                + date.toLocaleTimeString();
            this.editingDocument = '';
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
                    _this.updateUiByState();
                });
            }
        };

      TBNWebClient.prototype.saveDocument = function() {
            var title = $("#doc_title").val();
            var body = $("#formula_area").val();
            this.replaceEditingDocument(title, body);
        };

        TBNWebClient.prototype.replaceEditingDocument = function(title, body) {
            var docs = this.allDocuments();
            if (this.editingDocument) {
                // remove from localstorage by the old file name first
                delete docs[this.editingDocument];
            }
            this.editingDocument = title;
            if (title && body) {
                docs[title] = body;
            }
            localStorage.setItem('docs', JSON.stringify(docs));
        };
        TBNWebClient.prototype.openDocument = function(name) {
            var body = this.allDocuments()[name];
            $("#doc_title").val(name);
            $('#formula_area').val(body);
            this.editingDocument = name;
        };

        TBNWebClient.prototype.evaluateDocument = function() {
            var value = $("#formula_area").val();
            $.getJSON("/api", {"input": value}, function(data) {
                $("#result_area").val(data['result'].join("\n"));
            });
        };

        TBNWebClient.prototype.updateUiByState = function() {
            var newBadge = $('#save_button .badge');
            var deleteLi = $('#delete_li');
            if (this.editingDocument) {
                newBadge.text('');
                deleteLi.removeClass('disabled');
            } else {
                newBadge.text('new');
                deleteLi.addClass('disabled');
            }
        };

        TBNWebClient.prototype.displayDeleteWarning = function() {
            $("#delete-title").text(this.editingDocument);
            $("#delete-warning").show();
        };

        TBNWebClient.prototype.downloadFile = function() {
            var blob = new Blob([$('#formula_area').val()], {type: "text/plain;charset=utf-8"});
            saveAs(blob, $('#doc_title').val()+'.txt');
        };

      return TBNWebClient;

    })();

    new TBNWebClient();
});
