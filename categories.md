---
layout: default
title: Categories
permalink: /categories/
---

## Categories

{% assign categories = site.posts | map: "categories" | flatten | uniq | sort %}

{% for category in categories %}
<h3 id="{{ category | slugify }}">{{ category | capitalize }}</h3>
<ul>
{% for post in site.posts %}
  {% if post.categories contains category %}
  <li><a href="{{ post.url | relative_url }}">{{ post.title }}</a> <span class="lightText">{{ post.date | date: "%B %Y" }}</span></li>
  {% endif %}
{% endfor %}
</ul>
{% endfor %}
