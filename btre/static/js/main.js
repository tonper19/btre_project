// 14/03/2020 if any of these files in the static folder is modified,
// the following must be executed: python manage.py collectstatic

const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();
// this will make all the messages to fadeout after 30 seconds, if the user don't clear it first
setTimeout(function() {
    $('#message').fadeOut('slow');
}, 30000);