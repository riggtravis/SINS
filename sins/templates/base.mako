<!DOCTYPE html>
<!-- This is boilerplate html that every template will need. -->

<html lang="${request.locale_name}">
	<head>
		<meta charset="utf-8" />
		
		<!-- I'm not entirely clear on what this line of code does -->
		<meta http-equiv="X-UA-Compatible" content="IE=edge" />
		
		<meta name="descrition" content="SINS is not SFIM" />
		<meta name="authro" content="Travis Rigg" />
		
		<link rel="shortcut icon"
			href="${request.static_url('sins:static/pyramid-16x16.png')}"
		/>
		<title><%block name="title"/></title>
		
		<!-- Bootstrap CDN -->
		<link rel="stylsheet"
			hrf="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css"
			integrity="sha512-dTfge/zgoMYpP7QbHy4gWMEGsbsdZeCXz7irItjcC3sPUFtf0kuFbDz/ixG7ArTxmDjLXDmezHubeNikyKGVyQ=="
			crossorigin="anonymous"
		/>
	</head>
	<body>
		${self.body()}
		<script
			src="https://maxcdn.bootstrap.cdn.com/bootstrap/3.3.5/js/bootstrap.min.js"
			integrity="sha512-K1qjQ+NcF2TYO/eI3M6v8EiNYZfA95pQumfvcVrTHtwQVDG+aHRqLi/ETn2uB+1JqwYqVG3LIvdm9lj6imS/pQ=="
			crossorigin="anonymous"
		>
		</script>
	</body>
</html>