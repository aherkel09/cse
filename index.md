# CSE 115 JavaScript Exercises

{% for post in site.posts reversed %}
  [Day {{ post.day }} - Exercise {{ post.num }}: {{ post.description }}]({{ post.url | relative_url }})
{% endfor %}
