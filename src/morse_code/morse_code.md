# Morse Decoder

The challenge is to implement a function which decodes a morse code string!
The morse code will have a space between each letter and four between each word

## Examples:

```py
morse_decode(".... ..");
# "HI"

morse_decode(".... . .-.. .-.. ---");
# "HELLO"

morse_decode("-. --- .-. - .... -.-. --- -.. . .-. ...");
# "NORTHCODERS"

morse =
	"--. --- --- -..    -- --- .-. -. .. -. --.    -. --- .-. - .... -.-. --- -.. . .-. ...";
morse_decode(morse);
# "GOOD MORNING NORTHCODERS"
```

##### Morse Code Table

<table>

<tbody>
        <tr>
        <td>.-</td><td>A</td>
        </tr>
        <tr>
        <td>-...</td><td>B</td>
        </tr>
        <tr>
        <td>-.-.</td><td>C</td>
        </tr>
        <tr>
        <td>-..</td><td>D</td>
        </tr>
        <tr>
        <td>.</td><td>E</td>
        </tr>
        <tr>
        <td>..-.</td><td>F</td>
        </tr>
        <tr>
        <td>--.</td><td>G</td>
        </tr>
        <tr>
        <td>....</td><td>H</td>
        </tr>
        <tr>
        <td>..</td><td>I</td>
        </tr>
        <tr>
        <td>.---</td><td>J</td>
        </tr>
        <tr>
        <td>-.-</td><td>K</td>
        </tr>
        <tr>
        <td>.-..</td><td>L</td>
        </tr>
        <tr>
        <td>--</td><td>M</td>
        </tr>
        <tr>
        <td>-.</td><td>N</td>
        </tr>
        <tr>
        <td>---</td><td>O</td>
        </tr>
        <tr>
        <td>.--.</td><td>P</td>
        </tr>
        <tr>
        <td>--.-</td><td>Q</td>
        </tr>
        <tr>
        <td>.-.</td><td>R</td>
        </tr>
        <tr>
        <td>...</td><td>S</td>
        </tr>
        <tr>
        <td>-</td><td>T</td>
        </tr>
        <tr>
        <td>..-</td><td>U</td>
        </tr>
        <tr>
        <td>...-</td><td>V</td>
        </tr>
        <tr>
        <td>.--</td><td>W</td>
        </tr>
        <tr>
        <td>-..-</td><td>X</td>
        </tr>
        <tr>
        <td>-.--</td><td>Y</td>
        </tr>
        <tr>
        <td>--..</td><td>Z</td>
        </tr>
        <tr>
        <td>.----</td><td>1</td>
        </tr>
        <tr>
        <td>..---</td><td>2</td>
        </tr>
        <tr>
        <td>...--</td><td>3</td>
        </tr>
        <tr>
        <td>....-</td><td>4</td>
        </tr>
        <tr>
        <td>.....</td><td>5</td>
        </tr>
        <tr>
        <td>-....</td><td>6</td>
        </tr>
        <tr>
        <td>--...</td><td>7</td>
        </tr>
        <tr>
        <td>---..</td><td>8</td>
        </tr>
        <tr>
        <td>----.</td><td>9</td>
        </tr>
        <tr>
        <td>-----</td><td>0</td>
        </tr>
</tbody>

</table>
