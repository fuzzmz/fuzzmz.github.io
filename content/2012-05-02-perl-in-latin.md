Date: 2012-05-02
Title: Meum Perlum equum
Tags: perl, latin, geek
Category: debug
Slug: perl_in_latin

I'm not one of the fans of Perl and would chose Python over it every day of the week, but I still have to admit that it has some really fun things built around it.

So, you know how, in order to have a good programming language, you need to have a good lexical structure. Most programming languages are based on English, which, let's be honest here, isn't the most consistent language out there when it comes to grammar and structure. This would also mean that programming languages based on English could be improved if they were based on some other language, right?

Well, someone though about that and decided to write a module that makes it possible to write Perl programs in Latin. You can find the module and the reasoning behind it [here](http://www.csse.monash.edu.au/~damian/papers/HTML/Perligata.html).

Just for fun, here's the code for the [sieve of Eratosthenes](http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) (sic, it's a Greek mathematical algorithm for finding all the prime numbers up to a given limit.)

	:::perl
	use Lingua::Romana::Perligata;
	maximum inquementum tum biguttam egresso scribe.
	meo maximo vestibulo perlegamentum da.
	da duo tum maximum conscribementa meis listis.
	dum listis decapitamentum damentum nexto
		fac sic
			nextum tum novumversum scribe egresso.
			lista sic hoc recidementum nextum cis vannementa da listis.
		cis.

Believe it or not that is absolutely grammatically correct Latin.
