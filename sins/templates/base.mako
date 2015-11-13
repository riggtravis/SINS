<!DOCTYPE html>
<!-- This is boilerplate html that every template will need. -->

<html lang="${request.locale_name}">
	<head>
		<meta charset="utf-8" />
		
		<!-- I'm not entirely clear on what this line of code does -->
		<meta http-equiv="X-UA-Compatible" content="IE=edge" />
		
		<!-- This meta tag must absolutely come after the previous two. -->
		<meta name="viewport" content="width=device-width, initial-scale=1" />
		
		<meta name="description" content="SINS is not SFIM" />
		<meta name="author" content="Travis Rigg" />
		
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
		<!-- Create a navbar -->
		<nav class="navbar navbar-default">
			<div class="container-fluid">
				<!-- The following comment comes from the bootstrap documentation and 
							does not make sense to me. 
				-->
				<!-- Brand and toggle get grouped for better mobile display -->
				<!-- All this means is that when the display is small, both the branding
							and the menu toggle will be visable.
				-->
				<div class="navbar-header">
					<!-- So this navbar-header div seems to make sure that the navbar goes
								at the top of the page and is able to respond to changing sizes
								of screen display.
					-->
					<!-- This button creates the expand/collapse button for the navbar
								when the display is small
					-->
					<button 
						type="button"
						class="navbar-toggle collapse" 
						data-toggle="collapse"
						data-target="#main-nav"
					>
						<!-- This line of code makes it so that people using screen readers
									know about the expand collapse button.
						-->
						<span class="sr-only">Toggle navigation</span>
						
						<!-- These three lines of code create the hamburger icon in the
									button. I'm sure other icons could also be used.
						-->
						<span class="icon-bar"></span>
						<span class="icon-bar"></span>
						<span class="icon-bar"></span>
					</button>
					<!-- This line of code creates the big title for this whole thing. I
								need to seriously consider creating a variable so that users can
								set the names of their forums. That said, this might actually be
								the only place where this branding appears.
					-->
					<!-- It's time to create a logo -->
					<a class="navbar-brand" href="/">SINS</a>
				</div>
				
				<!-- Collect the nav links, forms, and other content for toggling. -->
				<!-- This is the stuff that will appear in the navbar and the menu. -->
				<div class="collapse navbar-collapse" id="main-navbar">
					<!-- Here is where our main navigation links go. I need to consider
								what the main navigational requests will be.
					-->
					<!-- The things that need to be available all the time are: -->
					<!--	make searches -->
					<!-- actually, I should use WTForms for this. -->
					
					<!-- For the following actions it will be necessary to know who a
								user is. I will leave this for later.
					-->
					<!--	view their profile/register -->
					<!--	log in/out -->
				</div>
			</div>
		</nav>
		
		${self.body()}
		<script
			src="https://maxcdn.bootstrap.cdn.com/bootstrap/3.3.5/js/bootstrap.min.js"
			integrity="sha512-K1qjQ+NcF2TYO/eI3M6v8EiNYZfA95pQumfvcVrTHtwQVDG+aHRqLi/ETn2uB+1JqwYqVG3LIvdm9lj6imS/pQ=="
			crossorigin="anonymous"
		>
		</script>
	</body>
</html>