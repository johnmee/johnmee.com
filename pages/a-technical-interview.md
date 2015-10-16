title: A Technical Interview
published: 2007-12-23
tag: tech
disqus: http://sydneyboy.com.au/2007/12/the-technical-interview/

> Describes, and solves, the puzzle I was given in a Skype interview for a SFO startup in 2007. 
It was a friend-of-family for an unadvertised position on the other side of the world, so don't
read too much into my performance, but the puzzle was fun.  I'm not such a
fan of this type of thing now and think they're overused and can be gamed&mdash;read
the resum&eacute; and have a chat with the candidate before requesting a test.


# A Technical Interview

I just did a _Technical Interview_ for a San Francisco start up.  This type of interview seems to be 
common in the US when looking for programmers.  Despite being a complete flop at it myself, and this 
is the second time in my life I've been put through such - flopped that one too, I very much appreciate 
the concept.  To make myself feel better I like to think there are very few guys I've worked with (in 
Sydney) who would be able to get this on the spot.  If I could learn how to get through these tests 
then perhaps I'd actually get to work with some people who know what they're doing.

Anyway, after a five minute preamble, the guy (I won't name names as he may be very well known in 
SFO circles) poses a puzzle.  Important lesson to remember when getting this puzzle is: you have 
to solve it.  You might be super bright and solve it in five minutes, or you might not be thinking 
clearly and need an hour.  The interviewer is not going to move on until you actually solve it. 
That was unexpected.  I knew the guy knew a few solutions so I was just kinda phaffing about 
waiting for him to get bored of waiting for me so then he could jump in and show me the answer. 
Any other kind of situation I know this doesn't take long because people are always keen to 
show off how smart they are :)   If/when I get into this situation again I'll have to resign myself 
to doing the groundwork to solving the puzzle.  But in this case, by the time I worked out that he 
wasn't going to jump in and give me the answer I was all ready for the earth to open up and swallow 
me, but I digress...

The puzzle is perhaps a classic, at least it sure smells like a tried and true trick for sorting sheep and goats.

> A tree of nodes.  Each node has a label (eg "A") and some children. Write an iterator "next" such 
that it returns A, B, E, H, O, F, G, H, C, I, J, K, P, Q, D, L, M.  You'll want to create a 
constructor for the iterator.  Each node knows who its parent is.

![Tree of Nodes](/static/images/tech-interview-tree-of-nodes.jpg)

Sounds easy, and probably is.  I couldn't do it.  Still haven't solved it!

I mean I think I can walk the tree to get the right result easily enough like this:

```{.pseudocode}
walk (node) {
   print node;
   foreach child of node
      walk (child);
}
```

But the 'next' node is still out of grasp; perhaps this is where the initializer comes in; to keep state in the 
walk you're on? I was instructed that the tree might be dynamic which ruled out walking the tree 
in the initializer then stepping through that list with each call to next().  The real trick seems 
to lie in finding the next() of Q; ie D via the arbitrarily deep ancestor A.  I went to google and 
found some uni lecture notes which place a stack in the iterator which must be the solution which I 
never came close to finding.


## The Solution


Like a dog to vomit I just kept on coming back to <a href="/p=23">yesterday's puzzle</a>. 
I've finally solved it.  There is absolutely no way I would ever have got this thing out 
during an interview.  It took me three distinct 'lightbulb' moments before I understood 
the solution.


### Ah-ha #1. You need a stack.

```{.java}
public class TheIterator implements Iterator<node> {
	private Stack<iterator <node>> stack = new Stack</iterator><iterator <node>>();

	public TheIterator(Node node) {
	        stack = new Stack</iterator><iterator <node>>();
	        ArrayList<node> list = new ArrayList</node><node>();
	        list.add(node);
	        stack.push(list.iterator());
	}
}
```

To preserve some kind of state inside the iterator use a _stack_.  Digging around some 
university lecture notes <a href="http://www.jezuk.co.uk/files/iteration/slide-23.html">here</a> and <a href="http://www.cs.grinnell.edu/~rebelsky/Courses/CS152/97F/Outlines/outline.41.html">here</a> I discover this is common knowledge to anyone who is familiar with the construction of iterators.  Queues and stacks are the usual tools for keeping track of where you are.

To start things off put the first node into an iterator and push that onto the stack.

### Ah-ha #2. Put iterators on the stack, not nodes

```
stack.push(node.kids.iterator());
```

I can't pretend this possibility occurred to me at the time.  I know it because I do recall 
feeling particularly pained over the question of whether or not the nodes were aware of the 
order of their children.  At the time, this question formed a big grey cloud of confusion 
because here I was building an iterator so wouldn't assuming there's an iterator over the 
children be cheating somehow?

In hindsight this concern was an unnecessary confusion.  The way it was described to me 
there was obviously a sequence amongst the children.  You have to be able get the kids 
some way!  Having an iterater over the kids is not cheating here, just a little more 
convenient. Say the collection was unordered, like in a bag, it doesn't make a much difference 
to the solution: so you push unordered bags onto the stack rather than ordered lists.  
the object on the stack returns that  something you haven't seen before.  The main blocker here 
was that there are two distinct iterators: the single layer one to traverse the children, and 
the multi-layer one we're building to traverse the whole tree.  This is probably a lightbulb in 
itself.

So for this particular solution to the puzzle - as I imagine there are other ways to do it - 
is _not_ to put nodes onto the stack.  Ok, well you probably can, but it doesn't make life 
any easier because you still have the problem of finding the next node.  Knowing where you 
have been is useful but leaves a lot of work yet to get a 'next'.  I'm sure you _could_ 
struggle through and achieve a brute force queue-based solution by putting nodes on the 
stack and digging through them, but it would be probably be ugly.

The magic lightbulb?  Push the ITERATORS onto the stack.

After all we're interested in the next node, not the current one.  Now, with a stack of 
iterators, we're in business!  Want to know the next node?  Well just ask the iterator at 
the top of the stack!

Ok, but we still have problem: what do you do when the iterator at the top of the stack runs out of kids?

### Ah-ha #3. Clean up the stack before you leave

```{.java}
while(!stack.empty() && !stack.peek().hasNext())
    stack.pop();
```

I ran aground on the trailing edge condition repeatedly. Every time I thought it through I'd do a bunch 
of stuff and then find myself with the same problem: digging through an arbitrary number of dead ancestors 
to find the next node.

In the end I cheated. No, not exactly. I just stumbled over 
<a href="http://www.koders.com/java/fidA2A75E8A5DC25A8BB8D3BEC455E5E5A8AD389CFC.aspx">this solution</a> which 
was finished and working which was a vast improvement on what I had at the time.  It uses recursion which 
I always like to see.

But this solution includes a trick which I don't like: calling hasNext() changes the state of the 
iterator.  The hasNext should be <a href="http://en.wikipedia.org/wiki/Idempotent">idempotent</a> which, 
admittedly this is; but it does use side effects in hasNext to make next work.  Tightly coupling these 
routines together strike me as a poor form.

So I reworked it, and discovered a much neater solution anyway.  It doesn't need the recursion!  All it 
does is clean up the stack ready for the next call by running a little while loop to pop spent iterators 
off the stack before returning.  This optimization trims of a whole bunch of code from the solution i'd 
found.  Leaving nothing more than:

```{.java}
// fetch next node from iterator at top of stack
// push iterator for its kids onto the stack
// pop spent iterators off the stack
// now return that 'next' node

public Node next() {
    Node node = stack.peek().next();
    stack.push(node.kids.iterator());
    while(!stack.empty() && !stack.peek().hasNext())
        stack.pop();
    return node;
}
public boolean hasNext() {
        return !stack.empty();
}
```

Ok, it's little inefficient to push empty kids iterators onto the stack only to immediately pop 
them off again, but its so pretty without a conditional there, and i'm well over this thing by now.

Tada. I'm, finally, happy.  I tell you again that I would never-ever-in-a-million-years have solved 
this inside an hour under any conditions ever.  Reason? I'm getting older and duller?  Even as a youngster I don't know that I could have solved this on the spot.  One thing is sure: there is going to be one very bright collection of people in that startup.

My full and final solution is:

```{.java}
import java.lang.Iterable;
import java.util.Iterator;
import java.util.ArrayList;
import java.util.Stack;

public class Puzzle {

	public class TheIterator implements Iterator<node> {
		private Stack&lt;Iterator&lt;Node&gt;&gt; stack = new Stack&lt;Iterator&lt;Node>>();

		public TheIterator(Node node) {
		        stack = new Stack&lt;Iterator&lt;Node>>();
	        	ArrayList&lt;Node> list = new ArrayList&lt;Node>();
		        list.add(node);
		        stack.push(list.iterator());
		}
		public Node next() {
			Node node = stack.peek().next();
			stack.push(node.kids.iterator());
			while(!stack.empty() && !stack.peek().hasNext())
				stack.pop();
			return node;
		}
		public boolean hasNext() {
	        	return !stack.empty();
		}
		public void remove() {}
	}

	public class Node implements Iterable</node><node> {
		public char name;
		public ArrayList</node><node> kids;

		public Node(char name) {
			this.name = name;
			this.kids = new ArrayList</node><node>();
		}

		public Iterator</node><node> iterator() {
			return new TheIterator(this);
		}
	}

	public static void main(String[] args) {

		Puzzle puzzle = new Puzzle();
		Node a = puzzle.new Node('A');
		Node b = puzzle.new Node('B');
		Node c = puzzle.new Node('C');
		Node d = puzzle.new Node('D');
		Node e = puzzle.new Node('E');
		Node f = puzzle.new Node('F');
		Node g = puzzle.new Node('G');
		Node h = puzzle.new Node('H');
		Node i = puzzle.new Node('I');
		Node j = puzzle.new Node('J');
		Node k = puzzle.new Node('K');
		Node l = puzzle.new Node('L');
		Node m = puzzle.new Node('M');
		Node n = puzzle.new Node('N');
		Node o = puzzle.new Node('O');
		Node p = puzzle.new Node('P');
		Node q = puzzle.new Node('Q');
		a.kids.add(b); a.kids.add(c); a.kids.add(d);
		b.kids.add(e); b.kids.add(f); b.kids.add(g); b.kids.add(h);
		c.kids.add(i); c.kids.add(j); c.kids.add(k);
		d.kids.add(l); d.kids.add(m);
		e.kids.add(n); e.kids.add(o);
		k.kids.add(p); k.kids.add(q);

		for( Node node : a) {
			System.out.println(node.name);
		}
	}

}
```
