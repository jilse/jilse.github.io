---
layout: page
title: From motor boat to sail boat through Lake Michigan and Lake Superior
excerpt: "Sailing from Lake Michigan to Lake Superior"
search_omit: true
image:
  feature: "2015-07-16 14.03.21.jpg"
  
---
![2015 map]({{ site.imagehost }}/2015-map.png "Route")

For the short version, here is a list of legs I sailed from Muskegon MI ultimately to Dulth, MN. Each leg has many special memories and special people I met along the way. Read the posts below for more details.

  1. Whitehall, MI Jeff solo sailing **July, 4**
  2. Pentwater, MI **July, 5**
  3. Frankfort, MI **July, 6**
  4. Good Harbor Bay 
  5. Leland, MI (picked up Heather and Ethan)(marina)
  6. Back to South Manitou Island for some relaxation and island fun
  7. Dropped Heather off in Leland, MI **July, 17**
  8. St. Helana Island Ethan continues with Jeff**July, 18**
  9. Drummand Island **July, 19**
  10. Sault St. Marie (marina) **July, 21** (overnight up the river)
  11. Whitefish point harbor of refuge **July, 23**
  12. Grand Marais, MI **July, 27**
  13. Munising, MI Pictured Rocks National lake shore and Grand Island **July, 28**
  14. Copper Harbor, MI **Aug, 1**
  15. Grand Marais, MN **Aug, 6**
  16. Cruising around Bayfiled and the Apostle Islands National Lakeshore
  17. Duluth, MN
  18. Grand Marais, MN
  19. Isle Royale, MI
  20. Duluth, MN
  21. Lots of day sails until haulout Nov. 5


<ul class="post-list">
{% for post in site.categories.2015-MichiganToMinnesota reversed %} 
  <li><article><a href="{{ site.github.url }}{{ post.url }}">{{ post.title }} <span class="entry-date"><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}</time></span>{% if post.excerpt %} <span class="excerpt">{{ post.excerpt | remove: '\[ ... \]' | remove: '\( ... \)' | markdownify | strip_html | strip_newlines | escape_once }}</span>{% endif %}</a></article></li>
{% endfor %}
</ul>

-----------



