---
layout: default
title: Archives
permalink: /archives/
---
{% assign posts_sorted = site.posts | sort: "date" | reverse %}
{% for post in posts_sorted %}
- <a href="{{ post.url | relative_url }}">{{ post.title }}</a> <span class="lightText">{{ post.date | date: "%B %-d, %Y" }}</span>
{% endfor %}
