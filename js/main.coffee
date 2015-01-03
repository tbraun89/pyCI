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

      if $('#downloads_list')
        converter = new Markdown.Converter();

        for version in data
          zip_link = "https://github.com/tbraun89/pyCI/archive/#{version['tag_name']}.zip"
          tar_link = "https://github.com/tbraun89/pyCI/archive/#{version['tag_name']}.tar.gz"
          $('#downloads_list').append "<h2>pyCI #{version['tag_name']} <small><a href=\"#{zip_link}\">[.zip]</a> · <a href=\"#{tar_link}\">[.tar.gz]</a></small></h2>"
          $('#downloads_list').append "<p>#{converter.makeHtml(version['body'])}</p>"
