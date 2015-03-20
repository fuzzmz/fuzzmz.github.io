PELICAN=pelican

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

publish:
	$(PELICAN) $(INPUTDIR) --debug --output $(OUTPUTDIR) --settings $(CONFFILE)

github:
	cd $(OUTPUTDIR)
	git init
	git add .
	git commit -m "New blog post"
	git push -fq https://e4b434af975e4f9833cf1e8866029d11302aedfd@github.com/fuzzmz/fuzzmz.github.io.git master