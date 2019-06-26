---
layout: default
---

{{ content }}

<div style="display:flex;justify-content:space-between;">
  {% if page.previous.url %}
    <a href="{{ page.previous.url | relative_url }}">Previous: {{ page.previous.title }}</a>
  {% endif %}

  {% if page.next.url %}
    <a href="{{ page.next.url | relative_url }}">Next: {{ page.next.title }}</a>
  {% endif %}
</div>
