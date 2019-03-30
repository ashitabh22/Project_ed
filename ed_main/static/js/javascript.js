//var text = querySelector(".questionInput");
//text = text.getText();

//----------------------- Question Details ----------------------
var classSelectionValue;
var classSelectionText;
var subjectSelectionValue;
var subjectSelectionText;
var difficultySelectionValue;
var difficultySelectionText;
var store;
var question;
var changeDifficulty;
var changeClass;
var changeSubject;


$(".classSelection").click(function(clicked){
    classSelectionValue = $(this).val();
    classSelectionText = $(this).attr('id');
    changeClass = $(this).text();
    $("#changeClass").text(changeClass);
});

$(".subjectSelection").click(function(clicked){
    subjectSelectionValue = $(this).val();
    subjectSelectionText = $(this).text();
    $("#changeSubject").text(subjectSelectionText);
});

$(".difficultySelection").click(function(clicked){
    difficultySelectionValue = $(this).val();
    difficultySelectionText = $(this).text();
    $("#changeDifficulty").text(difficultySelectionText);
});

//-----------------keyboard---------------------//

var buttonArr = [];

$(".strong").click(function strong(){
    var text = $(".boldQuestion");
    text.val(text.val() + "<strong></strong>");
});

$(".italic").click(function italic(){
    var text = $(".boldQuestion");
    text.val(text.val() + "<i></i>");
});

$(".underline").click(function underline(){
    var text = $(".boldQuestion");
    text.val(text.val() + "<ul></ul>");
});

$(".create").click(function create() {

    store = $("#editor").html();
    
    question = "<div class=\"card mb-3 questionList\" style=\"width:auto\" " +
                    "data-id=\"" + subjectSelectionValue + "\" data-category=\"" + 
            classSelectionValue + " " + difficultySelectionValue + " " + subjectSelectionValue + "\">" +
                    "<div class=\"card-body\">" +
                        "<div class=\"md-0 d-flex justify-content-between\">" +
                            "<h2 class=\"card-title\">Question</h2>" +
                            "<span class=\"mt-1\">" +
                                "<p class=\"mr-3\"><strong>Class: </strong>" + classSelectionText + 
                                "</p>" +
                                "<p class=\"mr-3\"><strong>Subject: </strong>" + subjectSelectionText +
                                "</p>" +
                                "<p><strong>Difficulty: </strong>" + difficultySelectionText + "</p>" +
                            "</span>" +
                        "</div>" +
                        "<p class=\"card-text questionField\">" + store + "</p>" +
                        "<br>" +
                        "<button type=\"button\" class=\"d-flex mt-3 p-1 btn btn-success\">ADD QUESTION</button>" +
                    "</div>" +
                "</div>";

    $(question).appendTo(".addQuestionInThisClass");

    MathJax.Hub.Queue(["Typeset", MathJax.Hub, "questiond"]);
});




//-----------------------formula--------------------------------

$('.formulaButton').click(function(){
    var selection = (document.all) ? document.selection.createRange().text : document.getSelection();
    var selection_text = selection.toString();
    var newText = "$" + selection_text +"$";
    console.log(newText);
    
    // How do I add a span around the selected text?
    
    var span = document.createElement('SPAN');
    span.textContent = selection_text;
    
    var range = selection.getRangeAt(0);
    range.deleteContents();
    range.insertNode("$");
    
    MathJax.Hub.Queue(["Typeset", MathJax.Hub, "formulaButton"]);
});




//----------------------- keyboard -------------------------- 


function addHTML(tag) {
    var selection = window.getSelection();
    var range = selection.getRangeAt(0);
    var strong = document.createElement(tag);
    range.surroundContents(strong);
    $("#editor").focus();
};

var a = ["a", "b", "c"];

for (var index = 0; index < a.length; ++index) {
    console.log(a[index]);
}

function image(){
    var url = prompt("Enter the URL of the image to insert");
    document.execCommand('insertImage', false, url);
}

$(document).on('keyup', function () {
    $('#res').text($('#editor').html());
});

$(document).on('click', function () {
    $('#res').text($('#editor').html());
});

$(".panel-default .panel-heading .btn-group .btn").on('click', function () {
    $('#res').text($('#editor').html());
});





//---------------------------- Filtering ----------------------------

var $filterCheckboxes = $('input[type="checkbox"]');

$filterCheckboxes.on('change', function() {

  var selectedFilters = {};

  $filterCheckboxes.filter(':checked').each(function() {

    if (!selectedFilters.hasOwnProperty(this.name)) {
      selectedFilters[this.name] = [];
    }

    selectedFilters[this.name].push(this.value);

  });

  // create a collection containing all of the filterable elements
  var $filteredResults = $('.questionList');

  // loop over the selected filter name -> (array) values pairs
  $.each(selectedFilters, function(name, filterValues) {

    // filter each .flower element
    $filteredResults = $filteredResults.filter(function() {

      var matched = false,
        currentFilterValues = $(this).data('category').split(' ');

      // loop over each category value in the current .flower's data-category
      $.each(currentFilterValues, function(_, currentFilterValue) {

        // if the current category exists in the selected filters array
        // set matched to true, and stop looping. as we're ORing in each
        // set of filters, we only need to match once

        if ($.inArray(currentFilterValue, filterValues) != -1) {
          matched = true;
          return false;
        }
      });

      // if matched is true the current .flower element is returned
      return matched;

    });
  });

  $('.questionList').hide().filter($filteredResults).show();

});








//What is the empirical formula of ethane $C_2H_6$?
//(a) $CH$
//(b) $CH_2$
//(c) $CH_3$
//(d) N.O.T


//What is the empirical formula of ethane $$C_2H_6$$?
//(a) $$CH$$
//(b) $$CH_2$$
//(c) $$CH_3$$
//(d) N.O.T
