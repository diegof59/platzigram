
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from posts.forms import PostForm

from .models import Post
# now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
# Posts de ejemplo inicial
"""
posts = [
	{
		'title': 'Cat',
		'user': {
			'name': 'Melissa',
			'profile_pic': '
		},
		'timeStamp': now,
		'photo': 'https://instagram.fclo1-1.fna.fbcdn.net/vp/86127ab438026d540ee5475f021e2789/5C0E868B/t51.2885-15/e35/17076917_1069370833206354_5977160313437421568_n.jpg'
	},
	{
		'title': 'Milky Way',
		'user': {
			'name': 'R. Linn&aacute;s',
			'profile_pic': 'https://revistadiners.com.co/wp-content/uploads/2013/09/1221.jpg'
		},
		'timeStamp': now,
		'photo': 'http://en.es-static.us/upl/2017/04/zodiacal-light-milky-way-Yuri-Beletsky.jpg'
	},
	{
		'title': 'Bass',
		'user': {
			'name': 'Bassist59',
			'profile_pic': 'https://scontent.fclo1-1.fna.fbcdn.net/v/t1.0-9/10410251_939364396082597_2718251335655532159_n.jpg?_nc_cat=0&oh=2eef18478c8d314beff2ec958556b9d6&oe=5C1214DA'
		},
		'timeStamp': now,
		'photo': 'https://i.ytimg.com/vi/QnwT7Pjwv3Y/maxresdefault.jpg'
	},
]
"""

@login_required
def list_posts(request):

	posts = Post.objects.all().order_by('created')

	return render(request, 'posts/feed.html', {'posts': posts})
	
"""
# Escribir el Html mediante un for.
def list_posts(request):

	for post in posts:
		content = []
		content.append(""
				<p><strong>{title}</strong></p>
				<p><small>{name} - <i>{timeStamp}</i></small></p>
				<figure><image src="{photo}"/></figure>			
			"".format(**post)
		)
	return HttpResponse('<br>'.join(content))
"""
@login_required
def create_post(request):

	user = request.user
	profile = user.profile

	if request.method == 'POST':

		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('feed')
	else:
		form = PostForm()

	return render(request, 'posts/create.html',
				  {'user': user, 'profile': profile, 'form': form})