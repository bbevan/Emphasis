# Emphasis
Reads in a plaintext file from the command line. Outputs a randomly emphasized and bolded HTML5 file by adding either 
`<b></b>` or `<i></i>` tags to random words.

## use
`$~ python3 emphasis.py text.txt > emphasized_text.txt`

## Example output
`text.txt`
Slouching away from the twisted sheets no laundered item rested on the chair, or layed neatly folded in oak drawers, or layed dirty on the floor. Beyond comprehension clothing I own had vanished. I wore the pair of jeans slept in, a red hoodie and blue sports coat paired with black slippers out the door late. The heat built-up in Spring. It was humid and I could feel the skipped shower manifesting itself within the aroma of my unwashed clothes. One shoe worn down to the skin. The other talking. Jeans slightly sagged from sweat and the sun shown hard into the corneas of my eyes.

`newtext.html` 
```
<html lang="en"><head>
    <meta charset="utf-8">

    <title>Emphasize.py</title>
    <meta name="description" content="The HTML5 Herald">
    <meta name="author" content="SitePoint">

    <link rel="stylesheet" href="css/styles.css?v=1.0">

    </head>

    <body>
    
Slouching <em>away</em> from <em>the</em> twisted <em>sheets</em> <em>no</em> laundered <em>item</em> <b>rested</b> on the <b>chair,</b> <b>or</b> layed <em>neatly</em> folded in <b>oak</b> drawers, <b>or</b> layed dirty <b>on</b> the <em>floor.</em> Beyond <b>comprehension</b> <b>clothing</b> <em>I</em> <em>own</em> had <em>vanished.</em> <em>I</em> <em>wore</em> the <b>pair</b> of jeans slept in, a red hoodie and <em>blue</em> sports <em>coat</em> <em>paired</em> with <b>black</b> <em>slippers</em> <em>out</em> <em>the</em> <em>door</em> <em>late.</em> The <em>heat</em> <em>built-up</em> <em>in</em> <em>Spring.</em> It was <b>humid</b> <b>and</b> <b>I</b> <b>could</b> feel <em>the</em> skipped shower manifesting <b>itself</b> within <em>the</em> aroma of my unwashed <em>clothes.</em> <em>One</em> shoe <b>worn</b> <b>down</b> to the skin. The <em>other</em> talking. <em>Jeans</em> <b>slightly</b> sagged <b>from</b> sweat and <em>the</em> sun <b>shown</b> <b>hard</b> into <b>the</b> <em>corneas</em> of <b>my</b> <b>eyes.</b>

</body></html>
```

### Rendered
Slouching <em>away</em> from <em>the</em> twisted <em>sheets</em> <em>no</em> laundered <em>item</em> <b>rested</b> on the <b>chair,</b> <b>or</b> layed <em>neatly</em> folded in <b>oak</b> drawers, <b>or</b> layed dirty <b>on</b> the <em>floor.</em> Beyond <b>comprehension</b> <b>clothing</b> <em>I</em> <em>own</em> had <em>vanished.</em> <em>I</em> <em>wore</em> the <b>pair</b> of jeans slept in, a red hoodie and <em>blue</em> sports <em>coat</em> <em>paired</em> with <b>black</b> <em>slippers</em> <em>out</em> <em>the</em> <em>door</em> <em>late.</em> The <em>heat</em> <em>built-up</em> <em>in</em> <em>Spring.</em> It was <b>humid</b> <b>and</b> <b>I</b> <b>could</b> feel <em>the</em> skipped shower manifesting <b>itself</b> within <em>the</em> aroma of my unwashed <em>clothes.</em> <em>One</em> shoe <b>worn</b> <b>down</b> to the skin. The <em>other</em> talking. <em>Jeans</em> <b>slightly</b> sagged <b>from</b> sweat and <em>the</em> sun <b>shown</b> <b>hard</b> into <b>the</b> <em>corneas</em> of <b>my</b> <b>eyes.</b></body></html>

# Note
Firefox does not always render `em` tags without a CSS file.

# Download
Code located at http://github.com/bbevan/Emphasis. Clone the repository with 

```
$:~/Emphasis$ mkdir Emphasis
$:~/Emphasis$ git clone https://github.com/bbevan/Emphasis.git
Cloning into 'Emphasis'...
remote: Enumerating objects: 31, done.
remote: Counting objects: 100% (31/31), done.
remote: Compressing objects: 100% (23/23), done.
remote: Total 31 (delta 10), reused 24 (delta 6), pack-reused 0
Unpacking objects: 100% (31/31), done.

 ```
 
 ..or download the .zip located @ https://github.com/bbevan/Emphasis/archive/master.zip
