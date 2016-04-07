---
layout: page
title: "St. Paul to Muskegon MI on the Mississippi and Illinois Rivers"
excerpt: "a race to leave town before the snow hit."
search_omit: true
image:
  feature: "IMG_20140917_125043.jpg" 
---
![]({{ site.imagehost }}/2014rivermap.png)

It was mid September. The boat was ready enough, so we packed up some food and took off. Some high level facts:

* 26 locks and 626 miles on the Mississippi River
* 8 locks and 328 miles upstream on the Illinois River
* 110 miles across Lake Michigan from Chicago to Muskegon, MI

We spent around half of our nights at anchor and the other half tied up to either free municipal docks and a few marinas. Our longest stay was 7 nights in Chicago waiting for a fall gale to pass, so we could have an easier trip across the lake. 
 

<ul class="post-list">
{% for post in site.categories.2014-River reversed %} 
  <li><article><a href="{{ site.github.url }}{{ post.url }}">{{ post.title }} <span class="entry-date"><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}</time></span>{% if post.excerpt %} <span class="excerpt">{{ post.excerpt | remove: '\[ ... \]' | remove: '\( ... \)' | markdownify | strip_html | strip_newlines | escape_once }}</span>{% endif %}</a></article></li>
{% endfor %}
</ul>













