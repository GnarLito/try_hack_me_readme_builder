
# THM readme builder

Auto create README.md files for Try Hack Me rooms.


### Installation
```bash
  git clone https://github.com/GnarLito/try_hack_me_readme_builder.git
  pip install -r requirements.txt
```


### Usage
```bash
THM_md_builder.py 
  -r <room name (from url)> 
  [ -o <output file path/name> ]
  [ -s <connect-sid cookie> (only needed to auto fill in the answers) ]
  [ -a (dont auto fill in answers) ]
```


### Example
```bash
THM_md_builder.py -r introduction -o readme.md -s {thm:cookie:connect-sid}
```


### config
The markdown layout is also customizable, for more info: [config.md](./config.md)

If u find any room that didnt turn out great, feel free to make an issue for it.
Also feel free to edit/improve the script and create a pull request afterward!
