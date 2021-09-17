
# THM readme builder

Auto create README.md file for Try Hack Me rooms.

```
Usage: THM_md_builder.py 
  -r <room name (from url)> 
  -o <output file path/name> 
  [-s <connect-sid cookie> (only needed for auto fill of the README.md) ]
  [-a (dont auto fill in answers)]
```
Note:
  The connect.sid cookie from THM is a static cookie which is not session based (as far as i know).

If u find any room that doesn't look good, feel free to make an issue for it.

Feel free to edit/improve the script and create a pull request afterward!
