---
layout: default
---

{{ content }}

{% if page.previous.url %}
  [{{ page.previous.url}}](Previous: {{ page.previous.title }})
{% endif %}

{% if page.next.url %}
  [{{ page.next.url}}](Next: {{ page.next.title }})
{% endif %}
