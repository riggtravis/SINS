<!-- Step one. Fetch the base template. -->
<%inherit file="base.mako"/>

<!-- Step two. Set the title. -->
<%block name="title">
  ${action} topic
</%block>

<!-- Step three. Create a human readable heading -->
<h1>${action} topic</h1>

<!-- Step four. Create the form. -->
<form action="${request.route_url('')}"