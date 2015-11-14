<!-- Step one. Bring in the base view. -->
<%inherit file="base.mako"/>

<!-- Step two. Set the title. -->
<%block name="title">
  ${status}
</%block>

<!-- Step three. Deliver the message to the user if they have logged out. -->
<div class="alert alert-success" role="alert">
	${message}
</div>

<!-- Step four. Create a form that can be used for logging in. -->
<!-- This is another place where WTForms come into play. -->