---
layout: default
title: Archives
permalink: /archives/
---

{% assign posts_by_year = site.posts | group_by_exp: "post", "post.date | date: '%Y'" %}

{% for year in posts_by_year %}
## {{ year.name }}

{% for post in year.items %}
- <a href="{{ post.url | relative_url }}">{{ post.title }}</a> <span class="lightText">{{ post.date | date: "%B %-d" }}</span>
{% endfor %}

{% endfor %}
