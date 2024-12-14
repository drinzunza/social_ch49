function init() {
    console.log("Post list page");

    $(".comment-form").on('submit', function(event) {
        event.preventDefault();
        console.log("about to create a comment");

        const $form = $(this);
        const postId = $form.find('[name="post_id"]').val();
        const text = $form.find('[name="text"]').val();
        const token = $form.find('[name="csrfmiddlewaretoken"]').val();

        saveComment(postId, text, token);
        $form.find('[name="text"]').val(''); // clear the text area
    }); 
}

function saveComment(postId, text, token) {
    $.ajax({
        url: '/posts/save_comment/',
        method: 'POST',
        data: {
            post_id: postId,
            text: text,
            csrfmiddlewaretoken: token
        },
        success: function(data) {
            console.log("Worked!!");
            displayComment(data.comment, postId);
        },
        error: function(error) {
            console.log("ERROR", error);
        }
    });
}

function displayComment(comment, postId) {

    const formatted = new Date(comment.created_on);
    const options = {
        month: 'short',
        day: 'numeric',
        year: 'numeric',
        hour: 'numeric',
        minute: '2-digit',
        hour12: true
    };

    let showDate = formatted.toLocaleString("en-US", options);
    showDate = showDate.replace("PM", "p.m.").replace("AM", "a.m.");

    const syntax = `<div class="comment">
                        <p class="author">${comment.user}</p>
                        <p class="text">${comment.text}</p>
                        <p class="date"><small>${showDate}</small></p>
                    </div>`;

    $("#comments-" + postId + " > form").before(syntax);
}

function showComments(postId) {
    const div = document.getElementById("comments-" + postId);
    if(div.classList.contains('hidden')) {
        div.classList.remove('hidden');
    }
    else {
        div.classList.add('hidden');
    }
}

var bookmarkingPostId = 0;
var myModal = null;

function showModal(postId){
    bookmarkingPostId = postId;
    myModal = new bootstrap.Modal($('#bookmarkModal'))
    myModal.show();
}

function saveBookmark() {
    const title = $("#txtBookmarkTitle").val();
    const token = $("input[name='csrfmiddlewaretoken']").val();
    $.ajax({
        url: "/posts/save_bookmark/",
        method: "POST",
        data: {
            post_id: bookmarkingPostId,
            title: title,
            csrfmiddlewaretoken: token
        },
        success: function() {
            console.log("bookmark saved!");
            myModal.hide();
        },
        error: function(err){
            console.log("Error", err);
        }
    });
}

window.onload = init;