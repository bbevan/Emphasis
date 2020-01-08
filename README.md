# Emphasis
Reads in a plaintext file from the command line. Outputs a randomly emphasized and italicized HTML5 file by adding either 
`<em></em>` or `<i></i>` tags to random words.

## use
`$~ python3 emphasis.py text.txt > emphasized_text.txt`

## Example output
`text.txt`
Slouching away from the twisted sheets no laundered item rested on the chair, or layed neatly folded in oak drawers, or layed dirty on the floor. Beyond comprehension clothing I own had vanished. I wore the pair of jeans slept in, a red hoodie and blue sports coat paired with black slippers out the door late. The heat built-up in Spring. It was humid and I could feel the skipped shower manifesting itself within the aroma of my unwashed clothes. One shoe worn down to the skin. The other talking. Jeans slightly sagged from sweat and the sun shown hard into the corneas of my eyes.

`newtext.html`
`<html><body>
<i>Slouching</i> away from the twisted <em>sheets</em> no laundered <i>item</i> rested <i>on</i> <em>the</em> chair, <em>or</em> layed neatly folded <i>in</i> oak <em>drawers,</em> or <i>layed</i> <i>dirty</i> on the floor. <em>Beyond</em> comprehension <em>clothing</em> <em>I</em> <i>own</i> <em>had</em> <i>vanished.</i> <i>I</i> wore the pair <em>of</em> <em>jeans</em> <em>slept</em> in, <i>a</i> <em>red</em> hoodie <i>and</i> <i>blue</i> <em>sports</em> coat paired with black slippers out <i>the</i> <em>door</em> <em>late.</em> <em>The</em> <em>heat</em> built-up <em>in</em> Spring. It was <em>humid</em> and <i>I</i> could feel the <i>skipped</i> shower manifesting <em>itself</em> <em>within</em> <em>the</em> aroma <i>of</i> my <em>unwashed</em> clothes. One shoe worn <em>down</em> to the <i>skin.</i> <i>The</i> other talking. <i>Jeans</i> slightly sagged <i>from</i> <i>sweat</i> <em>and</em> the sun <em>shown</em> hard into <em>the</em> corneas <em>of</em> my <i>eyes.</i>
</body></html>`

# Note
Firefox does not always render `em` tags without a CSS file.
