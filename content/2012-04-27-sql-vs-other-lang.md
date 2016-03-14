Date: 2012-04-27
Title: SQL vs insert_language_here
Tags: SQL, geek
Category: debug
Slug: sql_vs_other_lang

I was chatting online a few days ago about why people use SQL instead of writing regular code in whatever language you use to do data storage, querying and manipulation. It was a fun and long conversation stemming from the fact that the one who started it knew next to nothing about SQL as a language nor did he want to learn.

But this made me think about a good example to show why one would chose SQL instead of reinventing the wheel, and, because I was hungry as hell at that point, this is what I came up with.

Think of it like this. Say I want a pizza, and I have to tell a computer how to make it.

In C#, it would be:

	:::c#
	Flour f = new Flour(FlourType.Wheat);
	Water w = new Water(WaterType.Filtered);
	Yeast y = new Yeast();
	TomatoSauce ts = new TomatoSauce("Ragu");
	Sausage s = new Sausage("pork", Spiciness.Medium);
	Pepperoni p = new Pepperoni();
	CheeseMix cm = new CheeseMix(new {"mozzarella", "cheddar", "parmesan"});

	Mixer m = new Mixer();
	Dough d = m.Mix(f, w, y);
	Knead(d);
	Thread.Sleep(20 * 60 * 1000);
	Roll(d);
	ts.Spread(d);
	c.Apply(d);
	s.Apply(c);
	p.Apply(s);

	using (Oven o = new Oven(400, Degrees.Fahrenheit)){
		o.Bake(d);
		Thread.Sleep(15 * 60 * 1000);
		o.Remove(d);
	}

In SQL the same thing would be described as:

	:::sql
	select
		pizza
		, topping
	from
		Pizzas p
		cross join Toppings t
	where
		t.topping in ('tomato sauce', 'cheese', 'sausage', 'pepperoni')

So, what would you chose? And do you have any other good examples?
