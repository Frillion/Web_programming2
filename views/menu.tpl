<ul>
	<li><a href='/'>{{home}}</a></li>
	% for i in info:
		<li><a href={{info[i]}}>{{i}}</a> : <a href={{info[i]}}>{{info[i]}}</a></li>
	%end
</ul>