---
layout: page
title: Chillin on Lake Superior
excerpt: Taking it slower this summer
search_omit: true
image:
 feature: "2016/2016routemap.png"
---

After some very busy times recently, we decided to stay closer to home go without destinations in mind for the summer. We hopped aboard with some food, there was a strong west wind, so we sailed East and ended up in Grand Marias, MN. We started to make plans to sail back to the SW to meet some family in the Apostle islands, but the west winds never died, so we...went East again and found ourselves in Copper Harbor, MI. It was starting to feel like a circle trip and we hadn't yet been through the portage canal, so it was off to Marquette, MI. We liked it there so much, we just stayed until the wind came around to allowing us to head back towards home. I like not having a plan, because if the wind isn't blowing where you want to go, simply change the destination.

<ul class="post-list">
{% for post in site.categories.2016-LakeSuperior reversed %} 
  <li><article><a href="{{ site.url }}{{ post.url }}">{{ post.title }} <span class="entry-date"><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}</time></span>{% if post.excerpt %} <span class="excerpt">{{ post.excerpt | remove: '\[ ... \]' | remove: '\( ... \)' | markdownify | strip_html | strip_newlines | escape_once }}</span>{% endif %}</a></article></li>
{% endfor %}
</ul>
