  {% extends 'markdown.tpl' %}</p>
<p><!-- Add Div for input area -->
  {% block input %}
{{'{% code-tabs %}
{% code-tabs-item title="In:" %}'}}
{{ super() }}
{{'{% endcode-tabs-item %}
{% endcode-tabs %}'}}
  {% endblock input %}
</p>

<p><!-- Remove indentations for output text and add div classes  -->
  {% block output %}
  {% if 'text/latex' not in output.data %}
<p>
{{ super() }}
</p>
  {% else %}
{{ super() }}
  {% endif %}
  {% endblock output %}
</p>

<p>{% block traceback_line  %}
  {:.output_traceback_line}</p>

<pre><code>  {{ line | strip_ansi }}</code></pre>
<p>{% endblock traceback_line  %}</p>
<p><!-- Tell Jekyll not to render HTML output blocks as markdown -->
  {% block data_html %}
  <div markdown="0">
  {{ output.data['text/html'] }}
  </div>
  {% endblock data_html %}