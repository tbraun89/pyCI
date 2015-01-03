---
---

$(document).ready ->
  $.ajax
    type: 'GET',
    url:  'https://api.github.com/repos/tbraun89/pyCI/releases'
    headers:
      Accept: 'application/vnd.github.v3+json'
    success: (data) ->
      $('#download_zip').attr    'href', "https://github.com/tbraun89/pyCI/archive/#{data[0]['tag_name']}.zip"
      $('#download_tar_gz').attr 'href', "https://github.com/tbraun89/pyCI/archive/#{data[0]['tag_name']}.tar.gz"
