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
	ghp-import -n -b master -m ${TRAVIS_COMMIT_DESCRIPTION} $(OUTPUTDIR)
	@git push -fq https://${GH_TOKEN}@github.com/fuzzmz/fuzzmz.github.io.git master > /dev/null