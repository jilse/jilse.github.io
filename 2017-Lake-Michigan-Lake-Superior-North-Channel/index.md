---
layout: page
title: We traveled around 1600nm this summer. 
excerpt: ""
search_omit: true
image: 
  feature: "2017/routemap.png"
---

<ul class="post-list">
{% for post in site.categories.2017-NorthChannel reversed %} 
  <li><article><a href="{{ site.url }}{{ post.url }}">{{ post.title }} <span class="entry-date"><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}</time></span>{% if post.excerpt %} <span class="excerpt">{{ post.excerpt | remove: '\[ ... \]' | remove: '\( ... \)' | markdownify | strip_html | strip_newlines | escape_once }}</span>{% endif %}</a></article></li>
{% endfor %}
</ul>
