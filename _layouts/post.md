---
layout: default
---

{{ content }}

{% if page.previous.url %}
  [{{ page.previous.url}}]({{ page.previous.title }})
{% endif %}

{% if page.next.url %}
  [{{ page.next.url}}]({{ page.next.title }})
{% endif %}
