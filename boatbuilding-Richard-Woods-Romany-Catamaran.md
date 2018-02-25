---
layout: page
title: building Richard Woods Romany Catamaran
excerpt: "a long history of an insane project...that turned out ok."
search_omit: true
image:
  feature: "DSC_3073.jpg"
---
Just the facts: I received the first shipment of materials August 2007 and launched September 3, 2014. I worked on the boat about 2/3 of the year when the weather was warm enough. During that time I also had a full time job, a son who aged from 6-13, and a wife who supported my crazy dreams. I estimate that I averaged 30+ hours per week building during those months of the year. I built the hulls inside my Uncle's shop in Finland, MN and the rest of the smaller parts in my garage in Minneapolis. Fully assembled, the boat is 20' wide and difficult to trailer on the roads, so in September of 2011, I moved the hulls, cabin, and lots of other bits to Watergate Marina in St. Paul (5 miles from my Minneapolis home) to put it all together where Meadowhawk was ultimately launched in the Mississippi river.

I'm writing this after some time has passed and I've lived aboard 5 months over 2 seasons and I'm pretty sure building was a good experience. I joke that it was a terrible idea and in some ways it probably was, but those wonderful 5 months have softened my attitude. The two things I walked away with: The boat is more than I ever hoped for and while I still have **much** to learn, I have developed more skills and knowledge than I hoped for.

Maybe this is true of all boats, but it seems home built boats are never "done". I have many ideas to improve the space, sail handling, and just finish little things left undone, but this spring (2016) will be the shortest project list I've ever dealt with, so that's a good thing. More sailing and less not sailing.

--------------------------------
**Building Stages**
<ul class="post-list">
{% for post in site.categories.boatbuilding reversed %} 
  <li><article><a href="{{ site.url }}{{ post.url }}">{{ post.title }} <span class="entry-date"><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}</time></span>{% if post.excerpt %} <span class="excerpt">{{ post.excerpt | remove: '\[ ... \]' | remove: '\( ... \)' | markdownify | strip_html | strip_newlines | escape_once }}</span>{% endif %}</a></article></li>
{% endfor %}
</ul>
