# Git info & rules

## Table of contents:
- **[Git structure](#structure)**
    - [Branching](#branching)
    - [Merging](#merging)
    - [Hotfixes](#hotfix)
- **[Commit practises](#commit-practises)**
- **[Links](#links)**
</br>
</br>
</br>

### <a id="structure"></a>Git structure:

**<a id="branching"></a>Branching:**</br>
 `Feature branch` are merged into `development` once singular application partition feature is ready.
 Each sprint `branches` TTL is translated into two weeks. 


**<a id="merging"></a>Merging:**</br>
Only production ready stuff into `master` and after customer review `merge` into `master` which causes into new `release`.</br> Keeping track on changes actively done within `development` is good thing to keep in mind.</br> By doingthis way it helps to fix `merge conflicts` properly but inviduals can always ask student fellow to be sure about to get right changes into conflict resolving commit.  

**<a id="hotfix"></a>Hotfixes:**</br>
A case where customer notices faults or has extra needs for changes after `pull request` review there is needed `hotfix branch` or using just `dev branch` to fix those.</br> New minor `release` is done into `master` after fixes & problems are resolved.  
</br>
</br>
****

### <a id="commit-practises"></a>Commit practises:</br>
Overall practise goal is be 
enough clear with `commit` messages (examples on 1st article inside links).</br>
Also second thing is avoiding adding too much content inside one commit and being enough specific with commit messages.
</br>
</br> 
****


### <a id="links"></a>Links:
https://chris.beams.io/posts/git-commit/  
https://nvie.com/posts/a-successful-git-branching-model/
https://github.com/mruonavaara/hh-git-opas.github.io/blob/master/README.md#commitin-muuttaminen