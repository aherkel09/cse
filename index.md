# CSE 115 JavaScript Exercises

{% for post in site.posts %}
  [{{ post.description }}](cse/{{ post.url }})
{% endfor %}
