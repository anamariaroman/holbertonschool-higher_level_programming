$.get('https://fourtonfish.com/hellosalut/?lang=fr', say => {
  $('DIV#hello').html(say.hello);
});
