---
layout: default
---

{{ content }}

{% if page.previous.url %}
  [Previous: {{ page.previous.title }}]({{ page.previous.url | relative_url }})
{% endif %}

{% if page.next.url %}
  [Next: {{ page.next.title }}]({{ page.next.url | relative_url }})
{% endif %}
