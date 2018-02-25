---
layout: page
title: Duluth to the North Channel...and back. 
excerpt: ""
search_omit: true
image: 
  feature: "2017/routemap.png"
---
The rough plan was for me to sail the boat to Escanaba, MI for my Grandma's 90th b-day party where Heather and Ethan would meet me and we'd sail back together taking a slight right turn at the North Channel for some exploring. It turns out that's exactly what happened and everything went roughly to plan. 
<ul class="post-list">
{% for post in site.categories.2017-NorthChannel reversed %} 
  <li><article><a href="{{ site.url }}{{ post.url }}">{{ post.title }} <span class="entry-date"><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}</time></span>{% if post.excerpt %} <span class="excerpt">{{ post.excerpt | remove: '\[ ... \]' | remove: '\( ... \)' | markdownify | strip_html | strip_newlines | escape_once }}</span>{% endif %}</a></article></li>
{% endfor %}
</ul>
