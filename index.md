# CSE 115 JavaScript Exercises

{% for post in site.posts reversed %}
  [{{ post.num }}. {{ post.description }}]({{ post.url | relative_url }})
{% endfor %}
