title: Frontend Development Primer
published: 2015-11-13
tag: technical
disqus: http://johnmee.com/frontend-development-primer


# Frontend Development Primer

> Runs through some basics of the Frontend Developer role: their tools, skills, and resources&mdash;I spent a little time recently 
 being schooled by a Frontend Developer and learned a few things which demonstrated the world never stops changing:
 CSS3 has arrived.


__Frontend Developer__ is a technical job which fills the gap between the
 *graphic designer* and the *web developer*.  They convert a design, typically a photoshop or illustrator file,
 into static HTML, CSS, Javascript files and images.  
 
 It is specialisation which fills a longstanding gray zone whereby programmers are 
 told a creative will give them a design to work from&mdash;but the deal makers fail to
 describe the format of that design: a low-resolution jpeg? a Photoshop PSD? or HTML/CSS perhaps?
 
 If lucky,
 a talented designer would deliver beautifully handcoded HTML/CSS/JS; ready for the chop and change that
 a backend developer needs to do to give it all the function and features the salesman has promised.

If unlucky, the programmer gets a machine-generated HTML/CSS&mdash;which is perhaps the worst: because
 they think they've done you a favour but have actually made it hardest.
 
 It is a rare talent, creative enough, to put colors and shapes together aesthetically, yet delivers it as pleasing code.
 Such a person is both rare and expensive.
 Thus enters the frontend developer: a role through whom the beautiful creatives and nerdy programmers can meet.

 <small><sup>*</sup> The same label/role can be used in app development.</small>

## CSS Compiler

Whilst frontend developers *can* still code vanilla [CSS], tools&mdash;
like [LESS] and [SASS]&mdash;add so much flexibility, reuseability, and programmability
that picking one, or the other, is now the first port of call.

I have used both [LESS] and [SASS], and my preference is driven by inconveniences of the environment,
rather than the feature comparison, or their language structure.  I suppose I lean toward Sass, but have happily used Less 
when Ruby is not convenient or unavailable.

An auto-compiler is (almost) an essential tool. More on that now&hellip;

## LiveReload

The auto-refresh is also (almost) an essential tool. 
Fundamentally these two auto-thingys do nothing greater than save you mindless keystrokes (and/or RSI).
It's the sheer volume of keystrokes saved that if you show me someone who doesn't use one, I can show you someone who has _never_ used one.

Packaged solutions like [Codekit] and [Prepros] will get you off the ground immediately. But if you're 
<del>cheap</del> <ins>a purist</ins>
you can certainly accomplish the same tasks, for free, with [Gulp] or [Grunt] coupled with [Node] or [Ruby] or [Python].
For example, right now I have python's [Livereload] hitting the refresh button for me on every save&mdash;and I can't live without it.
Frontend work involves _a lot_ of try, and retry, and try again!

## Grids, Resets, and Frameworks

Responsive design is the order of the day, as more and more people are using the web with more and more varied
devices.  An HTML grid framework makes for an important starting
slate: they tackle some of the complexity, glitches, tedium, and repetition involved in ensuring design elements render
sensibly on all screen sizes and browsers. They condense the tricks, that overcome the quirks and annoyances of the myriad platforms
you need to serve, into a single reuseable launchpad.

But which one?! There are so many alternatives it will make you dizzy: some are minimalist whilst others are
 comprehensive; some offer widgets and gadgets in a uniform style whilst some offer widgets and gadgets in a 
 maximum flexibility style; some vehenemently refuse to do gadgets whilst others promise "coming soon".
 
These are the few that I've actually used. A quick search will find you many, many more:

[Bootstrap]: The most popular&mdash;includes a full complement of components and features&mdash;pretty good, but 
so popular that the tide of complaints is rolling in that now everyone looks the same  
[Foundation]: I liked the design but found it painful work to get up and going with    
[Skeleton]: Really plain and simple.  I'm using it here  
[Bourbon]: Simple starting point with _level-up_ frills in the form of Neat, Bitters, and Refill templates. Might switch to this soon?  
[SemanticUI]: Loved the concept and really wanted to use it but&mdash;at the time not being familiar
with node and gulp&mdash;found the learning curve too steep in the time available  

Pick something, set up your compiler/reload tools, and you're ready to write HTML/CSS/JS.

Congratulations, you're a frontend developer.

Now you have some actual work to do constructing html and attaching css styles. Essentially that is all
you have to do. But don't underestimate the task!

Ok, so the _big bucks_ go to guys who have such a weight of ongoing experience, that they've discovered all the typical problems&mdash;and the
solutions, or workarounds.  So they're fast and time predictable. A thorough knowledge of CSS, and it's primary
resources and community, are your bread and butter.
 Knowing your way around photoshop, being competant 
with source control, having some javascript ability, all contribute toward your guru status.  And real Guru's
 assert themselves by overlapping their ability deep into the designers and programmer's turf; able to dive in, and out, of
 those roles as the need waxes and wanes.

---

## Fonts

It was a long time coming, and a major source of frustration between designers and developers, as the
perfect font could never be rendered reliably across platforms.  Fortunately
this problem is now mostly solved, the only remaining issue being price; fonts are not (always) free.

Hopefully the designer told you the fonts, or you can work out how to find the names of them in Photoshop.
(select the layer->text tool->right click?).  If you're on the [Adobe KoolAid](https://en.wikipedia.org/wiki/Drinking_the_Kool-Aid),
 [Typekit] is probably your
first port of call.  I found the fastest solution was to search for a CDN version publically available and just
link to it. Done. Next.

This loads a font from google's CDN:

```{.html}
<link rel="stylesheet" href="//fonts.googleapis.com/css?family=Raleway:400,300,600" type="text/css" />
```

Thus we can use it in various parts of the document:

```{.css}
.pretty { font-family: 'Raleway', Sans; }
```

[Typekit] is only useful if you know someone with an Adobe subscription  
[GoogleFonts] is the competition. With a great value proposition: free!  
[FontSquirrel] is also a popular destination  

## Margin Alignments

Straight lines make clean designs.  Everything needs to line up just...so.  

A lesser frontend designer needs to spend a lot of time ensuring all the text on the page
to hits their margins, yet still have backgrounds and background colors running free.  I can't 
pretend to actually know anything about this myself, except that it is important, and occasionally tricksy,
and _Class 101_ of being a frontend dev.

What I can suggest is that `auto` is more useful than it has ever been.

```{.scsshl_lines="10"}
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

For example, exactly how long since I've done this, was completely exposed by my ignorance of
the new (CSS3) attribute `background-size`.  The `cover` option makes it easy to stick a background on a 
box and ensure it adapts to various sizes.  <small>(Or perhaps better is to use `object-fit`?)</small>

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

No matter how I resize the container, the image remains centered, which is often better than reducing
to a top-left corner consisting of empty sky.

<small>Image <a href="http://creativecommons.org/licenses/by/2.0">CC BY 2.0</a> or Public domain <a href="https://commons.wikimedia.org/wiki/File%3AFirst_passenger_train_over_Sydney_Harbour_Brisge.jpg">via Wikimedia Commons</a></small>

## Tinted Overlay

But the problem with using a photo as a background is that it can make the text hard to read: some parts of the image
contrast the text color whilst others match it, making it illegible.

A solution is to wrap the box in another which is a semi-transparent pane of color, effectively putting
a tint over the image, then putting the text on top of them both so that the image, but not the text, is tinted.

```{.css}
.inner { background-color: rgba(255,255,255,0.7); }
```

![Background Image legible text](/static/images/background-image-legible-black.png)

Or if you prefer white on black:
```{.css}
.inner { background-color: rgba(60,60,60, 0.7); }
```

![Background Image legible text](/static/images/background-image-legible-white.png)


Obviously I flipped the text `color` as well.  But you can fiddle around with
the opacity and filter color endlessly to drag out your agony deciding on the best result.


## Horizontal and Vertical Alignment

You'd think horizontal alignment would be a cinch, but great designers have a knack for making complex things
look really simple. That's what makes them great.  It also makes life hell for frontend devs.

Take a simple masthead with a logo on the left and login button on the right.

![horizontal alignments](/static/images/horizontal-alignments.png)

Things to consider are:

* the logo needs to scale and maintain perspective as size changes
* the button needs to stay in the center of it's space&mdash;both vertically and horizontally
* the text of the button also needs to remain centered relative to it's borders

The values to juggle can engage all of `display` (and it's plethora of values), `float`, `text-align`, `vertical-align`, `width`, and `height`
in various contortions and in conjunction with your prefered grid framework.

I'll come back and expand an example, just as soon as I can make sense of all these balancing acts myself!


## Photoshop

Some basic manouveurs in Photoshop don't go astray.
Especially how to:

* determine the name of the font of some text
* determine the exact color of a pixel, border, text, or background
* resize, optimize, and save images


## Parallax

Design is fashion and [parallax effects](https://ihatetomatoes.net/demos/parallax-scroll-effect/) are currently fashionable.
That's the thing where you continuously scroll down and the background changes, giving you the sense of having
turned the page, although you haven't really.
Learn the word `Parallax`, and what it means, so you don't have to pretend you know what they're talking
about then rush off to look it up.

## Sliders

Another fashion, now in its twilight.  There are gazzilions out there, and I've lost the links to the ones suggested
to me.  If I stumble across them again I'll post here.

## In Conclusion

A Frontend developer is a specialized role.  One that spends a lot of time scouring websites for how to do
stuff initially, and ultimately graduates into finding funky new ways to push the limits of what is currently
possible&mdash;and so create your own fashion.  The field is a moving target as new fashions are added to browsers
and new devices create new issues.

But hopefully this article gives you an overview of where to start and what you'll be dealing with.

[Alistapart]: Is where it all started  
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
