.PHONY: all

DIST=_dist

all:
	echo "hi."
dist:
	if [ -d "$(DIST)" ];then rm -Rf $(DIST);echo "del: " $(DIST); fi
	rsync --exclude="*~" --exclude="*.swp" --exclude="*.bak" --exclude="*.svn" --exclude="*.git"\
		-rl src/* $(DIST)/
	
clean:
	if [ -d "$(DIST)" ];then rm -rf $(DIST);echo "del: " $(DIST); fi
