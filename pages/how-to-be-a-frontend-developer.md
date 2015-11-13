title: Frontend Development Primer
published: 2015-11-13
tag: technical
disqus: http://johnmee.com/frontend-development-primer


# Frontend Development Primer

> Runs through some basics of the Frontend Developer role, their tools, skills, and resources&mdash;I spent a little time recently 
 being schooled by a Frontend Developer and learned a few things which
 might be useful to my future self and others.


__Frontend Development__ is a technical position filling the gap in the software development cycle between the
 *designer* and the *backend programmer*.  It converts a design, typically a photoshop or illustrator file,
 into static HTML, CSS, and Javascript files and images.  
 
 This is relatively new specialisation which fills a longstanding gray zone whereby programmers would be 
 told a creative will give them a design to work from&mdash;but there would be no
 specification exactly what form that design would come in.  Worst case it would be a low-resolution jpeg. More
 often a Photoshop PSD.  If you were lucky,
 a talented designer would provide beautifully handcoded HTML/CSS/JS ready for all the chopping and changing that
 a backend developer needs to do to add all the function and features which the salesman promised was trivial, 
 easy, and cheap to do.

 And, if you're unlucky it would be a machine-generated HTML/CSS&mdash;perhaps worse than the jpeg because
 they think they've made it easy for the programmer, but have actually made it harder.
 
 It is a rare talent who 
 is creative enough to put colors and shapes together aesthetically, as well as turn it into pleasing code.
 So, enter the frontend developer: the role in whom beautiful creatives and nerdy programmers might meet.

 <small>The same label/role can be used in app development.</small>

## CSS Compiler

Whilst frontend developers can still code vanilla [CSS], tools 
like [LESS] and [SASS] add so much flexibility, reuseability, and programmability
that picking one of them is now the first port of call.

I have used both Less and SCSS, and my preference for one over the other is driven by inconveniences of the environment
rather than the feature comparison or their language structure.  I suppose I lean toward Sass, but have happily used Less 
when Ruby is not convenient or available.

An auto-compiler is, almost, an essential tool.

## LiveReload

Meanwhile the auto-refresh is also, almost, an essential tool. 
Fundamentally these two auto-thingys do nothing greater than save you brainless keystrokes; but it's just so many 
keystrokes that if you show me someone who doesn't use one, I can show you someone who has _never_ used one.

Packaged solutions like [Codekit] and [Prepros] will get you off the ground immediately. But if you're 
<del>cheap</del> <ins>purist</ins>
enough you can certainly accomplish the same tasks with [Gulp] or [Grunt] coupled with [Node], [Ruby] and/or [Python].
For example, right now I'm not using Sass, but I have [Livereload] hitting the refresh button for me on every save.

## Grids, Resets, and Frameworks

Responsive design is the order of the day as more and more people are using the web with more and more varied
devices.  To take some of the tedium, glitches, complexity, and repetition out of getting design elements to
adapt to varying screen sizes and browser implementations an HTML grid framework makes for an important starting
slate.  They try to condense all the tricks that overcome the quirks and annoyances of the myriad platforms
you need to serve into a single reuseable launchpad.

But which one?! There are so many options it will make you dizzy. Some are minimalist and others are
 comprehensive.  Some offer widgets and gadgets in a uniform style.  Some offer widgets and gadgets in a wholly
 customisable style.  Some vehenemently refuse to do gadgets, others promise "coming soon".
 
These are the few that I've actually used. Google around as there are many, many more:

[Bootstrap]: The runaway most popular and includes a full complement of components and features  
[Foundation]: I liked the design but found it a lot of work to get up and going with    
[Skeleton]: Really plain and simple.  I'm using it here  
[Bourbon]: Simple starting point with layer-on frills in the form of Neat, Bitters, and Refill templates  
[SemanticUI]: Loved the concept and really wanted to use it but&mdash;at the time&mdash;not being familiar
with node and gulp made the learning curve too steep for the time available  

Pick one, set up your compiler/reload tools, and you're ready to write HTML/CSS/JS.

Congratulations, you're now a frontend developer!

Now you have to actually do some work adding html tags and attaching css styles. Which is essentially all
you have to do. You will have to fiddle around with javascript to make fancy things work, or some will get away
 with fake-it-till-you-make-it for that part.  
 
The big bucks go to guys who have a system and have 
such a weight of ongoing experience that they've discovered all the typical problems, and their
solutions or workarounds.  So they're fast and predictable.  Basic credit accumulates if you have good javascript 
 skills, know your way around photoshop, and/or are familiar with source control. Guru's
 assert themselves by bleeding their skills into the designers and programmer's turf; able to dive in and out of
 those roles as well.

---

## Fonts

It was a long time coming and a major source of frustration between designers and developers as the
perfect font could not be rendered reliably across platforms.  Fortunately
this problem is now mostly solved, the only remaining issue being price; fonts are not always free.

Hopefully the designer told you the fonts, or you can work out how to find the names of them in Photoshop.
(select the layer->text tool->right click?).  If you're on the Adobe KoolAid [Typekit] is probably your
first port of call.  I found the fastest solution was to look for a CDN version publically available and just
link to it. Done. Next.

This loads the font from google's CDN:

```{.html}
<link rel="stylesheet" href="//fonts.googleapis.com/css?family=Raleway:400,300,600" type="text/css" />
```

Thence we can assign it to various parts of the document:

```{.css}
.pretty { font-family: 'Raleway', Sans; }
```

[GoogleFonts] is the competition. With a great value proposition: free.  
[FontSquirrel] is also a popular destination.

## Margin Alignments

Straight lines make clean designs.  Everything needs to line up just... so.  A bad
frontend designer needs to spend a lot of time working out how to get all the text on the page
to hit their margins, yet still have backgrounds, and background colors, run free.  I can't 
pretend to actually know anything about this myself, except that it is important, and a little tricky,
and class 101 to be a frontend dev.

What I can suggest is that `auto` is more useful than it has ever been.

```{.html}
<div class="backcolor">
	<div class="margin">
		Lorem was a bear. Whatever lorem wanted, lorem got. But who was this lorem bear inside? What really made it tick?
	</div>
	<div class="margin-deep">
This was the question that really confronted Billy.	What makes a bear really bearable&mdash;in the grand scheme of things&mdash;but is more interesting than unintelligible latin!
	</div>
</div>
```
```{.scss}
/* use variables */
$gutterline: solid 1px black;
$outer-margin: 2em;
$inner-margin: $outer-margin + 1em;

.backcolor {
	background-color: lightblue;
}
.margin {
	margin: auto $outer-margin;
	padding: 0 0.5em;
	border-left: $gutterline;
	border-right: $gutterline;
	background-color: lightyellow;
}
/* reuse and layer up definitions */
.margin-deep {
	@extend .margin;
	padding: 1em 2em;
	text-align: justify;
	background-color: white;	
}
```

![page alignments](/static/images/page-alignments.png)

## Media Queries

*Responsive* is supposed to look good at any size, on any device.  There is a lot of serious **"fun"** involved
in getting that to happen.  And media queries are where it all goes on.  This needs to be second nature.
For example, one look at the above from a phone and you'll realize the outer margin is hogging valuable real estate.
It needs to disappear&hellip;

```{.css}
@media (max-width: 30em) {
  .margin { margin: 0; }
}
```

![narrow page alignment](/static/images/page-alignments-narrow.png)

[CSS Media Queries](http://cssmediaqueries.com/) might be a useful resource.


## Backgrounds

Background images have long been popular and are never going away, so a deep understanding will not hurt.

For example, exactly how long since I've done this kind of thing was completely exposed by my ignorance of
the new (CSS3) attribute `background-size`.  The `cover` option makes it easy to stick a background on a 
box and ensure it adapts to various sizes.  Or perhaps better is to use `object-fit`?

```{.html}
<div class="outer">
    <div class="inner">
        <div class="text">
            <h1>Hello World</h1>
            <p>Here's that dang-doodle lorem again.</p>
        </div>
    </div>
</div>
```

```{.css}
.outer {
	background: url(https://upload.wikimedia.org/wikipedia/commons/0/0b/First_passenger_train_over_Sydney_Harbour_Brisge.jpg) no-repeat center center;
	object-fit: cover;
}
.text {
	color: black;
	text-align: center;
    padding: 2em 0;
}
```

![Background Image Illegible text](/static/images/background-image-illegible-text.png)

No matter how I resize the container, the image remains fairly centered, which is prettier than reducing
to a corner of blank sky.

<small>Image <a href="http://creativecommons.org/licenses/by/2.0">CC BY 2.0</a> or Public domain <a href="https://commons.wikimedia.org/wiki/File%3AFirst_passenger_train_over_Sydney_Harbour_Brisge.jpg">via Wikimedia Commons</a></small>

## Tinted Overlay

But the problem with using a photo as a background is that it can make the text hard to read. Some parts of the image
contrast the text color, but others match it, making it illegible.

A solution is to wrap the box in another which is a semi-transparent pane of color, effectively putting
a tint over the image, then putting the text on top of them both so that it is not tinted.

```{.css}
.inner { background-color: rgba(255,255,255,0.7); }
```

![Background Image legible text](/static/images/background-image-legible-black.png)

Or if you prefer white on black:
```{.css}
.inner { background-color: rgba(60,60,60, 0.7); }
```

![Background Image legible text](/static/images/background-image-legible-white.png)


Now the black text on top of a black and white image is somewhat legible again. You can fiddle around with
the opacity and filter color endlessly to drag out your agony over what is the best result.


## Horizontal and Vertical Alignment

You'd think horizontal alignment would be a cinch, but great designers have a knack for making complex things
look really simple. That's what makes them great.  It also makes life hell for frontend devs.

Take a simple masthead with a logo on the left and login button on the right.

![horizontal alignments](/static/images/horizontal-alignments.png)

Things to consider are:

* the logo needs to scale and maintain perspective as size changes
* the button needs to stay in the center of it's space&mdash;both vertically and horizontally
* the text of the button also needs to remain centered relative to it's borders

The values to juggle can engage all of `display`, `float`, `text-align`, `vertical-align`, `width`, and `height`
in various contortions and in conjunction with your prefered grid framework.

I'll come back and expand an example, just as soon as I can make sense of all the balancing acts myself.


## Photoshop

Some basic manouveurs in Photoshop don't go astray.
Especially how to:

* determine the name of the font of some text
* determine the exact color of a pixel, border, text, or background
* resize, optimize, and save images


## Parallax

Design is fashion and [parallax effects](https://ihatetomatoes.net/demos/parallax-scroll-effect/) are currently fasionable.
It's the thing where you continuously scroll down and the background changes, giving you the sense of having
turned the page, although you haven't really.
Learn the word `Parallax` and what it means so you don't have to pretend you know what they're talking
about then rush off to look it up.

## Sliders

Another fashion, now in its twilight.  There are gazzilions out there, and I've lost the links to the ones suggested
to me.  If I stumble across them again I'll post here.

## In Conclusion

A Frontend developer is a very specialized role; one that spends a lot of time scouring websites for how to do
stuff initially, and ultimately graduates into finding funky new ways to push the limits of what is currently
possible and so create your own trend.  The field is a moving target as new features are introduced to browsers
and new devices create new issues.

But hopefully this article gives you an overview of where to start and what you'll be dealing with.

[Alistapart]: Is perhaps where it all started  
[CSSTricks]: Will saturate your search results  
[StackOverflow](http://stackoverflow.com/questions/tagged/css): Can be pretty helpful if you can work out how to search for or define your problem  
[MozillaCSS]: Is well laid out documentation (the moz specific features are well identifiable)  
[W3C](http://www.w3.org/standards/webdesign/htmlcss): The authoritative source of the standards  

May all your layouts be beautiful.


[CSS]: http://www.w3.org/Style/CSS/ "CSS"
[LESS]: http://lesscss.org/
[SASS]: http://sass-lang.com/
[Prepros]: https://prepros.io
[Codekit]: https://incident57.com/codekit/
[Gulp]: http://gulpjs.com/
[Grunt]: http://gruntjs.com/
[Ruby]: https://www.ruby-lang.org/en/
[Python]: https://www.python.org/
[Node]: https://nodejs.org/
[Livereload]: https://pypi.python.org/pypi/livereload
[Bootstrap]: http://getbootstrap.com/
[Foundation]: http://foundation.zurb.com/
[Skeleton]: http://getskeleton.com/
[Bourbon]: http://bourbon.io/
[Typekit]: https://typekit.com/fonts
[GoogleFonts]: https://www.google.com/fonts
[FontSquirrel]: http://www.fontsquirrel.com/
[SemanticUI]: http://semantic-ui.com/
[MozillaCSS]: https://developer.mozilla.org/en-US/docs/Web/CSS
[CSSTricks]: https://css-tricks.com/
[AListApart]: http://alistapart.com/


