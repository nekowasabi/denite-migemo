# denite-migemo

Matcher with [migemo](https://www.kaoriya.net/software/cmigemo/) for [Denite.nvim](https://github.com/Shougo/denite.nvim).

## requirement
* cmigemo

* Denite.nvim

## install

### for vim-plug
> Plug 'nekowasabi/denite-migemo'

### for dein
> call dein#add('nekowasabi/denite-migemo')

## setting
By default, cmigemo's dict path is set **/usr/share/migemo/utf-8/migemo-dict**.

If you want to change dict path, setting like this.

> call denite#custom#filter('matcher/migemo', 'dict_path', '/usr/local/share/migemo/utf-8/migemo-dict')

## usage
Set matcher like this.

> call denite#custom#source('line', 'matchers', ['matcher/migemo'])
