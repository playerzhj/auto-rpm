.PHONY: all

DIST=_dist

all:
	echo "hi."
dist:
	# 拷贝文件到_dist目录中，_dist是打包用的程序目录
	if [ -d "$(DIST)" ];then rm -Rf $(DIST);echo "del: " $(DIST); fi

	# 需要有过滤的同步时一般用rsync
	rsync --exclude="*~" --exclude="*.swp" --exclude="*.bak" --exclude="*.svn" --exclude="*.git"\
		-rl src/{index1.html,index2.html} $(DIST)/

	# 单独文件直接cp
	cp -f src/index3.html $(DIST)/
	
clean:
	if [ -d "$(DIST)" ];then rm -rf $(DIST);echo "del: " $(DIST); fi
