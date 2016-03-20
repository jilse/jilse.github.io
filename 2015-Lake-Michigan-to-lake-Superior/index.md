---
layout: page
title: From motor boat to sail boat through Lake Michigan and Lake Superior
excerpt: ""
search_omit: true
image:
  feature: "2015-07-16 14.03.21.jpg"
  
---

<ul class="post-list">
{% for post in site.categories.2015-MichiganToMinnesota reversed %} 
  <li><article><a href="{{ site.url }}{{ post.url }}">{{ post.title }} <span class="entry-date"><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}</time></span>{% if post.excerpt %} <span class="excerpt">{{ post.excerpt | remove: '\[ ... \]' | remove: '\( ... \)' | markdownify | strip_html | strip_newlines | escape_once }}</span>{% endif %}</a></article></li>
{% endfor %}
</ul>
