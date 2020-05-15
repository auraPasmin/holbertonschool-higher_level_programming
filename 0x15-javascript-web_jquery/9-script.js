const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
$.getJSON(url, res => $('#hello').text(res.hello));
