---
layout: default
---

{{ content }}

{% if page.previous.url %}
  <a href="{{ page.previous.url | relative_url }}">Previous: {{ page.previous.title }}]</a>
{% endif %}

{% if page.next.url %}
  <a href="{{ page.next.url | relative_url }}">Next: {{ page.next.title }}</a>
{% endif %}
