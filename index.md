# CSE 115 JavaScript Exercises

{% for post in site.posts %}
  [{{ post.num }}. {{ post.description }}]({{ post.url | relative_url }})
{% endfor %}
