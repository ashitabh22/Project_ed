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
var newOption;

var inputs;
var optionString;
var optionValue;


$(".classSelection").click(function (clicked) {
    classSelectionValue = $(this).val();
    classSelectionText = $(this).attr('id');
    changeClass = $(this).text();
    $("#changeClass").text(changeClass);
});

$(".subjectSelection").click(function (clicked) {
    subjectSelectionValue = $(this).val();
    subjectSelectionText = $(this).text();
    $("#changeSubject").text(subjectSelectionText);
});

$(".difficultySelection").click(function (clicked) {
    difficultySelectionValue = $(this).val();
    difficultySelectionText = $(this).text();
    $("#changeDifficulty").text(difficultySelectionText);
});

//---------------question-options---------------//

$('.addOptionButton').on('click', function () {
    newOption = '<div class="mt-2 d-flex d-inline-flex input-group input-group-md newOptionTextField">' +
        '<span class="optionDeleteButton input-group-text" id="inputGroup-sizing-sm"><i class="far fa-trash-alt"></i></span>' +
        '<input type="text" class="optionField form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-sm">' + '<span class="correctOption input-group-text" id="inputGroup-sizing-sm"><i class="far fa-trash-alt"></i></span>' + 
        '</div>';
    $(newOption).appendTo("#answer_form");
});

$('.addOption').on('click', '.optionDeleteButton', function (e) {
    $(this).parent().remove();
});


//-----------------keyboard---------------------//

var buttonArr = [];

$(".strong").click(function strong() {
    var text = $(".boldQuestion");
    text.val(text.val() + "<strong></strong>");
});

$(".italic").click(function italic() {
    var text = $(".boldQuestion");
    text.val(text.val() + "<i></i>");
});

$(".underline").click(function underline() {
    var text = $(".boldQuestion");
    text.val(text.val() + "<ul></ul>");
});

$(".create").click(function create() {

    store = $("#editor").html();

    question = '<div class="card mb-3 questionList" style="width:auto" ' +
        'data-id="' + subjectSelectionValue + '" data-category="' +
        classSelectionValue + ' ' + difficultySelectionValue + ' ' + subjectSelectionValue + '">' +
        '<div class="card-body">' +
        '<div class="md-0 d-flex justify-content-between">' +
        '<h2 class="card-title">Question</h2>' +
        '<span class="mt-1">' +
        '<p class="mr-3"><strong>Class: </strong>' + classSelectionText +
        '</p>' +
        '<p class="mr-3"><strong>Subject: </strong>' + subjectSelectionText +
        '</p>' +
        '<p><strong>Difficulty: </strong>' + difficultySelectionText + '</p>' +
        '</span>' +
        '</div>' +
        '<p class="card-text questionField">' + store + '</p>' +
        '<br>' +
        '<div class="addOptionHere"></div> ' +
        '<button type="button" class="mt-3 p-1 btn btn-outline-success">SUBMIT</button>' +
        '</div>' +
        '</div>';

    $(question).appendTo(".addQuestionInThisClass");


    inputs = $(".optionField");
    var optionArray = [];
    for (var option = 0; option < inputs.length; option++) {
        optionValue = $(inputs[option]).val();
        optionString = '<div class="input-group my-2">' +
            '<div class="input-group-prepend">' +
            '<div class="input-group-text">' +
            '<input type="radio" class="selectedOption' + option + '">' +
            '</div>' +
            '</div>' +
            '<p type="text" class="form-control" aria-label="Text input with radio button">' + optionValue + '</p>' +
            '</div>';
        optionArray[option] = optionString;
        $(optionString).appendTo(".addOptionHere");
    }

    //    $(optionString).appendTo(".addOptionHere");


    MathJax.Hub.Queue(["Typeset", MathJax.Hub, "questiond"]);
});




//-----------------------formula--------------------------------

$('.formulaButton').click(function () {
    var selection = (document.all) ? document.selection.createRange().text : document.getSelection();
    var selection_text = selection.toString();
    var newText = "$" + selection_text + "$";
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

function image() {
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

$filterCheckboxes.on('change', function () {

    var selectedFilters = {};

    $filterCheckboxes.filter(':checked').each(function () {
        if (!selectedFilters.hasOwnProperty(this.name)) {
            selectedFilters[this.name] = [];
        }
        selectedFilters[this.name].push(this.value);
    });
    
    var $filteredResults = $('.questionList');
    
    
    $.each(selectedFilters, function (name, filterValues) {
        $filteredResults = $filteredResults.filter(function () {

            var matched = false,
                currentFilterValues = $(this).data('category').split(' ');
            $.each(currentFilterValues, function (_, currentFilterValue) {
                if ($.inArray(currentFilterValue, filterValues) != -1) {
                    matched = true;
                    return false;
                }
            });
            return matched;

        });
    });

    $('.questionList').hide().filter($filteredResults).show();

});




//-----------------BLUR POP UP-----------------------------//








//----------------FOR_STUDENT_INTERFACE---------------------//
//----------------FOR_STUDENT_INTERFACE---------------------//
//----------------FOR_STUDENT_INTERFACE---------------------//
//----------------FOR_STUDENT_INTERFACE---------------------//
//----------------FOR_STUDENT_INTERFACE---------------------//

//var inputs;
//var optionString;
//var optionValue;
//
//    inputs = $(".optionField");
//    var optionArray = [];
//    for (var option = 0; option < inputs.length; option++) {
//        optionValue = $(inputs[option]).val();
//        optionString = '<div class="input-group my-2">' +
//            '<div class="input-group-prepend">' +
//            '<div class="input-group-text">' +
//            '<input type="radio" class="selectedOption' + option + '">' +
//            '</div>' +
//            '</div>' +
//            '<p type="text" class="form-control" aria-label="Text input with radio button">' + optionValue + '</p>' +
//            '</div>';
//        optionArray[option] = optionString;
//        $(optionString).appendTo(".addOptionHere");
//    }
